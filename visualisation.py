import matplotlib.pyplot as plt

#PLOTTING HISTORGRAM

def plot_histogram(historical_x_day_returns_rs, days, confidence, VAR):
    plt.hist(historical_x_day_returns_rs, bins=50, alpha=0.5,
             label=f'{days}- Day Returns')

    for cl, var in zip(confidence, VAR):
        plt.axvline(x=-var, linestyle="--", color="red",
                    label=f'VaR at {int(cl*100)}% confidence')

    plt.xlabel(f"{days}- Day Portfolio Return (Rs)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Portfolio {days}- Day Returns and Parametric VaR estimates")
    plt.legend()
    plt.savefig("hist.png")
    plt.show()




