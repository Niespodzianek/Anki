import pandas as pd

slownik = {
    "aberration": "odchylenie od normy",
    "disposition": "dyspozycja / usposobienie",
    "geotropism": "geotropizm",
    "inadmissible": "niedopuszczalny",
    "inevitability": "nieuchronność",
    "irreversible": "nieodwracalny",
    "liquidate": "zlikwidować",
    "non-survival": "brak zdolności przetrwania",
    "oblong": "podłużny / wydłużony",
    "penetrated": "przeniknięty",
    "phylogenic": "filogenetyczny",
    "postponement": "odroczenie",
    "reassignment": "przypisanie na nowo",
    "recalibration": "ponowna kalibracja",
    "repudiation": "odrzucenie / wyparcie się",
    "segregated": "odseparowany",
    "specimen": "egzemplarz / okaz",
    "stability": "równowaga / trwałość",
    "submit": "poddawać się / przedstawiać",
    "televocal": "zdalnie sterowany głosowo"
}

dane_do_csv = []
for key, value in slownik.items():
    dane_do_csv.append({"angielski": key, "polski": value})

print(dane_do_csv)

slowka = pd.DataFrame(dane_do_csv)
slowka.to_csv("hello_tomorrow_C2.csv", index=False, encoding="utf-8", header=False, sep="\t")
