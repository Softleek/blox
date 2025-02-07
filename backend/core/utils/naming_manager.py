import re
import uuid
from datetime import datetime
from django.db import transaction
from ..models import Series
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

NAMING_SERIES_PATTERN = re.compile(r"^[\w\- \/.#{}]+$", re.UNICODE)


class InvalidNamingSeriesError(Exception):
    pass


class NamingManager:
    def __init__(self, instance, doctype_config):
        """
        Initialize with the model instance and doctype configuration.

        :param instance: The model instance.
        :param doctype_config: A dict containing `naming_rule` and `autoname`.
        """
        self.instance = instance
        self.config = doctype_config
        
        

    def generate_code(self, _, field_options):
        """
        Generate a barcode or QR code based on the field configuration.

        :param fieldname: The name of the field to generate code for.
        :param field_options: The specific field options from the config.
        :return: Generated code as a string.
        """
        return self.generate_by_format(field_options)

    def generate_name(self):
        """
        Generate a name based on the naming configuration.
        :return: Generated name as a string.
        """
        if self.config:
            naming_rule = self.config.get("naming_rule", "Random")
            autoname = self.config.get("autoname", "hash")
            
            if naming_rule == "Set by user":
                return self.instance.id

            if naming_rule == "Autoincrement":
                return self.generate_autoincrement()

            if naming_rule.startswith("By fieldname"):
                fieldname = autoname.split(":", 1)[1].strip()
                return self.generate_by_field(fieldname)

            if naming_rule == 'By "Naming Series" field':
                # Retrieve the series field from the instance dynamically
                fieldname = autoname.split(":", 1)[1].strip() or getattr(self.instance, 'naming_series', None) or getattr(self.instance, 'series', None)

                if not fieldname:
                    # Load from docconfig fields if no series field is found
                    docconfig_fields = self.config.get("fields", [])
                    series_field = next((field for field in docconfig_fields if field.get("fieldname") in {"series", "naming_series"}), None)

                    if not series_field or not series_field.get("options"):
                        raise ValueError("No naming series field or options found in docconfig.")

                    # Use the first value in the options
                    series = series_field["options"].split("\n")[0]
                else:
                    series = str(getattr(self.instance, fieldname))
                return self.generate_by_naming_series(series)


            if naming_rule == "Expression":
                return self.generate_by_format(autoname[autoname.index(":") + 1:].strip())

            if naming_rule == "Expression (old style)":
                return self.generate_by_old_style_expression(autoname)

            if naming_rule == "Random":
                return self.generate_by_hash()

            if naming_rule == "By script":
                return self.generate_by_script(autoname)

            raise ValueError(f"Unsupported naming rule: {naming_rule}")

    def generate_autoincrement(self):
        return generate_autoincrement(self.instance)

    def generate_by_field(self, field_name):
        """Generate name based on the value of a specific field."""
        if not hasattr(self.instance, field_name):
            raise ValueError(f"Field '{field_name}' not found in the model.")
        return str(getattr(self.instance, field_name))

    def generate_by_series(self, series_pattern):
        """Generate name using a series pattern."""
        naming_series = NamingSeries(series_pattern)
        return naming_series.generate_next_name(self.instance)

    def generate_by_naming_series(self, series):
        """Generate a name using a naming series."""
        naming_series = NamingSeries()
        return naming_series.generate_next_name(series, self.instance)
    
    def generate_by_format(self, format_pattern):
        """
        Generate a name using a flexible format pattern.
        Handles tokens like {fieldname}, {MM}, {DD}, {YYYY}, {###}, and more.
        Auto-increment tokens ({###}) consider the latest instance in the database.
        """
        return generate_next_id(self.instance, format_pattern)


    def generate_by_old_style_expression(self, expression):
        """
        Generate name using an old-style expression.
        Supports format like 'PREFIX-.#####' where prefix and series are separated by a dot.
        """
        parts = expression.split('.')
        if len(parts) != 2 or not parts[1].startswith("#"):
            raise ValueError(
                "Invalid old-style expression format. Expected 'PREFIX-.#####'."
            )

        prefix = parts[0]
        series_pattern = parts[1]
        digits = series_pattern.count("#")

        # Generate the next value in the series with the prefix
        next_value = self.get_series_with_prefix(prefix, digits)
        return f"{prefix}.{next_value}"

    def get_series_with_prefix(self, prefix, digits):
        """
        Retrieve the next number in the series for the given prefix.
        Ensures unique numbering for each prefix.
        """
        with transaction.atomic():
            obj, _ = Series.objects.get_or_create(
                name=prefix, defaults={"current": 0}
            )
            obj.current += 1
            obj.save()
            return str(obj.current).zfill(digits)

    def generate_by_hash(self):
        """Generate a random hash-based name."""
        return str(uuid.uuid4())

    def generate_by_script(self, script):
        """Generate a name using a script or callable."""
        if callable(script):
            return script(self.instance)
        raise ValueError("Script must be a callable")

    def get_series(self, digits):
        """Retrieve the next number in the series with the specified digits."""
        prefix = ""
        with transaction.atomic():
            obj, _ = Series.objects.get_or_create(name=prefix, defaults={"current": 0})
            obj.current += 1
            obj.save()
            return str(obj.current).zfill(digits)


class NamingSeries:
    def __init__(self):
        pass

    def validate(self, series):
        """
        Validates the provided naming series format.

        Args:
            series (str): The naming series to validate.

        Raises:
            InvalidNamingSeriesError: If the series is invalid.
        """
        if "." not in series:
            raise InvalidNamingSeriesError(f"Invalid naming series {series}: dot (.) missing")

        if not NAMING_SERIES_PATTERN.match(series):
            raise InvalidNamingSeriesError(
                f"Special characters except '-', '#', '.', '/', '{{' and '}}' not allowed in naming series {series}"
            )

    def generate_next_name(self, series, instance):
        """
        Generate the next name based on the provided naming series and instance.

        Args:
            series (str): The naming series defining the format.
            instance: The model instance for which the name is generated.

        Returns:
            str: The next name in the series.
        """
        # Add default numeric placeholder if not present
        if "#" not in series:
            series += ".#####"

        # Validate the series format
        self.validate(series)

        # Split the series into parts and process it
        parts = series.split(".")
        return parse_naming_series(parts, instance, series)


def parse_naming_series(parts, instance, series, number_generator=None):
    if isinstance(parts, str):
        parts = parts.split(".")

    if not number_generator:
        number_generator = get_series

    name = ""
    today = datetime.now()

    # Get the model name (doctype) to ensure uniqueness per doctype
    doctype = instance._meta.model_name  # This gets the model name (lowercase)
    
    for part in parts:
        if part.startswith("#"):
            digits = len(part)
            name += number_generator(doctype, digits, series)  # Pass the doctype to the number generator
        elif part in ["YY", "MM", "DD", "YYYY"]:
            name += today.strftime({
                "YY": "%y",
                "MM": "%m",
                "DD": "%d",
                "YYYY": "%Y"
            }[part])
        else:
            name += str(getattr(instance, part, part))

    return name


def get_series(doctype, digits, series):
    """
    Get the next series number for a given doctype, ensuring uniqueness,
    but still keeping the original series name.
    
    Args:
        doctype (str): The name of the doctype (model).
        digits (int): The number of digits to pad the series number.
    
    Returns:
        str: The next series number with padding, keeping original name.
    """
    with transaction.atomic():
        # Keep the original series name, but make it unique by adding the doctype
        obj, _ = Series.objects.get_or_create(id=f"{doctype}_{series}_series", name=f"{doctype}_{series}_series", defaults={"current": 0})
        obj.current += 1
        obj.save()
        return str(obj.current).zfill(digits)


def generate_autoincrement(instance):
    model = instance._meta.model
    try:
        # Get the last entry in the table based on the primary key
        last_entry = model.objects.latest('id')
        new_id = int(last_entry.id) + 1
    except ObjectDoesNotExist:
        # If there are no entries in the table, start with ID 1
        new_id = 1
    
    return new_id


def generate_next_id(instance, format_pattern):
    """
    Generate the next ID by matching the last ID to the format pattern,
    replacing placeholders with current or incremented values.

    Args:
        instance: The model instance for which the ID is generated.
        format_pattern: The format pattern defining the ID structure.

    Returns:
        str: The next ID based on the format pattern.
    """
    import re
    from django.core.exceptions import ObjectDoesNotExist

    model = instance._meta.model

    try:
        # Fetch the latest entry in the database
        last_entry = model.objects.latest('created')  # Adjust 'created' field as needed
        last_id = str(getattr(last_entry, "id", ""))  # Adjust field name if needed
    except ObjectDoesNotExist:
        # Start fresh if no entries exist
        last_id = ""

    # Match tokens enclosed in `{}` (e.g., `{#####}`, `{from_time}`, etc.)
    token_pattern = re.compile(r"{([^{}]+)}")
    tokens = token_pattern.findall(format_pattern)

    # Escape the format pattern to prepare for regex generation
    escaped_pattern = re.escape(format_pattern)

    # Replace `{tokens}` with regex patterns for matching
    for token in tokens:
        if token.startswith("#"):
            token_length = len(token)
            escaped_pattern = escaped_pattern.replace(
                re.escape(f"{{{token}}}"), rf"(\d{{{token_length}}})"
            )
        elif any(c in token for c in ["Y", "m", "d", "H", "M", "S", "%"]):  # Date/Time format placeholders
            escaped_pattern = escaped_pattern.replace(
                re.escape(f"{{{token}}}"), r"(\d+)"
            )
        else:
            # Assume other tokens are dynamic fields or static placeholders
            escaped_pattern = escaped_pattern.replace(
                re.escape(f"{{{token}}}"), r"(.*?)"
            )


    # Match the last ID against the generated regex pattern
    match = re.match(escaped_pattern, last_id)
    if match:
        # Extract matched values
        matched_values = match.groups()
    else:
        # If no match, initialize default values
        matched_values = ["_"] * len(tokens)


    # Generate the next ID by replacing tokens with incremented/current values
    result = format_pattern
    for i, token in enumerate(tokens):
        if token.startswith("#"):
            # Handle numeric tokens
            try:
                # Try to convert matched_values[i] to an integer, defaulting to 0 if it fails
                last_number = int(matched_values[i])
            except ValueError:
                # If the value is not an integer, set it to 0
                last_number = 0
            replacement = str(last_number + 1).zfill(len(token))
        elif hasattr(instance, token):
            # Handle dynamic fields from the instance
            value = getattr(instance, token, None)
            
            if value is not None:
                # Check if the value is an instance (i.e., a related model or object)
                if hasattr(value, 'id'):
                    # Use the 'id' field of the related model if it exists
                    replacement = str(value.id)
                else:
                    # Otherwise, use the value directly (for non-instance fields)
                    replacement = str(value)
            else:
                # If the value is None, just use an empty string
                replacement = ""


        elif any(c in token for c in ["Y", "m", "d", "H", "M", "S", "%"]):  # Handle extended date/time formats
            today = datetime.today()
            # Replace the placeholders with their respective date format
            replacement = today.strftime(
                token.replace("YYYY", "%Y")  # Full year
                    .replace("YY", "%y")      # Two-digit year
                    .replace("MM", "%m")      # Month (01 to 12)
                    .replace("DD", "%d")      # Day of the month (01 to 31)
                    .replace("hh", "%H")      # Hour (00 to 23)
                    .replace("mm", "%M")      # Minute (00 to 59)
                    .replace("ss", "%S")      # Second (00 to 59)
            )
        else:
            # Default replacement for unmatched tokens
            replacement = matched_values[i] if matched_values[i] else f"{{{token}}}"

        # Replace the token in the result
        result = result.replace(f"{{{token}}}", replacement, 1)

    return result
