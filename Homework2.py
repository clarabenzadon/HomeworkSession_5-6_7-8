solution = "SSNWES"

print("Welcome to the magic maze game!")

moves = 0
lives = 0
pathcompletion = 0

while True:

    for letter in solution:
        direction = input("Enter one of the following directions: N | W | S | E")
        moves += 1
        if moves % 10 == 0:
            lives-=1
            print("you lost a life, you have", lives, "life left")
        if direction != letter:
            print("Incorrect direction")
            pathcompletion = 0
            break

        pathcompletion += 1

    if pathcompletion == 6:
        print("Congratulations you escaped the magic maze")
        break

    if lives == 0:
        print("GAME OVER")
        break