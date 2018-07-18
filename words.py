import random

word_list = ["cat",
             "dog",
             "car",
             "hat",
             "food",
             "water",
             "book",
             "desk",
             "chair",
             "hair",
             "shelf",
             "horse",
             "movie",
             "game",
             "bike",
             "floor",
             "card",
             "box",
             "toy",
             "race",
             "store",
             "wheel",
             "shoe"]

def get_word():
    num = random.randint(0, len(word_list))
    word = word_list[num]
    return word
