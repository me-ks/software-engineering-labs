from src.level1 import ArrayList
from src.level2 import LinkedStack

def hex_to_decimal(hex_str):
    return int(hex_str, 16)

def main():
    print("Рівень 3: Список -> Стек\n")
    list_obj = ArrayList(10)
    hex_values = ["1A", "2F", "B4", "0D", "FF", "3C", "7E"]
    for val in hex_values: list_obj.insert(val)
    list_obj.print_list()
    
    decimal_values = []
    for i in range(list_obj.size):
        dec = hex_to_decimal(list_obj.get(i))
        decimal_values.append(dec)
    
    stack = LinkedStack()
    for i in range(len(decimal_values)):
        prev = decimal_values[i - 1] if i > 0 else 0
        curr = decimal_values[i]
        nxt = decimal_values[i + 1] if i < len(decimal_values) - 1 else 0
        stack.push(prev + curr + nxt)
    
    stack.print_stack()

if __name__ == "__main__":
    main()