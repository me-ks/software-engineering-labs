import re
import os

# Стан
S, O, NC, AP, ST, CP, ACC, ERR = 0, 1, 2, 3, 4, 5, 6, 7
STATE_NAMES = ["START", "OPEN", "NC", "AFTER_PCT", "STAR", "CAP", "ACCEPT", "ERROR"]

# Класи символів: ( , [^A-Z], %, *, [A-Z], #, інше
def get_cls(ch):
    if ch == "(": return 0
    if ch == "%": return 2
    if ch == "*": return 3
    if 'A' <= ch <= 'Z': return 4
    if ch == "#": return 5
    if ch.isprintable(): return 1
    return 6

# Таблиця переходів
#             (   nc   %   * AZ   #  other
TRANSITION = [
    [O,   ERR, ERR, ERR, ERR, ERR, ERR], # START
    [ERR, NC,  ERR, ERR, ERR, ERR, ERR], # OPEN
    [ERR, NC,  AP,  ST,  ERR, ERR, ERR], # NC
    [ERR, ERR, ERR, ERR, ERR, ACC, ERR], # AFTER_PCT
    [ERR, ERR, ERR, ERR, CP,  ERR, ERR], # STAR
    [ERR, ERR, ERR, ERR, CP,  ACC, ERR], # CAP
    [ERR, ERR, ERR, ERR, ERR, ERR, ERR], # ACCEPT
    [ERR, ERR, ERR, ERR, ERR, ERR, ERR]  # ERROR
]

def recognize(word):
    state = S
    for i, ch in enumerate(word):
        cls = get_cls(ch)
        state = TRANSITION[state][cls]
        if state == ERR:
            return False, STATE_NAMES[ERR], i, ch
    return state == ACC, STATE_NAMES[state], -1, None

def main():
    file_path = input("Введіть шлях до файлу (або Enter для data.txt): ").strip() or "data.txt"
    if not os.path.exists(file_path):
        print("Файл не знайдено.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Розбивка за * або %% як у твому JS
    raw_words = re.split(r'\*|%%', content)
    words = [w.strip() for w in raw_words if w.strip()]

    print(f"\nАналіз файлу: {file_path}")
    print(f"{'№':>3} | {'Слово':<20} | {'Стан':<10} | {'Результат'}")
    print("-" * 60)

    for i, w in enumerate(words, 1):
        ok, last_state, err_pos, err_ch = recognize(w)
        res = "✓ ПРИЙНЯТИЙ" if ok else f"✗ ВІДХИЛЕНИЙ (поз.{err_pos})"
        print(f"{i:3} | {w:20} | {last_state:10} | {res}")

if __name__ == "__main__":
    main()