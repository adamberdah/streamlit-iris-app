import matplotlib.pyplot as plt

def quick_plot(df, x, y):
    fig, ax = plt.subplots()
    if x in df.columns and y in df.columns:
        ax.scatter(df[x], df[y])
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{y} vs {x}")
    return fig
