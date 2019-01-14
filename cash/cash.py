import cs50

# infinite while loop, breaking when valid input is provided
while True:
    input = cs50.get_float("How much change is owed?\n")
    if input > 0:
        break

# Round floats, because their values are not perfect
cents = round(input * 100)
totalCoins = 0

# While loops remove change accordingly
while cents >= 25:
    cents -= 25
    totalCoins += 1
while cents < 25 and cents >= 10:
    cents -= 10
    totalCoins += 1
while cents < 10 and cents >= 5:
    cents -= 5
    totalCoins += 1
while cents < 5 and cents > 0:
    cents -= 1
    totalCoins += 1

print(totalCoins)