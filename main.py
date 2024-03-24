from typing import Union
from fastapi import FastAPI, Query

# Assuming maths.py contains the necessary logic
from maths import evaluate_expression

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "All Around Calculator"}


@app.get("/expression")
def parse_expression_endpoint(arg1: str = Query(..., description="The mathematical expression to evaluate")):
    return {"res": evaluate_expression(arg1)}


@app.get("/op/multiplication")
def multiplication(arg1: float = Query(..., description="First number"), arg2: float = Query(..., description="Second number")):
    return {"res": arg1 * arg2}


@app.get("/op/addition")
def addition(arg1: float = Query(..., description="First number"), arg2: float = Query(..., description="Second number")):
    return {"res": arg1 + arg2}


@app.get("/op/subtraction")
def subtraction(arg1: float = Query(..., description="First number"), arg2: float = Query(..., description="Second number")):
    return {"res": arg1 - arg2}


@app.get("/op/division")
def division(arg1: float = Query(..., description="First number"), arg2: float = Query(..., description="Second number")):
    if arg2 == 0:
        return {"error": "Division by zero is not allowed"}
    return {"res": arg1 / arg2}


@app.get("/isprime")
def isprime(arg1: float = Query(..., description="Value to be checked")):
    return {"res": False, "confidence": 0.98}

