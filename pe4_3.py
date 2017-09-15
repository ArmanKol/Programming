#als lengtepersoon hoger of gelijk is aan 120 cm krijg je "Je bent lang....". Als lengtepersoon kleiner is dan 120 cm dan print die "Sorry je bent te klein!"
def lang_genoeg(centimeters):
    if centimeters >= 120:
        print("Je bent lang genoeg voor de attractie!")
    elif centimeters < 120:
        print("Sorry, je bent te klein!")

lengtepersoon = int(input("Vul hier je lengte in (cm): "))
lang_genoeg(lengtepersoon)