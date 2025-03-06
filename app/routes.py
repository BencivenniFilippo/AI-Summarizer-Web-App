from flask import Blueprint, render_template, request

main_blueprint = Blueprint('main', __name__) # create a blueprint named 'main'

# define a route inside the blueprint
@main_blueprint.route('/')
def home():
    input = 'testo'
    return render_template('home.html', shown_input=input)

@main_blueprint.route('/playground')
def playground():
    l = [1, 2, 'giovanni', 4]

    return render_template('stuff.html', lista=l)

# ADDING HISTORY
# @main.route('/history')
# def history():
#     return render_template("history.html")  # Displays history