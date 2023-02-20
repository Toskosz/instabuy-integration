

class Product:

    def __init__(self) -> None:
        self.internal_code: str
        self.barcode: list[str]
        self.name: str
        self.price: float
        self.promo_price: float
        self.promo_end_at: str
        self.stock: float 
        self.visible: bool

