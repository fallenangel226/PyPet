"""
   pypet V1.2

   Welcome to pypet, my first attempt at building a python game

   Currently you can create and save new pets, allowing you to have as many
   pets as you would like. You have 5 main game options, will be changing
   that shortly :). You have 3 pet type to chose from, again more  will be
   add shortly. The game is broken up into 3 classes, stats, pets, and setup.
   Setup holds all the main functions of the game. Pets holds all the pet types
   and the functions for creating a new pet. Stats read the txt files the game
   data is stored in and creates the attribute dictionary for each pet after creation
   Only one pet can be ran at any time, but would like to add a "play date" function
   to have pets interact with each other, if only on a limited basis.

   GAMEPLAY - In the game you can chose to play with your pet by feeding, cuddling,
   rubbing their belly, and playing fetch. These options are generic across all pets but
   would like be able to change game play and messages based on pet type. Each option has 3
   outcomes, which are fall asleep, negative response, and positive response. Each response
   has a random chance of happening. Can you find the easter egg?

   FIXME - Float used for age is supposed to be set to the second decimal point, but doesnt
           reflect the coding - code in class Stats

"""


from random import randint
import glob


# Defines Pet attributes
class Stats:
    def __init__(self):
        self.attribute = {}

    def attributes(self, file):
        with open(file, "r+") as saved_stats:
            stat = saved_stats.readline()
            stat_list = list(stat.split(","))
        self.attribute = {
            "name": stat_list[0],
            "age": round(float(stat_list[1]), 2),
            "health": int(stat_list[2]),
            "weight": int(stat_list[3]),
            "hungry": True,
            "photo": stat_list[5],
            "gender": stat_list[6],
            "awake": True

        }
        return run.begin(self.attribute)


# Class for creating new pypets
# FIXME: Add more pets here
class Pet:
    def __init__(self):
        self.base_atributes = {
            "name": "none",
            "age": 0.01,
            "health": 100,
            "weight": 0,
            "hungry": True,
            "photo": "none",
            "gender": "female",
            "awake": True

        }

    def chose_pet(self):
        try:
            pet_type = int(input("Enter the type of pet you would like:\n"
                                 "  1.Cat\n"
                                 "  2.Mouse\n"
            
                                 "  3.Dog\n"))
            if pet_type == 1:
                create_pet.cat()
            elif pet_type == 2:
                create_pet.mouse()
            elif pet_type == 3:
                create_pet.dog()
        except ValueError:
            print("I din't understand")
            create_pet.chose_pet()


    def cat(self):
        self.base_atributes["name"] = str(input("Enter your cat's name:\n"))
        self.base_atributes["weight"] = 13
        self.base_atributes["photo"] = "(=^o.o^=)"
        return run.begin(self.base_atributes)

    def mouse(self):
        self.base_atributes["name"] = str(input("Enter your mouse's name:\n"))
        self.base_atributes["weight"] = 2
        self.base_atributes["photo"] = "<:{ }~~~~"
        return run.begin(self.base_atributes)

    def dog(self):
        self.base_atributes["name"] = str(input("Enter your dog's name:\n"))
        self.base_atributes["weight"] = 35
        self.base_atributes["photo"] = "^o_=x=_o^"
        return run.begin(self.base_atributes)


