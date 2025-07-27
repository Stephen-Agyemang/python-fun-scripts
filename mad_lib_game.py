# Mad Lib Game
def play_game():
    import inflect
    import json
    p = inflect.engine()

    print("🎉 WELCOME TO THE MAD LIB GAME 🎉")
    with open("colors.json") as file:
        valid_colors = set(name.strip().lower() for name in json.load(file).values())

    while True:
        color_input = input("Enter a color: ").strip().lower()
        if color_input in valid_colors:
            break
        print("⚠️ Invalid color! Try one like blue, red, magenta, or pink.\n"
            "You know—colors people actually use!"
    )

    def is_plural(plural_noun):
        return p.singular_noun(plural_noun) is not False
    def get_plural_noun():
        for attempt in range(2):
            plural_noun = input("Enter a plural noun: ").strip().lower()
            if is_plural(plural_noun):
                return plural_noun
            if attempt == 0:
                print("Not really plural, what you typed, is it? Anyways its MadLibs it's just as messy carry on Mate!\n"
                    "You still gotta try again!😆just one more time, I promise"
            )
        return plural_noun

    noun_input = get_plural_noun()
    celebrity = input("Enter a celebrity's name: ").strip().capitalize()

    print("\nHere’s your Mad Lib:")
    print(f"Roses are {color_input.title()}")
    print(f"{noun_input.title()} are blue")
    print(f"I love {celebrity}!❤️")

def valid_replay_response():
    while True:
        response = input("\nSo wanna play again?😁This time input different stuff, make it rhymy this time!!\n"
                "yes or no: ").strip().lower()
        if response in ["yes", "no"]:
            return response
        print("Let's keep it classy and simple, your options are yes and no!")


while True:
    play_game()
    replay = valid_replay_response()

    if  replay == "no":
        print("\nThanks for playing! Hop on anytime you want to play again😌")
        break