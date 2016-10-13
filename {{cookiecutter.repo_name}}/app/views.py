import logging
import json

from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required

from . import app, estimator, target_names


logger = logging.getLogger('app')

class PredictForm(Form):
    """Fields for Predict"""
    sepal_length = fields.DecimalField('Sepal Length:', places=2, validators=[Required()])
    sepal_width = fields.DecimalField('Sepal Width:', places=2, validators=[Required()])
    petal_length = fields.DecimalField('Petal Length:', places=2, validators=[Required()])
    petal_width = fields.DecimalField('Petal Width:', places=2, validators=[Required()])

    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index page"""
    form = PredictForm()
    predicted_iris = None

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data

        # Retrieve values from form
        sepal_length = float(submitted_data['sepal_length'])
        sepal_width = float(submitted_data['sepal_width'])
        petal_length = float(submitted_data['petal_length'])
        petal_width = float(submitted_data['petal_width'])

        # Create array from values
        flower_instance = [sepal_length, sepal_width, petal_length, petal_width]

        my_prediction = estimator.predict(flower_instance)
        # Return only the Predicted iris species
        predicted_iris = target_names[my_prediction]

    return render_template('index.html',
        form=form,
        prediction=predicted_iris)
