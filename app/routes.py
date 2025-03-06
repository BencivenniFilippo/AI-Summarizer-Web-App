from flask import Blueprint, render_template, request

main_blueprint = Blueprint('main', __name__) # create a blueprint named 'main'

# define a route inside the blueprint
@main_blueprint.route('/')
def home():
<<<<<<< HEAD
    input = 'testo'
    return render_template('home.html', shown_input=input)

@main_blueprint.route('/playground')
def playground():
    l = [1, 2, 'giovanni', 4]

    return render_template('stuff.html', lista=l)
=======
    return render_template('home.html')
>>>>>>> 03b32e032067faf84c84bea0529226db3449b767

# ADDING HISTORY
# @main.route('/history')
# def history():
#     return render_template("history.html")  # Displays history