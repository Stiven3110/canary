from typing import Optional
from pydantic import BaseModel

class Tweet (BaseModel):
    id: Optional[str]
    write: str

    class Config:
        orm_mode = True