from flask import Blueprint, render_template, request

main_blueprint = Blueprint('main', __name__) # create a blueprint named 'main'

# define a route inside the blueprint
@main_blueprint.route('/')
def home():
    return render_template('home.html')

# ADDING HISTORY
# @main.route('/history')
# def history():
#     return render_template("history.html")  # Displays history