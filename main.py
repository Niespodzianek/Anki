import pandas as pd

slownik = {"house" : "dom", "car" : "samochód", "cat" : "kot", "dog" : "pies"}
slownik_pd = pd.DataFrame(slownik, index=[0])
slownik_pd.to_csv("slownik.csv", index=False)
