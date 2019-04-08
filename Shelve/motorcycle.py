import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250"
    bike["colour"] = "red"
    bike["engine"] = 250

    print(bike["engine"])
    print(bike["colour"])

    del bike["colour"]

    for key in bike:
        print(key)

    # print(bike.items())
