from flask import Blueprint, jsonify

controller_index = Blueprint('controller_index', __name__)

@controller_index.route('/')
def index():
    return jsonify(dict(
        name='API the Users with Auth JWT',
        version='1.0',
        author=dict(
            name='Felipe Toffoli Martins',
            linkedin='https://www.linkedin.com/in/felipetoffoli',
            github='https://github.com/felipetoffoli'
        ),
        repository='https://github.com/felipetoffoli/flask-jwt-users'
        ))