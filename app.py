from random import randint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from opentelemetry import trace

# Acquire a tracer
tracer = trace.get_tracer("diceroller.tracer")

app = Flask(__name__)

# Acquire a database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.bin?mode=rwc'
db = SQLAlchemy(app)

@app.route("/rolldice")
def roll_dice():
    return str(roll())

def roll():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        return res
