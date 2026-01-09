from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import GameNight, db

@main_bp.route("/")
def index():
    nights = GameNight.query.all()
    return render_template("main/index.html", nights=nights)

@main_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_night():
    if request.method == "POST":
        night = GameNight(
            title=request.form["title"],
            date=request.form["date"],
            location=request.form["location"],
            notes=request.form["notes"],
            created_by=current_user.id
        )
        db.session.add(night)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("main/create_night.html")