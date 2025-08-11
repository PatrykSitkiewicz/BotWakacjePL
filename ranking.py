import pandas as pd

def calculate_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Oblicza ranking hoteli na podstawie oceny Google i ceny.
    Nadpisuje kolumnę 'Cena' wartościami numerycznymi.
    """

    # Zamień tekstowe ceny na liczby (np. "4 123 zł" → 4123.0)
    df["Cena"] = (
        df["Cena"]
        .astype(str)
        .str.extract(r"(\d+[\s\d,]*)")[0]
        .str.replace(" ", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
        .fillna(0)
    )

    # Punkty za ocenę Google: 4.5 = 0 pkt, każda 0.1 poniżej = -20, powyżej = +20
    def score_ocena(val):
        if pd.isna(val):
            return -300  # kara za brak oceny
        return round((val - 4.5) * 200)  # każda 0.1 = ±20 pkt

    df["Punkty - Ocena"] = df["Ocena Google"].apply(score_ocena)

    # Punkty za cenę (najniższa = 100, najwyższa = 0)
    min_cena = df["Cena"].min()
    max_cena = df["Cena"].max()

    if max_cena != min_cena:
        df["Punkty - Cena"] = df["Cena"].apply(
            lambda x: round(100 * (max_cena - x) / (max_cena - min_cena))
        )
    else:
        df["Punkty - Cena"] = 100

    # Całkowity wynik = suma punktów
    df["Wynik"] = df["Punkty - Ocena"] + df["Punkty - Cena"]

    # Posortuj malejąco wg wyniku
    df = df.sort_values(by="Wynik", ascending=False).reset_index(drop=True)

    return df
