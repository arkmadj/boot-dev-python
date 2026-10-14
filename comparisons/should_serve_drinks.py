def should_serve_customer(customer_age, on_break, time):
    if customer_age < 21:
        return False
    elif on_break:
        return False
    elif time < 5 and time > 10:
        return False
    return True


print(should_serve_customer(21, False, 6))
print(should_serve_customer(21, True, 6))
print(should_serve_customer(12, False, 6))
print(should_serve_customer(21, False, 1))
print(should_serve_customer(21, False, 16))
