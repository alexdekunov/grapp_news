from flask import Flask, render_template
from python_org_news import get_python_news

app = Flask(__name__)

@app.route('/')
def index():
    title = "Новости Python"
    news = get_python_news()
    return render_template('index.html', page_title=title)


if __name__ == "__main__":
    app.run(debug=True)