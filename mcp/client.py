from fastmcp import Client


class ProductAgentClient:

    def __init__(self):

        self.client = Client(
            "product_agent/mcp_server.py"
        )

    async def search_product(
        self,
        product_name: str
    ):

        async with self.client:

            result = await self.client.call_tool(
                "search_product",
                {
                    "product_name":
                    product_name
                }
            )

            return result

    async def recommend_products(
        self,
        category: str
    ):

        async with self.client:

            result = await self.client.call_tool(
                "get_recommendations",
                {
                    "category":
                    category
                }
            )

            return result