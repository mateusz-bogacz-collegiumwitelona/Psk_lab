import math
import random
import statistics


# Parametry zadania
LAMBDA_SZKOD = 10.0          # intensywnosc procesu Poissona [szkody/dzien]
SREDNIA_SZKODA = 1000.0      # srednia kwoty szkody
STAWKA_WPLAT = 11000.0       # ciagly naplyw wplat [jednostek/dzien]
KAPITAL_POCZATKOWY = 25000.0
HORYZONT_CZASU = 365.0       # dni

# Parametry symulacji Monte Carlo
LICZBA_REPLIKACJI = 100_000
ZIARNO_LOSOWOSCI = 42


def symuluj_jedna_sciezke():
    """
    Jedna replikacja metody zdarzen dyskretnych.
    Zwraca True, jesli kapital pozostaje dodatni przez caly okres [0, T].
    """
    czas = 0.0
    kapital = KAPITAL_POCZATKOWY

    while True:
        odstep = random.expovariate(LAMBDA_SZKOD)
        czas_szkody = czas + odstep

        if czas_szkody > HORYZONT_CZASU:
            # Do konca horyzontu kapital rosnie liniowo, nie ma juz szkod.
            kapital += STAWKA_WPLAT * (HORYZONT_CZASU - czas)
            return kapital > 0.0

        # Naplyw wplat do chwili zgloszenia szkody
        kapital += STAWKA_WPLAT * (czas_szkody - czas)
        czas = czas_szkody

        kwota_szkody = random.expovariate(1.0 / SREDNIA_SZKODA)
        kapital -= kwota_szkody

        if kapital <= 0.0:
            return False


def przedzial_ufnosci_dla_proporcji(sukcesy, proby, poziom_ufnosci=0.95):
  """Przyblizony przedzial ufnosci dla estymatora prawdopodobienstwa."""
  if proby == 0:
    return None

  p_hat = sukcesy / proby
  alpha = 1.0 - poziom_ufnosci
  z = 1.959963984540054  # dla 95% (duza proba)

  mianownik = 1.0 + z**2 / proby
  srodek = (p_hat + z**2 / (2.0 * proby)) / mianownik
  margines = (
      z
      * math.sqrt((p_hat * (1.0 - p_hat) + z**2 / (4.0 * proby)) / proby)
      / mianownik
  )

  return max(0.0, srodek - margines), min(1.0, srodek + margines), p_hat


def main():
    random.seed(ZIARNO_LOSOWOSCI)

    wyniki = [symuluj_jedna_sciezke() for _ in range(LICZBA_REPLIKACJI)]
    sukcesy = sum(1 for wynik in wyniki if wynik)
    niepowodzenia = LICZBA_REPLIKACJI - sukcesy

    p_hat = sukcesy / LICZBA_REPLIKACJI
    puf = przedzial_ufnosci_dla_proporcji(sukcesy, LICZBA_REPLIKACJI)

    print("=== LISTA 2, ZADANIE 5 ===")
    print("Metoda zdarzen dyskretnych - kapital firmy ubezpieczeniowej")
    print()
    print("--- Parametry modelu ---")
    print(f"Intensywnosc szkod (proces Poissona): {LAMBDA_SZKOD} / dzien")
    print(f"Srednia kwoty szkody (wykladniczy): {SREDNIA_SZKODA}")
    print(f"Stawka wplat: {STAWKA_WPLAT} / dzien")
    print(f"Kapital poczatkowy: {KAPITAL_POCZATKOWY}")
    print(f"Horyzont czasowy: {HORYZONT_CZASU} dni")
    print()
    print("--- Symulacja Monte Carlo ---")
    print(f"Liczba replikacji: {LICZBA_REPLIKACJI}")
    print(f"Ziarno generatora: {ZIARNO_LOSOWOSCI}")
    print()
    print("--- Wyniki ---")
    print(f"Liczba scenariuszy z dodatnim kapitalem: {sukcesy}")
    print(f"Liczba scenariuszy z kapital <= 0: {niepowodzenia}")
    print(f"Estymacja prawdopodobienstwa p_hat: {p_hat:.6f}")
    if puf is not None:
        print(
            f"95% przedzial ufnosci dla p_hat: "
            f"({puf[0]:.6f}, {puf[1]:.6f})"
        )
    print()
    print("--- Odpowiedz ---")
    print(
        "Szacowane prawdopodobienstwo, ze kapital pozostanie dodatni "
        f"w ciagu pierwszych {int(HORYZONT_CZASU)} dni:"
    )
    print(f"p ≈ {p_hat:.4f} ({p_hat * 100:.2f}%)")


if __name__ == "__main__":
    main()
