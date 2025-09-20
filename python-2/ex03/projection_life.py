from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import os


def display_diagram(data, file_name, date):
    """
    it will build diagram and show it
    """
    plt.title(date)
    sns.scatterplot(x="GDP", y="Life expectancy", data=data)
    plt.savefig(file_name)
    Image.open(file_name).show()
    os.remove(file_name)


def main():
    """
    it will display the projection of life expectancy vs income
    """
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    year = "1900"
    income_1900 = income[["country", year]]
    life_1900 = life[["country", year]]

    merged = income_1900.merge(life_1900, on="country")
    merged.columns = ["country", "GDP", "Life expectancy"]

    display_diagram(merged, "diagram_1900.png", year)


if __name__ == "__main__":
    main()
