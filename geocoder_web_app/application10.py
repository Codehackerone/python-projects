from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import ArcGIS

nom = ArcGIS()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method == 'POST':
        try:
            file = request.files["file"]
            df = pandas.read_csv(file)
            try:
                df["Coordinates"] = df["Address"].apply(nom.geocode)
            except IndexError:
                df["Coordinates"] = df["address"].apply(nom.geocode)
            df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
            df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x is not None else None)
            df = df.drop("Coordinates", 1)
            df.to_csv("uploads/GeocodedFile.csv", index=None)
            return render_template("index.html", btn="download1.html", mytext=df.to_html())
        except:
            return render_template("index.html", mytext="You dont have any Address Column in your .csv file")


@app.route("/download1")
def download1():
    return send_file("uploads/GeocodedFile.csv", attachment_filename="GeocodedFile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run()
