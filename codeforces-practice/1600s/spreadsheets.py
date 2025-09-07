t = int(input())

def solve_rc_to_excel(string: str) -> str:
    c = string.find("C")
    
    row = string[1:c]
    col = int(string[c+1:])

    def helper(value):
        if value == 0:
            return []
        value -= 1
        output = helper(value // 26)
        c = chr((value % 26) + ord('A'))
        output.append(c)
        return output
    
    str_col = "".join(helper(col))
    return str_col + row
    

def solve_excel_to_rc(string: str) -> str:
    row = None
    for i in range(len(string)):
        if string[i].isdigit():
            row = string[i:]
            break

    col = string[:i]
    digit_col = 0
    base = 1
    for c in reversed(col):
        digit_col += (ord(c) - ord('A') + 1) * base
        base *= 26

    return "R" + row + "C" + str(digit_col)

def is_rc(string: str) -> bool:
    switches = 0
    is_number = False
    for c in string:
        if is_number != c.isalpha():
            is_number = c.isalpha()
            switches += 1
    return switches == 4


for _ in range(t):
    st = input()
    if is_rc(st):
        print(solve_rc_to_excel(st))
    else:
        print(solve_excel_to_rc(st))