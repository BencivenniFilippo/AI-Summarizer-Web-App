from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SummarizeForm(FlaskForm):
    text_input = TextAreaField("Enter text to summarize", validators=[DataRequired()], render_kw={"placeholder": "Enter text to summarize"})
    submit = SubmitField("Summarize")