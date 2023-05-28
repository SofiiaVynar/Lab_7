from collections.abc import Iterable


def check_battery(file_path):
    def decorator(method):
        def wrapper(self, battery_presence):
            with open(file_path, 'a+') as file:
                file.seek(0)
                data = file.read()
                count = data.count(method.__name__)
                file.write(f"{method.__name__}: {count}\n")
            return method(self, battery_presence)
        return wrapper
    return decorator


def print_length(method):
    def wrapper(self):
        result = method(self)
        if isinstance(result, Iterable):
            length = len(result)
        else:
            length = 1
        print(f"The length: {length}")
        return result

    return wrapper
