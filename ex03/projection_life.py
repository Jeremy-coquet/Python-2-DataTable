# from matplotlib import plt
import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def projection_life():
    gdp_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")

    if gdp_data is None or life_expectancy_data is None:
       exit()

    if "1900" not in gdp_data.columns or "1900" not in life_expectancy_data.columns:
        print("error: columns 1900 doesn't exist")
        exit()

    gdp_1900 = gdp_data[["country", "1900"]]
    life_expectancy_1900 = life_expectancy_data[["country", "1900"]]

    merged_data = pd.merge(gdp_1900, life_expectancy_1900, on="country", suffixes=("_gdp", "_life"))

    #clean data
    merged_data = merged_data.dropna()
    merged_data["1900_gdp"] = merged_data["1900_gdp"].astype(float)
    merged_data["1900_life"] = merged_data["1900_life"].astype(float)

    print(merged_data)
    plot_pojection(merged_data)

def plot_pojection(merged_data):
    """display graph"""
    plt.figure(figsize=(10, 6))

    plt.scatter(merged_data["1900_gdp"], merged_data["1900_life"], alpha=0.7, edgecolors="k")
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy)")
    # plt.grid(True)
    plt.show()

if __name__ == "__main__":
    projection_life()