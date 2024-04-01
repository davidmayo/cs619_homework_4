from pprint import pprint


numbers: list[float] = [3, -2, 1, 4, 7, 1]

size = len(numbers)

table: list[list[list[float] | None]] = []

for x in range(size):
    table.append([])
    for y in range(size):
        table[-1].append(None)

def longest(seq: list[float], i: int, j: int) -> list[float]:
    # If memoized result available, use it
    if table[i][j] is not None:
        return table[i][j]

    # Base case: For length 1, longest sequence is 
    if i == j:
        table[i][j] = [seq[i]]
    else:
        # Get the left and right parents
        left: list[float] = longest(seq, i, j - 1)[:]
        right: list[float] = longest(seq, i + 1, j)[:]

        # Determine if either (or both) can grow
        if seq[j] > left[-1]:
            left.append(seq[j])
        if seq[i] < right[0]:
            right.insert(0, seq[i])

        if len(left) > len(right):
            table[i][j] = left
        else:
            table[i][j] = right

    return table[i][j]


for diff in range(20):
    for x in range(size):
        y = x + diff
        if y > size - 1:
            continue
        longest(seq=numbers, i=x, j=y)

print(f"Table:")
pprint(table)

print()
longest_sequence = longest(numbers, 0, size - 1)
print(f"Longest sequence: {longest_sequence}")
print(f"Longest sequence length: {len(longest_sequence)}")
