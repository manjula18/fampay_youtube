import datetime
from django.db.models import ManyToManyField


def parse_datetime_to_text(datetime_obj, datetime_format):
    """
    this converts datetime to string based on the datetime format
    """
    return datetime_obj.strftime(datetime_format)


def parse_text_to_datetime(datetime_obj, datetime_format):
    """
    this converts string to datetime
    """
    return datetime.datetime.strptime(datetime_obj, datetime_format)


def to_dict(instance, datetime_format):
    """
    this method converts the obj to a dictionary and converts all the datetime fields to string format
    """
    model_options = instance._meta
    data = {}
    for option in model_options.concrete_fields + model_options.many_to_many:
        if not isinstance(option, ManyToManyField):
            data[option.name] = option.value_from_object(instance)
            if type(data[option.name]) == datetime.datetime:
                data[option.name] = parse_datetime_to_text(data[option.name], datetime_format)
    return data
