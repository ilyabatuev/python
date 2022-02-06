price = [22, 12, 52.52, 61.52, 132.2, 61, 6.2]

price_id = id(price)
print(id(price))

for last_price, num in enumerate(price):

    new_price = str(f"{float(num):.2f}").split(".")

    if last_price == len(price) - 1:
        perevod_na_stroky = "\n"

    print(f"{new_price[0]} руб {new_price[1]} коп")


price.sort()
print(price)
print(id(price))



copy_price = price.copy()
copy_price.sort(reverse=True)

print(copy_price)
print(id(copy_price))

new_copy_price = copy_price[0: 5]
for last_price in new_copy_price:
    if last_price != new_copy_price[len(new_copy_price) - 1]:
        print(f'{last_price}')
    else:
        print(last_price)























