from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation.translator import frenchtoenglish, englishtofrench
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext = englishtofrench(textToTranslate)
    return frenchtext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishtext = frenchtoenglish(textToTranslate)
    return englishtext

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
