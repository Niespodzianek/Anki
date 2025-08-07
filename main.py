import sys, os
import pandas as pd

APP_NAME: str = "Pomocnik Anki"
APP_VERSION: str = "1.0.1"
DEBUG:bool = "--debug" in sys.argv
QUIET:bool = "--quiet" in sys.argv
nazwa_pliku_tsv: str = "domyslna_nazwa_pliku_tsv_dla_programu_Anki"

# --------------------------------------------------------------------
# ----------  PONIŻEJ UMIESZCZAMY, CHWILOWO, KOD SŁOWNIKA  -----------
# --------------------------------------------------------------------
# -----------------------------  KOD  --------------------------------
# --------------------------------------------------------------------
# ------------------------  KONIEC SŁOWNIKA  -------------------------
# --------------------------------------------------------------------

slownik: dict[str, str] = {
    "after": "po"
}

def debug_print(tekst: str) -> None:
    if DEBUG:
        input(f"DEBUG: {tekst} Naciśnij ENTER aby kontynuować !!!")
    return None

def info_print(tekst: str):
    if QUIET:
        print(f"INFO: {tekst}")
    return None

def program() -> None:
    lista_do_csv: pd.DataFrame
    debug_print(f"Oto pythonowy słownik przekształcany do pliku tsv.\n{slownik}")
    debug_print("Przekształcam słownik do listy.")
    dicts = list(slownik.items())
    debug_print(f"Oto lista powstała ze słownika, która teraz zostanie zapisana do pliku tsv.\n{dicts}")
    debug_print("Tworzę z listy DataFrame.")
    lista_do_csv = pd.DataFrame(dicts)
    debug_print("Zapisuje DataFrame do pliku tsv.")
    lista_do_csv.to_csv(f"{nazwa_pliku_tsv}.tsv", sep="\t", index=False, header=False, encoding="utf-8")
    debug_print("Plik zapisany, ale jeszcze nie wiem czy poprawnie.")
    return None

if __name__ == "__main__":
    if "--help" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""Pomoc do programu {APP_NAME}:

        Funkcja programu:
            Program ułatwiający współpracę z programem Anki.
            Aktualnie, program przekształca słowniki ze słówkami angielskimi i polskimi do plików tsv,
            celem ich późniejszego dodania do programu Anki.
            
        Flagi:
            --help - pomoc,
            --version - wersja programu,
            --history - historia wersji programu,
            --output plik - zapisuje do pliku tsv o nazwie plik.tsv (należy wpisać nazwę pliku bez rozszerzenia tsv),
            --quiet - uruchomienie programu w trybie z komentarzami,
            --debug - uruchamianie programu w trybie debug.
        """)
        sys.exit()
    if "--version" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Program {APP_NAME} - Wersja {APP_VERSION}")
        sys.exit()
    if "--history" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""Historia wersji programu {APP_NAME}. Aktualna wersja: {APP_VERSION}.
        
        1.0.1
        Poprawka zapobiegająca błędowi związanemu z wpisaniem bezpośrednio po fladze --output innej flagi, z pominięciem
        nazwy pliku tsv i błędnemu zapisaniu pliku tsv pod nazwą flagi wpisanej po fladze --output.
        
        1.0.0
        Program przekształca słownik ze słówkami angielskimi i polskimi do plików tsv, celem ich późniejszego
        dodania do programu Anki. Słownik jest w kodzie pliku main.py.
        """)
        sys.exit()
    if "--quiet" in sys.argv:
        DEBUG = False
    if "--output" in sys.argv:
        index = sys.argv.index("--output")
        try:
            if sys.argv[index + 1].startswith("--"):
                print("Uwaga błąd !!! W miejscu symbolu spółki wpisano flagę.")
                sys.exit(1)
            if index + 1 < len(sys.argv):
                nazwa_pliku_tsv = sys.argv[index + 1]
                if nazwa_pliku_tsv.endswith(".tsv"):
                    nazwa_pliku_tsv = nazwa_pliku_tsv[:-4]
            else:
                debug_print("Błąd, nie podano nazwy pliku !!!")
                sys.exit(1)
        except IndexError as error:
            debug_print(f"Wystąpił błąd związany z wystąpieniem wyjątku: {error}, ale to nie ma znaczenia.")
            print("Błąd !!! Nie podano nazwy pliku !!!")
            sys.exit(1)
    os.system("cls" if os.name == "nt" else "clear")
    info_print("Program pracuje !!!")
    program()
    info_print("\nDo zobaczenia !!!")
    sys.exit()

# todo - pobieranie słownika z pliku z kontrolą błędów
# todo - pobieranie słowników z plików z kontrolą błędów
# todo - wpisywanie nazw plików z flagami CLI