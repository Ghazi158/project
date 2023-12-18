from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///tracker.db")



# Delete Route for When User Selects to Delete All the Rows
@app.route("/delete_all", methods=["POST"])
def delete_all():
    db.execute("DELETE FROM items")
    return redirect("/")


# Delete Route for When User Deletes a Single Row
@app.route("/delete_row", methods=["POST"])
def delete_row():

    row_id = request.form.get("row_id")
    db.execute("DELETE FROM items WHERE id = ?", row_id)
    return redirect("/")


# Route for Index Page
@app.route("/", methods=["GET", "POST"])
def index():



    if request.method == "GET":
        rows = db.execute(
        "SELECT * FROM items ORDER BY timestamp DESC;"
        )

        return render_template("index.html", rows=rows)


    if request.method == "POST":

        # Get item name and Price as Input
        item_name = request.form.get("item")
        price_amount = request.form.get("price")
        try:
            price_amount = int(price_amount)
        except ValueError:
            if price_amount is None:
                return render_template("error.html")

        # Check if user entered correct Input
        if not item_name:
            return render_template("error.html")
        if not price_amount or price_amount < 0:
            return render_template("error.html")

        # Enter Item and Price of Item in DataBase
        else:
            db.execute("INSERT INTO items(item, price) VALUES (?, ?);",item_name, price_amount)
            rows = db.execute(
            "SELECT * FROM items"
            )

        return redirect("/")


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

