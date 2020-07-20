class Gameschema:
    def __init__(self):
        self.params = {"p1": " ", "p2": " ", "p3": " ", "p4": " ", "p5": " ", "p6": " ", "p7": " ", "p8": " ", "p9": " "}
        self.players = [1, 2]
        
    def get_input(self):
        command = input("Your turn: Enter the command: (x, o):\t")
        return command

    def get_col(self):
        col = input("Enter the place:\t")
        return col

    def validate_command(self):
        self.command = self.get_input()
        self.col = self.get_col()
        self.params[self.col] = self.command
        return self.params

    # def find_player(self):
    #     iteration = iter(self.players)
    #     for i in range(len(self.players)):
    #         next(iteration)

    def find_winner(self):
        if self.params["p1"]==self.params["p2"]==self.params["p3"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p1"]==self.params["p5"]==self.params["p9"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p3"]==self.params["p5"]==self.params["p7"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p3"]==self.params["p6"]==self.params["p9"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p1"]==self.params["p4"]==self.params["p7"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p7"]==self.params["p8"]==self.params["p9"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p2"]==self.params["p5"]==self.params["p8"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p1"]==self.params["p2"]==self.params["p3"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p1"]==self.params["p5"]==self.params["p9"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p3"]==self.params["p5"]==self.params["p7"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p3"]==self.params["p6"]==self.params["p9"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p1"]==self.params["p4"]==self.params["p7"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p7"]==self.params["p8"]==self.params["p9"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p2"]==self.params["p5"]==self.params["p8"]=="o":
            print("\nPLAYER 2 WINS!\n")
        else:
            return self.params

    def show_result(self):
        print(f'  {self.params["p1"]} | {self.params["p2"]} | {self.params["p3"]}')
        print("-------------")
        print(f'  {self.params["p4"]} | {self.params["p5"]} | {self.params["p6"]}')
        print("-------------")
        print(f'  {self.params["p7"]} | {self.params["p8"]} | {self.params["p9"]}')
