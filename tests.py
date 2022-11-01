import pytest
from click.testing import CliRunner

from pizza_click import order, menu
from pizza import Pepperoni, Hawaiian, Margherita


PIZZAS = ["Margherita", "Pepperoni", "Hawaiian"]
SIZES = ["L", "XL"]


@pytest.mark.parametrize(
    "source, exp",
    [
        ("Pepperoni", "'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni']"),
        ("Margherita", "'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']"),
        ("Hawaiian", "'Hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']")
    ]
)
def test_pizza_dict(source: str, exp: str) -> None:
    """Test pizza dict method"""
    pizza_class = globals()[source]
    pizza = pizza_class()

    assert str(pizza.dict()) == exp


def test_menu() -> None:
    """Test menu"""
    runner = CliRunner()
    result = runner.invoke(menu)

    assert result.exit_code == 0
    assert "tomato sauce" in result.output
    assert "Pepperoni" in result.output


@pytest.mark.parametrize(
    "s, exp",
    [
        (PIZZAS[0], f"Start baking {PIZZAS[0]}!"),
        (PIZZAS[1], f"Start baking {PIZZAS[1]}!"),
        (PIZZAS[2],  f"Start baking {PIZZAS[2]}!"),
    ]
)
def test_bake(s: str, exp: str) -> None:
    """Test bake"""
    runner = CliRunner()
    result = runner.invoke(order, s.lower())

    assert result.exit_code == 0
    assert exp in result.output


def test_order_with_delivery() -> None:
    """Test order with delivery"""
    runner = CliRunner()
    result = runner.invoke(order, [PIZZAS[0], "--delivery"])

    assert result.exit_code == 0
    assert f"{PIZZAS[0]} L size is coming!" in result.output
    assert "Pizza is delivered in" in result.output


def test_order_with_pickup() -> None:
    """Test order with pickup"""
    runner = CliRunner()
    result = runner.invoke(order, [PIZZAS[1], "--pickup"])

    assert result.exit_code == 0
    assert f"{PIZZAS[1]} L size is ready for pick-up!" in result.output
    assert "Picked up in" in result.output
