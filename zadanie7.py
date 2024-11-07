import random
pogoda = random.choice([0, 1])
while True:
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").strip().lower()
    if odpowiedz == "tak" and pogoda == 1:
        print("Brawo! Zgadłeś, pada deszcz.")
        break
    elif odpowiedz == "nie" and pogoda == 0:
        print("Brawo! Zgadłeś, nie pada deszcz.")
        break
    else:
        print("Nie zgadłeś! Spróbuj ponownie.")
