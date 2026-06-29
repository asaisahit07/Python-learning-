cart_value = int(input("Enter the cart value = "))

# Cart Discount
if (cart_value >= 5000):
    discounted_price = cart_value * (20 / 100)
    new_amount = cart_value - discounted_price
    print("Cart discount =", discounted_price)
    print("Amount after cart discount =", new_amount)

elif (cart_value >= 2000):
    discounted_price = cart_value * (10 / 100)
    new_amount = cart_value - discounted_price
    print("Cart discount =", discounted_price)
    print("Amount after cart discount =", new_amount)

else:
    discounted_price = 0
    new_amount = cart_value
    print("No cart discount")
    print("Amount =", new_amount)

# Prime Membership
prime_member = input("Are you a prime member? (YES/NO): ")

if (prime_member.upper() == "YES"):
    additional_discount = new_amount * (5 / 100)
    new_amount = new_amount - additional_discount
    print("Prime discount =", additional_discount)
    print("Amount after prime discount =", new_amount)
else:
    additional_discount = 0
    print("No prime discount")
    print("Amount =", new_amount)

# Coupon
coupon_code = input("Enter the coupon code: ")

if (coupon_code == "SAVE200"):
    if (new_amount >= 1000):
        print("Valid coupon code")
        coupon_discount = 200
        new_amount = new_amount - coupon_discount
        print("Coupon discount =", coupon_discount)
        print("Amount after coupon =", new_amount)
    else:
        coupon_discount = 0
        print("Coupon cannot be applied because amount is less than ₹1000.")
else:
    coupon_discount = 0
    print("Invalid coupon code")

# Delivery Charges
if (new_amount >= 1000):
    delivery_charge = 0
    print("Delivery Charge = FREE")
else:
    delivery_charge = 80
    new_amount = new_amount + delivery_charge
    print("Delivery Charge = ₹80")

# Final Bill
print("\n----------- FINAL BILL -----------")
print("Original Cart Value :", cart_value)
print("Cart Discount       :", discounted_price)
print("Prime Discount      :", additional_discount)
print("Coupon Discount     :", coupon_discount)
print("Delivery Charge     :", delivery_charge)
print("Final Amount        :", new_amount)