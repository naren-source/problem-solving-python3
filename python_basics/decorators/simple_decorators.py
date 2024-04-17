user = {"username": "jose", "access_level": "admin"}


def get_admin_password():
    return "!234"


def secure_get_admin(func):
    def secure_func():
        if user["access_level"] == "admin":
            return func()

    return secure_func


get_admin_password = secure_get_admin(get_admin_password)

print(get_admin_password())
