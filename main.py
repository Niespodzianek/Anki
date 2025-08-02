import pandas as pd

slownik = {"house" : "dom", "car" : "samochód", "cat" : "kot", "dog" : "pies"}
dane_do_csv = []
for key, value in slownik.items():
    dane_do_csv.append({"angielski": key, "polski": value})

print(dane_do_csv)

slowka = pd.DataFrame(dane_do_csv)
slowka.to_csv("slowka.csv", index=False, encoding="utf-8", header=False, sep="\t")
