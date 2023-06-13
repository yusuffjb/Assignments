def role_based_access(user_roles):
    def decorator_func(func):sjehebfdbasljfhh
        def wrapper(*args, **kwargs):
            ip = input('enter the input:')
            if ip in user_roles:
                print("accessible")
                return func(*args, **kwargs)
            else:
                print("Access Denied.")
                print("This function is only accessed by admin")
        return wrapper()

    return decorator_func


@role_based_access(['admin', 'Vidya'])
def inner_function():
    print("ya...its Accessible!!")




