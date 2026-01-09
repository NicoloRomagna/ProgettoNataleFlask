from flask import render_template
from flask_login import login_required, current_user
from ..models import GameNight
from . import dashboard_bp

@dashboard_bp.route("/dashboard")
@login_required
def stats():
    total = GameNight.query.filter_by(created_by=current_user.id).count()
    return render_template("dashboard/stats.html", total=total)