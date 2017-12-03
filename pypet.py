"""
   pypet V1.3

   Welcome to pypet, my first attempt at building a python game

   Currently you can create and save new pets, allowing you to have as many
   pets as you would like. You have 5 main game options, will be changing
   that shortly :). You have 3 pet types to chose from, again more  will be
   added shortly. The game is broken up in to 3 classes and 3 subclasses. The 3 classes are
   Stats, Pet, and Setup. The subclasses are Cat, Dog, and Mouse. They are all subclasses of Pet.
   Each pet has its own functionality with some, like fed and sleep, being universal across all of them.

   GAMEPLAY - Interactions with pets are based on which type of pet you have.The Dog has walk, fetch, and relax.
   The cat has cuddle and give catnip. The mouse has build tunnels and run on running wheel. The cat and the mouse
   share a function rub that allows you to pet your PyPet. The functions feed and sleep are accessible across all
   pets.
   FIXME: Work out turtle graphics for pet animation
   FIXME - Float used for age is supposed to be set to the second decimal point, but doesnt reflect the coding
   FIXME: recode total steps to change hunger status
   FIXME: sleep counter not functioning, recode
   FIXME: work out saved pets interacting with each other, atleast one other pet

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
            "type": stat_list[6],
            "awake": True
        }
        return run.play(self.attribute)


# Class for creating and interacting with PyPets
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
            "type": "none",
            "awake": True
        }
        self.options = []
        self.sleep_chance = randint(0, 2)
        self.steps = 0
        self.easter = randint(1, 100)
        self.real_chance = randint(1, 10)

    # Function to build new pet
    def chose_pet(self):
        try:
            pet_type = int(input("Enter the type of pet you would like:\n"
                                 "  1.Cat\n"
                                 "  2.Mouse\n"
                                 "  3.Dog\n"))
            if pet_type == 1:
                cat.create()
            elif pet_type == 2:
                mouse.create()
            elif pet_type == 3:
                dog.create()
        except ValueError:
            print("I didn't understand")
            create_pet.chose_pet()

    # Builds the gameplay option menu
    # FIXME: general_interactions need to be available to all pets on top of type special interactions
    def option_menu(self, pet):
        if pet["type"] == "cat":
            self.options = cat.menu(pet)
        elif pet["type"] == "mouse":
            self.options = mouse.menu(pet)
        elif pet["type"] == "dog":
            self.options = dog.menu(pet)

    # Base interactions that are generic across all pets
    def general_interactions(self, pet, x):
        self.real_chance = randint(1, 5)

        # Puts the pet to sleep for a turn
        def sleep(stat):
            print("Your PyPet is sleeping")
            print("  Z Z Z Z Z Z . . . . . ")
            stat["health"] += 1
            return run.play(stat)

        # Feeds the pet
        def feed(stat):
            print("Your pet is joyous as you put their food in their dish.")
            if stat["hungry"] is True:
                stat["weight"] += 1
                stat["health"] += 3
                stat["hungry"] = False
                self.total_steps = 0
            elif stat["hungry"] is False:
                print("Sorry but your pet isn't hungry right now!!")
            return run.play(stat)

        # Option to 'pet' the PyPet
        def rub(stat):
            if self.real_chance <= 2:
                print("%s growls and bites you!!" % stat["name"])
                stat["health"] -= 2
            else:
                print("%s likes the rubbing and snuggles closer to you!!" % stat["name"])
                stat["health"] += 1
            return run.play(pet)

        if x == 1:
            sleep(pet)
        elif x == 2:
            feed(pet)
        elif x == 3:
            rub(pet)

    # Function for interacting with PyPet
    def gameplay(self, pet):
        create_pet.option_menu(pet)
        try:
            usr_input = int(input())
            if usr_input:
                pet["age"] += 0.01
                if self.sleep_chance == 2:
                    self.sleep_chance = randint(0, 2)
                    create_pet.general_interactions(pet, 1)
                else:
                    if self.easter == 25:
                        print("Your pet does something amazing"
                          "and reads the zen of python to you!!!")
                        import this
                        print(this)
                        return run.play(pet)
                    else:
                        if usr_input == 1:
                            self.easter = randint(1, 100)
                            self.sleep_chance = randint(0, 2)
                            if pet["type"] == "cat":
                                cat.interactions(pet, 1)
                            elif pet["type"] == "mouse":
                                mouse.interactions(pet, 1)
                            elif pet["type"] == "dog":
                                dog.interactions(pet, 1)
                        elif usr_input == 2:
                            self.easter = randint(1, 100)
                            self.sleep_chance = randint(0, 2)
                            if pet["type"] == "cat":
                                cat.interactions(pet, 2)
                            elif pet["type"] == "mouse":
                                mouse.interactions(pet, 2)
                            elif pet["type"] == "dog":
                                dog.interactions(pet, 2)
                        elif usr_input == 3:
                            self.easter = randint(1, 100)
                            self.sleep_chance = randint(0, 2)
                            create_pet.general_interactions(pet, 3)
                        elif usr_input == 4:
                            self.easter = randint(1, 100)
                            self.sleep_chance = randint(0, 2)
                            create_pet.general_interactions(pet, 2)
                        elif usr_input == 5:
                            create_pet.general_interactions(pet, 1)
                        elif usr_input == 6:
                            run.start_menu(pet)
                        else:
                            print("Sorry, that is not a option!!")
                            return run.play(pet)

        except ValueError:
            print("I didn't understand that!!")
            return run.play(pet)

# Class for pet Cat
class Cat(Pet):

    def __init__(self):
        super().__init__()

    # Creates new cat type pet
    def create(self):
        self.base_atributes["name"] = str(input("Enter your cats name:\n"))
        self.base_atributes["photo"] = "(=^o.o^=)"
        self.base_atributes["type"] = "cat"
        self.base_atributes["weight"] = 13
        return run.play(self.base_atributes)

    # cat specific menu
    # FIXME: options 3,4, and 5 are universal and need to be treated as such
    def menu(self, pet):
        self.options = [print("1. Cuddle with %s" % pet["name"]), print("2. Give %s catnip" % pet["name"]),
                        print("3. pet %s" % pet["name"]), print("4. Feed %s" % pet["name"]),
                        print("5. Make %s fall asleep" % pet["name"]), print("6. Return to main menu")]
        return self.options

    # cat specific interactions
    def interactions(self, pet, x):
        self.real_chance = randint(1, 5)

        # Choice to cuddle with pet
        def cuddle(stat):
            if self.real_chance <= 2:
                print("your pet goes rabid and starts tearing up the couch!!")
                stat["health"] -= 10
                stat["weight"] -= 1
                self.steps += self.real_chance
            else:
                print("You and your pet snuggle in for a long cuddle session!")
                stat["health"] += 3
            return run.play(stat)

        # Choice to give cat catnip
        def catnip(stat):
            if self.real_chance <= 2:
                print("Your pet goes crazy and bites you!!")
                stat["health"] -= 4

            else:
                print("%s is in love and plays with the catnip joyfully!!" % stat["name"])
                stat["health"] += 4
                stat["weight"] -= 1
            self.steps += self.real_chance
            return run.play(stat)
        if x == 1:
            cuddle(pet)
        elif x == 2:
            catnip(pet)


# Class for pet Mouse
class Mouse(Pet):
    def __init__(self):
        super().__init__()

    # Creates new mouse type pet
    def create(self):
        self.base_atributes["name"] = str(input("Enter your mouse's name:\n"))
        self.base_atributes["weight"] = 2
        self.base_atributes["photo"] = "<:{ }~~~~"
        self.base_atributes["type"] = "mouse"
        return run.play(self.base_atributes)

    # Mouse specific menu
    # FIXME: options 3,4, and 5 are universal and need to be treated as such
    def menu(self, pet):
        self.options = [print("1. Build tunnels"), print("2. Put %s on running wheel" % pet["name"]),
                        print("3. Pet %s" % pet["name"]), print("4. Feed %s" % pet["name"]),
                        print("5. Make %s fall asleep" % pet["name"]), print("6. Return to main menu")]
        return self.options

    # Mouse specific interactions
    def interactions(self, pet, x):
        self.real_chance = randint(1, 10)

        # Choice to build tunnels for mouse
        def build(stat):
            print("You buy some new tunnel pieces for your mouse cage.")
            print(". . .")
            if self.real_chance <= 3:
                print("Two of the pieces break and you throw the rest away in frustration!!")
                stat["weight"] += 1
            else:
                print("You build %d sections of tunnel and %s seems very happy" % (self.real_chance, stat["name"]))
                stat["weight"] -= 1
                stat["health"] += 2
            return run.play(stat)

        # Choice to put mouse on running wheel
        def wheel(stat):
            print("You put %s on the running wheel" % stat["name"])
            print(". . .")
            if self.real_chance <= 3:
                print("%s just climbs back off the wheel!!" % stat["name"])
                stat["health"] -= 2
                stat["weight"] += 1
            else:
                print("%s runs like no other!!" % stat["name"])
                stat["health"] += 2
                stat["weight"] -= 1
            return run.play(stat)
        if x == 1:
            build(pet)
        elif x == 2:
            wheel(pet)


# Class for pet Dog
class Dog(Pet):
    def __init__(self):
        super().__init__()

    # Creates new dog type pet
    def create(self):
        self.base_atributes["name"] = str(input("Enter your dog's name:\n"))
        self.base_atributes["weight"] = 35
        self.base_atributes["photo"] = "^o_=x=_o^"
        self.base_atributes["type"] = "dog"
        return run.play(self.base_atributes)

    # Dog specific menu
    # FIXME: options 3,4, and 5 are universal and need to be treated as such
    def menu(self, pet):
        self.options = [print("1. Take %s for a walk" % pet["name"]), print("2. Play fetch"),
                        print("3. pet %s" % pet["name"]), print("4. Feed %s" % pet["name"]),
                        print("5. Make %s fall asleep" % pet["name"]), print("6. Return to main menu")]
        return self.options

    # Dog specific interactions
    def interactions(self, pet, x):
        self.real_chance = randint(1, 10)

        # Choice to walk dog
        def walk(stat):
            print("Your show %s the leash. ' wana go for a walk?' " % stat["name"])
            print(". . .")
            if self.real_chance <= 1:
                print("%s growls at you, then runs and hides!!")
                stat["health"] -= 2
            else:
                stat["hungry"] = True
                print("You hook the lease to %s's collar and take a %d minute hike across the park." %
                      (stat["name"], self.real_chance))
                stat["health"] += 3
                stat["weight"] -= 1
                self.steps += self.real_chance
            return run.play(stat)

        # Choice to play fetch with dog
        def fetch(stat):
            print("You throw the ball", end=" ")
            print(". . .")
            if self.real_chance <= 1:
                print("%s looks at you lazily and rolls over!!" % stat["name"])
                stat["health"] += 1
            else:
                print("%s runs after the ball and looks delighted bringing it back!!" % stat["name"])
                print("%s took %d steps" % (stat["name"], self.real_chance))
                stat["health"] -= 1
                stat["weight"] -= 1
                self.steps += self.real_chance
            return run.play(pet)
        if x == 1:
            walk(pet)
        elif x == 2:
            fetch(pet)





# Class for base game setup, holds the options for creating new pet, continuing saved pets,
# saving the current pet, and quiting the game
class Setup:
    def __init__(self):
        self.usr_input = 0
        self.total_steps = 0
        self.turns = 0
        self.file_in_use = "none"

    # Main menu
    # FIXME: change initial print statements to a print list for uniformity
    def start_menu(self, pet=None):
        print("Welcome to pypet!!!")
        print("--------------------\n")
        print("1. New Pet\n"
              "2. Continue\n"
              "3. save.\n"
              "4. quit.\n")
        try:
            self.usr_input = int(input())
            if self.usr_input == 1:
                create_pet.chose_pet()
            elif self.usr_input == 2:
                # import from glob, used to search the directory for all txt files
                files = glob.glob("*txt")
                print(files)
                chose_file = str(input("Enter pypets name:\n") + ".txt")
                selected_file = files.index(chose_file)
                self.file_in_use = files[selected_file]
                return stats.attributes(files[selected_file])
            # Save game options
            # FIXME: make this a function
            elif self.usr_input == 3:
                print("1. Over wright current game.\n"
                      "2. Save new game.")
                save_option = int(input(""))
                # Overwrites continued save file,
                if save_option == 1:
                    if self.file_in_use == "none":
                        print("Sorry there is no previous save for this pet!!")
                        return run.start_menu(pet)
                    else:
                        txt = open(self.file_in_use, "w")
                        for key, value in pet.items():
                            txt.write(str(value) + ",")
                        txt.close()
                # Saves to a new txt file
                elif save_option == 2:
                    file_name = str(input("Enter pets name:\n")) + ".txt"
                    txt = open(file_name, "w")
                    for key, value in pet.items():
                        txt.write(str(value) + ",")
                    txt.close()
                run.start_menu(pet)
            elif self.usr_input == 4:
                exit(0)
        except ValueError:
            print("I didn't understand.")
            run.start_menu()

    # Handles stat print outs and adjustments
    # FIXME: rewrite to make play handle all the stat adjustments, I.E  steps = hunger
    def play(self, pet):
        print(pet, "\n")
        if pet["health"] == 0:
            print("Oh no, It looks like your pet died!!!")
            del self.file_in_use
            return run.start_menu(pet)

        if pet["hungry"] is True:
            if pet["weight"] <= ((1/3 * ) ):
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
        create_pet.gameplay(pet)


if __name__ == "__main__":
    run = Setup()
    create_pet = Pet()
    stats = Stats()
    cat = Cat()
    dog = Dog()
    mouse = Mouse()
    run.start_menu()
