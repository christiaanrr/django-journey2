from django.core.exceptions import ValidationError

CATEGORIES = ['mexican', 'asian', 'american', 'fast food']

def validate_category(value):
    if not value.lower() in CATEGORIES:
        raise ValidationError(str(value) + ' is not a valid category')