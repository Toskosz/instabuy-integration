from src.api import API
from src.integrations.product import ProductIntegration

def main():
    InstabuyProducts = ProductIntegration()
    InstabuyProducts.update("./assets/data/items.csv", 1000)

if __name__ == '__main__':
    main()
