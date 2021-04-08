from flask_login import current_user
from flask import abort
from flask_login.utils import login_required
# ? Basic Functions


def greating(dfdfd):
    print(f"Hello {dfdfd}")


# greating("Hiba")

# A function that takes another function and returns
# without modifying


def great_cibar(another_function):
    return greating("Cibaar")


# great_cibar(greating)

# inner functions


def parent_function():
    print("Printing from parent function")

    def first_child():
        print("Printing from the first child")

    def second_child():
        print("printing from the second child")

    second_child()
    first_child()


# parent_function()

# returning functions from functions


def parent(num: int):
    def child_one():
        return "Child One"

    def child_two():
        return "Child Two"
    if num == 1:
        return child_one
    else:
        return child_two


# first = parent(10)
# print(first())

second = parent(10)
# print(second())
# <function parent. < locals > .child_one at 0x7fda318ff940 >


# ? Decorators
def my_decorator(salaam):
    def inner():
        print("Before your function")
        salaam()
        print("After your function")
    return inner


# @my_decorator
def salaam():
    print("Salaam")


# 1-Way
# decorator = my_decorator(salaam)
# print(decorator)

# Decorating functions with arguments
def dec_fun_with_args(func):
    def inner(*args, **kwrgs):
        print("Decorating ...")
        func(*args, **kwrgs)
    return inner


@dec_fun_with_args
def great(*args, **kwrgs):
    print(f"hello {args}")


# decorator = my_decorator(great('Ali'))
# print(decorator())

# great("Ali", "name", "ali")

def admin_required(route):
    def decorator(*args, **kwrgs):
        # check if current_user is admin
        if current_user.role == 'ADMIN':
            return route()
        else:
            abort(401)  # exit program with 401 unauthorized
    return decorator


# users Model
# user.role

# name = "ali is my name"
# print(name.upper())

@users.route('/list/all', methods=['POST', 'GET'])
@login_required
@admin_required
def user_list():
    return 'user list'
