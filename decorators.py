from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise

            if filename:
                with open(filename, "a") as file:
                    file.write(message + "\n")
            else:
                print(message)

            return result

        return wrapper

    return decorator
