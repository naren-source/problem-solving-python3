import functools


user = {"username": "jose", "access_level": "guest"}


def secure_get_admin(func):

    @functools.wraps(func)
    def secure_func():
        if user["access_level"] == "admin":
            return func()

    return secure_func


@secure_get_admin
def get_admin_password():
    return "!234"


print(get_admin_password())
