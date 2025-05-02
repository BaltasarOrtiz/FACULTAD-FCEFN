
# (D * 1000 + E * 100 + L * 10 + E) + (T * 1000 + O * 100 + D * 10 + O) = A * 10000 + D * 1000 + I * 100 + O * 10 + S

# haceme fuerza bruta de la ecuacion de arriba


def solve():
    for A in range(1, 10):
        for D in range(0, 10):
            for I in range(0, 10):
                for E in range(0, 10):
                    for L in range(0, 10):
                        for O in range(0, 10):
                            for S in range(0, 10):
                                for T in range(1, 10):
                                    if len(set([A, D, I, E, L, O, S, T])) == 8:
                                        if (D * 1000 + E * 100 + L * 10 + E) + (T * 1000 + O * 100 + D * 10 + O) == A * 10000 + D * 1000 + I * 100 + O * 10 + S:
                                            print(f"A: {A}, D: {D}, I: {I}, E: {E}, L: {L}, O: {O}, S: {S}, T: {T}")

solve()