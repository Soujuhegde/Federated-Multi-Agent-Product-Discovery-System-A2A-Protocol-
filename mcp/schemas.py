from pydantic import BaseModel


class ProductSearchRequest(BaseModel):

    product_name: str


class RecommendationRequest(BaseModel):

    category: str