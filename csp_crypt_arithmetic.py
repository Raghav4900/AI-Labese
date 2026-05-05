import itertools

def solve_cryptarithmetic(word1, word2, result):
    letters = set(word1 + word2 + result)
    if len(letters) > 10:
        return None

    letters = list(letters)
    first_letters = {word1[0], word2[0], result[0]}

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        if any(mapping[char] == 0 for char in first_letters):
            continue

        num1 = int("".join(str(mapping[c]) for c in word1))
        num2 = int("".join(str(mapping[c]) for c in word2))
        res = int("".join(str(mapping[c]) for c in result))

        if num1 + num2 == res:
            return mapping
    return None

if __name__ == "__main__":
    print(solve_cryptarithmetic("SEND", "MORE", "MONEY"))
