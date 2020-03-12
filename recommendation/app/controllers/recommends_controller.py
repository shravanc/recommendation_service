from flask import request, jsonify, render_template

from app.helpers.factory.movie_recommendation import MovieRecommendation

def index():
  engine = MovieRecommendation()
  movies = engine.recommend_movies('content_based')
  return jsonify({'data': movies})


def home():
  return render_template('index.html')

