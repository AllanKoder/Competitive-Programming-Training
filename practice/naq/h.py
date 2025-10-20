import heapq

class Person:
    def __init__(self, left, right, position, weight, people):
        self.value = weight/people

        self.left = left
        self.right = right
        self.position = position
        self.weight = weight
        self.people = people
        self.active = True

n = int(input())

heap = []
last_person = None
id_to_person = {}
current_balance = 0
for _ in range(n):
    position, weight = map(int, input().split())

    new_person = Person(None, None, position, weight, 1)
    if last_person:
        last_person.right = new_person
    new_person.left = last_person
    
    last_person = new_person

    current_balance += position * weight

    id_to_person[id(new_person)] = new_person
    heapq.heappush(heap, (-new_person.value, id(new_person)))

def print_person(p):
    print("-"*50)
    print(p.value)
    print(p.position)
    print(p.left)
    print(p.right)
    print("-"*50)

def delete_person():
    pass

amount_moved = 0
epsilon = 1e-6 
while abs(current_balance) >= epsilon:
    _, person_id = heapq.heappop(heap)
    person = id_to_person[person_id]

    if person.active == False:
        # do deletion on them, or not, idk, we can memory leak, it's chill. 
        continue

    direction_right = True if current_balance < 0 else False 
    neighbor = person.right if direction_right else person.left

    movement_direction = -(current_balance / person.weight)
    new_pos = movement_direction + person.position

    print(person.position, current_balance, amount_moved)
    if direction_right:
        if not neighbor or new_pos <= neighbor.position:
            amount_moved += abs(movement_direction * person.people)
            current_balance = 0
            break
        else:
            movement_amount = abs(neighbor.position - person.position)
            current_balance += movement_amount * person.weight
            amount_moved += movement_amount * person.people

            neighbor.active = False
            person.active = False

            new_person = Person(person.left, neighbor.right, neighbor.position, neighbor.weight + person.weight, neighbor.people + person.people)
            person.right = new_person
            neighbor.left = new_person

            id_to_person[id(new_person)] = new_person
            heapq.heappush(heap, (-new_person.value, id(new_person)))
    if not direction_right:
        if not neighbor or new_pos >= neighbor.position:
            amount_moved += abs(movement_direction * person.people)
            current_balance = 0
            break
        else:
            movement_amount = abs(neighbor.position - person.position)
            current_balance -= movement_amount * person.weight
            amount_moved += movement_amount * person.people

            neighbor.active = False
            person.active = False

            new_person = Person(neighbor.left, person.right, person.position, neighbor.weight + person.weight, neighbor.people + person.people)
            neighbor.right = new_person
            person.left = new_person

            id_to_person[id(new_person)] = new_person
            heapq.heappush(heap, (-new_person.value, id(new_person)))
    
print(amount_moved)
    




