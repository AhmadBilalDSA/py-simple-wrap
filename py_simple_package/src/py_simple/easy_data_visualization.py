"""
easy_data_visualization aims to simplify data visualization.
without requiring users to memorize every chart type or matplotlib function.
"""

import matplotlib.pyplot as plt
from typing import Literal


def plot_data(X:list, Y: list = None) -> int:
    """
    This function checks the type of variable(s) and suggests the most appropriate charts.

    Args:
        Two lists representing the data.
        :param X: list
        :param Y: list - optional

    """

    type_X = _infer_type(X)
    type_Y = _infer_type(Y) if Y is not None else None

    CHART_SUGGESTIONS = {
        ("quantitative", None): ["histogram", "line"],
        ("categorical", None): ["barchart", "pie"],
        ("quantitative", "quantitative"): ["scatter", "histogram_x", "histogram_y"],
        ("quantitative", "categorical"): ["barchart"],
        ("categorical", "quantitative"): ["barchart"],
        ("categorical", "categorical"): ["barchart_grouped"],
    }

    fig, axes = plt.subplots(3, 3, figsize=(12, 12))

    charts = 0 # this variable can be helpful in future

    is_X_quantitative = isinstance(X, (int, float)) and not isinstance(X, bool) # If false, X is a categorical variable.

    if Y is None:                       # If Y is None, that means that X is the only variable.
        if is_X_quantitative:
            axes[0, 0].hist(X)
            axes[0, 0].set_title("Histogram")
            charts += 1

            axes[0, 1].plot (X)
            axes[0, 1].set_title("Line")
            charts += 1

            ### Todo: KDE chart
        else:
            axes[0, 0].hist(X)
            axes[0, 0].set_title("Histogram")
            charts += 1
            pass
        pass


    if Y is not None:
        assert len(X) == len(Y), "X and Y must have the same length"

        is_Y_quantitative = all(isinstance(y, int) for y in Y)

        if is_Y_quantitative:
            axes[0, 0].hist(X, Y)
            axes[0, 0].set_title("Histogram")
            charts += 1


    # With two categorical variables, one can be used for counting, creating a quantitative variable.
    # and we can color the chart based on the other categorical variable.

    # Are X and Y quantitatives? scatterplot
    # if (is_X_quantitative and is_Y_quantitative):
    #     # plot_scatter()
    #     pass
    #
    # Is one list categorical and the other quantitative? Barchart
    # if(is_X_quantitative and not is_Y_quantitative):
    #     # plot_barchart()
    #     pass
    # elif(is_Y_quantitative and not is_X_quantitative):
    #     # plot_barchart()
    #     pass

    print("Plotting data...")
    plt.show()
    # Is one of them categorical with fewer than 5 categories? pie, donut, barchart
    return 0


def _infer_type(series) -> Literal["quantitative", "categorical"]:
    # If the list only numbers so it quantitative
    is_quantitative = all(
        isinstance(x, (int, float)) and not isinstance(x, bool)
        for x in series
    )
    return "quantitative" if is_quantitative else "categorical"


# Testing, this is will be removed
# %%
X = [1,2,3,1]
Y = [4,5,6]
counts = {}
type(1)

for item in X:
    counts[item] = counts.get(item, 0) + 1

counts

# %%
X = [5,10,1]
Y = [4,5,6]
                                          # False: Y is a categorical variable.
print(all(isinstance(x, int) for x in Y)) # True: Y is a quantitative variable
type(Y)

# If there is only one list, we can visualize its distribution.
plot_data(X)
# %%