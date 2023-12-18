from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///tracker.db")




@app.route("/", methods=["GET", "POST"])
def index():

   
    
    if request.method == "GET":
        rows = db.execute(
        "SELECT * FROM items"
        )
    
        total_rows = db.execute(
        "SELECT COUNT(*) as count FROM items;"
        )[0]["count"] 
        
        return render_template("index.html", rows=rows)
    
    
    if request.method == "POST":
        rows = db.execute(
        "SELECT * FROM items"
        )
    
        total_rows = db.execute(
        "SELECT COUNT(*) as count FROM items;"
        )[0]["count"] 
        item_name = request.form.get("item")
        price_amount = request.form.get("price")

        if not item_name:
            return "<h1> ENTER ITEM </h1>"
        if not price_amount:
            return "<h1>ENTER PRICE</h1>"
        
        
        elif item_name and price_amount:
            db.execute("INSERT INTO items(item, price) VALUES (?, ?);",item_name, price_amount)
            return render_template("index.html", rows=rows, total_row=total_rows)




