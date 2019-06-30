from collections import Iterable

numeric = [int, float]

"""
Class method decorator
----------------------
Verifies if method argument is the expected type
"""


def verify_types(*args, **kwargs):
    types = {
        position: type_id for (position, type_id) in enumerate(args)
    }

    def decorator(func):
        def type_check(self, *args, **kwargs):
            arguments = {
                position: type_id for (position, type_id) in enumerate(args)
            }
            arguments.update(kwargs)

            for position in types.keys():
                if position in arguments.keys() and\
                    type(arguments[position]) != types[position] and\
                    not(isinstance(types[position], Iterable) and
                        type(arguments[position]) in types[position]):
                    raise TypeError(
                        f"Argument {position} of {func} is not {types[position]}"
                    )

            return func(self, *args, **kwargs)
        return type_check
    return decorator


"""
Class method decorator
----------------------
Verifies if all method arguments are positive
(usually used with type verification for arguments to be numeric)
"""


def verify_positive(func):
    def check_positive(self, *args, **kwargs):
        positive = all(
            type(argument) not in numeric or argument >= 0
            for argument in list(args)
        ) & all(
            type(argument) not in numeric or argument >= 0
            for argument in kwargs.values()
        )
        if not positive:
            raise ValueError(
                "All arguments must be positive"
            )
        return func(self, *args, **kwargs)
    return check_positive


# Verifying if an argument value is in a list of expected values
def verify_value(arg, values):
    if arg not in values:
        raise ValueError(f"{values} expected")


# calculates distance between two points
def get_distance(position1, position2):
    from math import sqrt
    distance = (position1[0] - position2[0]) ** 2 +\
               (position1[1] - position2[1]) ** 2
    return distance
