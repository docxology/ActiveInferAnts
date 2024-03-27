import hashlib
import hmac
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import constant_time
from cryptography.fernet import Fernet

class CryptographyUtils:
    """
    A collection of common cryptographic primitives for serialization, enterprise security, Linux kernel, and network encryption.
    """

    @staticmethod
    def generate_rsa_keys():
        """
        Generates a pair of RSA keys.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def rsa_encrypt(public_key, message):
        """
        Encrypts a message using RSA public key.
        """
        encrypted = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted

    @staticmethod
    def rsa_decrypt(private_key, encrypted_message):
        """
        Decrypts an encrypted message using RSA private key.
        """
        original_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original_message

    @staticmethod
    def generate_fernet_key():
        """
        Generates a Fernet key for symmetric encryption.
        """
        return Fernet.generate_key()

    @staticmethod
    def fernet_encrypt(key, message):
        """
        Encrypts a message using Fernet symmetric encryption.
        """
        f = Fernet(key)
        return f.encrypt(message)

    @staticmethod
    def fernet_decrypt(key, encrypted_message):
        """
        Decrypts an encrypted message using Fernet symmetric encryption.
        """
        f = Fernet(key)
        return f.decrypt(encrypted_message)

    @staticmethod
    def hash_message(message):
        """
        Hashes a message using SHA-256.
        """
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(message)
        return digest.finalize()

    @staticmethod
    def hmac_message(key, message):
        """
        Creates an HMAC of a message using SHA-256.
        """
        h = hmac.new(key, message, hashlib.sha256)
        return h.digest()
