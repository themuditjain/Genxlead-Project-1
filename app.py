# Import necessary modules
from flask import Flask, render_template, request, redirect
import hashlib
import sqlite3
import pyshorteners



# Create a Flask app
app = Flask(__name__)

# Set up a connection to the database
conn = sqlite3.connect("urls.db", check_same_thread=False)
c = conn.cursor()

# Create a table to store the URLs and their shortened versions
c.execute('''CREATE TABLE IF NOT EXISTS urls(id INTEGER PRIMARY KEY AUTOINCREMENT,original_url TEXT,short_url TEXT)''')
conn.commit()


# Define a function to generate the shortened URL
def get_short_url(url):
    # Use SHA256 to hash the URL
    hash_object = hashlib.sha256(url.encode())
    hash_value = hash_object.hexdigest()
    # Take the first 8 characters of the hash value as the shortened URL
    short_url = hash_value[:8]
    return short_url

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("form.html")

# Define a route to handle the form submission
@app.route("/", methods=["GET","POST"])
def shorten_url():
    # Get the URL entered by the user
    original_url = request.form["url"]
    # Check if the URL is already in the database
    c.execute('SELECT short_url FROM urls WHERE original_url=?', (original_url,))
    result = c.fetchone()
    if result:
        # If the URL is already in the database, return the existing shortened URL
        short_url = result[0]
    else:
        # If the URL is not in the database, generate a new shortened URL
        short_url = get_short_url(original_url)
        # Store the mapping between the original URL and the shortened URL in the database
        c.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
        conn.commit()
    # Return the shortened URL to the user
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(short_url)
    return "The shortened and encrypted URL:  "+short_url
    # return short_url

# Run the app
if __name__ == "__main__":
    app.run(debug=True)