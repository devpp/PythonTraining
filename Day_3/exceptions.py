# def div():
#     try:
#         a = 10
#         b = 0
#         c = a / b
#         print("Div is ", c)
#     except Exception:
#         print("Please enter a number Gr than 0 ")
#     print("Hello End")
#
#
# div()

def div1():
    try:
        a = 10
        b = 0
        if b < 0:
            raise Exception("Please enter a num gr than 0") # Raise an Exception manually.
        c = a / b
        print("Div is ", c)
    except ZeroDivisionError as e:
        print("Please enter a number Gr than 0 ")
    except IOError:
        print("IO Exception")
    else:
        print("No error")

    finally:                # usually written to free up the resource
        print("Finally called")
print("Hello End")

div1()
