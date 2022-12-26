from os import read



def part1():
    day = 1
    part = 1

    input = readFile(day)
    elves = input.split('\n\n')

    i = 1
    elfCarryingMost = 1
    maxElfCalories = 0
    for elf in elves:
        total = 0
        calories = elf.split('\n')
        for calory in calories:
            total += int(calory)
        if total > maxElfCalories:
            elfCarryingMost = i
            maxElfCalories = total
        i += 1

    print('part ' + str(part) + ': ' + str(elfCarryingMost))
    print(maxElfCalories)

def part2():
    day = 1
    part = 2

    input = readFile(day)
    elves = input.split('\n\n')

    i = 1
    elfCarrying = []
    for elf in elves:
        total = 0
        calories = elf.split('\n')
        for calory in calories:
            total += int(calory)
        elfCarrying.append(total)

        i += 1

    elfCarryingSorted = sorted(elfCarrying, reverse=True)
    elfCarryingMost = elfCarryingSorted[0] + elfCarryingSorted[1] + elfCarryingSorted[2]

    print('part ' + str(part) + ': ' + str(elfCarryingMost))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()


if __name__ == '__main__':
    part1()
    part2()