from collections import Counter

def minimum_keypad(text):
    counter = Counter(text)

    sorted_values = sorted(counter.items(), key=lambda x: -x[1])
    print(sorted_values)

    min_score = 0
    buttons = 9
    for i in range(len(sorted_values)):
        value = sorted_values[i][1]
        score = value * ((i//buttons)+1)
        min_score += score

    return min_score

print(minimum_keypad("hellothereabcdefghikjleimzpoqeetzxuyiewalllllll"))
