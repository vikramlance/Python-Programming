def announce(f):
    def wrapper():
        print("Begining to execute the function ...")
        f()
        print("Finished the execution of the function.")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()
