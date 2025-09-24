from typing import Any

def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            function()



def main():
    @callLimit(3)
    def f():
        print ("f()")
    
    @callLimit(1)
    def g():
        print ("g()")
    for i in range(3):
        f()
        g()

if __name__ == "__main__":
    main()