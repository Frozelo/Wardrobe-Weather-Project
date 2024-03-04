from .decorators import get_object_or_404_decorator, only_objects_decorator, select_related_objects_decorator, \
    objects_exist, prefetch_related_objects_decorator


# def get_queryset_from_object(object, *args, **kwargs):
#     return get_object_or_404(Client, user=user)

@only_objects_decorator
@select_related_objects_decorator
def all_objects(obj: callable):
    return obj.all()


# @only_objects_decorator
def get_objects(obj: callable, **kwargs):
    return obj.get(**kwargs)


@objects_exist
@only_objects_decorator
@select_related_objects_decorator
@prefetch_related_objects_decorator
def filter_objects(obj: callable, **kwargs):
    return obj.filter(**kwargs)


def create_objects(obj: callable, **kwargs):
    print(kwargs)
    return obj.create(**kwargs)

def update_objects(obj: callable, **kwargs):
    for attr, ids, in kwargs.items():
        print(kwargs)
        setattr(obj, attr, ids)

def set_related_objects(obj, **kwargs):
    for field_name, ids in kwargs.items():
        field = getattr(obj, field_name)
        field.add(*ids)
