alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
digitos = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

print(f"A unión B: {alfabeto.union(digitos)}")  # type: ignore
print("")
print(f"A intersección B: {alfabeto.intersection(digitos)}")
print("")
print(f"A x B: {[(a, b) for a in alfabeto for b in digitos]}")
print("")
print(f"A^3: {[(a, b, c) for a in alfabeto for b in alfabeto for c in alfabeto]}")
print("")
print(f"B^2: {[(a, b, c) for a in digitos for b in digitos for c in digitos]}")
print("")
