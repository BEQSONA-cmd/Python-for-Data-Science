

def is_iterable(object: any):
    try:
        iter(object)
        return True
    except TypeError:
        pass
    return False


def all_thing_is_obj(object: any) -> int:
    def get_str(object: any):
        if type(object) is str:
            return object + " is in the kitchen"
        elif is_iterable(object) and not type(object) is str:
            str_ret = type(object).__name__.title() + " : " + str(type(object))
            return str_ret
        return "Type not Found"
    print(get_str(object))
    return 42
