class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"Item(name={self.name}, sell_in={self.sell_in}, quality={self.quality})"
