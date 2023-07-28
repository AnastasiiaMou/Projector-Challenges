def catch_errors_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"An error occurred while executing '{func.__name__}': {e}")

    return wrapper
