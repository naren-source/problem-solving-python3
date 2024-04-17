import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
        return secure_func
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("db")
def get_db_password():
    return "db: 1234"


print(get_admin_password())
print(get_db_password())

user = {"username": "jose", "access_level": "admin"}

print(get_admin_password())
print(get_db_password())

user = {"username": "jose", "access_level": "db"}

print(get_admin_password())
print(get_db_password())
