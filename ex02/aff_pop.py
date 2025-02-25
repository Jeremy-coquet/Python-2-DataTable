import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def clean_population_data(data: pd.Series) -> pd.Series:
    """
    Fonction pour nettoyer les valeurs contenant des suffixes comme 'k' et 'M'
    et les convertir en float.
    """
    def convert_to_float(value: str) -> float:
        if isinstance(value, str):
            value = value.lower().strip()
            if 'k' in value:
                return float(value.replace('k', '').strip()) * 1000
            elif 'm' in value:
                return float(value.replace('m', '').strip()) * 1000000
            elif 'b' in value:
                return float(value.replace('b', '').strip()) * 1000000000
            else:
                try:
                    return float(value)
                except ValueError:
                    return None  # Si la conversion échoue, on retourne None
        return value

    return data.apply(convert_to_float)


def plot_population(countries: list, path: str = "population_total.csv"):
    """
    calls the load function, loads the file population_total.csv,
    and displays the country information of your campus versus
    other country of your choice
    """
    df = load(path)

    if df is None:
        print("Error: Impossible to load dataset")
        return

    for country in countries:
        if country not in df.iloc[:, 0].values:
            print(f"Error: {country} doesn't exist in dataset")
            return

    df.set_index(df.columns[0], inplace=True)

    plt.figure(figsize=(12,6)) #size

    for country in countries:
        country_data = df.loc[country].astype(str)
        country_data = clean_population_data(country_data)

        # Conversion de l'index en entier (si ce n'est pas déjà le cas)
        country_data.index = pd.to_numeric(country_data.index, errors='coerce')

        # Filtrage des années entre 1800 et 2050
        country_data = country_data[(country_data.index >= 1800) & (country_data.index <= 2050)]

        # Tracer la courbe de population
        sns.lineplot(x=country_data.index, y=country_data.values, label=country)


    plt.title("Population vs. Year for Selected Countries")
    plt.xlabel("Year")
    plt.ylabel("Total Population")
    plt.xticks(range(1800, 2051, 40), rotation=45)
    plt.legend(title="Countries")
    plt.grid(True)
    plt.show()

