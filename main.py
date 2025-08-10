import sys, os
import pandas as pd

APP_NAME: str = "Pomocnik Anki"
APP_VERSION: str = "1.1.0"
DEBUG:bool = "--debug" in sys.argv
INFO:bool = "--info" in sys.argv
nazwa_pliku_tsv: str = "domyslna_nazwa_pliku_tsv_dla_programu_Anki"
katalog_dla_plikow_tsv: str = ""

# TEMP
slownik: dict[str, str]= {
    "lolo" : "momo"
}
# NOTE - słownik ma być pobierany z osobnego pliku

def debug_print(tekst: str) -> None:
    if DEBUG:
        input(f"DEBUG: {tekst}. Naciśnij ENTER aby kontynuować !!!")
    return None

def info_print(tekst: str) -> None:
    if INFO or DEBUG:
        input(f"INFO: {tekst}. Naciśnij ENTER aby kontynuować !!!")
    return None

# DEPRECATED
def program101() -> None:
    debug_print(f"Oto pythonowy słownik przekształcany do pliku tsv.\n{slownik}")
    debug_print("Przekształcam słownik do listy.")
    dict_to_csv = list(slownik.items())
    debug_print(f"Oto lista powstała ze słownika, która teraz zostanie zapisana do pliku tsv.\n{dict_to_csv}")
    debug_print("Tworzę z listy DataFrame.")
    lista_do_csv: pd.DataFrame = pd.DataFrame(dict_to_csv)
    debug_print("Zapisuje DataFrame do pliku tsv.")
    lista_do_csv.to_csv(f"{nazwa_pliku_tsv}.tsv", sep="\t", index=False, header=False, encoding="utf-8")
    debug_print("Plik zapisany, ale jeszcze nie wiem czy poprawnie.")
    return None

def program():
    debug_print(f"Oto pythonowy słownik przekształcany do pliku tsv.\n{slownik}")
    info_print("Przekształcam słownik do listy.")
    # HACK - otypować dict_to_csv
    dict_to_csv = list(slownik.items())
    debug_print(f"Oto lista powstała ze słownika, która teraz zostanie zapisana do pliku tsv.\n{dict_to_csv}")
    debug_print("Tworzę z listy DataFrame.")
    lista_do_csv: pd.DataFrame = pd.DataFrame(dict_to_csv)
    debug_print("Rozpoczynam etap zapisywania DataFrame do pliku tsv.")
    debug_print("Tworze katalog gdzie będą zapisane pliki tsv. Miejsce zapisu zależy od tego czy użytkownik skorzystał"
                " z flagi --folder")
    if katalog_dla_plikow_tsv =="":
        sciezka_do_katalogu_dla_zapisanych_plikow_tsv = "tsv_to_anki"
    else:
        sciezka_do_katalogu_dla_zapisanych_plikow_tsv = os.path.join("tsv_to_anki", katalog_dla_plikow_tsv)
    os.makedirs(name=sciezka_do_katalogu_dla_zapisanych_plikow_tsv, exist_ok=True)
    sciezka_do_zapisywanego_pliku_tsv = os.path.join(sciezka_do_katalogu_dla_zapisanych_plikow_tsv, nazwa_pliku_tsv)
    info_print(f"Zapisuje plik tsv w katalogu {sciezka_do_katalogu_dla_zapisanych_plikow_tsv}")
    lista_do_csv.to_csv(sciezka_do_zapisywanego_pliku_tsv, sep="\t", index=False, header=False, encoding="utf-8")
    debug_print("Plik zapisany, ale jeszcze nie wiem czy poprawnie.")
    return None

if __name__ == "__main__":
    if "--help" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        Pomoc do programu {APP_NAME}:

        Funkcja programu:
            Program ułatwiający współpracę z programem Anki, którego funkcja polega na przekształcaniu pythonowego 
            słownika ze słówkami angielskimi i polskimi do plików tsv, celem ich późniejszego dodania do programu Anki.
            
        Flagi:
            --help - pomoc,
            --version - wersja programu,
            --history - historia wersji programu,
            --folder nazwa - nazwa katalogu, w którym są zapisywane pliki tsv (domyślnie: tsv_to_anki),
            --output nazwa - zapisuje do pliku tsv: nazwa.tsv (z ochroną przed błędnym wpisaniem rozszerzenia tsv),
            --info - uruchomienie programu w trybie z informacjami o rozpoczęciu poszczególnych etapów pracy programu,
            --debug - uruchamianie programu w trybie debug.
        """)
        sys.exit()
    if "--version" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        Program {APP_NAME} - Wersja {APP_VERSION}
        """)
        sys.exit()
    if "--history" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        Historia wersji programu {APP_NAME}. Aktualna wersja: {APP_VERSION}.
        
        1.1.0
        Wprowadzenie flagi --folder wymusiło spore zmiany w kodzie a sama flaga spowodowała duże usprawnienie
        w automatyzacji pracy programu.
        Poza tym:
        - poprawki zauważonych błędów w wyświetlanych informacjach debug dla flagi --output.
        - zmiany w kodzie funkcji info_debug jak i logice jej działania.
        
        1.0.1
        Poprawka zapobiegająca błędowi związanemu z wpisaniem bezpośrednio po fladze --output innej flagi, z pominięciem
        nazwy pliku tsv i błędnemu zapisaniu pliku tsv pod nazwą flagi wpisanej po fladze --output.
        
        1.0.0
        Działający program, który przekształca słownik ze słówkami angielskimi i polskimi do plików tsv, celem ich
        późniejszego dodania do programu Anki.
        Program wykorzystuje flagi CLI.
        Słownik jest w kodzie pliku main.py.
        """)
        sys.exit()
    # HACK - otypować co jeszcze nie jest otypowane
    if "--folder" in sys.argv:
        index = sys.argv.index("--folder")
        try:
            if sys.argv[index + 1].startswith("--"):
                print("Uwaga błąd !!! W miejscu nazwy katalogu wpisano flagę.")
                sys.exit(1)
            if index + 1 < len(sys.argv):
                katalog_dla_plikow_tsv = sys.argv[index + 1]
            else:
                debug_print("Błąd, nie podano nazwy pliku !!!")
                sys.exit(1)
        except IndexError as error:
            debug_print(f"Wystąpił błąd związany z wystąpieniem wyjątku: {error}, ale to nie ma znaczenia.")
            print("Błąd !!! Nie podano nazwy katalogu !!!")
            sys.exit(1)
    if "--output" in sys.argv:
        index = sys.argv.index("--output")
        try:
            if sys.argv[index + 1].startswith("--"):
                print("Uwaga błąd !!! W miejscu nazwy pliku wpisano flagę.")
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
    info_print("Do zobaczenia !!!")
    sys.exit()

# TODO - flaga określająca katalog gdzie będą szukane pliki ze słownikami, z uwzględnieniem podkatalogów,
# TODO - przeszukanie katalogu w poszukiwaniu plików .py ze słownikami
# TODO - odczytanie pliku jeżeli zostanie znaleziony
# DONE - nazwanie pliku tsv:
#   - jeżeli użytkownik wykorzysta flagę --output: nazwa pliku jest taka jaką podano po fladze --output
#   - jeżeli użytkownik nie wykorzysta flagi --output: nazwy pliku pozostaje bez zmian, zmienia się tylko rozszerzenie
#   z .py na.tsv
# DONE- zapis pliku na dysku w katalogu o podanej nazwie lub w domyślnym miejscu
# TODO - archiwizacja pliku .py w odpowiednim katalogu
# TODO - biblioteka ?Path? zamiast flag
# TODO - wersja z innym rozwiązaniem niż moduł os
