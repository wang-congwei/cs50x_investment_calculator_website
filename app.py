from flask import Flask, render_template, request
from helpers import apology

app = Flask(__name__)


def month_calculate(n, p):
    """
    Calculate the future value of a series of monthly investments.
    n: monthly investment amount
    p: annual interest rate as a percentage
    Returns the future value after 12 months, compounded monthly.
    """
    r = p / 1200  # Convert annual rate percentage to monthly decimal rate
    # If rate is not zero, use compound formula; else, simple sum
    return n * (1 + r) * ((1 + r)**12 - 1) / r if r != 0 else n * 12


@app.route("/", methods=["GET", "POST"])
def index():
    # Handle POST request: process form submission
    if request.method == "POST":
        try:
            # Extract form parameters from POST request
            capital = float(request.form.get("capital"))
            month_invest = float(request.form.get("month_invest"))
            invest_year = int(request.form.get("invest_year"))
            invest_rate = float(request.form.get("invest_rate"))

            # Validate that all input values are positive (except for 0 capital/monthly investment)
            if capital < 0 or month_invest < 0 or invest_year <= 0 or invest_rate < 0:
                return apology("All input values must be positive.", 400)

            # Ensure that both capital and monthly investment are not zero at the same time
            if capital == 0 and month_invest == 0:
                return apology("Start capital and monthly investment cannot both be zero.", 400)

            # Prepare lists to store results for each year
            years = list(range(1, invest_year + 1))  # List of years (1 to invest_year)
            capitals = []  # Cumulative principal invested up to each year
            returns = []   # Cumulative investment return up to each year
            totals = []    # Total value (principal + returns) at each year

            monthly_rate = invest_rate / 100 / 12
            total_invested = capital
            total = capital

            # Loop over each year to compute compound interest and accumulate investment
            for year in years:
                for m in range(12):
                    total = total * (1 + monthly_rate)
                    total += month_invest
                    total_invested += month_invest
                capitals.append(round(total_invested, 2))
                returns.append(round(total - total_invested, 2))
                totals.append(round(total, 2))

            # Render result template with all computed values
            return render_template(
                "result.html",
                years=years,
                capitals=capitals,
                returns=returns,
                totals=totals,
                capital=capital,
                month_invest=month_invest,
                invest_year=invest_year,
                invest_rate=invest_rate
            )

        except Exception as e:
            # Handle invalid input or conversion errors
            return apology("Invalid input, please check your entries.", 400)

    # Render the index page (form) for GET requests
    return render_template("index.html")
