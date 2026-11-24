from ast import literal_eval
from pathlib import Path
from threading import Lock
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)
DATA = Path(__file__).with_name("library.txt")
lock = Lock()
STATUSES = ("В наличии", "Выдана")


def load_books():
    if not DATA.exists():
        return []
    raw = DATA.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp1251")
    return [literal_eval(line) for line in text.splitlines() if line.strip()]


def save_books(books):
    # Preserve the existing file format and replace atomically.
    try:
        DATA.read_bytes().decode("utf-8-sig")
        encoding = "utf-8"
    except UnicodeDecodeError:
        encoding = "cp1251"
    except FileNotFoundError:
        encoding = "utf-8"
    temporary = DATA.with_suffix(".tmp")
    temporary.write_text("".join(repr(book) + "\n" for book in books), encoding=encoding)
    temporary.replace(DATA)


@app.get("/")
def index():
    query = request.args.get("q", "").strip()
    with lock:
        books = load_books()
    total = len(books)
    available = sum(b["статус"].casefold() == "в наличии" for b in books)
    filtered = [b for b in books if not query or any(
        query.casefold() in str(b[key]).casefold()
        for key in ("описание", "автор", "год издания")
    )]
    return render_template("index.html", books=filtered, total=total,
                           available=available, q=query, error=request.args.get("error"),
                           statuses=STATUSES)


@app.post("/add")
def add():
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    try:
        year = int(request.form.get("year", ""))
    except ValueError:
        year = 0
    if not title or not author or not 1 <= year <= 9999:
        return redirect(url_for("index", error="Заполните название, автора и корректный год."))
    with lock:
        books = load_books()
        if any(b["описание"].casefold() == title.casefold() and
               b["автор"].casefold() == author.casefold() for b in books):
            return redirect(url_for("index", error="Такая книга уже существует."))
        books.append({"id": max((b["id"] for b in books), default=0) + 1,
                      "описание": title, "автор": author,
                      "год издания": year, "статус": "В наличии"})
        save_books(books)
    return redirect(url_for("index"))


@app.post("/books/<int:book_id>/status")
def status(book_id):
    value = request.form.get("status")
    if value not in STATUSES:
        abort(400)
    with lock:
        books = load_books()
        book = next((b for b in books if b["id"] == book_id), None)
        if book is None:
            abort(404)
        book["статус"] = value
        save_books(books)
    return redirect(url_for("index", q=request.form.get("q", "")))


@app.post("/books/<int:book_id>/delete")
def delete(book_id):
    with lock:
        books = load_books()
        remaining = [b for b in books if b["id"] != book_id]
        if len(remaining) == len(books):
            abort(404)
        save_books(remaining)
    return redirect(url_for("index", q=request.form.get("q", "")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
