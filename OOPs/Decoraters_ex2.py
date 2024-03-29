def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        result = fx(*args, **kwargs)
        print("Thanks for using this function")
        return result
    return mfx

@greet
def hello():
    print("Hello World")

@greet    
def add(a, b):
    print(a + b)
    return a + b  # Adding a return statement

hello()
add(3, 5)

'''
Output: Good Morning
        Hello World
        Thanks for using this function
        Good Morning
        8
        Thanks for using this function '''