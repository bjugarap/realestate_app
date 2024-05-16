from flask import Blueprint, jsonify, abort, request
from ..models import Agent, Listing, db

bp = Blueprint('agents', __name__, url_prefix='/agents')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    agents = Agent.query.all() # ORM performs SELECT query
    result = []
    for a in agents:
        result.append(a.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Agent.query.get_or_404(id)
    return jsonify(a.serialize())

@bp.route('', methods=['POST'])
def create():
    required_keys = ['first_name','last_name','email','phone']
    if all(key in request.json for key in required_keys):
        a = Agent(
            first_name=request.json['first_name'],
            last_name=request.json['last_name'],
            email=request.json['email'],
            phone=request.json['phone']
            )
        db.session.add(a)
        db.session.commit()
        return jsonify(a.serialize())
    else:
        return abort(400)