from pydantic import BaseModel

class CarHouse(BaseModel):
    carName:str
    carColor:str
    seat:int
    modelName:int