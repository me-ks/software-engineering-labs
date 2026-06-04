class State:
    START = "START"
    OPEN = "OPEN"
    NC = "NC"
    AFTER_PCT = "AFTER_PCT"
    STAR = "STAR"
    CAP = "CAP"
    ACCEPT = "ACCEPT"
    ERROR = "ERROR"

def get_char_class(ch):
    if ch == "(": return "OPEN_PAREN"
    if ch == "#": return "HASH"
    if ch == "%": return "PERCENT"
    if ch == "*": return "STAR"
    if 'A' <= ch <= 'Z': return "UPPER"
    return "NONCAP"

def next_state(state, ch):
    cls = get_char_class(ch)
    
    if state == State.START:
        return State.OPEN if cls == "OPEN_PAREN" else State.ERROR
    
    elif state == State.OPEN:
        return State.NC if cls == "NONCAP" else State.ERROR
    
    elif state == State.NC:
        if cls == "NONCAP": return State.NC
        if cls == "PERCENT": return State.AFTER_PCT
        if cls == "STAR": return State.STAR
        return State.ERROR
    
    elif state == State.AFTER_PCT:
        return State.ACCEPT if cls == "HASH" else State.ERROR
    
    elif state == State.STAR:
        return State.CAP if cls == "UPPER" else State.ERROR
    
    elif state == State.CAP:
        if cls == "UPPER": return State.CAP
        if cls == "HASH": return State.ACCEPT
        return State.ERROR
    
    return State.ERROR

def analyze(text):
    current = State.START
    trace = []
    for i, ch in enumerate(text):
        prev = current
        current = next_state(current, ch)
        trace.append((i, ch, prev, current))
        if current == State.ERROR: break
    return current == State.ACCEPT, trace

def main():
    print("Рівень 2 — Автомат ([^A-Z]+(%|\\*[A-Z]+)#")
    while True:
        s = input("\nВведіть рядок (або 'exit'): ").strip()
        if s.lower() == 'exit': break
        
        ok, trace = analyze(s)
        print(f"{'Поз':>3} | {'Сим':<3} | {'Стан ДО':<10} | {'Стан ПІСЛЯ'}")
        for pos, ch, fr, to in trace:
            print(f"{pos:3} | {ch:3} | {fr:10} | {to}")
        print(f"Результат: {'✓ ПРИЙНЯТИЙ' if ok else '✗ ВІДХИЛЕНИЙ'}")

if __name__ == "__main__":
    main()