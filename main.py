from fastapi import FastAPI

app = FastAPI()

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@app.get("/fibonacci/{n}")
def read_fibonacci(n: int):
    result = fibonacci(n)
    return {"fibonacci_number": result}