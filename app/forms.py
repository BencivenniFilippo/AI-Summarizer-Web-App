from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Length

class SummarizeForm(FlaskForm):
    text_input = TextAreaField("Enter text to summarize", validators=[Length(min=10)], render_kw={"placeholder": "Enter text to summarize"})
    submit = SubmitField("Summarize")