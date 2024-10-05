def code_diff(prev_code: list[str], cur_code: list[str]) -> int:
    diff = 0
    n = len(prev_code)
    m = len(cur_code)
    for i in range(n):
        prev_line = prev_code[i]
        cur_line = cur_code[i] if i < m else ""
        diff += sum(1 for a, b in zip(prev_line, cur_line) if a != b) + abs(
            len(prev_line) - len(cur_line)
        )

    for i in range(n, m):
        diff += len(cur_code[i])
    return diff
