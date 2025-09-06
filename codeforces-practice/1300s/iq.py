input()
nums = [int(i) for i in input().split()]

parities = [n % 2 for n in nums[:3]]
majority_parity = 0 if parities.count(0) > 1 else 1  # 0 = even, 1 = odd

looking_for_even = majority_parity % 2 == 1
for i in range(len(nums)):
    if nums[i] % 2 == 0 and looking_for_even:
        print(i+1)
        break
    if nums[i] % 2 == 1 and not looking_for_even:
        if nums[i] % 2 == 1:
            print(i+1)
            break
