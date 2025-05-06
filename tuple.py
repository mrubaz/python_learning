countries = ("Pakistan", "India", "UAE")
temp = list(countries)
print(countries)

temp.append("Germany")  # add item

temp.pop(1)  # remoove item


temp[1] = "UK"  # change item


countries = tuple(temp)
print(countries)
