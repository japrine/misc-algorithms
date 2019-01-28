def is_unique(s):
    chars = []
    for _ in s:
        if _ not in chars:
            chars.append(_)
        else:
            return False
    return True


def is_unique_no_data(s):
    for idx, _ in enumerate(s):
        if _ in s[idx+1:] or _ in s[:idx]:
            return False
    return True


def check_permutation(s1, s2):
    if s1 in s2 or s2 in s1:
        return True
    return False


def urlify(s):
    # s = s.replace(' ', '%20')
    while True:
        for idx, _ in enumerate(s):
            if _ == ' ':
                s = s[:idx] + '%20' + s[idx+1:]
                break
            if idx+1 == len(s):
                return s


def palindrome_permutations(s):
    if len(s) == 0:
        return ""
    output = []

    def add_letter(idx):
        output.append([])
        if len(output) == 1:
            output[idx].append(s[idx])
            return
        for x in range(len(output[idx-1])):
            for _ in range(idx + 1):
                string1 = output[idx-1][x][:_]
                string2 = output[idx-1][x][_:]
                string3 = s[idx]
                output[idx].append(string1 + string3 + string2)
        return

    for _ in range(len(s)):
        add_letter(_)
    print(len(output[len(output)-1]))
    return output[len(output)-1]


# print('Is Unique:', is_unique('Jon'))
# print('Is Unique (no additional data structure):', is_unique_no_data('Jonath'))
# print('Is String a permutation:', check_permutation('Jon', 'Jonathan'))
# print(urlify('John Thomas Smith'))
print('Palindromes :', palindrome_permutations('Adam'))
