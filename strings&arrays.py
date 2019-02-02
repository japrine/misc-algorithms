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


def is_permutation(s1, s2):
    chars = [0] * 128
    for _ in range(len(s1)):
        chars[s1[_].encode()[0]] += 1
    for _ in range(len(s2)):
        chars[s2[_].encode()[0]] -= 1
        if chars[s2[_].encode()[0]] == -1:
            return False
    return True


def urlify(s):
    while True:
        for idx, _ in enumerate(s):
            if _ == ' ':
                s = s[:idx] + '%20' + s[idx+1:]
                break
            if idx+1 == len(s):
                return s


def palindrome_permutations(s):
    print(b'J'.decode())
    for _ in range(len(s)):
        print(_)


def permutations(s):
    if len(s) == 0:
        return ""
    output = []

    def add_letter(idx):
        new_output = []
        if len(output) == 0:
            new_output.append(s[idx])
            return new_output
        for x in range(len(output)):
            for _ in range(idx + 1):
                string1 = output[x][:_]
                string2 = output[x][_:]
                string3 = s[idx]
                new_output.append(string1 + string3 + string2)
        return new_output

    for _ in range(len(s)):
        output = add_letter(_)
    return len(output), output


def one_away(s1, s2):
    if s1 == s2:
        return True
    if len(s1) > len(s2):
        for _ in range(len(s1)):
            x = s1[:_] + s1[_+1:]
            if x == s2:
                return True
    elif len(s2) > len(s1):
        for _ in range(len(s2)):
            y = s2[:_] + s2[_+1:]
            if y == s1:
                return True
    elif len(s1) == len(s2):
        for _ in range(len(s1)):
            x = s1[:_] + s1[_+1:]
            y = s2[:_] + s2[_+1:]
            if x == y:
                return True
    return False


def string_compression(s):
    rep = 1
    output = ''
    for _ in range(0, len(s) - 1):
        if s[_] == s[_+1]:
            rep += 1
        else:
            output = output + s[_] + str(rep)
            rep = 1
        if _ == len(s) - 2:
            output = output + s[_+1] + str(rep)
    if len(output) >= len(s):
        output = s
    return output


def rotate_matrix(data):
    for y in range(len(data) // 2):
        n = len(data) - 1 - y
        for x in range(y, n):
            z = n-x+y
            data[y][x], data[x][n], data[z][y], data[n][z] = data[x][n], data[n][z], data[y][x], data[z][y]
    return data


def zero_matrix(data):
    output = []
    for y in range(len(data)):
        output.append([])
        for x in range(len(data[0])):
            output[y].append(data[y][x])
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 0:
                for _ in range(len(data[0])):
                    output[y][_] = 0
                for _ in range(len(data)):
                    output[_][x] = 0
    return output


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    for _ in range(len(s2)):
        z = s2[_:] + s2[:_]
        if z == s1:
            return True


print('Is Unique:', is_unique('Jon'))
print('Is Unique (no additional data structure):', is_unique_no_data('Jonath'))
print('Is String a permutation:', check_permutation('Jon', 'Jonathan'))
print('Is String1 a permutation of String2:', is_permutation('Jon', 'noJ'))
print('URLify:', urlify('John Thomas Smith'))
print('Palindromes:', palindrome_permutations('thht'))
print('Permutations:', permutations('John'))
print('One Away:', one_away('Jonx', 'Jons'))
print('String Compression:', string_compression('aabcccccaaa'))
print('Rotate Matrix:', rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print('Zero Matrix:', zero_matrix([[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12]]))
print('String Rotation:', string_rotation('waterbottle', 'erbottlewat'))
