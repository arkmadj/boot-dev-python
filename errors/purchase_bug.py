def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price

try:
    print(purchase_item(18, 10))
except Exception as e:
    print(e)
