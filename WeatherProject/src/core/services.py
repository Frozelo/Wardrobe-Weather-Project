from .decorators import get_object_or_404_decorator, only_objects_decorator, select_related_objects_decorator, \
    objects_exist


# def get_queryset_from_object(object, *args, **kwargs):
#     return get_object_or_404(Client, user=user)

@only_objects_decorator
def all_objects(obj: callable):
    return obj.all()


# @only_objects_decorator
def get_objects(obj: callable, **kwargs):
    return obj.get(**kwargs)


@objects_exist
@only_objects_decorator
@select_related_objects_decorator
def filter_objects(obj: callable, **kwargs):
    return obj.filter(**kwargs)


def create_objects(obj: callable, **kwargs):
    return obj.create(**kwargs)
