import heapq

n = int(input())
potions = list(map(int, input().split()))


def solve(potions):
    n = len(potions)
    current_health = 0  
    taken_potions = 0

    largest_bad_potions = []
    for i in range(n):
        if potions[i] > 0:
            current_health += potions[i]
            taken_potions += 1
        else:
            heapq.heappush(largest_bad_potions, potions[i])
            current_health += potions[i]
            taken_potions += 1
            while current_health < 0:
                largest_bad_potion = heapq.heappop(largest_bad_potions)
                current_health -= largest_bad_potion
                taken_potions -= 1
    
    return taken_potions


print(solve(potions))