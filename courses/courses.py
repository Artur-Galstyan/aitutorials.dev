from flask import Blueprint, render_template


courses_bp = Blueprint("courses_bp", __name__, template_folder="templates")


@courses_bp.route("/")
def home():
    return render_template("courses/index.html")


@courses_bp.route("feedforward_nn/")
@courses_bp.route("feedforward_nn/<course_number>")
def feedforward_nn(course_number=None):
    if not course_number:
        course_number = 1
    return render_template(f"courses/feedforward_nn/{course_number}.html")
