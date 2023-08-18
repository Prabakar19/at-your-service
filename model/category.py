from uuid import UUID

from pydantic import BaseModel

from utils.id_generator import IdGenerator


class Category(BaseModel):
    category_id: UUID = IdGenerator.generate_uuid() # fix random id generator
    category_name: str
    category_pic: str = ''  # TODO: find datatype for all the picture variable
