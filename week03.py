# set은 순서가 없음

def duplicate_city(cites):
    result_city = []
    s = set()

    for city in cites:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)

    return set(result_city)


cities = ["Incheon","Seoul","Incheon","Incheon","Gwangju"]
# cities = set(cities)
# cities.add("Incheon")
# cities.add("Suwon")
cities.append("Suwon")
cities.append("Incheon")
cities.append("Seoul")
print(cities)
print(duplicate_city(cities))