import os
import base64
import zlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CryptoHelpers:
    @staticmethod
    def _get_fernet_instance(password: str, salt: bytes) -> Fernet:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
        return Fernet(key)

    @staticmethod
    def secure_encrypt(data: bytes, password: str) -> bytes:
        # 1. Compress
        compressed_data = zlib.compress(data)
        
        # 2. Encrypt
        salt = os.urandom(16)
        f = CryptoHelpers._get_fernet_instance(password, salt)
        encrypted_data = f.encrypt(compressed_data)
        
        # Combine salt and ciphertext so they travel together
        return salt + encrypted_data

    @staticmethod
    def secure_decrypt(data: bytes, password: str) -> bytes:
        """Separate the salt, decrypt the data, and decompress it back to original bytes."""
        if len(data) < 16:
            raise ValueError("Data is too short to contain a valid encryption salt.")
            
        salt = data[:16]
        encrypted_data = data[16:]
        
        try:
            f = CryptoHelpers._get_fernet_instance(password, salt)
            compressed_data = f.decrypt(encrypted_data)
        except Exception as e:
            raise ValueError("Decryption failed. Incorrect password or corrupted data.") from e
        
        try:
            return zlib.decompress(compressed_data)
        except Exception as e:
            raise ValueError("Decompression failed. Data may be corrupted.") from e