# Main game class, holds all game commands
class Setup:
    def __init__(self):
        self.usr_input = 0
        self.total_steps = 0
        self.turns = 0
        self.file_in_use = "none"

    # First display menu
    def start_menu(self):
        print("Welcome to pypet!!!")
        print("--------------------\n")
        print("1. New Pet\n"
              "2. Continue\n")
        try:
            self.usr_input = int(input())
            if self.usr_input == 1:
                create_pet.chose_pet()
            elif self.usr_input == 2:
                files = glob.glob("*txt")
                print(files)
                chose_file = str(input("Enter pypets name:\n") + ".txt")
                selected_file = files.index(chose_file)
                self.file_in_use = files[selected_file]
                return stats.attributes(files[selected_file])
        except ValueError:
            print("I didn't understand.")
            run.start_menu()

    # Called from start_menu, prints pypet stats and holds initial game options
    def begin(self, pet):
        print(pet, "\n")
        if pet["health"] == 0:
            print("Oh no, It looks like your pet died!!!")
            del self.file_in_use
            return run.start_menu()

        print("Your pypet wakes from a long nap.")
        print("What would you like to do?\n\n"
                "  1. play with your pet.\n"
                "  2. save.\n"
                "  3. quit.\n")
        try:
            usr_input = int(input("\n"))
            if usr_input == 1:
                run.play(pet)
            elif usr_input == 2:
                print("1. Over wright current game.\n"
                      "2. Save new game.")
                save_option = int(input(""))
                if save_option == 1:
                    txt = open(self.file_in_use, "w")
                    for key, value in pet.items():
                        txt.write(str(value) + ",")
                    txt.close()
                elif save_option == 2:
                    file_name = str(input("Enter pets name:\n")) + ".txt"
                    txt = open(file_name, "w")
                    for key, value in pet.item2s():
                        txt.write(str(value) + ",")
                    txt.close()
                run.begin(pet)
            elif usr_input == 3:
                exit(1)
        except ValueError:
            print("I didn't understand!!")
            run.begin(pet)

    # Main Game function, Holds the rest of the game commands
    def play(self, pet):
        print(pet)
        print(self.total_steps)
        if pet["hungry"] is True:
            if pet["weight"] <= 10:
                print("your pet is starving\n")
            print("Your pet is hungry.\n")

        if pet["health"] >= 100:
            print("Your pet is Perfectly Happy!!")
        elif 75 <= pet["health"] <= 99:
            print("your pet is happy.")
        elif 50 < pet["health"] <= 74:
            print("Your pet is content.")
        elif pet["health"] <= 50:
            print("Your pet is sad\n")

        print("As you walk over to your pet, What do you do?\n"
              "  1. Make %s fall asleep\n"
              "  2. play fetch\n"
              "  3. rub belly\n"
              "  4. cuddle\n"
              "  5. feed\n"
              "  6. return to main menu\n" % pet["name"])

        try:
            choice = int(input())
            easter = randint(1, 100)
            if choice <= 5:
                if easter == 25:
                    print("Your pet does something amazing"
                          "and reads the zen of python to you!!!")
                    import this
                    print(this)
                pet["age"] += 0.01

            if 5 < self.total_steps < 10:
                pet["weight"] -= 1
            elif 10 < self.total_steps <= 15:
                pet["weight"] -= 2

            if pet["weight"] <= 10:
                pet["hungry"] = True

            # Make pet fall asleep
            if choice == 1:
                if self.turns >= 1:
                    print("Your pypet is sleeping")
                    print("  Z Z Z Z Z Z . . . . . ")
                    pet["health"] += 1
                    self.turns -= 1
                    run.play(pet)
                else:
                    pet["awake"] = False
                    pet["health"] += 2
                    self.turns = 2
                    run.play(pet)

            # Make pet play fetch
            if choice == 2:
                if self.turns >= 1:
                    print("Your pypet is sleeping")
                    print("  Z Z Z Z Z Z . . . . . ")
                    pet["health"] += 1
                    self.turns -= 1
                    run.play(pet)
                else:
                    run.fetch(pet)

            # Rub pets belly
            if choice == 3:
                real_chance = randint(1, 5)
                sleep_chance = randint(0, 1)
                if self.turns >= 1:
                    print("Your pypet is sleeping")
                    print("  Z Z Z Z Z Z . . . . . ")
                    pet["health"] += 1
                    self.turns -= 1
                    run.play(pet)
                else:
                    print("You sit down next to %s and start rubbing!!" % pet["name"])
                    if real_chance <= 2:
                        print("%s growls and bites you!!" % pet["name"])
                        pet["health"] -= 2
                    else:
                        print("%s likes the rubbing and snuggles closer to you!!" % pet["name"])
                        pet["health"] += 1
                        self.turns += sleep_chance
                    run.play(pet)

            # Cuddle with pet
            if choice == 4:
                real_chance = randint(1, 5)
                sleep_chance = randint(0, 2)
                if self.turns >= 1:
                    print("Your pypet is sleeping")
                    print("  Z Z Z Z Z Z . . . . . ")
                    pet["health"] += 1
                    self.turns -= 1
                    run.play(pet)
                else:
                    if real_chance <= 2:
                        print("your pet goes rabid and starts tearing up the couch!!")
                        pet["health"] -= 10
                        self.turns = sleep_chance
                    else:
                        print("You and your pet snuggle in for a long cuddle session!")
                        pet["health"] += 3
                        self.turns = sleep_chance
                    run.play(pet)

            # Feed your pet
            if choice == 5:
                if self.turns >= 1:
                    print("Your pypet is sleeping")
                    print("  Z Z Z Z Z Z . . . . . ")
                    pet["health"] += 1
                    self.turns -= 1
                    run.play(pet)
                else:
                    run.feed(pet)

            if choice == 6:
                run.begin(pet)
        except ValueError:
            print("I didn't understand.")
            run.play(pet)

    # Feeds the pet
    def feed(self, pet):
        if pet["hungry"] is True:
            pet["weight"] += 1
            pet["health"] += 3
            pet["hungry"] = False
            self.total_steps = 0
            return run.play(pet)
        elif pet["hungry"] is False:
            print("Sorry but your pet isn't hungry right now!!")
            return run.play(pet)

    def fetch(self, pet):
        steps = randint(0, 10)
        print("You throw the ball", end=" ")
        print(". . .")
        if steps <= 1:
            print("%s looks at you lazily and rolls over!!" % pet["name"])
            pet["health"] += 1
        else:
            print("%s runs after the ball and looks delighted bringing it back!!" % pet["name"])
            pet["health"] -= 1
        self.total_steps += steps
        print("%s took %d steps" % (pet["name"], steps))
        run.play(pet)


if __name__ == "__main__":
    run = Setup()
    create_pet = Pet()
    stats = Stats()
    run.start_menu()
