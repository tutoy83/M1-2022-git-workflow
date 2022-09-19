from typing import List


def dec_to_bin(n: int) -> List[int]:
    bit = [0 if n % 2 == 0 else 1]
    return bit if n <= 1 else dec_to_bin(n // 2) + bit

