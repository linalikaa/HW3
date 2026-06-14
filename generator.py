import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["GENRE", "COLOR1", "COLOR2", "MATERIAL", "STYLE"]

GENRES = ["Пейзаж", "Портрет", "Натюрморт","Анималистика","Бытовой"]
COLORS = ["Красный", "Синий", "Зелёный", "Жёлтый", "Оранжевый", "Фиолетовый", "Розовый", "Белый", "Чёрный", "Бирюзовый", "Охра", "Серый"]
MATERIALS = ["Акварель", "Масло", "Карандаш", "Пастель","Акрил"]
STYLES = ["Реализм", "Импрессионизм", "Романтизм", "Абстракционизм", "Сюрреализм", "Кубизм","Поп-арт"]

def generate_row():

    return {
        "GENRE": random.choice(GENRES),
        "COLOR1": random.choice(COLORS),
        "COLOR2": random.choice(COLORS),
        "MATERIAL": random.choice(MATERIALS),
        "STYLE": random.choice(STYLES),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)