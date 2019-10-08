from item import Item
from gilded_rose import GildedRose

import pytest


def test_regular_items_decrease_by_one():
    items = [Item("+5 Dexterity Vest", 10, 20)]
    GildedRose.update_quality(items)
    expected = {'sell_in': 9, 'quality': 19}
    item = items[0]
    assert item.quality == expected['quality']
    assert item.sell_in == expected['sell_in']


def test_quality_goes_up_for_improving_products():
    items = [Item("Aged Brie", 20, 30)]
    items.append(Item("Backstage passes to a TAFKAL80ETC concert", 20, 30))
    GildedRose.update_quality(items)
    expected = [
        {'sell_in': 19, 'quality': 31},
        {'sell_in': 19, 'quality': 31},
    ]

    for index, expectation in enumerate(expected):
        item = items[index]
        assert item.quality == expectation['quality']
        assert item.sell_in == expectation['sell_in']


def test_quality_goes_up_by_two_for_improving_products_with_10_days_or_less_left():
    items = [Item("Aged Brie", 10, 34)]
    items.append(Item("Backstage passes to a TAFKAL80ETC concert", 8, 30))
    GildedRose.update_quality(items)
    expected = [
        {'sell_in': 9, 'quality': 36},
        {'sell_in': 7, 'quality': 32},
    ]

    for index, expectation in enumerate(expected):
        item = items[index]
        assert item.quality == expectation['quality']
        assert item.sell_in == expectation['sell_in']


def test_quality_goes_up_by_three_for_improving_products_with_5_days_or_less_left():
    items = [Item("Aged Brie", 4, 11)]
    items.append(Item("Backstage passes to a TAFKAL80ETC concert", 5, 15))
    GildedRose.update_quality(items)
    expected = [
        {'sell_in': 3, 'quality': 14},
        {'sell_in': 4, 'quality': 18},
    ]

    for index, expectation in enumerate(expected):
        item = items[index]
        assert item.quality == expectation['quality']
        assert item.sell_in == expectation['sell_in']


def test_quality_and_sellin_decrease_twice_as_fast_after_sell_by():
    items = [Item("+5 Dexterity Vest", 0, 20)]
    items.append(Item("Conjured Mana Cake", 0, 6))
    GildedRose.update_quality(items)
    expected = [
        {'sell_in': -1, 'quality': 18},
        {'sell_in': -1, 'quality': 4},
    ]

    for index, expectation in enumerate(expected):
        item = items[index]
        assert item.quality == expectation['quality']
        assert item.sell_in == expectation['sell_in']


def test_backstage_passes_and_brie_go_to_quality_zero_after_sell_by():
    items = [Item("Aged Brie", 0, 20)]
    items.append(Item("Backstage passes to a TAFKAL80ETC concert", 0, 20))
    GildedRose.update_quality(items)
    expected = [
        {'sell_in': -1, 'quality': 0},
        {'sell_in': -1, 'quality': 0},
    ]

    for index, expectation in enumerate(expected):
        item = items[index]
        assert item.quality == expectation['quality']
        assert item.sell_in == expectation['sell_in']


def test_sulfuras_the_immutable():
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    GildedRose.update_quality(items)
    expected = {'sell_in': 0, 'quality': 80}
    item = items[0]
    assert item.quality == expected['quality']
    assert item.sell_in == expected['sell_in']


def test_quality_does_not_increase_past_50():
    items = [Item("Aged Brie", 4, 49)]
    GildedRose.update_quality(items)
    expected = {'sell_in': 3, 'quality': 50}
    item = items[0]
    assert item.quality == expected['quality']
    assert item.sell_in == expected['sell_in']


@pytest.mark.xfail(reason="Reasons!!!")
def test_conjured_items_decrease_in_quality_twice_as_fast():
    items = [Item("Conjured Mana Cake", 3, 6)]
    GildedRose.update_quality(items)
    expected = {'sell_in': 2, 'quality': 2}
    item = items[0]
    assert item.quality == expected['quality']
    assert item.sell_in == expected['sell_in']
