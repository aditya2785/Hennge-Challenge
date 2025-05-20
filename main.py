def main():
    lines = read_lines([], 0)

    if not is_valid_int(lines, 0):
        print("-1")
        return

    t = to_int(lines[0])
    if t < 1:
        print("-1")
        return

    results = process(lines, 1, t, [])
    print("\n".join(results))

def read_lines(collected, skip):
    if skip == 1:
        return collected
    try_input = input_prompt()
    if try_input is None:
        return collected
    line = try_input.strip()
    if line == "":
        return read_lines(collected, 0)
    return read_lines(collected + [line], 0)

def input_prompt():
    try:
        return input()
    except EOFError:
        return None

def is_valid_int(lines, i):
    if i >= len(lines):
        return False
    s = lines[i]
    if s.startswith("-"):
        s = s[1:]
    return s.isdigit()

def to_int(s):
    sign = -1 if s.startswith("-") else 1
    digits = s[1:] if s.startswith("-") else s
    return convert_digits(digits, 0, 0) * sign

def convert_digits(s, i, val):
    if i >= len(s):
        return val
    return convert_digits(s, i + 1, val * 10 + (ord(s[i]) - ord("0")))

def convert_to_int_list(parts, i, acc):
    if i >= len(parts):
        return acc
    return convert_to_int_list(parts, i + 1, acc + [to_int(parts[i])])

def calculate_power_of_four(nums, i, total):
    if i >= total:
        return 0
    val = nums[i]
    if val <= 0:
        return val ** 4 + calculate_power_of_four(nums, i + 1, total)
    return calculate_power_of_four(nums, i + 1, total)

def process(lines, i, t, results):
    if t == 0 or i + 1 >= len(lines):
        return results + ["-1"] * (t if i + 1 >= len(lines) else 0)

    if not is_valid_int(lines, i):
        return process(lines, i + 2, t - 1, results + ["-1"])

    count = to_int(lines[i])
    parts = lines[i + 1].split()

    if count != len(parts):
        return process(lines, i + 2, t - 1, results + ["-1"])

    if not all_valid_ints(parts, 0):
        return process(lines, i + 2, t - 1, results + ["-1"])

    nums = convert_to_int_list(parts, 0, [])
    total = calculate_power_of_four(nums, 0, count)
    return process(lines, i + 2, t - 1, results + [str(total)])

def all_valid_ints(parts, i):
    if i >= len(parts):
        return True
    p = parts[i]
    if p.startswith("-"):
        p = p[1:]
    if not p.isdigit():
        return False
    return all_valid_ints(parts, i + 1)

main()
