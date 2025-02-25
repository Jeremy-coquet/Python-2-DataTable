import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load

def plot_life_expectancy(country: str, path: str = "life_expectancy_years.csv"):
    """
    calls the load function, loads the file, life_expectancy_years.csv,
    and displays the country information of your campus in parameter
    """
    df = load(path)

    if df is None:
        print("Error: Impossible to load dataset")
        return

    if country not in df.iloc[:, 0].values:
        print(f"Error: {country} doesn't exist in dataset")
        return

    df.set_index(df.columns[0], inplace=True)
    country_data = df.loc[country].astype(float)

    plt.figure(figsize=(12,6)) #size

    years = [int(year) for year in country_data.index]
    sns.lineplot(x=years, y=country_data.values, label=country)

    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(years[::40], rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

