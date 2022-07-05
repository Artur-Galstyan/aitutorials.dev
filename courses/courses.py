from flask import Blueprint, render_template


courses_bp = Blueprint("courses_bp", __name__, template_folder="templates")


@courses_bp.route("/")
def home():
    return render_template("courses/index.html")
