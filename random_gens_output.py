import random_gens
import random
def get_dict(url: str):
    return random_gens.get_result(url)


if __name__ == '__main__':

    #meme_dict = get_dict("https://api.imgflip.com/get_memes")
    #meme_image = d[3]
    #print(meme_image)

    dog_dict = get_dict("https://dog.ceo/api/breeds/image/random/1")
    dog_image = dog_dict["message"][0]

    cat_dict = get_dict("https://api.thecatapi.com/v1/images/search")
    cat_image = cat_dict[0]["url"]

    joke_dict = get_dict("https://official-joke-api.appspot.com/random_joke")
    joke_setup = joke_dict["setup"]
    joke_punchline = joke_dict["punchline"]

#    quote_dict = get_dict("http://quotes.rest/qod.json?category=inspire")
#    quote_text = quote_dict["contents"]["quotes"][0]["quote"]

    #meme_dict = get_dict("https://meme-api.herokuapp.com/gimme")
    #meme_image = meme_dict["url"]

    tip_dict = get_dict("https://api.adviceslip.com/advice")
    tip_text = tip_dict["slip"]["advice"]

    triv_dict = get_dict("https://opentdb.com/api.php?amount=1&category=9&difficulty=medium")
    triv_ques = triv_dict["results"][0]["question"]
    triv_ans = triv_dict["results"][0]["correct_answer"]
    triv_wrongans = triv_dict["results"][0]["incorrect_answers"]



    print(dog_image)
    print()
    print(cat_image)
    print()
    print(joke_setup)
    print(joke_punchline)
    print()
#    print(quote_text)
    print()
#    print(meme_image)
    print()
    print(tip_text)
    print()
    print(triv_ques)
    print(triv_ans)
    print(triv_wrongans)
