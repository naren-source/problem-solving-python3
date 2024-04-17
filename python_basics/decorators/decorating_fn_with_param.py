import functools


user = {"username": "jose", "access_level": "admin"}


def secure_get_admin(func):

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)

    return secure_func


@secure_get_admin
def get_admin_password(panel):
    if panel == "billing":
        return "!234"
    elif panel == "hr":
        return "abc"


print(get_admin_password("hr"))
