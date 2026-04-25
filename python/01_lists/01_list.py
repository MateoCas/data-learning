#Con la ayuda de un loop , verifico una condición
# dentro de una lista , cuento y almaceno en dos
# variables de diferente tipo. 

nums = [10, 15, 22, 33, 40, 55, 60]

pairs=0
more_than_30 = []
for num in range(len(nums)):
    if nums[num] % 2 == 0:
        pairs +=1
    if nums[num] > 30:
        more_than_30.append(nums[num])

print("hay", pairs ,"números pares")
print( more_than_30 , "son mayores a 30")

# Construyendo una nueva lista con números pares 
# y multiplicados por 2.

nums_2 = [4, 7, 2, 9, 1, 5, 8, 3, 6]
pairs_for_two = []

for num in nums_2:
    if num % 2 == 0:
        pairs_for_two.append(num*2)
print(pairs_for_two)

# Encontrar el segundo número mas grande 
nums = [2, 3, 6, 6, 5, 4, 6]

if nums[1] > nums[0]:
    num_max = nums[1]
    second_max = nums[0]
else:
    num_max = nums[0]
    second_max = None

for num in range(2, len(nums)):
    if nums[num] > num_max and nums[num] > second_max:
        num_max = nums[num]
    elif nums[num] != num_max and (second_max is None or nums[num] > second_max) :
        num_max = second_max
        second_max = nums[num]
    else:
        continue


 

print(second_max)

# Eliminar repetidos de una lista sin usar metodos python

unique_nums = []
unique_nums.append(nums[0])
j = 0
for i in range(1, len(nums)):
    if nums[i] != unique_nums[j] and nums[i] not in unique_nums :
        unique_nums.append(nums[i])
        j +=1
    else:
        continue

print(unique_nums)
    

