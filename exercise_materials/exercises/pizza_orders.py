class Pizza:

    SIZES: dict[str, float] = {
        "Small": 10.00,
        "Medium": 12.00,
        "Large": 15.00,
        "Extra-large": 18.00
    }

    def __init__(self, toppings: list[str], size: str = "Medium") -> None:
        self._toppings: list[str] = toppings

        if size.lower() in [s.lower() for s in self.SIZES]:
            for s in self.SIZES:
                if s.lower() == size.lower():
                    self._size: str = s
        else:
            self._size = "Medium"

    def display(self) -> None:
        print(self._size, "pizza with", ", ".join(self._toppings))

    def get_size(self) -> str:
        return self._size

    def set_size(self, new_size: str) -> bool:
        for size in self.SIZES:
            if size.lower() == new_size.lower():
                self._size = size
                return True

        return False

    def get_num_toppings(self) -> int:
        return len(self._toppings)

    def add_topping(self, topping: str) -> bool:
        self._toppings.append(topping)
        return True

    def remove_topping(self, topping: str) -> bool:
        for item in self._toppings:
            if item.lower() == topping.lower():
                self._toppings.remove(item)
                return True

        return False

    def calc_price(self) -> float:
        price: float = self.SIZES[self._size]
        price = price + (self.get_num_toppings() * 0.85)
        return price
