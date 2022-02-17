from typing import AnyStr
from tkinter import N
import random as rnd


def convert_character_to_number(character: int) -> int:
    # TODO Test
    return ord(character)


def convert_number_to_character(number: int) -> int:
    # TODO Test
    return chr(number)


def generate_prime_number(lower_bound: int = 100000, upper_bound: int = 1000000) -> int:
    while (True):
        n = rnd.randint(lower_bound, upper_bound)
        tested = set()
        while len(tested) < 9:
            a = rnd.randint(2, n - 2)

            if a in tested:
                continue
            if not is_potentially_prime(a, n):
                break

            tested.add(a)
        return n


def generate_public_key(p: int, q: int) -> tuple:
    return 0


def generate_private_key(e: int, phi_N: int) -> tuple:
    return 0


def encrypt_message(public_key: tuple, message_to_encrypt: AnyStr) -> list[int]:
    # TODO Code review
    # TODO Need to add private key?
    return [
        pow(
            convert_character_to_number(num), public_key[0]) % public_key[1]
        for num in message_to_encrypt
    ]


def decrypt_message(private_key: tuple, message_to_decrypt: list[int]) -> AnyStr:
    return [  # TODO Code review. dont think this logic is right
        pow(
            convert_number_to_character(num), private_key[0]) % private_key[1]
        for num in message_to_decrypt
    ]


def generate_digital_signature(msg, private_key) -> tuple:
    # TODO type message, but will it be a string or list of numbers
    return 0


def authenticate_signature(msg: AnyStr, public_key: tuple, private_key: tuple) -> bool:
    return False


def get_count_coprime_number_count(prime_1: int, prime_2: int) -> int:
    return (prime_1 - 1) * (prime_2 - 1)


def is_potentially_prime(a: int, n: int) -> bool:
    return pow(a, n-1, n) == 1


def is_coprime(number_to_check_if_coprime: int, N: int) -> bool:
    return True
