from flask import Flask, request, render_template_string, redirect, url_for
import os
import re

app = Flask(__name__)

DATA_DIR = "websites"

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def sanitize_filename(title):
    # Remove special chars, keep only letters, numbers, underscores, dashes
    safe = re.sub(r'[^A-Za-z0-9_\- ]', '', title)
    return safe.replace(' ', '_') + ".html"

def index_websites():
    SEARCH_INDEX = {}
    for fname in os.listdir(DATA_DIR):
        with open(os.path.join(DATA_DIR, fname), "r", encoding="utf8") as f:
            text = f.read().lower()
            for word in set(text.split()):
                SEARCH_INDEX.setdefault(word, set()).add(fname)
    return SEARCH_INDEX

@app.route("/")
def home():
    return render_template_string("""
    <h1>Mini Search Engine & Website Builder</h1>
    <form action="/search" method="get">
        <input name="q" placeholder="Search websites..." />
        <input type="submit" value="Search" />
    </form>
    <br>
    <a href="{{ url_for('create_site') }}">Create a Website</a>
    """)

@app.route("/search")
def search():
    q = request.args.get("q", "").lower().split()
    ensure_data_dir()
    SEARCH_INDEX = index_websites()
    results = set()
    for word in q:
        results |= SEARCH_INDEX.get(word, set())
    items = ""
    for fname in results:
        items += f'<li><a href="/site/{fname}">{fname}</a></li>'
    if not items:
        items = "<li>No results found</li>"
    return f"<h2>Results for {' '.join(q)}:</h2><ul>{items}</ul><a href='/'>Home</a>"

@app.route("/create", methods=["GET", "POST"])
def create_site():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        fname = sanitize_filename(title)
        ensure_data_dir()
        try:
            with open(os.path.join(DATA_DIR, fname), "w", encoding="utf8") as f:
                f.write(f"<h1>{title}</h1>\n{content}")
        except Exception as e:
            return f"<h3>Error saving file: {e}</h3><a href='/'>Home</a>"
        return redirect(url_for("site", sitename=fname))
    return render_template_string("""
    <h2>Create a Website</h2>
    <form method="post">
        Title: <input name="title" required/><br>
        Content (HTML):<br>
        <textarea name="content" rows="10" cols="40" required></textarea><br>
        <input type="submit" value="Create" />
    </form>
    <a href="/">Home</a>
    """)

@app.route("/site/<sitename>")
def site(sitename):
    ensure_data_dir()
    try:
        with open(os.path.join(DATA_DIR, sitename), "r", encoding="utf8") as f:
            return f.read() + "<hr><a href='/'>Home</a>"
    except FileNotFoundError:
        return "<h3>Site not found.</h3><a href='/'>Home</a>"
    except Exception as e:
        return f"<h3>Error loading site: {e}</h3><a href='/'>Home</a>"

if __name__ == "__main__":
    ensure_data_dir()
    app.run(debug=True)