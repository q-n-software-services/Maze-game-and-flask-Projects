TRAP = 1
FREE = 0

game_map = (
    'FREE', 'TRAP', 'TRAP', 'TRAP', 'TRAP',
    'FREE', 'FREE', 'FREE', 'TRAP', 'TRAP',
    'FREE', 'TRAP', 'FREE', 'TRAP', 'TRAP',
    'FREE', 'FREE', 'FREE', 'FREE', 'FREE',
    'TRAP', 'TRAP', 'TRAP', 'TRAP', 'FREE'
)


def ask_user():
    response = ''
    while response.lower() not in {"up", "down", "left", "right", "look", "exit"}:
        response = input("Please enter your action (up, down, left, right, look, exit): ")
    return response


class Maze:

    def __init__(self, game_map, start_position, exit_position):
        self._game_map = game_map
        self._start_position = start_position
        self._exit_position = exit_position

        self.playing = True
        self.position = 0

    def left(self):
        global game_map
        self.position -= 1
        if self.position < 0:
            self.position = 25 + self.position
        if self.position > 25:
            self.position = self.position - 25
        if game_map[self.position] == 'TRAP':
            self.position = 0
            print(" You fell in trap, \t the game has restarted")
            return

        return

    def right(self):
        global game_map
        self.position += 1
        if self.position < 0:
            self.position = 25 + self.position
        if self.position > 25:
            self.position = self.position - 25
        new_map = game_map
        if game_map[self.position] == 'TRAP':
            self.position = 0
            print(" You fell in trap, \t the game has restarted")
            return

        return

    def up(self):
        global game_map
        self.position -= 5
        if self.position < 0:
            self.position = 25 + self.position
        if self.position > 25:
            self.position = self.position - 25
        if game_map[self.position] == 'TRAP':
            self.position = 0
            print(" You fell in trap, \t the game has restarted")
            return
        return

    def down(self):
        global game_map
        self.position += 5
        if self.position < 0:
            self.position = 25 + self.position
        if self.position > 25:
            self.position = self.position - 25

        if game_map[self.position] == 'TRAP':
            self.position = 0
            print(" You fell in trap, \t the game has restarted")
            return
        return


    def look(self):
        print("Here is the message for you")

    def run(self):
        while self.playing:
            response = ask_user()

            if response == "exit":
                print("Sorry see you leaving...")
                exit()
            print(response)
            print()

            if response == 'up':
                self.up()
            elif response == 'down':
                self.down()
            elif response == 'left':
                self.left()
            elif response == 'right':
                self.right()
            elif response == 'look':
                self.look()

            new_map = [item for item in game_map]

            print()
            print(game_map)
            print()
            new_map[self.position] += '*'
            print(new_map[0], new_map[1], new_map[2], new_map[3], new_map[4])
            print(new_map[5], new_map[6], new_map[7], new_map[8], new_map[9])
            print(new_map[10], new_map[11], new_map[12], new_map[13], new_map[14])
            print(new_map[15], new_map[16], new_map[17], new_map[18], new_map[19])
            print(new_map[20], new_map[21], new_map[22], new_map[23], new_map[24])
            print()
            print()
            print()

if __name__ == '__main__':

    Maze(game_map=game_map, start_position=(0, 0), exit_position=(4, 4)).run()
