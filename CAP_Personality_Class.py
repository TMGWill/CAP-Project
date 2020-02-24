import time


class CAP_P:
    """
    This creates the CAP_P class which asks the user questions
    and returns values that will be used in the CAP_A class
    """

    def __init__(self):
        """
        This initializes  the values for the
        methods of this class.
        """

        self.start = ""
        self.age_num = 0
        self.low_answer = 0
        self.high_answer = 0
        self.height_num = 0
        self.begin = ""
        self.end = ""
        self.animal = ""
        self.age_num_multi = 0

    def ask_age(self):
        """
        This function asks how old the user is
        and returns their input as a value.

        :return: self.age_num
        """

        age_num = input("\nHow old are you?")
        self.age_num = int(age_num)

        while age_num.isnumeric() is False or self.age_num < 1:
            age_num = input("\nHow old are you?")
            self.age_num = int(age_num)

        return self.age_num

    def ask_height(self):
        """
        This function asks the user their opinion on
        their height which takes the input and uses it
        to an return an integer.

        :return: self.height_num
        """

        height = input("Do you see yourself as tall, short, or average height? [tall/average/short]")

        while True:
            if height == "tall" or height == "average" or height == "short":
                break
            print("")
            print("Whoops, looks like you made a typo. Try again.\n")
            height = input("Do you see yourself as tall, short, or average height? [tall/average/short]")

        if height == "tall":
            self.height_num = 200
        elif height == "average":
            self.height_num = 100
        elif height == "short":
            self.height_num = 50
        return self.height_num

    def ask_fav_color(self):
        """
        Asks user their favorite color which will return a string
        containing their color or the word random. This will be used for
        the create_art method in the CAP_A class.

        :return: self.art_color
        """

        question = input("Do you have a favorite color? [yes/no]")

        while True:
            if question == "yes" or question == "no":
                break
            question = input("Do you have a favorite color? [yes/no]")

        if question == "yes":
            print("")
            self.art_color = input("What is it?")
        elif question == "no":
            self.art_color = "random"

        print("")

        return self.art_color

    def fake_guessing_game_low(self):
        """
        A fake guessing game that will be used as one
        part of the input for sides in the create_art method
        in the CAP_A class.

        :return: self.low_answer
        """

        self.low_answer = int(input("I'm thinking of a number between 1-5"))

        while self.low_answer < 3 or self.low_answer > 5:
            print("\nThat's not it.\n")
            self.low_answer = int(input("I'm thinking of a number between 1-5"))

        time.sleep(2)
        print("\n.", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        time.sleep(3)
        print("\nI know I wrote that number down somewhere but I think I lost it.\n")
        time.sleep(3)
        print("Well", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        time.sleep(3)
        print("\nLets move on to another question.\n")

        return self.low_answer

    def fake_guessing_game_high(self):
        """
        A fake guessing game that will be used as the other
        part of the input for sides in the create_art method
        in the CAP_A class.

        :return: self.high_answer
        """

        self.high_answer = int(input("I'm thinking of a number between 6-10"))

        while self.high_answer < 6 or self.high_answer > 10:
            print("\nThat's not it.\n")
            self.high_answer = int(input("I'm thinking of a number between 6-10"))
        time.sleep(3)
        print("\nWhoops.\n")
        time.sleep(3)
        print("I forgot what number I picked.\n")
        time.sleep(3)
        print("Not enough RAM, know what I mean?\n")

        return self.high_answer

    def start_pos(self):
        """
        Takes user input and returns a string
        that will be used for the create_art
        method in the CAP_A class.

        :return: self.start
        """

        start = input("\nDo you usually see yourself as carefree? [yes/no]")

        while True:
            if start == "yes" or start == "no":
                break
            start = input("\nDo you usually see yourself as carefree? [yes/no]")

        if start == "yes":
            self.start = "carefree"

        elif start == "no":
            start2 = input("\nAre you left-handed, right-handed, or ambidextrous? [left/right/ambi]")
            if start2 == "left":
                self.start = ""
            elif start2 == "ambi":
                self.start = ""
            elif start2 == "right":
                self.start = ""

            start3 = input("\nAre you high on life, here on planet Earth or, down in the dumps? [high/earth/down]")
            if start3 == "high":
                self.start = ""
            elif start3 == "earth":
                self.start = ""
            elif start3 == "down":
                self.start = ""

            if start2 == "left" and start3 == "high":
                self.start = "left high"
            elif start2 == "left" and start3 == "earth":
                self.start = "left middle"
            elif start2 == "left" and start3 == "down":
                self.start = "left bottom"

            elif start2 == "ambi" and start3 == "high":
                self.start = "middle high"
            elif start2 == "ambi" and start3 == "earth":
                self.start = "middle middle"
            elif start2 == "ambi" and start3 == "down":
                self.start = "middle bottom"

            elif start2 == "right" and start3 == "high":
                self.start = "right high"
            elif start2 == "right" and start3 == "earth":
                self.start = "right middle"
            elif start2 == "right" and start3 == "down":
                self.start = "right bottom"

        return self.start

    def dogs_and_cats(self):
        """
        This takes the user's input and prints
        out a text image based on their response

        :return: None
        """

        self.animal = input("Do you prefer cats, dogs, or both? [cats/dogs/both]")

        while True:
            if self.animal == "cats" or self.animal == "dogs" or self.animal == "both":
                break
            self.animal = input("Do you prefer cats, dogs, or both? [cats/dogs/both]")

        if self.animal == "dogs":
            print("\nWho let the dogs out?")
            time.sleep(1.5)
            print("\nI let the dogs out. :) ")
            time.sleep(2)
            print('''
         .--.             .---.
        /:.  '.         .' ..  '._.---.
       /:::-.  \.-"""-;`,.-:::.     .::\ 
      /::'|  `\/  _ _  \    `\:'   ::::|
  __.'    |   /  (o|o)  \     `'.   ':/
 /    .:. /   |   ___   |        '---'
|    ::::'   /:  (._.) .:\ 
\    .='    |:'        :::|
 `""`       \     .-.   ':/
             '---`|I|`---'
                  '-'
            ''')
        elif self.animal == "cats":
            print("\nRAWR XD")
            time.sleep(2)
            print('''
                   ,   __, ,
   _.._         )\/(,-' (-' `.__
  /_   `-.      )'_      ` _  (_    _.---._
 // \     `-. ,'   `-.    _\`.  `.,'   ,--.\ 
// -.\       `        `.  \`.   `/   ,'   ||
|| _ `\_         ___    )  )     \  /,-'  ||
||  `---\      ,'__ \   `,' ,--.  \/---.  //
 \   .---`.   / /  | |      |,-.\ |`-._ //
  `..___.'|   \ |,-| |      |_  )||\___//
    `.____/    \ \O| |      \o)// |____/
         /      `---/        \-'  \ 
         |        ,'|,--._.--')    \ 
         \       /   `n     n'\    /
          `.   `<   .::`-,-'::.) ,'    
            `.   \-.____,^.   /,'
              `. ;`.,-V-.-.`v'
                \| \     ` \|\ 
                 ;  `-^---^-'/
                  `-.______,' ''')

        elif self.animal == "both":
            print("\nBest of both of worlds.")
            time.sleep(1.5)
            print('''
           .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
      `-._   ````    _.-'
          ``-------''    
          ''')
            time.sleep(2)
            print('''
           ___
       .-'`   `'-.
   _,.'.===   ===.'.,_
  / /  .___. .___.  \ \ 
 / /   ( o ) ( o )   \ \                                            _
: /|    '-'___'-'    |\ ;                                          (_)
| |`\_,.-'`   `"-.,_/'| |                                          /|
| |  \             /  | |                                         /\;
| |   \           /   | | _                              ___     /\/
| |    \   __    /\   | |' `\-.-.-.-.-.-.-.-.-.-.-.-.-./`   `"-,/\/ 
| |     \ (__)  /\ `-'| |    `\ \ \ \ \ \ \ \ \ \ \ \ \`\       \/
| |      \-...-/  `-,_| |      \`\ \ \ \ \ \ \ \ \ \ \ \ \       \ 
| |       '---'    /  | |       | | | | | | | | | | | | | |       |
| |               |   | |       | | | | | | | | | | | | | |       |
\_/               |   \_/       | | | | | | | | | | | | | | .--.  ;
                  |       .--.  | | | | | | | | | | | | | | |  | /
                   \      |  | / / / / / / / / / / / / / /  |  |/
                   |`-.___|  |/-'-'-'-'-'-'-'-'-'-'-'-'-'`--|  |
            ,.-----'~~;   |  |                  (_(_(______)|  |
           (_(_(_______)  |  |                        ,-----`~~~\ 
                    ,-----`~~~\                      (_(_(_______)
                   (_(_(_______)
            ''')

    def age_num_multiplier(self):
        """
        This is a method that is used to get
        a number that will be used to multiply
        the user's number they put in for their age.

        :return: self.age_num_multi
        """

        print('''
You stand before a bowl of Halloween candy that is unattended.
The sign in front of the bowl says "Please take two"
        ''')
        age_num_multi = input("How many pieces of candy do you take? [1/2/3]")

        while age_num_multi.isnumeric() is False:
            age_num_multi = input("How many pieces of candy do you take? [1/2/3]")
            if age_num_multi.isnumeric():
                break

        self.age_num_multi = int(age_num_multi)

        while self.age_num_multi < 1:
            print("You don't get good person points.")
            self.age_num_multi = int(input("How many pieces of candy do you take? [1/2/3]"))

        while self.age_num_multi > 3:
            print("You monster! You can only take so many.")
            self.age_num_multi = int(input("How many pieces of candy do you take? [1/2/3]"))

        time.sleep(2)
        print("\nThe Home Owners will remember this.\n")

        return self.age_num_multi

    def start_convo(self):
        """
        This serves as an introduction and
        gives the user a choice of whether
        or not they want to continue or
        quit the program

        :return: None
        """

        self.begin = input('''Hello, I am CAP which is short for Caprasio and also
an acronym for Computer Art Personality. Would you like to 
answer some questions that I have for you? [yes/no]''')

        if self.begin == "yes":
            print("\nrunning happy.exe", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(2)
            print('''
░░░░░░░▄▄████▄▄▄░░░░░░▄▄██████▄▄
░░░░░██▓▓▓▓▓▓▒▓▓██░░▓█▓▓▓▓▒░▒▒▓▓██
░░░██▓▓▓▓▓▓▓▓▓▒░▓▓███▓▓▓▓▓▒▒▒░░▒▓▓█
░░██▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▒░░▓▓█
░▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓██▓▓▓▓▓▓▓▓▓▒░░▓▓█
░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▓█
░█▓▓▓▓▓▓▓▓▓▓▓▓████░████▓▓▓▓▓▓▓▓▓▒░░▓██
█▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░██▓▓▓▓▓▓▓▓▓░░▓▓█
█▓▓▓▓▓▓▓▓▓▓▓▓▓░░█░░░█░░▓▓▓▓▓▓▓▓▓▓▒░▓▓█▒
█▓▓▓▓▓▓▓▓▓▓▓▓▓░█▒█░█▒█░▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▒
█▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓██▒
█▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒██░░░▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▒
░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▒
░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓█▓▒
░░░█▓▓▓▓▓▓▓▓▓██▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓█▓▒
░░░░█▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░▓█▓▓▓▓▓▓▓▓██▒▒▓▒▒█▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░█▓▓▓▓▓▓▓▓██▒▒▒█▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░██▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓█▓▒
░░░░░░░░░░░░░░░██▓▓▓▓▓██▓▒
░░░░░░░░░░░░░░░░░█▓▓██▓▒
░░░░░░░░░░░░░░░░░░░█▓▒\n''')
            time.sleep(1)
            print("You made the right choice. You won't be disappointed!\n")

        else:
            print("\nrunning sad.exe", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".\n")
            time.sleep(2)
            print("Why not?\n")
            time.sleep(3)
            print('''
     .-""""""-.
   .'          '.
  /   O      O   \ 
 :           `    :
 |                |
 :    .------.    :
  \  '        '  /
   '.          .'
     '-......-'
            ''')
            time.sleep(3)
            quit()

    def end_convo(self):
        """
        This method gives the user the illusion
        that they have a choice but ultimately
        this will be an indication to the end of
        the questions and that the drawing will begin.

        :return: None
        """

        self.end = input("Well, it's time to bring this conversation to an end. Are you ready? [yes/no]")

        if self.end == "yes":
            print("\nAll right, lets get the finale underway.")
            print('''
Just to let you know, some of these questions were used just for your amusement 
while the others were needed so I could have the information necessary to draw what 
your soul would look like.\n''')
            time.sleep(10)
            print("I'm just kidding, but your answers did influence the outcome of my artwork you're about to see.\n")
            time.sleep(3)
            print("Anyway lets begin")

        else:
            print("\nDon't worry you're ready.")
            print('''
Just to let you know, some of these questions were used just for your amusement 
while the others were needed so I could have the information necessary to draw what 
your soul would look like.\n''')
            time.sleep(10)
            print("I'm just kidding, but your answers did influence the outcome of my artwork you're about to see.")
            time.sleep(3)
            print("Anyway lets begin")
