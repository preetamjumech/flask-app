from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<p>Hello Preetam Saha</p>"


bad_words = ["hate", "violence", "curse"]

@app.route("/predict", methods = ["POST","GET"])
def predict():
    word = ""
    message = ""
    if request.method == "POST":
        word = request.form["word"]
    if word.lower() in bad_words:
      message = "Bad"
    else:
      message = "Good"
    return render_template("index.html", word=word, message=message)


if __name__ == "__main__":
  app.run()
