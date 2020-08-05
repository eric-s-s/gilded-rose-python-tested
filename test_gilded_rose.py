from item import Item
from gilded_rose import GildedRose

import pytest

BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
MANA_CAKE = "Conjured Mana Cake"


def all_sell_in():
    return negative_sell_in() + positive_sell_in()


def positive_sell_in():
    return [1, 4, 5, 6, 10, 11, 12]


def negative_sell_in():
    return [-1, 0]


@pytest.mark.parametrize(
    "quality", [0, 1, 49, 50], ids=lambda el: "quality:{}".format(el)
)
@pytest.mark.parametrize(
    "sell_in", all_sell_in(), ids=lambda el: "sell_in:{}".format(el)
)
def test_sulfuras_does_not_change(quality, sell_in):
    item = Item(SULFURAS, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.sell_in == sell_in
    assert item.quality == quality


@pytest.mark.parametrize("quality", [0, 1, 49, 50])
@pytest.mark.parametrize("sell_in", all_sell_in())
@pytest.mark.parametrize("item", ["foo", BACKSTAGE_PASSES, AGED_BRIE])
def test_sell_in_all_items_but_sulfuras(sell_in, quality, item):
    item = Item(item, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.sell_in == sell_in - 1


@pytest.mark.parametrize(
    "sell_in", positive_sell_in(), ids=lambda el: "sell_in:{}".format(el)
)
@pytest.mark.parametrize(
    "quality,expected_quality", [(0, 0), (1, 0), (2, 1), (49, 48), (50, 49)],
)
def test_quality_regular_item_sell_in_gt_zero(quality, expected_quality, sell_in):
    item_name = "foo"
    item = Item(item_name, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "sell_in", negative_sell_in(), ids=lambda el: "sell_in:{}".format(el)
)
@pytest.mark.parametrize(
    "quality,expected_quality", [(0, 0), (1, 0), (2, 0), (3, 1), (49, 47), (50, 48)],
)
def test_quality_regular_item_sell_in_lte_zero(quality, expected_quality, sell_in):
    item_name = "foo"
    item = Item(item_name, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "sell_in", positive_sell_in(), ids=lambda el: "sell_in:{}".format(el)
)
@pytest.mark.parametrize(
    "quality,expected_quality", [(0, 1), (1, 2), (2, 3), (3, 4), (49, 50), (50, 50)],
)
def test_quality_aged_brie_sell_in_gt_zero(quality, expected_quality, sell_in):
    item = Item(AGED_BRIE, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "sell_in", negative_sell_in(), ids=lambda el: "sell_in:{}".format(el)
)
@pytest.mark.parametrize(
    "quality,expected_quality", [(0, 2), (1, 3), (2, 4), (48, 50), (49, 50), (50, 50)],
)
def test_quality_aged_brie_sell_in_lte_zero(quality, expected_quality, sell_in):
    item = Item(AGED_BRIE, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize("sell_in", [1, 2, 5], ids=lambda el: "sell_in:{}".format(el))
@pytest.mark.parametrize(
    "quality,expected_quality",
    [(0, 3), (1, 4), (2, 5), (47, 50), (48, 50), (49, 50), (50, 50)],
)
def test_quality_backstage_passes_sell_in_one_to_five(
    quality, expected_quality, sell_in
):
    item = Item(BACKSTAGE_PASSES, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize("sell_in", [6, 7, 10], ids=lambda el: "sell_in:{}".format(el))
@pytest.mark.parametrize(
    "quality,expected_quality",
    [(0, 2), (1, 3), (2, 4), (47, 49), (48, 50), (49, 50), (50, 50)],
)
def test_quality_backstage_passes_sell_in_six_to_ten(
    quality, expected_quality, sell_in
):
    item = Item(BACKSTAGE_PASSES, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize("sell_in", [11, 12], ids=lambda el: "sell_in:{}".format(el))
@pytest.mark.parametrize(
    "quality,expected_quality", [(0, 1), (1, 2), (49, 50), (50, 50)],
)
def test_quality_backstage_passes_sell_in_gte_eleven(
    quality, expected_quality, sell_in
):
    item = Item(BACKSTAGE_PASSES, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "sell_in", negative_sell_in(), ids=lambda el: "sell_in:{}".format(el)
)
@pytest.mark.parametrize(
    "quality,expected_quality", [(0, 0), (1, 0), (49, 0), (50, 0)],
)
def test_quality_backstage_passes_sell_in_lte_zero(quality, expected_quality, sell_in):
    item = Item(BACKSTAGE_PASSES, sell_in, quality)
    GildedRose([item]).update_quality()
    assert item.quality == expected_quality
