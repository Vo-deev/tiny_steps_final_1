from src.config import app, db
from src import models
import src.routes


@app.before_first_request
def create_table():
    db.create_all()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 'Teacher': models.Teacher,
        'Order': models.Order, 'Request': models.RequestModel
    }


if __name__ == "__main__":
    app.run(debug=True)
