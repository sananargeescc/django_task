from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize=value.size
    if filesize > 100024:
        raise ValidationError("you cannot upload file more than 10Mb")
    else:
        return value