import statistics



numbers = []


while True:
    number = int(input("Enter a number between 0 and 10 : "))

    if number == -999:
        break

    if number < 0 or number > 10:
        continue

numbers.append(number)

print(f"statistics.mean(numbers) = {statistics.mean(numbers) : .2f}")
for i in range(11):
    count = numbers.count(i)
    if count > 0:
        print(f"[ {i} ]: {count}", end=" ")
print()