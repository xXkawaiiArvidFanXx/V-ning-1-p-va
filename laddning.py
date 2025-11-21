import time
import random as rand

def rand_delay(min_delay, max_delay):
    delay = rand.uniform(min_delay, max_delay)
    time.sleep(delay)

def game_loading():
    print("Laddar orkester...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar trummor...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar gitarrer...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar bas...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar trumpeter...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar fioler...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar trummor igen...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar berättaröst...")
    time.sleep(rand_delay(0.01, 0.03))
    print("Laddar lite annat gojs...")
    time.sleep(rand_delay(2, 5))
    print("Allt laddat! Nu kör vi!")
    # Här skulle du lägga in kod för att spela upp ett ljud
    pass
