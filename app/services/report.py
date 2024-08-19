from flask import Blueprint
from app.common.http_methods import GET
from ..controllers import ReportController
from .base import entity_response


report = Blueprint("report", __name__)


@report.route("/", methods=GET)
def get_report():
    report, error = ReportController.get_report()
    return entity_response(report, error)
