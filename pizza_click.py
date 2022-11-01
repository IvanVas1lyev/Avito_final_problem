import click
import emoji

from log import log
from pizza import RECIPES_DICT, EMOJI_DICT, Pepperoni, Margherita, Hawaiian


@click.group()
def cli() -> None:
    """Cli for pizza"""
    pass


@log("Baked in {:.0f} s!")
def bake(pizza) -> None:
    """Bakes pizza"""
    print(f"Start baking {pizza.name}!")


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--pickup", default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, pickup: bool) -> None:
    """Order pizzas with delivery option"""
    pizza_class = globals()[pizza.title()]
    pizza = pizza_class()

    print(EMOJI_DICT[pizza.name], end="")
    bake(pizza)

    if delivery:
        print(emoji.emojize(':motorcycle:'), end="")
        deliver(pizza)
    elif pickup:
        print(emoji.emojize(':house:'), end="")
        pick(pizza)


@log("Pizza is delivered in {:.0f} s!")
def deliver(pizza) -> None:
    """Delivers baked pizza"""
    print(f"{pizza.name} {pizza.size} size is coming!")


@log("Picked up in {}s!")
def pick(pizza) -> None:
    """Controls process of customer pick-up"""
    print(f"{pizza.name} {pizza.size} size is ready for pick-up!")


@cli.command()
def menu() -> None:
    """Shows pizza menu"""
    for pizza, recipe in RECIPES_DICT.items():
        print(f"{pizza} {EMOJI_DICT[pizza]}: {RECIPES_DICT[pizza]}")


if __name__ == '__main__':
    cli()
