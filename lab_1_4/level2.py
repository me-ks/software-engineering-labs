from level1 import Student, display_table

def compare(a, b):
    if a.group != b.group: return a.group - b.group
    return a.student_id - b.student_id

def shell_sort_standard(arr):
    n = len(arr)
    h = n // 2
    while h >= 1:
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and compare(arr[j - h], temp) > 0:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        state = "  ".join([f"{s.last_name}({s.group}/{s.student_id})" for s in arr])
        print(f"  [h={h:<2}] {state}")
        h //= 2

if __name__ == "__main__":
    students = [
        Student("Іваненко", "Олег", 103, 1050), Student("Петренко", "Марія", 101, 730),
        Student("Сидоренко", "Андрій", 105, 1320), Student("Коваль", "Ірина", 102, 540),
        Student("Бойко", "Василь", 104, 890), Student("Мельник", "Оксана", 101, 1600)
    ]
    display_table(students, "ДО СОРТУВАННЯ")
    shell_sort_standard(students)
    display_table(students, "ПІСЛЯ СОРТУВАННЯ (Група + Квиток)")