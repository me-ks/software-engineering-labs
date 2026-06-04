import math

class Student:
    def __init__(self, last_name, first_name, group, gender, record_book_id):
        self.last_name = last_name
        self.first_name = first_name
        self.group = group
        self.gender = gender
        self.record_book_id = record_book_id

    def gender_code(self):
        return 0 if self.gender == 'М' else 1

def display_table(arr, title):
    print(f"\n--- {title} ---")
    print(f"{'#':<3} | {'Прізвище':<11} | {'Ім\'я':<11} | {'Група':<6} | {'Стать':<5} | № залікової")
    print("-" * 65)
    for i, s in enumerate(arr, 1):
        print(f"{i:<3} | {s.last_name:<11} | {s.first_name:<11} | {s.group:<6} | {s.gender:<5} | {s.record_book_id}")
    print("-" * 65 + "\n")

def interpolation_search(arr, target_id):
    males = [s for s in arr if s.gender == 'М']
    if not males: return None

    lo, hi = 0, len(males) - 1
    steps = 0

    while lo <= hi and target_id >= males[lo].record_book_id and target_id <= males[hi].record_book_id:
        steps += 1
        if males[lo].record_book_id == males[hi].record_book_id:
            return males[lo] if males[lo].record_book_id == target_id else None

        pos = lo + int(((target_id - males[lo].record_book_id) * (hi - lo)) / 
                       (males[hi].record_book_id - males[lo].record_book_id))

        print(f"  [крок {steps}] lo={lo}, hi={hi}, pos={pos}, перевіряємо №{males[pos].record_book_id}")

        if males[pos].record_book_id == target_id:
            return males[pos]
        elif males[pos].record_book_id < target_id:
            lo = pos + 1
        else:
            hi = pos - 1
    return None

if __name__ == "__main__":
    raw_students = [
        Student("Іваненко", "Олег", 103, "М", 1001), Student("Петренко", "Марія", 101, "Ж", 1002),
        Student("Сидоренко", "Андрій", 105, "М", 1003), Student("Коваль", "Ірина", 102, "Ж", 1004),
        Student("Ткаченко", "Роман", 102, "М", 1015)
    ]
    
    students = sorted(raw_students, key=lambda x: (x.gender_code(), x.record_book_id))
    display_table(students, "Впорядкований масив")
    
    res = interpolation_search(students, 1003)
    print(f"\nРезультат: {res.last_name if res else 'Не знайдено'}")