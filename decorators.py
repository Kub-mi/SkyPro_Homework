from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования выполнения функции.
    Логирует начало, конец и результат выполнения функции, а также ошибки.

    :param filename: Имя файла для логирования. Если None, логируется в консоль.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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
