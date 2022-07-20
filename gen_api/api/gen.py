from flask import jsonify, request, g, abort

from api import api

@api.post("/gen")
def generate():
    data = request.get_json(force=True)
    fb = data.get("end", None)
    