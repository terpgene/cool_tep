# tutorial file to learn

qa = ["What is your name? ",
      "What is your fav. color? ",
      "What is your quest? "]

n = 0
while True:
    print("Type q to quit")
    a = input(qa[n])
    if a == "q".lower():
        break
    n = (n + 1) % 3
