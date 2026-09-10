from pydantic import BaseModel

class AiroPlaneMode(BaseModel):
    name:str
    seats:int