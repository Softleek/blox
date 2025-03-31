from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from django.core.files.storage import default_storage

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)  # Handle multipart/form-data

    def post(self, request, *args, **kwargs):
        # Get the file, folder, and filename from the request
        file = request.FILES.get("file")
        folder = request.data.get("folder")
        filename = request.data.get("filename")

        if not file or not folder or not filename:
            return Response(
                {"error": "File, folder, and filename are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Ensure the folder exists
        folder_path = os.path.join(settings.MEDIA_ROOT, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Save the file to the specified folder with the desired filename
        file_path = os.path.join(folder_path, filename)
        with default_storage.open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Generate the file URL
        file_url = request.build_absolute_uri(
            os.path.join(settings.MEDIA_URL,  folder, filename)
        )

        return Response({"url": parse_url(file_url)}, status=status.HTTP_201_CREATED)

def parse_url(file_url):
    from urllib.parse import urlparse

    parsed_url = urlparse(file_url)

    # Extract the path and find the `/media` part
    media_index = parsed_url.path.find("/media")
    if media_index != -1:
        return parsed_url.path[media_index:]  # Return only the `/media/...` part

    # If `/media` is not found, return the original path
    return parsed_url.path

