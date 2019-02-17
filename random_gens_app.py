from flask import Flask, render_template
import json
import random_gens_output
import random

app = Flask(__name__)

@app.route('/index/main_menu/')  #decorator
def main():
    return render_template('main_menu.html')

@app.route('/index/')
def cover():
    return render_template('index.html')

@app.route('/index/main_menu/animal_pics/')
def animal_pics():
    return render_template('animal_pics.html')

@app.route('/index/main_menu/animal_pics/dogs_pic/')
def dog():
    dog_dict = random_gens_output.get_dict("https://dog.ceo/api/breeds/image/random/1")
    dog_image = dog_dict["message"][0]
    return render_template('dogs_pic.html', dog = dog_image)

@app.route('/index/main_menu/animal_pics/cats_pic/')
def cat():
    cat_dict = random_gens_output.get_dict("https://api.thecatapi.com/v1/images/search")
    cat_image = cat_dict[0]["url"]
    return render_template('cats_pic.html', cat = cat_image)

@app.route('/index/main_menu/advice/')
def advice():
    tip_dict = random_gens_output.get_dict("https://api.adviceslip.com/advice")
    tip_text = tip_dict["slip"]["advice"]
    return render_template('advice.html', tip = tip_text)

@app.route('/index/main_menu/meme/')
def meme():
    d = ["https://memegen.link/_YnV6egltZW1lcy9tZW1lcy1ldmVyeXdoZXJl.jpg", "https://i.redd.it/4c2t8vhf23h21.jpg", "https://i.redd.it/vzp9nqdch3h21.jpg", "https://i.redd.it/ka2ch49xh1h21.jpg","https://i.redd.it/i6sdyng7n3h21.jpg", "https://i.redd.it/7lvc7jsf01h21.jpg", "https://i.redd.it/t68fn6dqi0h21.jpg", "https://i.redd.it/tsp8qpamc3h21.png", "https://i.redd.it/q10ywip210h21.jpg","https://i.redd.it/7eqgb33qc1h21.jpg", "https://i.redd.it/qg6o8m7cm0h21.jpg", "https://i.redd.it/q10ywip210h21.jpg","https://i.redd.it/qhcc023un2h21.jpg","https://i.redd.it/zf5zgl3hwyg21.png", "https://static1.squarespace.com/static/57cbffbce4fcb57e0d35466a/5c1a6768f950b72a334e1bc7/5c1a67690e2e72c2bcb3c6b1/1545234284176/3f357b363a5a7944f3fa772c9bc77405.jpg", "https://static1.squarespace.com/static/57cbffbce4fcb57e0d35466a/5c1a6768f950b72a334e1bc7/5c1a677e562fa7f0b0e9410b/1545234307964/exams+funny.png"]

    n = random.randint(0,len(d)-1)

    return render_template('meme.html', meme = d[n])

@app.route('/index/main_menu/rant/')
def rant():
    return render_template('rant.html')

@app.route('/index/main_menu/checklist/')
def checklist():
    return render_template('checklist.html')

@app.route('/index/main_menu/email/')
def email():
    return render_template('email.html')

@app.route('/index/main_menu/joke/')
def joke():
    joke_dict = random_gens_output.get_dict("https://official-joke-api.appspot.com/random_joke")
    joke_setup = joke_dict["setup"]
    joke_punchline = joke_dict["punchline"]
    return render_template('joke.html', setup = joke_setup, punchline = joke_punchline)

@app.route('/index/main_menu/trivia/')
def trivia():
    triv_dict = random_gens_output.get_dict("https://opentdb.com/api.php?amount=1&category=9&difficulty=medium")
    triv_ques = triv_dict["results"][0]["question"]
    triv_ans = triv_dict["results"][0]["correct_answer"]
    triv_wrongans = triv_dict["results"][0]["incorrect_answers"]
    return render_template('trivia.html', question = triv_ques, answer = triv_ans, wrong_answers = triv_wrongans)



if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment
