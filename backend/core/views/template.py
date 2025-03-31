import ast
import traceback
import sys
from django.conf import settings
from django.db import models
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import click

from ..utils.data_validation import validate_serializer_data
from ..utils.get_model_details import get_file_content

from functools import wraps

# Update the handle_errors decorator to preserve function names
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, tb = sys.exc_info()
            filename = tb.tb_frame.f_code.co_filename
            line_number = tb.tb_lineno
            stack_trace = traceback.format_exc()
            exception_type = exc_type.__name__

            error_info = {
                "function": func.__name__,
                "file": filename,
                "line": line_number,
                "exception_type": exception_type,
                "error_message": str(e),
                "stack_trace": stack_trace,
            }

            click.secho("\n--- ERROR DETAILS ---", fg='red', bold=True)
            for key, value in error_info.items():
                click.secho(f"{key.capitalize()}: {value}", fg='red')
            click.secho("--- END ERROR DETAILS ---\n", fg='red', bold=True)

            return Response(
                {"error": f"An exception occurred, {error_info}", "details": error_info},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    return wrapper

class BaseModelMixin:
    """
    Contains common functionality shared between GenericViewSet and SingleInstanceViewSet
    """
    
    def load_model_config(self):
        model_name = self.queryset.model.__name__.lower()
        try:
            config_data = get_file_content(model_name)
            return config_data
        except Exception as e:
            print(f"Error loading config for {model_name}: {e}")
            return {}

    def process_filter_kwargs(self, kwargs):
        processed_kwargs = {}
        for key, value in kwargs.items():
            if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                try:
                    value = ast.literal_eval(value)
                    if not isinstance(value, list):
                        continue
                except (ValueError, SyntaxError):
                    pass
            processed_kwargs[key] = value
        return processed_kwargs

    def paginate_queryset(self, queryset, page, page_length):
        total = max(queryset.count(), 1)
        if page_length == 0:
            return queryset, total, 1, 1

        total_pages = (total + page_length - 1) // page_length
        if page > total_pages or page < 1:
            return None, total, total_pages, None

        start_index = (page - 1) * page_length
        end_index = start_index + page_length
        paginated_queryset = queryset[start_index:end_index]
        return paginated_queryset, total, total_pages, page

    def apply_filters(self, queryset, query_params):
        filter_kwargs = self.process_filter_kwargs(query_params)
        search_query = filter_kwargs.pop("search", None)

        is_set_filters = {k: v for k, v in filter_kwargs.items() if k.endswith("__is_set")}
        for key, value in is_set_filters.items():
            field = key[:-8]
            if value.lower() in ["true", "1", "yes"]:
                queryset = queryset.exclude(**{f"{field}": None}).exclude(**{f"{field}": ""})
            else:
                queryset = queryset.filter(Q(**{f"{field}": None}) | Q(**{f"{field}": ""}))
            del filter_kwargs[key]

        if search_query:
            config_data = self.load_model_config()
            search_fields = config_data.get("search_fields", [])
            if isinstance(search_fields, str):
                search_fields = [field.strip() for field in search_fields.split(",")]

            default_search_fields = ["id", config_data.get("title_field", "")]
            search_fields = default_search_fields + search_fields

            if search_fields:
                search_conditions = Q()
                for field in search_fields:
                    if field:
                        if "ForeignKey" in str(self.queryset.model._meta.get_field(field).__class__):
                            field = f"{field}__id"
                        search_conditions |= Q(**{f"{field}__icontains": search_query})
                queryset = queryset.filter(search_conditions)

        try:
            return queryset.filter(**filter_kwargs)
        except Exception as e:
            print(f"Filter error: {e}")
            return queryset

    # Common CRUD operations
    def _extract_pk_fields(self, data):
        pk_fields = {}
        for field in self.queryset.model._meta.get_fields():
            field_name = field.name
            if isinstance(field, (models.ForeignKey, models.OneToOneField)) and field_name in data:
                pk_fields[field_name] = data.pop(field_name)
        return pk_fields

    def _handle_pk_fields(self, data, pk_fields):
        for field_name, related_data in pk_fields.items():
            related_model = self.queryset.model._meta.get_field(field_name).related_model
            if isinstance(related_data, dict):
                if "id" in related_data:
                    related_instance = related_model.objects.get(pk=related_data["id"])
                else:
                    serialized_data = self._serialize_nested_data(related_model, related_data)
                    related_instance = related_model.objects.create(**serialized_data)
            else:
                related_instance = related_model.objects.get(pk=str(related_data))
            data[field_name] = related_instance

    def _extract_m2m_fields(self, data):
        m2m_fields = {}
        for field in self.queryset.model._meta.get_fields():
            if field.many_to_many and field.name in data:
                m2m_fields[field.name] = data.pop(field.name)
        return m2m_fields

    def _handle_m2m_fields(self, instance, m2m_fields):
        for field_name, related_data in m2m_fields.items():
            related_field = getattr(instance, field_name)
            related_model = related_field.model
            if isinstance(related_data, list):
                processed_instances = []
                for item in related_data:
                    if isinstance(item, dict):
                        if "id" in item:
                            related_instance = related_model.objects.get(pk=item["id"])
                        else:
                            serialized_data = self._serialize_nested_data(related_model, item)
                            related_instance = related_model.objects.create(**serialized_data)
                    else:
                        related_instance = related_model.objects.get(pk=item)
                    processed_instances.append(related_instance)
                related_field.set(processed_instances)
            else:
                raise ValueError(f"Invalid data type for field '{field_name}': {related_data}")

    def _serialize_nested_data(self, model, data):
        serialized_data = {}
        for key, value in data.items():
            field = model._meta.get_field(key)
            if field.is_relation:
                related_model = field.related_model
                if isinstance(value, dict):
                    serialized_data[key] = self._serialize_nested_data(related_model, value)
                elif isinstance(value, list) and field.many_to_many:
                    serialized_data[key] = [
                        (related_model.objects.get_or_create(**item)[0] if isinstance(item, dict)
                        else related_model.objects.get(pk=item))
                        for item in value
                    ]
                else:
                    serialized_data[key] = related_model.objects.get(pk=value)
            else:
                serialized_data[key] = value
        return serialized_data

    def _create_instance(self, data):
        pk_fields = self._extract_pk_fields(data)
        m2m_fields = self._extract_m2m_fields(data)

        serializer_data = data.copy()
        if pk_fields:
            self._handle_pk_fields(serializer_data, pk_fields)

        serializer = self.get_serializer(data=serializer_data)
        updated_serializer = validate_serializer_data(serializer, serializer_data)
        updated_serializer.is_valid(raise_exception=True)

        instance = updated_serializer.save()
        if m2m_fields:
            self._handle_m2m_fields(instance, m2m_fields)

        instance.save()
        return updated_serializer.data

    def _update_instance(self, instance, data, partial=False):
        pk_fields = self._extract_pk_fields(data)
        m2m_fields = self._extract_m2m_fields(data)

        serializer_data = data.copy()
        if pk_fields:
            self._handle_pk_fields(serializer_data, pk_fields)

        serializer = self.get_serializer(instance, data=serializer_data, partial=partial)
        updated_serializer = validate_serializer_data(serializer, serializer_data)
        updated_serializer.is_valid(raise_exception=True)

        instance = updated_serializer.save()
        if m2m_fields:
            self._handle_m2m_fields(instance, m2m_fields)

        return updated_serializer.data

    def _serialize_retrieve_instance(self, instance):
        serializer = self.get_serializer(instance)
        serialized_data = serializer.data

        relational_fields = [field for field in instance._meta.get_fields() if field.is_relation]
        for field in relational_fields:
            field_name = field.name
            related_model = field.related_model

            if related_model.__name__ in ["Token", "Session"]:
                continue

            if isinstance(field, models.ForeignKey):
                related_instance = getattr(instance, field_name, None)
                if related_instance:
                    serialized_data[field_name] = self._serialize_retrieve_related_instance(related_instance)
            elif isinstance(field, models.ManyToManyField):
                related_instances = getattr(instance, field_name).all()
                serialized_data[field_name] = [
                    self._serialize_retrieve_related_instance(related_instance)
                    for related_instance in related_instances
                ]
        return serialized_data

    def _serialize_retrieve_related_instance(self, related_instance):
        related_data = {}
        for field in related_instance._meta.get_fields():
            field_name = field.name
            value = getattr(related_instance, field_name, None)

            if isinstance(value, (list, dict)):
                continue

            if field.is_relation:
                if field.related_model.__name__ in ["Token", "Session"]:
                    continue
                if isinstance(value, models.Model):
                    serialized_value = value.id
                elif hasattr(value, "all"):
                    serialized_value = None
                else:
                    serialized_value = None
            else:
                if isinstance(value, models.fields.files.FieldFile) and not value:
                    serialized_value = None
                else:
                    serialized_value = value

            if serialized_value not in [None, "", [], {}, ()]:
                related_data[field_name] = serialized_value
        return related_data

class GenericViewSet(BaseModelMixin, viewsets.ModelViewSet):
    """
    A generic viewset with enhanced error handling, flexible filtering, search functionality,
    and reusable helpers.
    """
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]

    @handle_errors
    def list(self, request, *args, **kwargs):
        query_params = request.GET.copy()
        page = query_params.pop("page", [1])[0]
        page_length = query_params.pop("page_length", [25])[0]
        sort_field = query_params.pop("_sort_field", ["modified"])[0]
        sort_order = query_params.pop("_sort_order", ["desc"])[0]

        filtered_queryset = self.apply_filters(self.get_queryset(), query_params)

        if sort_field or sort_order:
            try:
                if sort_field:
                    if sort_field not in [field.name for field in self.queryset.model._meta.fields]:
                        sort_field = "id"
                else:
                    sort_field = "id"

                sort_prefix = "-" if sort_order.lower() == "desc" else ""
                filtered_queryset = filtered_queryset.order_by(f"{sort_prefix}{sort_field}")
            except Exception as e:
                return Response(
                    {"error": f"Error applying sorting: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        try:
            page = max(int(page), 1)
            page_length = max(int(page_length), 1) if int(page_length) > 0 else 0
        except ValueError:
            return Response(
                {"error": "Invalid pagination parameters."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        paginated_queryset, total, total_pages, current_page = self.paginate_queryset(
            filtered_queryset, page, page_length
        )

        if paginated_queryset is None:
            return Response(
                {"error": f"Page out of range. Page {page} of {total_pages}."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(paginated_queryset, many=True)
        return Response({
            "data": serializer.data,
            "total": total,
            "total_pages": total_pages,
            "current_page": current_page,
        })

    @handle_errors
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @handle_errors
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            return self._create_multiple_instances(request.data)
        return self._create_single_instance(request.data)

    def _create_multiple_instances(self, data_list):
        created_data = []
        for item_data in data_list:
            created_instance = self._create_instance(item_data)
            created_data.append(created_instance)
        return Response(created_data, status=status.HTTP_201_CREATED)

    def _create_single_instance(self, data):
        created_instance = self._create_instance(data)
        return Response(created_instance, status=status.HTTP_201_CREATED)

    @handle_errors
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        model_fields = [field.name for field in self.queryset.model._meta.fields]
        sort_field = "modified" if "modified" in model_fields else "id"
        queryset = self.get_queryset().order_by(sort_field)

        next_instance = queryset.filter(**{f"{sort_field}__lt": getattr(instance, sort_field)}).last()
        prev_instance = queryset.filter(**{f"{sort_field}__gt": getattr(instance, sort_field)}).first()

        data = self._serialize_retrieve_instance(instance)
        data["_prev"] = prev_instance.id if prev_instance else None
        data["_next"] = next_instance.id if next_instance else None

        return Response(data)

    @handle_errors
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        updated_instance = self._update_instance(instance, request.data, partial)
        return Response(updated_instance, status=status.HTTP_200_OK)




class SingleInstanceViewSet(BaseModelMixin, viewsets.ViewSet):
    """
    ViewSet for handling single instance models (singleton pattern).
    Automatically creates instance if it doesn't exist during GET requests.
    Provides list/retrieve (GET) and create/update (POST/PUT/PATCH) operations.
    DELETE operation is disabled.
    """
    permission_classes = [AllowAny]
    
    # Default empty data for new instance creation
    default_data = {}

    def get_instance_id(self):
        """Determine the ID to use for the single instance"""
        try:
            from ..utils.get_model_details import get_model_doctype_json
            doctype_config = get_model_doctype_json(self.queryset.model.__name__)
            return doctype_config.get("name", self.queryset.model.__name__).lower().replace(" ", "_")
        except Exception:
            return "1"

    def get_or_create_instance(self):
        """Get or create the single instance with default data"""
        instance_id = self.get_instance_id()
        instance, created = self.queryset.model.objects.get_or_create(
            pk=instance_id,
            defaults=self.default_data
        )
        return instance

    @handle_errors
    def list(self, request, *args, **kwargs):
        """
        Retrieve the single instance.
        Automatically creates with default data if doesn't exist.
        """
        instance = self.get_or_create_instance()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @handle_errors
    def retrieve(self, request, *args, **kwargs):
        """Alias for list() since we only have one instance"""
        return self.list(request, *args, **kwargs)

    @handle_errors
    def create(self, request, *args, **kwargs):
        """
        Create or fully update the single instance.
        Uses POST for both create and update operations.
        """
        instance = self.get_or_create_instance()
        updated_data = self._update_instance(instance, request.data)
        return Response(updated_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'])
    @handle_errors
    def update_instance(self, request, *args, **kwargs):
        """PUT endpoint for full updates"""
        return self.create(request, *args, **kwargs)

    @action(detail=False, methods=['patch'])
    @handle_errors
    def partial_update_instance(self, request, *args, **kwargs):
        """PATCH endpoint for partial updates"""
        instance = self.get_or_create_instance()
        updated_data = self._update_instance(instance, request.data, partial=True)
        return Response(updated_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """DELETE operation is explicitly disabled"""
        return Response(
            {"error": "DELETE operation not allowed for single instance configuration"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    # Disable standard update/partial_update endpoints
    def update(self, request, *args, **kwargs):
        return Response(
            {"error": "Use PUT /update_instance/ for full updates or PATCH /partial_update_instance/ for partial updates"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    """
    ViewSet for handling single instance models (singleton pattern).
    Automatically creates instance if it doesn't exist during GET requests.
    Provides list/retrieve (GET) and create/update (POST/PUT/PATCH) operations.
    DELETE operation is disabled.
    """
    permission_classes = [AllowAny]
    
    # Default empty data for new instance creation
    default_data = {}

    def get_instance_id(self):
        """Determine the ID to use for the single instance"""
        try:
            from ..utils.get_model_details import get_model_doctype_json
            doctype_config = get_model_doctype_json(self.queryset.model.__name__)
            return doctype_config.get("name", self.queryset.model.__name__)
        except Exception:
            return "1"

    def get_or_create_instance(self):
        """Get or create the single instance with default data"""
        instance_id = self.get_instance_id()
        instance, created = self.queryset.model.objects.get_or_create(
            pk=instance_id,
            defaults=self.default_data
        )
        return instance

    @handle_errors
    def list(self, request, *args, **kwargs):
        """
        Retrieve the single instance.
        Automatically creates with default data if doesn't exist.
        """
        instance = self.get_or_create_instance()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @handle_errors
    def retrieve(self, request, *args, **kwargs):
        """Alias for list() since we only have one instance"""
        return self.list(request, *args, **kwargs)

    @handle_errors
    def create(self, request, *args, **kwargs):
        """
        Create or fully update the single instance.
        Uses POST for both create and update operations.
        """
        instance = self.get_or_create_instance()
        updated_data = self._update_instance(instance, request.data)
        return Response(updated_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'])
    @handle_errors
    def update_instance(self, request, *args, **kwargs):
        """PUT endpoint for full updates"""
        return self.create(request, *args, **kwargs)

    @action(detail=False, methods=['patch'])
    @handle_errors
    def partial_update_instance(self, request, *args, **kwargs):
        """PATCH endpoint for partial updates"""
        instance = self.get_or_create_instance()
        updated_data = self._update_instance(instance, request.data, partial=True)
        return Response(updated_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """DELETE operation is explicitly disabled"""
        return Response(
            {"error": "DELETE operation not allowed for single instance configuration"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    # Disable standard update/partial_update endpoints
    def update(self, request, *args, **kwargs):
        return self._method_not_allowed()

    def partial_update(self, request, *args, **kwargs):
        return self._method_not_allowed()

    def _method_not_allowed(self):
        return Response(
            {"error": "Use the dedicated create/update endpoints instead"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )