from item import Item
from gilded_rose import GildedRose

import pytest

BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
MANA_CAKE = "Conjured Mana Cake"


def do_test_for_item_with_decrementing_sell_in(name: str, sell_in, current_quality,
                                               expected_quality):
    item = Item(name, sell_in, current_quality)
    expected = Item(name, sell_in - 1, expected_quality)
    do_one_item_test(item, expected)


def do_one_item_test(item: Item, expected_item: Item):
    GildedRose([item]).update_quality()
    assert item.quality == expected_item.quality, "QUALITY"
    assert item.sell_in == expected_item.sell_in, "SELL_IN"


def test_normal_item_degrades_when_not_expired():
    sell_in = 5
    quality = 7
    item = Item("foo", sell_in, quality)
    expected_item = Item("bar", sell_in - 1, quality - 1)
    do_one_item_test(item, expected_item)


def test_normal_item_quality_does_not_degrade_when_quality_is_zeron():
    sell_in = 5
    zero_quality = 0
    item = Item("foo", sell_in, zero_quality)
    expected_item = Item("bar", sell_in - 1, zero_quality)
    do_one_item_test(item, expected_item)


def test_normal_item_degrades_double_when_expire_is_zeron():
    sell_now = 0
    quality = 7
    item = Item("foo", sell_now, quality)
    expected_item = Item("bar", sell_now - 1, quality - 2)
    do_one_item_test(item, expected_item)


def test_normal_item_degrades_double_when_expire_is_less_than_zeron():
    too_late_get_rid_of_it = -1
    quality = 7
    item = Item("foo", too_late_get_rid_of_it, quality)
    expected_item = Item("bar", too_late_get_rid_of_it - 1, quality - 2)
    do_one_item_test(item, expected_item)


def test_sulfuras_quality_does_not_change():
    sell_in = 3
    quality = 80
    item = Item(SULFURAS, sell_in, quality)
    expected_item = Item("bar", sell_in, quality)
    do_one_item_test(item, expected_item)


def test_sulfuras_quality_does_not_change_when_expired():
    sell_in = -1
    quality = 80
    item = Item(SULFURAS, sell_in, quality)
    expected_item = Item("bar", sell_in, quality)
    do_one_item_test(item, expected_item)


def test_aged_brie_quality_increases_by_one_if_not_expired():
    sell_in = 1
    other_sell_in = 6
    quality = 5
    expected_quality = quality + 1
    do_test_for_item_with_decrementing_sell_in(AGED_BRIE, sell_in, quality, expected_quality)
    do_test_for_item_with_decrementing_sell_in(AGED_BRIE, other_sell_in, quality, expected_quality)


def test_aged_brie_quality_caps_at_fifty():
    sell_in = 1
    quality = 50
    item = Item(AGED_BRIE, sell_in, quality)
    expected_item = Item("bar", sell_in - 1, quality)
    do_one_item_test(item, expected_item)


def test_aged_brie_quality_increases_by_two_if_expired():
    sell_in = 0
    quality = 5
    item = Item(AGED_BRIE, sell_in, quality)
    expected_item = Item("bar", sell_in - 1, quality + 2)
    do_one_item_test(item, expected_item)


def test_aged_brie_quality_caps_at_fifty_when_expired():
    sell_in = 0
    quality = 50
    item = Item(AGED_BRIE, sell_in, quality)
    expected_item = Item("bar", sell_in - 1, quality)
    do_one_item_test(item, expected_item)


def test_aged_brie_quality_increases_by_two_when_super_expired():
    sell_in = -1
    quality = 40
    item = Item(AGED_BRIE, sell_in, quality)
    expected_item = Item("bar", sell_in - 1, quality + 2)
    do_one_item_test(item, expected_item)


def test_aged_brie_quality_caps_at_fifty_when_super_expired():
    sell_in = -1
    quality = 50
    item = Item(AGED_BRIE, sell_in, quality)
    expected_item = Item("bar", sell_in - 1, quality)
    do_one_item_test(item, expected_item)


def test_aged_brie_quality_caps_at_fifty_when_forty_nine_and_expired():
    sell_in = 0
    quality = 49
    top_quality = 50
    item = Item(AGED_BRIE, sell_in, quality)
    expected_item = Item("bar", sell_in - 1, top_quality)
    do_one_item_test(item, expected_item)


def test_backstage_pass_increases_by_one_when_greater_than_ten():
    sell_in = 11
    other_sell_in = 100
    quality = 20
    expected_quality = quality + 1
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in, quality, expected_quality)
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, other_sell_in, quality,
                                               expected_quality)


def test_backstage_pass_increases_by_two_when_between_six_and_ten():
    sell_in_top = 10
    sell_in_mid = 7
    sell_in_bottom = 6
    quality = 20
    expected_quality = quality + 2
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in_top, quality,
                                               expected_quality)
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in_mid, quality,
                                               expected_quality)
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in_bottom, quality,
                                               expected_quality)


def test_backstage_pass_increases_by_two_when_between_one_and_five():
    sell_in_top = 5
    sell_in_mid = 3
    sell_in_bottom = 1
    quality = 20
    expected_quality = quality + 3
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in_top, quality,
                                               expected_quality)
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in_mid, quality,
                                               expected_quality)
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in_bottom, quality,
                                               expected_quality)


def test_backstage_pass_goes_to_zero_when_expired():
    sell_in = 0
    other_sell_in = -1
    quality = 20
    expected_quality = 0
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in, quality, expected_quality)
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, other_sell_in, quality,
                                               expected_quality)


def test_backstage_pass_caps_at_fifty():
    sell_in = 1
    quality1 = 48
    quality2 = 49
    expected_quality = 50
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in, quality1,
                                               expected_quality)
    do_test_for_item_with_decrementing_sell_in(BACKSTAGE_PASSES, sell_in, quality2,
                                               expected_quality)


# def test_conjured_items_decrease_in_quality_twice_as_fast():
