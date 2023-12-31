nums = [20, 30, 79, 45, 12, 35, 28, 42, 15, 50]

# 1. Cəmi ən böyük olan iki massiv elementinin indexini göstərən funksiya yazın


def find_biggest_sum_couple():
    biggest_sum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] > biggest_sum:
                biggest_sum = nums[i] + nums[j]
                biggest_sum_couple = (i, j)
    return biggest_sum_couple


big_res = find_biggest_sum_couple()
print("Cəmi ən böyük olan iki massiv elementinin indexi: ", big_res)


# 2. Ən böyük ədədi tapan funksiya yazın


def max_num():
    max = nums[0]
    for num in nums:
        if (num > max):
            max = num
    return max


result = max_num()
print(f"Ən böyük ədəd: {result}")

# 3. Massivdəki ən böyük ədədlə ən kiçik ədəd arasındakı fərqi tapın


def find_min_value():
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value


def find_max_value():
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value


min_valu = find_min_value()
max_valu = find_max_value()
ferq = max_valu - min_valu
print("Massivdəki ən böyük ədədlə ən kiçik ədəd arasındakı fərq: ", ferq)


# def find_min_value(nums):
#     min_value = nums[0]
#     for num in nums:
#         if num < min_value:
#             min_value = num
#     return min_value


# def find_max_value(nums):
#     max_value = nums[0]
#     for num in nums:
#         if num > max_value:
#             max_value = num
#     return max_value
# min_val = find_min_value(nums)
# max_val = find_max_value(nums)

# ferq = max_val - min_val
# print("Ferq:", ferq)


# 4. Massivdəki tək ədədləri ayrı, cüt ədədləri ayrı massiv formasında göstərən funksiya yazın

def tek_or_cut():
    tekler = []
    cutler = []
    for num in nums:
        if num % 2 == 1:
            tekler.append(num)
        else:
            cutler.append(num)
    return tekler, cutler


tekler_cutler = tek_or_cut()
print("tək ədədlər: ", tekler_cutler[0])
print("cüt ədədlər:", tekler_cutler[1])

# 5. Massiv daxilində 20-dən böyük olan ədədləri silib yerdə qalan elementləri göstərən funksiya yazın

# def el_sil():
#     for num in nums:
#         if num<20:
#             nums.remove(num)

# netice = el_sil()
# print(netice)


def elem_sil():
    new_arr = []
    for num in nums:
        if num > 20:
            new_arr.append(num)
    return new_arr


res = elem_sil()
print("Massiv daxilində 20-dən böyük olan ədədlər: ", res)
