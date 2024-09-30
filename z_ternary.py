# z_ternary.py

def pythagore(a, b, c):
    """Teste si a, b, et c constituent les dimensions d’un triangle rectangle."""
    # Assurez-vous que les nombres sont triés pour trouver l'hypoténuse
    sides = sorted([a, b, c])
    # Théorème de Pythagore : a^2 + b^2 = c^2 (c étant le plus grand côté)
    return sides[0]**2 + sides[1]**2 == sides[2]**2
