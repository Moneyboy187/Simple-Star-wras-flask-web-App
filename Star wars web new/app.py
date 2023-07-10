from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/old_releases_only_movies")
def oldreleases():
    return render_template("re_only_movies.html",title="Only movies(not sorted)")

@app.route("/only_series")
def only_serieses():
    return render_template("only_series.html",title="Only Series (not sorted)")

@app.route("/every_series_sorted")
def sorted_series():
    return render_template("series_sorted.html",title="Every Star Wras Series (sorted)")

@app.route("/evry_release")
def every_release():
    return render_template("evry_release.html", title="Every Release ever (not sorted)")

@app.route("/every_movie_sorted")
def date_sorted_series():
    return render_template("date_sorted_movies.html",title="every movie sorted")

@app.route("/everything_sorted")
def everything_sorted():
    return render_template("everything_sorted.html",title=" Every Releses Sorted")

if __name__ == "__main__":
    app.run(debug = True)