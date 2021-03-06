"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesomes', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]



@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():

    play_game = request.args.get("game")

    if play_game == "no":
        return render_template("goodbye.html")
    else: 
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():

    species = request.args.get("species")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    feelings = request.args.getlist("feelings")
    print(feelings)
    feeling1= ', '.join(feelings[:-1])
    feeling2= str(feelings[-1])
    complete_feeling = feeling1 + ", and " + feeling2

    return render_template("madlib.html", 
                            species=species, 
                            color=color, 
                            noun=noun, 
                            adjective=adjective,
                            feelings=complete_feeling)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
