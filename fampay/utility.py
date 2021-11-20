import datetime
from django.db.models import ManyToManyField


def parse_datetime_to_text(datetime_obj, format):
    return datetime_obj.strftime(format)


def parse_text_to_datetime(datetime_obj, format):
    return datetime.datetime.strptime(datetime_obj, format)


def to_dict(instance, datetime_format):
    model_options = instance._meta
    data = {}
    for option in model_options.concrete_fields + model_options.many_to_many:
        if isinstance(option, ManyToManyField):
            if instance.pk is None:
                data[option.name] = []
            else:
                data[option.name] = list(option.value_from_object(instance).values_list('pk', flat=True))
        else:
            data[option.name] = option.value_from_object(instance)
            if type(data[option.name]) == datetime.datetime:
                data[option.name] = parse_datetime_to_text(data[option.name], datetime_format)
    return data