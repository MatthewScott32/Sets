showroom = set()
showroom.add("wrangler")
showroom.add("waggoneer")
showroom.add("batmobile")
showroom.add("A-Team Van")
print(showroom)
print(len(showroom))
showroom.add("batmobile")
print(showroom)
showroom.update(["Hummer", "Station Wagon"])
print(showroom)
showroom.discard("Station Wagon")
print(showroom)

junkyard = {"Ford F-150", "Camaro", "El Camino", "waggoneer",
            "Hummer"}
print(junkyard)

matches = showroom.intersection(junkyard)
print(matches)

new_showroom = showroom.union(junkyard)
print(new_showroom)
new_showroom.discard("Ford F-150")
new_showroom.discard("Hummer")
print(new_showroom)