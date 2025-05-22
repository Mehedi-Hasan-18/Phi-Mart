from rest_framework.exceptions import ValidationError

def file_size_validator(file):
    max_size = 10
    max_size_in_bytes = max_size * 1024 * 1024
    
    if file.size > max_size_in_bytes:
        ValidationError("File Size Can Not Be Excced {max_size} MB")