import random
from typing import List, Tuple
from dataclasses import dataclass


p = 1091
q = 1103


def gcd(x: int, y: int) -> int:
    while y != 0:
        t = y
        y = x % y
        x = t
    return x

def modular_inverse(a: int, modulus: int) -> int:
    t, new_t = (0, 1)
    (r, new_r) = (modulus, a)

    while new_r != 0:
        q = r // new_r
        (t, new_t) = (new_t, t - q* new_t)
        (r, new_r) = (new_r, r - q* new_r)

    if r > 1:
        raise RuntimeError("a is not invertible")
    if t < 0:
        t += modulus
    return t

def to_ints(message: str) -> List[int]:
    return []

@dataclass
class PublicKey:
    exponent: int
    modulus: int

@dataclass
class PrivateKey:
    d: int
    modulus: int

def create_keypair() -> Tuple[PublicKey, PrivateKey]:
    n = p * q

    d = max(p,q)+1
    while gcd(d, (p-1)*(q-1)) != 1:
        d += 1

    e = modular_inverse(d, n)

    return (PublicKey(exponent=e, modulus=n), PrivateKey(d=d, modulus=n))


def encrypt(message: int, public_key: PublicKey) -> int:
    return pow(message, public_key.exponent, public_key.modulus)

def decrypt(message: int, private_key: PrivateKey) -> int:
    return pow(message, private_key.d, private_key.modulus)


# def modular_inverse(a: int, m: int, phi_m: int) -> int:
#     ## a^-1 = a^phi_m-2 mod m

#     return pow(a, phi_m - 1, m)

class SignedMessage:
    message: str
    signature: str

    def verify_signature(self, public_key: str) -> bool:
        return True

class Signer:
    private_key: int
    public_key: int
    id: str

    def sign_message(self, message: str) -> SignedMessage:
        signed_message = SignedMessage()
        signed_message.message = message
        signed_message.signature = "xxx"
        return signed_message
