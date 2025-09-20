from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import os


def display_diagram(long_data, file_name):
    """
    it will build diagram and show it
    """
    plt.title("Germany Life expectancy Projections")
    sns.lineplot(x="year", y="Life expectancy", data=long_data)
    plt.savefig(file_name)
    Image.open(file_name).show()
    os.remove(file_name)


def main():
    """
    displays the country life expectancy
    """
    data = load("life_expectancy_years.csv")

    selected_country = data[data["country"] == "Germany"]

    selected_data = selected_country.melt(
        id_vars="country",  # keeps country same position
        var_name="year",  # puts each year on same column
        value_name="Life expectancy"  # make new column
    )

    selected_data["year"] = selected_data["year"].astype(int)
    display_diagram(selected_data, "life_expectancy.png")


if __name__ == "__main__":
    main()
