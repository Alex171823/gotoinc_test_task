from math import floor
from typing import Optional


def encrypt(text: str, n: int) -> Optional[str]:
    # check input
    if text in ('', None) or n <= 0:
        return text

    # encrypt
    for _ in range(n):
        first_part = text[1::2]
        second_part = text[::2]
        text = ''.join(first_part + second_part)

    return text


def decrypt(encrypted_text: str, n: int) -> Optional[str]:
    # check input
    if encrypted_text in ('', None) or n <= 0:
        return encrypted_text

    # decrypt
    for _ in range(n):
        separating_index = floor(len(encrypted_text) / 2)
        first_part = encrypted_text[:separating_index]
        second_part = encrypted_text[separating_index:]

        parts_to_join = []
        for fp, sp in zip(first_part, second_part):
            parts_to_join.append(sp)
            parts_to_join.append(fp)

        # add last symbol of second part if len of the word is odd
        if len(second_part) == len(first_part) + 1:
            parts_to_join.append(second_part[-1])

        encrypted_text = ''.join(parts_to_join)

    return encrypted_text
