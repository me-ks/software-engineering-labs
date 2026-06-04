from level1 import Student, display_table

def merge(arr, aux, lo, mid, hi):
    for k in range(lo, hi + 1): aux[k] = arr[k]
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid: 
            arr[k] = aux[j]; j += 1
        elif j > hi: 
            arr[k] = aux[i]; i += 1
        elif aux[j].group < aux[i].group: 
            arr[k] = aux[j]; j += 1
        else: 
            arr[k] = aux[i]; i += 1

def merge_sort_bottom_up(arr):
    n = len(arr)
    aux = [None] * n
    size = 1
    while size < n:
        print(f"  [розмір блоку = {size}]")
        for lo in range(0, n - size, size * 2):
            merge(arr, aux, lo, lo + size - 1, min(lo + size * 2 - 1, n - 1))
        state = "  ".join([f"{s.last_name}({s.group})" for s in arr])
        print(f"    {state}\n")
        size *= 2

if __name__ == "__main__":
    students = [
        Student("Іваненко", "Олег", 103, 1050), Student("Петренко", "Марія", 101, 730),
        Student("Сидоренко", "Андрій", 105, 1320), Student("Коваль", "Ірина", 102, 540),
        Student("Бойко", "Василь", 104, 890)
    ]
    display_table(students, "ДО ЗЛИТТЯ")
    merge_sort_bottom_up(students)
    display_table(students, "ПІСЛЯ ЗЛИТТЯ")