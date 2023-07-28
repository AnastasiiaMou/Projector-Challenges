def check_types_decorator(func):
    def wrapper(*args, **kwargs):
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            arg_annotation = func.__annotations__.get(arg_name)
            if arg_annotation and not isinstance(arg_value, arg_annotation):
                raise TypeError(
                    f"Invalid argument type for '{arg_name}'. \
                        Expected {arg_annotation.__name__}, but got \
                            {type(arg_value).__name__}."
                )
        return func(*args, **kwargs)

    return wrapper


@check_types_decorator
def multiply_by_5(num: int) -> int:
    print(num * 5)


# multiply_by_5("Hello")
multiply_by_5(5)
