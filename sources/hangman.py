import requests
from random import choice


class Hangman:
    def __init__(self):
        self.__URL = "https://city-and-state-search-api.p.rapidapi.com/countries"
        self.__headers = {
            "X-RapidAPI-Key": "b6beaf5d1amsh120379bf9b7d0afp109567jsn318869e970e3",
            "X-RapidAPI-Host": "city-and-state-search-api.p.rapidapi.com",
        }
        self.__temp_country = []
        self.__level_game = {"Easy": 5, "Medium": 3, "Hard": 1}
        self.guessed = ""

    # Will be return list
    def get_REQ(self) -> "list[str]":
        res = requests.get(self.__URL, headers=self.__headers)

        for i in res.json():
            self.__temp_country.append(i["name"].lower())

        return self.__temp_country

    def run_game(self):
        self.word = choice(self.__temp_country)

        username: str = input("What is your name >> ")
        print(f"Welcome to the game, {username} !")
        print("\n")

        print(f"Choose your level ! with range from 1 to {len(self.__level_game)}")
        for index, (key) in enumerate(self.__level_game.keys()):
            print(f"{index+1}. {key}")

        choosed = input("Your choice >> ")

        for index, value in enumerate(self.__level_game.values()):
            pass
