import importlib
from django.urls import re_path
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


def resolve_callable(module_path, callable_name):
    """
    Dynamically import a class from a module path.
    """
    try:
        module = importlib.import_module(module_path.replace("/", "."))
        return getattr(module, callable_name, None)
    except (ImportError, AttributeError):
        return None


class DynamicAPIView(APIView):
    """
    Handles dynamic class-based API calls.
    """

    def get(self, request, *args, **kwargs):
        return self.handle_request(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.handle_request(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.handle_request(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.handle_request(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.handle_request(request, *args, **kwargs)

    def handle_request(self, request, *args, **kwargs):
        """
        Determines if the target class is a ViewSet or an APIView and calls it correctly.
        """
        module_path = kwargs.get("module_path")
        callable_name = kwargs.get("callable_name")
        obj = resolve_callable(module_path, callable_name)

        if obj is None:
            return Response({"error": "Not found"}, status=404)

        if isinstance(obj, type):  # Ensure it's a class
            if issubclass(obj, ViewSet):  # Handle DRF ViewSet
                actions = self.get_viewset_actions(request, obj)
                if not actions:
                    return Response({"error": f"Method {request.method} not allowed"}, status=405)
                return obj.as_view(actions)(request._request, *args, **kwargs)  # Use request._request

            if hasattr(obj, "as_view"):  # Handle APIView or Django CBVs
                return obj.as_view()(request._request, *args, **kwargs)  # Use request._request

            return Response({"error": "Invalid class-based view"}, status=400)

        return Response({"error": "Not a class-based view"}, status=400)

    def get_viewset_actions(self, request, viewset_cls):
        """
        Dynamically maps HTTP methods to ViewSet actions.
        """
        method_map = {
            "GET": "list",
            "POST": "create",
            "PUT": "update",
            "PATCH": "partial_update",
            "DELETE": "destroy",
        }
        action = method_map.get(request.method)

        if action and hasattr(viewset_cls, action):
            return {request.method.lower(): action}
        return None
