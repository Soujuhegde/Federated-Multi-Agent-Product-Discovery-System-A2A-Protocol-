from fastmcp import FastMCP

from product_agent.product_api import (
    search_products,
    recommend_similar
)

mcp = FastMCP(
    "ProductDiscoveryAgent"
)


@mcp.tool()
def search_product(product_name: str):

    return search_products(
        product_name
    )


@mcp.tool()
def get_recommendations(category: str):

    return recommend_similar(
        category
    )


if __name__ == "__main__":

    mcp.run()