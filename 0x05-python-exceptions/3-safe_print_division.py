#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, zeroDivisionError);
        div = None
    finally:
        print("inside result: {}".format(div))
        return (div)
