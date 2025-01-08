from functools import partial


def load(filename):
    rules = {}
    updates = []
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            if "|" in line:
                a, b = line.strip().split("|")
                a, b = int(a), int(b)
                deps = rules.get(b, set())
                deps.add(a)
                rules[b] = deps
            elif "," in line:
                updates.append([int(x) for x in line.strip().split(",")])
    return rules, updates


def validate(rules, updates):
    for i, update in enumerate(updates):
        possible_rules = rules.get(update)
        for y in range(i + 1, len(updates)):
            if possible_rules and updates[y] in possible_rules:
                return None

    return updates[len(updates) // 2]


def validate_all(rules, updates):
    total = 0
    total_unordered = 0
    for update in updates:
        value = validate(rules, update)
        if value:
            total += value
        else:
            total_unordered += validate_with_reordering(rules, update)
    return total, total_unordered


def validate_with_reordering(rules, updates):
    for i, update in enumerate(updates):
        possible_rules = rules.get(update)
        for y in range(i + 1, len(updates)):
            if possible_rules and updates[y] in possible_rules:
                # if the rules are not respected try to swap values
                # risk of infinite cycles
                updates[i], updates[y] = updates[y], updates[i]
                return validate_with_reordering(rules, updates)

    return updates[len(updates) // 2]



if __name__ == '__main__':
    rules, updates = load("input")
    result, result_unordered = validate_all(rules, updates)
    print(result, result_unordered)
