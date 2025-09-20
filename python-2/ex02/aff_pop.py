from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import os


def display_diagram(data, file_name):
    """
    it will build diagram and show it
    """
    plt.title("population Projections")
    sns.lineplot(x="year", y="Population", hue="country", data=data)
    plt.savefig(file_name)
    Image.open(file_name).show()
    os.remove(file_name)


def main():
    """
    displays the countries populations
    """
    data = load("population_total.csv")

    countries = ["Germany", "France"]
    selected_countries = data[data["country"].isin(countries)]

    selected_data = selected_countries.melt(
        id_vars="country",
        var_name="year",
        value_name="Population"
    )

    new_pops = selected_data["Population"].str.replace("M", "").astype(float)
    new_years = selected_data["year"].astype(int)

    selected_data["year"] = new_years
    selected_data["Population"] = new_pops
    selected_data = selected_data[(selected_data["year"] >= 1800)
                                  & (selected_data["year"] <= 2050)]

    display_diagram(selected_data, "Population.png")


if __name__ == "__main__":
    main()
