import click

"""Pizza module"""

recipes_dict = {"Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"],
                "Margherita": ["tomato sauce", "mozzarella", "tomatoes"],
                "Hawaiian": ["tomato sauce", "mozzarella", "chicken", "pineapples"]}


class Pizza:
    """Common class for all types pizzas"""

    def __init__(self, size: str = "L", name: str = "Pepperoni") -> None:
        """Init pizza"""
        self.name = name
        self.recipe = recipes_dict[name]
        self.size = size

    def __eq__(self, other: object) -> bool:
        """Check if pizzas are equal"""
        if self.name == other.name and self.size == other.size:
            return True
        else:
            return False

    def dict(self) -> None:
        """Print pizza recipe in dict format"""
        print(f"{self.name} : {self.recipe}")






@click.group()
def cli() -> None:
    """Cli for pizza"""
    pass




@cli.command()
def menu():
    """Выводит меню"""
    print("\N{winking face}")


if __name__ == "__main__":
    cli()
