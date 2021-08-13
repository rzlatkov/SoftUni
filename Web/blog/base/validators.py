from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator

first_last_name_len = MinLengthValidator(3, 'Minimum length of 3 letters required.')
letters_n_whitespaces = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabet and whitespace characters are allowed.')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric and whitespace characters are allowed.')
category_n_title_min_len = MinLengthValidator(3, 'Minimum length of 3 letters required.')
location_name_validator = RegexValidator(r'^[0-9a-zA-Z ,-]*$',
                                         "Only alphanumeric, '-', ',' and whitespace characters are allowed.")
location_len_validator = MinLengthValidator(15, 'Minimum length of 15 letters required.')


def validate_capitalized(value):
    if value != value.capitalize():
        raise ValidationError('Invalid category name. First letter must be in CAPS.')


def no_present_nor_future(value):
    today = date.today()
    if value >= today:
        raise ValidationError('Date cannot be present or in the future.')
