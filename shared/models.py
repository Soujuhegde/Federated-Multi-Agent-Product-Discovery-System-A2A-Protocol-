from pydantic import BaseModel


class Product(BaseModel):
    name: str
    category: str
    features: list[str]
    price: str