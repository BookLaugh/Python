# ---- New decorator ----
def new_decorator(original_func):

    def wrap_func():
        print("Some extra codes before the original function!")
        original_func()
        print("Some extra codes after the original function!")
    return wrap_func

# The original function (Decorators {@})
@ new_decorator
def func_needs_decorator():
    print("I wanna be decorated!!")

# Testing .....

func_needs_decorator()
