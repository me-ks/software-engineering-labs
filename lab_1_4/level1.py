class Student:
    def __init__(self, last_name, first_name, group, student_id):
        self.last_name = last_name
        self.first_name = first_name
        self.group = group
        self.student_id = student_id

def display_table(arr, title):
    print(f"\n--- {title} ---")
    print(f"{'#':<3} | {'Прізвище':<11} | {'Ім\'я':<11} | {'Група':<6} | Квиток")
    print("-" * 60)
    for i, s in enumerate(arr, 1):
        print(f"{i:<3} | {s.last_name:<11} | {s.first_name:<11} | {s.group:<6} | {s.student_id}")
    print("-" * 60 + "\n")

def shell_sort_knuth(arr):
    n = len(arr)
    h = 1
    while h < n // 3: h = 3 * h + 1
    
    while h >= 1:
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and arr[j - h].group > temp.group:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        state = "  ".join([f"{s.last_name}({s.group})" for s in arr])
        print(f"  [h={h:<2}] {state}")
        h //= 3

if __name__ == "__main__":
    students = [
        Student("Іваненко", "Олег", 103, 1050), Student("Петренко", "Марія", 101, 730),
        Student("Сидоренко", "Андрій", 105, 1320), Student("Коваль", "Ірина", 102, 540),
        Student("Бойко", "Василь", 104, 890), Student("Мельник", "Оксана", 101, 1600),
        Student("Харченко", "Дмитро", 106, 310), Student("Левченко", "Наталія", 103, 1750),
        Student("Ткаченко", "Роман", 102, 670), Student("Захаренко", "Юлія", 105, 1100)
    ]
    display_table(students, "МАСИВ ДО СОРТУВАННЯ")
    shell_sort_knuth(students)
    display_table(students, "МАСИВ ПІСЛЯ СОРТУВАННЯ")