import re
import os

# Шаблон: {цифри (один або більше) -- або + цифри (один або більше) % (необов'язково)}
PATTERN = r'^\{[0-9]+(--|\+)[0-9]+%?$'

def analyze_word(word):
    if not re.match(PATTERN, word):
        return "не відповідає"
    
    has_percent = word.endswith("%")
    clean = word.strip("{}").replace("%", "")
    sep = "--" if "--" in clean else "+"
    left, right = clean.split(sep)
    
    res = f'{{ + "{left}" + "{sep}" + "{right}"'
    if has_percent:
        res += ' + "%" (кінцевий символ)'
    return res

def main():
    file_path = input("Введіть шлях до файлу (або Enter для words.txt): ").strip() or "words.txt"
    
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не знайдено.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    matched = []
    print(f"\n{'Рядок':>5} | {'Слово':<20} | {'Результат'}")
    print("-" * 50)

    for i, word in enumerate(lines, 1):
        is_ok = re.match(PATTERN, word)
        status = "✓ ВІДПОВІДАЄ" if is_ok else "✗ НЕ відповідає"
        print(f"{i:6} | {word:20} | {status}")
        if is_ok:
            matched.append((i, word))

    if matched:
        print("\n--- Розбір знайдених слів ---")
        for line_num, word in matched:
            print(f"рядок {line_num}: {word:20} -> {analyze_word(word)}")

if __name__ == "__main__":
    main()