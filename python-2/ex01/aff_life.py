from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")

    germany_data = data[data["country"] == "Germany"]

    germany_long = germany_data.melt(
        id_vars=["country"],
        var_name="year",
        value_name="Life expectancy"
    )

    germany_long["year"] = germany_long["year"].astype(int)

    sns.lineplot(x="year", y="Life expectancy", data=germany_long)
    plt.savefig("Germany_life_expectancy.png")


if __name__ == "__main__":
    main()
