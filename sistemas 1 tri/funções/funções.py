c = [700, 450, 400, 300]
g = [1700, 400,3100]

def soma(lst):
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
        i += 1
    return total

tc = soma(c)
tg = soma(g)

d = tg - tc

print(f"Total de custos: R${tc}")
print(f"Total de ganhos: R${tg}")
print(f"Diferença (ganhos - custos): R${d}")