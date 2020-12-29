import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():

    if request.method == "POST":

        if not request.form.get("old"):
            return apology("must provide old password", 400)
        elif not request.form.get("password"):
            return apology("must provide new password", 400)
        elif not request.form.get("confirmation"):
            return apology("must confirm new password", 400)
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("passwords must match", 400)

        rows = db.execute("SELECT * FROM users WHERE id = :id",
                          id=session["user_id"])
        if not check_password_hash(rows[0]["hash"], request.form.get("old")):
            return apology("wrong current password", 403)
        else:
            db.execute("UPDATE users SET hash = :hash WHERE id = :id",
                id=session["user_id"], hash=generate_password_hash(request.form.get("password")))

        return redirect("/logout")

    else:
        return render_template("password.html")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT * FROM stocks WHERE userid = :userid",
                          userid=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    stocks_total = 0

    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["total"] = quote["price"] * stock["shares"]
        stock["symbol"] = stock["symbol"].upper()
        stocks_total += stock["total"]

    return render_template("index.html", stocks=stocks, cash=usd(cash[0]["cash"]), total=usd(stocks_total + cash[0]["cash"]))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        elif not request.form.get("shares"):
            return apology("missing shares", 400)

        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("invalid symbol", 400)
        else:
            cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
            if float(request.form.get("shares")) * quote["price"] > float(cash[0]["cash"]):
                return apology("can't afford", 400)
            else:
                now = datetime.now()
                existing_shares = db.execute("SELECT shares FROM stocks WHERE userid = :userid AND symbol = :symbol",
                          userid=session["user_id"], symbol=request.form.get("symbol"))
                if existing_shares:
                    db.execute("UPDATE stocks SET shares = :shares WHERE userid = :userid AND symbol = :symbol",
                        shares=existing_shares[0]["shares"] + int(request.form.get("shares")), userid=session["user_id"], symbol=request.form.get("symbol"))
                    db.execute("UPDATE users SET cash = :cash WHERE id = :id",
                        cash=float(cash[0]["cash"]) - (float(request.form.get("shares")) * quote["price"]), id=session["user_id"])
                    db.execute("INSERT INTO history (userid, symbol, shares, price, transacted) VALUES (:userid, :symbol, :shares, :price, :transacted)",
                        userid=session["user_id"], symbol=request.form.get("symbol"), shares=request.form.get("shares"), price=quote["price"], transacted=now.strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    db.execute("INSERT INTO stocks (userid, symbol, name, shares) VALUES (:userid, :symbol, :name, :shares)",
                        userid=session["user_id"], symbol=request.form.get("symbol"), name=quote["name"], shares=request.form.get("shares"))
                    db.execute("UPDATE users SET cash = :cash WHERE id = :id",
                        cash=float(cash[0]["cash"]) - (float(request.form.get("shares")) * quote["price"]), id=session["user_id"])
                    db.execute("INSERT INTO history (userid, symbol, shares, price, transacted) VALUES (:userid, :symbol, :shares, :price, :transacted)",
                        userid=session["user_id"], symbol=request.form.get("symbol"), shares=request.form.get("shares"), price=quote["price"], transacted=now.strftime("%Y-%m-%d %H:%M:%S"))

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    history = db.execute("SELECT * FROM history WHERE userid = :userid ORDER BY transacted DESC",
        userid=session["user_id"])

    for entry in history:
        entry["price"] = usd(entry["price"])
        entry["symbol"] = entry["symbol"].upper()

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("missing symbol", 400)
        else:
            quote = lookup(request.form.get("symbol"))
            if not quote:
                return apology("invalid symbol", 400)
            else:
                quote["price"] = usd(quote["price"])
                return render_template("quoted.html", quote=quote)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation password", 400)

        # Check that passwords match
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("passwords must match", 400)

        check_username = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if check_username:
            return apology("user already exists", 400)
        else:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                          username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = db.execute("SELECT * FROM stocks WHERE userid = :userid",
                          userid=session["user_id"])

    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("missing symbol", 400)
        elif not request.form.get("shares"):
            return apology("missing shares", 400)
        elif int(request.form.get("shares")) == 0:
            return apology("shares must be positive", 400)

        requested_stock = db.execute("SELECT * FROM stocks WHERE userid = :userid AND symbol = :symbol",
                          userid=session["user_id"], symbol=request.form.get("symbol"))
        if requested_stock[0]["shares"] < int(request.form.get("shares")):
            return apology("not enough shares", 400)

        quote = lookup(request.form.get("symbol"))
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        now = datetime.now()

        if requested_stock[0]["shares"] == int(request.form.get("shares")):
            db.execute("DELETE FROM stocks WHERE userid = :userid AND symbol = :symbol",
                userid=session["user_id"], symbol=request.form.get("symbol"))
            db.execute("UPDATE users SET cash = :cash WHERE id = :id",
                id=session["user_id"], cash=float(cash[0]["cash"]) + (float(request.form.get("shares")) * quote["price"]))
            db.execute("INSERT INTO history (userid, symbol, shares, price, transacted) VALUES (:userid, :symbol, :shares, :price, :transacted)",
                        userid=session["user_id"], symbol=request.form.get("symbol"), shares="-" + request.form.get("shares"), price=quote["price"], transacted=now.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            db.execute("UPDATE stocks SET shares = :shares WHERE userid = :userid AND symbol = :symbol",
                userid=session["user_id"], symbol=request.form.get("symbol"), shares=requested_stock[0]["shares"] - int(request.form.get("shares")))
            db.execute("UPDATE users SET cash = :cash WHERE id = :id",
                id=session["user_id"], cash=float(cash[0]["cash"]) + (float(request.form.get("shares")) * quote["price"]))
            db.execute("INSERT INTO history (userid, symbol, shares, price, transacted) VALUES (:userid, :symbol, :shares, :price, :transacted)",
                        userid=session["user_id"], symbol=request.form.get("symbol"), shares="-" +request.form.get("shares"), price=quote["price"], transacted=now.strftime("%Y-%m-%d %H:%M:%S"))

        return redirect("/")
    else:
        return render_template("sell.html", stocks=stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
