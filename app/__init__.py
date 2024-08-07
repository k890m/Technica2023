from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv(dotenv_path)
app = Flask(__name__)


# DATA
char_data = [
    {
        "name": "Maya",
        "desc":"Owns a pet cat that eats frequently and only a specific brand of food that is expensive. She has debts that were sent to collections, luckily they have not accumulated any interest (for now). Her rent is 1,625 a month, gas and electric is separate/subject to change. She has 12k in her savings. She applies to 20 jobs a day on Indeed and they either don't respond, you get an interview but not a call back, or don’t pay well enough.",
        "image":"static/images/Maya.png"
    },
    {
        "name": "Ruka",
        "desc":"Ruka has four children that all attend a private school that she pays by semester to keep them in. They have expensive after school activities that need monthly payments. Her children are picky eaters so groceries tend to be very expensive. She works from home as her husband buys the groceries. Downside is that he does not know how to budget, and he uses her money and not his own. Although Ruka is a great and reliable worker, she works crazy hours and barely has time to spend with her family. Her children miss her. Ruka wants to cut her hours so she can spend more time with her family, but this may affect her pay and her position in the company.",
        "image":"static/images/Ruka.png"
    },
    {
        "name":"Ananya", 
        "desc":"Ananya is currently taking five classes while also trying to start up a small business. Her classes take up most of her time and it costs a lot to fund her projects. She is bad at time management but has great ideas for her business which would surely make her money. But, on top of paying for college, school supplies. And working a minimum wage job, she does not have enough to buy materials. Ananya is thinking of dropping some of her classes to have free time to work on her business, but this will set her back with graduating on time. She wants to draft a proposal letter to gain sponsors to help fully fund her project.",
        "image":"static/images/Maya.png"
    }
]


# ROUTES

@app.route('/')
def index():
    return render_template('index.html', char=char_data)


if __name__ == "__name__":
    app.run()

