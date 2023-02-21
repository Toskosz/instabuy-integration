from src.api import API
from src.integrations import ProductIntegration

def main():
    API.setup("instabuy")
    InstabuyProducts = ProductIntegration()
    InstabuyProducts.update("./assets/data/items.csv", 1000)

if __name__ == '__main__':
    main()
