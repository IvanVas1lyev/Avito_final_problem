import emoji


RECIPES_DICT = {"Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"],
                "Margherita": ["tomato sauce", "mozzarella", "tomatoes"],
                "Hawaiian": ["tomato sauce", "mozzarella", "chicken", "pineapples"]}

EMOJI_DICT = {"Pepperoni": emoji.emojize(':pizza:'),
              "Margherita": emoji.emojize(':tomato:'),
              "Hawaiian": emoji.emojize(':pineapple:')}


class Pepperoni:
    def __init__(self, size: str = "L") -> None:
        """Init pizza"""
        self.name = "Pepperoni"
        self.recipe = ["tomato sauce", "mozzarella", "pepperoni"]
        self.size = size
        self.emoji = emoji.emojize(':pizza:')

    def __eq__(self, other) -> bool:
        """Check if pizzas are equal"""
        if self.name == other.name and self.size == other.size:
            return True
        else:
            return False

    def dict(self) -> str:
        """Print pepperoni recipe in dict format"""
        return f"'{self.name}': {self.recipe}"


class Hawaiian:
    def __init__(self, size: str = "L") -> None:
        """Init pizza"""
        self.name = "Hawaiian"
        self.recipe = ["tomato sauce", "mozzarella", "chicken", "pineapples"]
        self.size = size
        self.emoji = emoji.emojize(':pineapple:')

    def __eq__(self, other) -> bool:
        """Check if pizzas are equal"""
        if self.name == other.name and self.size == other.size:
            return True
        else:
            return False

    def dict(self) -> str:
        """Print hawaiian recipe in dict format"""
        return f"'{self.name}': {self.recipe}"


class Margherita:
    def __init__(self, size: str = "L") -> None:
        """Init pizza"""
        self.name = "Margherita"
        self.recipe = ["tomato sauce", "mozzarella", "tomatoes"]
        self.size = size
        self.emoji = emoji.emojize(':tomato:')

    def __eq__(self, other) -> bool:
        """Check if pizzas are equal"""
        if self.name == other.name and self.size == other.size:
            return True
        else:
            return False

    def dict(self) -> str:
        """Print margherita recipe in dict format"""
        return f"'{self.name}': {self.recipe}"


if __name__ == "__main__":
    first_pizza = Pepperoni("L")
    print(first_pizza.dict())

    second_pizza = Hawaiian("XL")
    print(second_pizza.dict())

    print(second_pizza.__eq__(first_pizza))
