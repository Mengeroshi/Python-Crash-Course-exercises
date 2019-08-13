from random import choice

lot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, "a","z","b","y", "c"]
winner = []

while len(winner) < 4:
    numero_w = choice(lot)
    
    if numero_w not in winner:
        print(f"We pulled: {numero_w}")
        winner.append(numero_w)

        
print(f"The winner is {winner}")