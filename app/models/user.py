from pydantic import BaseModel
import uuid

class User(BaseModel):
    id: uuid.UUID
    username: str
    password: str # In a real application, this should be a hashed password
    role: str
    department: str