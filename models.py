from pydantic import BaseModel

class MeetingRequest(BaseModel):

    email:str

    urgent:bool=False