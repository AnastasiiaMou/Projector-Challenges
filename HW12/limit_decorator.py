import time


def set_limit(max_calls: int, period: int):
    def decorator(func):
        calls = []

        def wrapper(*args, **kwargs):
            now = time.time()
            call_with_period = [call for call in calls if now - call < period]

            if len(call_with_period) >= max_calls:
                raise ValueError("You has reached calls limit")
            result = func(*args, **kwargs)
            calls.append(now)
            return result

        return wrapper

    return decorator


@set_limit(max_calls=2, period=60)
def input_func():
    print(input("Enter from 1 to 10 ->"))


input_func()
input_func()
input_func()
input_func()
input_func()
