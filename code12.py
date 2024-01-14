def countNow(PLACES):
    for key, value in PLACES.items():
        if len(value) > 5:
            print(value.upper())

PLACES = {1: "Delhi", 2: "London", 3: "Paris", 4: "New York", 5: "Doha"}
countNow(PLACES)