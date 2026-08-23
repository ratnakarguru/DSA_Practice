num = input("Enter all number")
nums = list(map(int,num.split()))
freq = {}

for i in range(len(nums)):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1

for key, val in freq.items():
    print(f"{key} : {val}")