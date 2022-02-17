import pytest
from backend import *

def test_convert_character_to_number():
    try:
        test = convert_character_to_number('A')
        if (test != 65):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")
test_convert_character_to_number()

def test_convert_number_to_character():
    try:
        test = convert_number_to_character(65)
        if (test != 'A'):
            raise Exception
        pass
    except Exception:
        pytest.fail("Uncexpected Exception ..")
test_convert_number_to_character()

def test_generate_prime_number():
    # TODO Depends on is potentially prime passing
    # for i in range(4):
    try:
        prime = generate_prime_number(80, 130)
        for i in range(2, int(prime / 2)):
            if prime % i == 0:
                print(f'generated prime is {prime}')
                raise Exception
    except Exception:
        pytest.fail("Unexpected Exception ..")
test_generate_prime_number()

def test_generate_n():
    try:
        test = generate_n(2, 7)
        if (test[0] != 14):
            raise Exception
        if (test[1] != 6):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")
test_generate_n()

# def test_generate_public_key():
#       pass

# def test_generate_private_key(e, phi_N):
#     return 0

# def test_encrypt_message(public_key, message_to_encrypt):
#     pass

# def test_decrypt_message(private_key, message_to_decrypt):
#     pass

# def test_generate_digital_signature(msg, private_key):
#     pass

# def test_authenticate_signature(msg, public_key, private_key):
#     pass

def test_get_count_coprime_number_count():
    try:
        test = get_count_coprime_number_count(2, 7)
        if (test != 6):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")
test_get_count_coprime_number_count()

def test_is_potentially_prime():
    try:
        if (not is_potentially_prime(3, 7)):
            raise Exception
        if (is_potentially_prime(5, 8)):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")
test_is_potentially_prime()

# def test_is_coprime(number_to_check_if_coprime, N):
#     pass

# def test_is_coprime():
#     pass

# def test_gcd():
#     pass

# def test_extended_gcd():
#     pass

# def test_test_failing():
#     assert Example().value < 4