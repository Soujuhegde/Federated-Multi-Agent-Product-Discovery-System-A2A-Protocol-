from product_agent.catalog import products


def search_products(product_name: str):

    matches = []

    for product in products:

        if product_name.lower() in product["name"].lower():

            matches.append(product)

    return matches


def recommend_similar(category: str):

    recommendations = []

    for product in products:

        if product["category"].lower() == category.lower():

            recommendations.append(product)

    return recommendations