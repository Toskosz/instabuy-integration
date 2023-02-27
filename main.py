from src.api import API
from src.integrations.product import ProductIntegration

def main():
    InstabuyProducts = ProductIntegration()
    InstabuyProducts.update(api="instabuy", source="./assets/data/items.csv", batch_size=1000)

if __name__ == '__main__':
    main()
