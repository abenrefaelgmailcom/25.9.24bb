import statistics




temperatures: list[float] = []
SENTINEL: int = -999  # const

while True:
    temp = float(input("Enter Temperature : "))

    if temperatures == SENTINEL:
        break

    if not -50 <= temp <= 50:
        temperatures.append(temp)
        continue

more_temps: list[float] = [18.5 ,39.1 -20.0]
temperatures.extend(more_temps)

print()
print(f"Highest temperature: {max(temperatures)}")
print(f"Lowest temperature: {min(temperatures)}")

print(18.5 in temperatures)

print(temperatures.count(-20.0))

average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp}")

for temp in temperatures:
    print(temp)

print(temperatures.index(39.1))

del temperatures[0]

del temperatures[::2]

if 18.5 in temperatures:
    temperatures.remove(18.5)

last_temp = temperatures.pop()
print(f"Last temperature: {last_temp}")

ordered_temps = temperatures.copy()
ordered_temps.sort()
print(ordered_temps)



reversed_temps = temperatures.copy()
print(reversed_temps)


