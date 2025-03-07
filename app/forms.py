from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class SummarizeForm(FlaskForm):
    text_input = TextAreaField("Enter text to summarize", validators=[DataRequired()], render_kw={"placeholder": "Enter text to summarize"})
    submit = SubmitField("Summarize")

    def validate_text_input(self, field):
        word_count = len(field.data.split())  # Count words
        if word_count < 10:
            raise ValidationError("Text must have at least 10 words.")