from flask import Flask, request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/rep', methods=['GET'])
def rep():
    return render_template("rep.html")


@app.route('/algo', methods=['GET'])
def algo():
    return render_template("algo.html")


@app.route('/animation', methods=['GET'])
def animation():
    return render_template("animation.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
