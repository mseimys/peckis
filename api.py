import os
from uuid import uuid4

from flask import Blueprint, request, abort, jsonify, current_app as app
from werkzeug.utils import secure_filename

from ml import guess_number

api = Blueprint("api", __name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@api.route("/")
def index():
    return "Hello World! Make a POST request to /guess endpoint"


@api.route("/guess", methods=["POST"])
def guess():
    if "image" not in request.files:
        abort(400)

    f = request.files["image"]

    if not allowed_file(f.filename):
        abort(400)

    filename = secure_filename(f.filename)
    full_path = os.path.join(app.config["UPLOAD_FOLDER"], uuid4().hex + "_" + filename)
    f.save(full_path)

    return jsonify(guess_number(full_path))
