import sys
sys.path.append(".")
from gilded_rose import update_quality, Item

def test_normal_item_quality_decreases():
    items = [Item("Normal Item", 5, 10)]
    new_items = update_quality(items)
    assert new_items[0].quality == 9

def test_normal_item_quality_decreases_twice_after_sell_in():
    items = [Item("Normal Item", 0, 10)]
    new_items = update_quality(items)
    assert new_items[0].quality == 8

def test_quality_never_negative():
    items = [Item("Normal Item", 0, 0)]
    new_items = update_quality(items)
    assert new_items[0].quality == 0

def test_aged_brie_quality_increases():
    items = [Item("Aged Brie", 5, 10)]
    new_items = update_quality(items)
    assert new_items[0].quality == 11

def test_quality_never_more_than_50():
    items = [Item("Aged Brie", 5, 50)]
    new_items = update_quality(items)
    assert new_items[0].quality == 50

def test_sulfuras_quality_never_changes():
    items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
    new_items = update_quality(items)
    assert new_items[0].quality == 80

def test_backstage_passes_quality_increases_by_1():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
    new_items = update_quality(items)
    assert new_items[0].quality == 11

def test_backstage_passes_quality_increases_by_2_when_10_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
    new_items = update_quality(items)
    assert new_items[0].quality == 12

def test_backstage_passes_quality_increases_by_3_when_5_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
    new_items = update_quality(items)
    assert new_items[0].quality == 13

def test_backstage_passes_quality_drops_to_0_after_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
    new_items = update_quality(items)
    assert new_items[0].quality == 0

def test_sulfuras_quality_never_changes_even_after_sellin():
    items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
    new_items = update_quality(items)
    assert new_items[0].quality == 80