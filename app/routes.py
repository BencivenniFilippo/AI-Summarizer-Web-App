from flask import Blueprint, render_template
from app.forms import SummarizeForm
from app.nlp import summarize


main_blueprint = Blueprint('main', __name__) # create a blueprint named 'main'


# define a route inside the blueprint
@main_blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = SummarizeForm()
    summary = None

    if form.validate_on_submit():
        text = form.text_input.data

        summary = summarize(text) # summarization through BART

    return render_template("home.html", form=form, summary=summary)