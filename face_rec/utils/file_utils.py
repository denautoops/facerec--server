import os

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def create_jpeg_file_from_memory(in_memory_uploaded_file):
    path = default_storage.save('tmp/unknown.jpeg', ContentFile(in_memory_uploaded_file.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    return tmp_file