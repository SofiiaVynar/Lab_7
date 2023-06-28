import logging


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(e.message)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.ERROR)
                    logging.error(e.message)

        return wrapper

    return decorator

