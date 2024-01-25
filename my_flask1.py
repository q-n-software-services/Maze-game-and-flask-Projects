import os
import sys

from flask import Flask, jsonify

app = Flask(__name__)

TRAP = False
FREE = 0

game_map = (
    'FREE', 'TRAP', 'TRAP', 'TRAP', 'TRAP',
    'FREE', 'FREE', 'FREE', 'TRAP', 'TRAP',
    'FREE', 'TRAP', 'FREE', 'TRAP', 'TRAP',
    'FREE', 'FREE', 'FREE', 'FREE', 'FREE',
    'TRAP', 'TRAP', 'TRAP', 'TRAP', 'FREE'
)
new_map = []

def ask_user():
    response = ''
    while response.lower() not in {"up", "down", "left", "right", "look", "exit"}:
        response = input("  Please enter your action (up, down, left, right, look, exit): ")
    return response





_game_map = game_map
_start_position = (0, 0)
_exit_position = (4, 4)

playing = True
position = 0

def left():
    global game_map
    global position
    global TRAP
    position -= 1
    if position < 0:
        position = 25 + position
    if position >= 25:
        position = position - 25
    if game_map[position] == 'TRAP':
        position = 0
        TRAP = True
        return

    return

def right():
    global game_map
    global position
    global TRAP
    position += 1
    if position < 0:
        position = 25 + position
    if position >= 25:
        position = position - 25
    new_map = game_map
    if game_map[position] == 'TRAP':
        position = 0
        TRAP = True
        return

    return
def exit():
    position = 0

    return " <h1>You terminated the maze game, \t the game has restarted</h1>"
def up():
    global game_map
    global position
    global TRAP
    position -= 5
    if position < 0:
        position = 25 + position
    if position >= 25:
        position = position - 25
    if game_map[position] == 'TRAP':
        position = 0
        TRAP = True
        return
    return

def down():
    global game_map
    global position
    position += 5
    if position < 0:
        position = 25 + position
    if position >= 25:
        position = position - 25

    if game_map[position] == 'TRAP':
        position = 0
        TRAP = True

        return
    return


def look():

    return "<h1>Just follow the path you see visually best to reach the end <h1>"


@app.route("/")
def hello_world():

    return '''<h1>Please Enter the inputs in url after the base url and enter to proceed</h1><p>\n\n</p><h3>In the form 127.0.0.1:5000/up</h3><h4>LIKE THIS</h4>'''


@app.route("/<string:response>")
def play(response):
    global new_map
    global position
    global game_map
    global TRAP
    if response == "exit":
        print("Sorry see you leaving...")
        exit()
    print(response)
    print()

    if response == 'up':
        up()
    elif response == 'down':
        down()
    elif response == 'left':
        left()
    elif response == 'right':
        right()
    elif response == 'look':
        a = look()
        return jsonify(a)

    new_map = [item for item in game_map]
    new_map[position] += '*'

    '''new_map = "<h1><pre>" + '\t' + str(new_map[0]) + '\t' + str(new_map[1]) + '\t' + str(new_map[2]) + '\t' + str(new_map[3]) + '\t' + str(new_map[4]) + '\n\n' + '\t' + str(new_map[5]) + '\t' + str(new_map[6]) + '\t' + str(new_map[7]) + '\t' +  str(new_map[8]) + '\t' + str(new_map[9]) + '\n\n' + '\t' + str(new_map[10]) + '\t' + str(new_map[11]) + '\t' + str(new_map[12]) + '\t' + str(new_map[13]) + '\t' + str(new_map[14]) + '\n\n' + '\t' + str(new_map[15]) + '\t' + str(new_map[16]) + '\t' + str(new_map[17]) + '\t' +  str(new_map[18]) + '\t' + str(new_map[19]) + '\n\n' '\t' + str(new_map[20]) + '\t' + str(new_map[21]) + '\t' + str(new_map[22]) + '\t' + str(new_map[23]) + '\t' + str(new_map[24]) + "</pre></h1>"
    "'''
    new_map = [
        [str(new_map[0]) + '        ' + str(new_map[1]) + '        ' + str(new_map[2]) + '        ' + str(new_map[3]) + '        ' + str(new_map[4])],
        [str(new_map[5]) + '        ' + str(new_map[6]) + '        ' + str(new_map[7]) + '        ' + str(new_map[8]) + '        ' + str(new_map[9])],
        [str(new_map[10]) + '        ' + str(new_map[11]) + '        ' + str(new_map[12]) + '        ' + str(new_map[13]) + '        ' + str(new_map[14])],
        [str(new_map[15]) + '        ' + str(new_map[16]) + '        ' + str(new_map[17]) + '        ' + str(new_map[18]) + '        ' + str(new_map[19])],
        [str(new_map[20]) + '        ' + str(new_map[21]) + '        ' + str(new_map[22]) + '        ' + str(new_map[23]) + '        ' + str(new_map[24])]
    ]
    if TRAP:
        new_map.append("You Fell in Trap, The game maze game has restarted")
    TRAP = False
    return jsonify(new_map)
app.run(debug=True)