def cache_result_decorator(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache

    return wrapper


@cache_result_decorator
def calculate_by_5(num: int) -> int:
    print(num * 5)


res1 = calculate_by_5(5)
res2 = calculate_by_5(5)
res3 = calculate_by_5(5)
res4 = calculate_by_5(3)
print(res1)
print(res2)
print(res3)
print(res4)
