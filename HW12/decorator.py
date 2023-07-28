def require_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_type = kwargs.get("user_type")
            if user_type == require_role:
                return func(*args, **kwargs)
            else:
                raise PermissionError

        return wrapper

    return decorator


@require_role("admin")
def admin_access(*args, **kwargs):
    print("Admin")


@require_role("user")
def user_access(*args, **kwargs):
    print("User")


try:
    admin_access(user_type="admin")
    user_access(user_type="user")
except PermissionError as e:
    print(e)
