def lang_genoeg(centimeters):
    if centimeters >= 120:
        print("Je bent lang genoeg voor de attractie!")
    elif centimeters < 120:
        print("Sorry, je bent te klein!")

lengtepersoon = int(input("Vul hier je lengte in (cm): "))
lang_genoeg(lengtepersoon)