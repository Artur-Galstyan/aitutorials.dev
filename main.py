from flask import Flask
from index.index import index_bp
from courses.courses import courses_bp


app = Flask(__name__)

app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(courses_bp, url_prefix="/courses")
