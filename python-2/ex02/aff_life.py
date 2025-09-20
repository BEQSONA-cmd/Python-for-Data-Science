from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    data = load("population_total.csv")

    countries = ["Germany", "France"]
    selected_data = data[data["country"].isin(countries)]

    long_data = selected_data.melt(
        id_vars="country",
        var_name="year",
        value_name="Population"
    )

    long_data["Population"] = (
        long_data["Population"]
        .str.replace("M", "")
        .astype(float)
    )

    long_data["year"] = long_data["year"].astype(int)
    long_data = long_data[(long_data["year"] >= 1800) & (long_data["year"] <= 2050)]

    sns.lineplot(x="year", y="Population", hue="country", data=long_data)
    plt.savefig("Germany_France_life_expectancy.png")


if __name__ == "__main__":
    main()
