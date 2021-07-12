import turtle

file = open("thor-turtle", "r")
s = turtle.Screen()
t = turtle.Turtle()
t.left(90)

lines = file.readlines()
for line in lines:
    words = line.split(" ")
    if len(words) == 1:
        t.reset()
        t.left(90)
    elif words[0] == "Avance":
        t.forward(int(words[1]))
    elif words[0] == "Recule":
        t.backward(int(words[1]))
    elif words[0] == "Tourne":
        if words[1] == "gauche":
            t.left(int(words[3]))
        elif words[1] == "droite":
            t.right(int(words[3]))



file.close()