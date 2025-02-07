import re
from datetime import datetime
from uuid import uuid4
from django.db import transaction
from django.core.exceptions import ValidationError
from ..models import Series

NAMING_SERIES_PATTERN = re.compile(r"^[\w\- \/.#{}]+$", re.UNICODE)

class InvalidNamingSeriesError(Exception):
    pass

class NamingSeries:
    def __init__(self, series):
        self.series = series

        if "#" not in self.series:
            self.series += ".#####"

    def validate(self):
        if "." not in self.series:
            raise InvalidNamingSeriesError(f"Invalid naming series {self.series}: dot (.) missing")

        if not NAMING_SERIES_PATTERN.match(self.series):
            raise InvalidNamingSeriesError(
                "Special characters except '-', '#', '.', '/', '{{' and '}}' not allowed in naming series {0}".format(self.series)
            )

    def generate_next_name(self, instance, ignore_validate=False):
        if not ignore_validate:
            self.validate()
        parts = self.series.split(".")
        return parse_naming_series(parts, instance)

    def get_prefix(self):
        prefix = None

        def fake_counter_backend(partial_series, digits):
            nonlocal prefix
            prefix = partial_series
            return "#" * digits

        parse_naming_series(self.series, number_generator=fake_counter_backend)

        if not prefix:
            raise InvalidNamingSeriesError(f"Invalid Naming Series: {self.series}")

        return prefix

    def update_counter(self, prefix, new_count):
        with transaction.atomic():
            obj, created = Series.objects.get_or_create(name=prefix, defaults={"current": 0})
            obj.current = new_count
            obj.save()

    def get_current_value(self, prefix):
        try:
            return Series.objects.get(name=prefix).current
        except Series.DoesNotExist:
            return 0


def set_new_name(instance, meta):
    autoname = meta.get("autoname", "")

    if autoname.lower() == "uuid":
        instance.name = instance.name or str(uuid4())
        return

    if autoname.startswith("field:"):
        fieldname = autoname[6:]
        instance.name = getattr(instance, fieldname, None)
        if not instance.name:
            raise ValidationError(f"{fieldname} is required for naming")

    elif autoname.startswith("naming_series:"):
        set_name_by_naming_series(instance)

    elif autoname.startswith("format:"):
        instance.name = parse_format_autoname(autoname, instance)

    elif "#" in autoname:
        instance.name = make_autoname(autoname, instance)

    if not instance.name:
        raise ValidationError(f"Unable to determine name for {meta['model']}")


def set_name_by_naming_series(instance):
    if not instance.naming_series:
        raise ValidationError("Naming Series mandatory")

    series = NamingSeries(instance.naming_series + ".#####")
    instance.name = series.generate_next_name(instance)


def make_autoname(key, instance):
    if key == "hash":
        return generate_random_string()

    series = NamingSeries(key)
    return series.generate_next_name(instance)


def parse_naming_series(parts, instance, number_generator=None):
    if isinstance(parts, str):
        parts = parts.split(".")

    if not number_generator:
        number_generator = get_series

    name = ""
    today = datetime.now()

    for part in parts:
        if part.startswith("#"):
            digits = len(part)
            name += number_generator(name, digits)

        elif part == "YY":
            name += today.strftime("%y")
        elif part == "MM":
            name += today.strftime("%m")
        elif part == "DD":
            name += today.strftime("%d")
        elif part == "YYYY":
            name += today.strftime("%Y")
        else:
            name += str(getattr(instance, part, part))

    return name


def get_series(prefix, digits):
    with transaction.atomic():
        obj, created = Series.objects.get_or_create(name=prefix, defaults={"current": 0})
        obj.current += 1
        obj.save()
        return str(obj.current).zfill(digits)


def generate_random_string(length=10):
    import secrets
    import string

    return ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(length))


def parse_format_autoname(format_str, instance):
    return format_str.replace("{", "").replace("}", "")

