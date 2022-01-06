# try:
#     foobar
# except:
#     print("problem")
# print("after the try")
while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("that's not a number")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("Runs no matter what!")
