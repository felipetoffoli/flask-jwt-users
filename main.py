from src import create_app, db
from flask_migrate import Migrate
from src.model.users import User


app = create_app('dev')
Migrate(app, db)

@app.shell_context_processor
def shell_context():
    return dict (
        app=app,
        db=db,
        User=User
    )
app.run(debug=True)