from flask import request, jsonify, render_template


def index():
  data = {"data": {"recommends": "You got to wait for sometime"} }
  return jsonify(data)


def home():
  return render_template('index.html')
