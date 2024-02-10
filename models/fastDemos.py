from pydantic import BaseModel


class FastDemo(BaseModel):
    name: str
    desc: str
    complete: bool
