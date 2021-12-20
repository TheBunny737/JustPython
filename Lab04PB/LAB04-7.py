#Lab 04-7 (Pokemon)
pokemon_Level = int(input("Enter level pokemon: "))
pokeball_Level = input("Enter level pokeball: ")
distance = int(input("Enter distance: "))
x = 0.00
s = 0.00

if pokeball_Level == 'h' or pokeball_Level == 'H':
    if pokemon_Level == 0 and pokemon_Level <= 40:
        x = 0.01
    elif pokemon_Level > 40 and pokemon_Level <= 60:
        x = 0.01
    else:
        x = 0.01

elif pokeball_Level == 'm' or pokeball_Level == 'M':
    if pokemon_Level == 0 and pokemon_Level <= 40:
        x = 0.03
    elif pokemon_Level > 40 and pokemon_Level <= 60:
        x = 0.05
    else:
        x = 0.08

elif pokeball_Level == 'l' or pokeball_Level == 'L':
    if pokemon_Level == 0 and pokemon_Level <= 40:
        x = 0.05
    elif pokemon_Level > 40 and pokemon_Level <= 60:
        x = 0.03
    else:
        x = 0.1

s = 100 - (pokemon_Level * distance * x)
if s < 0.00 or s > 100.00:
    s = 0.00
print("{:.2f} percent." .format(s))