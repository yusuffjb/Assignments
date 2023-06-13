from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
def add(num1: float, num2: float):
    return {"The addition of two numbers:", num1 + num2}

@app.get("/sub/")
def sub(num1: float, num2: float):
    return {"The subtraction of two numbers:", num1 - num2}

@app.get("/mul/")
def mul(num1: float, num2: float):
    return {"The multiplication of two numbers:", num1 * num2}

@app.get("/div/")
def div(num1: float, num2: float):
   try:
      return {"The division of two numbers: ", num1 / num2}
   except:
       return {"Sorry...! Invalid input"}




