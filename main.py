""" 
This module will expose the rest apis

"""

from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def home ():
     return{"message": "Welcome to Calculator"}

@app.get("/add/{value1}/{value2}")
def add(value_1:int, value_2:int):
     return value_1 + value_2
	

