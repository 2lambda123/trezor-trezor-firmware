from typing import *
class aes:
        """
        AES context.
        """
        ECB: int
        CBC: int
        CFB: int
        OFB: int
        CTR: int
    def __init__(
        self,
        mode: int,
        key: bytes,
        iv: bytes | None = None,
    ) -> None:
        """
        Initialize AES context.
        """
    def encrypt(self, data: bytes) -> bytes:
        """
        Encrypt data and update AES context.
        """
    def decrypt(self, data: bytes) -> bytes:
        """
        Decrypt data and update AES context.
        """
class blake256:
        """
        Blake256 context.
        """
        block_size: int
        digest_size: int
    def __init__(self, __data: AnyStr | None = None) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
class blake2b:
        """
        Blake2b context.
        """
        block_size: int
        digest_size: int
    def __init__(
        self,
        data: bytes | None = None,
        outlen: int = blake2b.digest_size,
        key: bytes | None = None,
        personal: bytes | None = None,
    ) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
class blake2s:
        """
        Blake2s context.
        """
        block_size: int
        digest_size: int
    def __init__(
        self,
        data: bytes | None = None,
        outlen: int = blake2s.digest_size,
        key: bytes | None = None,
        personal: bytes | None = None,
    ) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
class chacha20poly1305:
        """
        ChaCha20Poly1305 context.
        """
    def __init__(self, key: bytes, nonce: bytes) -> None:
        """
        Initialize the ChaCha20 + Poly1305 context for encryption or decryption
        using a 32 byte key and 12 byte nonce as in the RFC 7539 style.
        """
    def encrypt(self, data: bytes) -> bytes:
        """
        Encrypt data (length of data must be divisible by 64 except for the
        final value).
        """
    def decrypt(self, data: bytes) -> bytes:
        """
        Decrypt data (length of data must be divisible by 64 except for the
        final value).
        """
    def auth(self, data: bytes) -> None:
        """
        Include authenticated data in the Poly1305 MAC using the RFC 7539
        style with 16 byte padding. This must only be called once and prior
        to encryption or decryption.
        """
    def finish(self) -> bytes:
        """
        Compute RFC 7539-style Poly1305 MAC.
        """
class groestl512:
        """
        GROESTL512 context.
        """
        block_size: int
        digest_size: int
    def __init__(self, __data: AnyStr | None = None) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
class hmac:
        """
        HMAC context.
        """
        SHA256: int
        SHA512: int
    def __init__(
        self,
        hashtype: int,
        key: bytes,
        message: bytes | None = None,
    ) -> None:
        """
        Create a HMAC context.
        """
    def update(self, message: bytes) -> None:
        """
        Update a HMAC context.
        """
    def digest(self) -> bytes:
        """
        Return the digest of processed data so far.
        """
class pbkdf2:
        """
        PBKDF2 context.
        """
        HMAC_SHA256: int
        HMAC_SHA512: int
    def __init__(
        self,
        prf: int,
        password: bytes,
        salt: bytes,
        iterations: int | None = None,
        blocknr: int = 1,
    ) -> None:
        """
        Create a PBKDF2 context.
        """
    def update(self, iterations: int) -> None:
        """
        Update a PBKDF2 context.
        """
    def key(self) -> bytes:
        """
        Retrieve derived key.
        """
class ripemd160:
        """
        RIPEMD160 context.
        """
        block_size: int
        digest_size: int
    def __init__(self, __data: AnyStr | None = None) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
class sha1:
        """
        SHA1 context.
        """
        block_size: int
        digest_size: int
    def __init__(self, __data: AnyStr | None = None) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
class sha256:
        """
        SHA256 context.
        """
        block_size: int
        digest_size: int
    def __init__(self, __data: AnyStr | None = None) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
class sha3_256:
        """
        SHA3_256 context.
        """
        block_size: int
        digest_size: int
    def __init__(
        self,
        data: bytes | None = None,
        keccak: bool = False,
    ) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
    def copy(self) -> sha3_256:
        """
        Returns the copy of the digest object with the current state
        """
class sha3_512:
        """
        SHA3_512 context.
        """
        block_size: int
        digest_size: int
    def __init__(
        self,
        data: bytes | None = None,
        keccak: bool = False,
    ) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
    def copy(self) -> sha3_512:
        """
        Returns the copy of the digest object with the current state
        """
class sha512:
        """
        SHA512 context.
        """
        block_size: int
        digest_size: int
    def __init__(self, __data: AnyStr | None = None) -> None:
        """
        Creates a hash context object.
        """
    def update(self, __data: AnyStr) -> None:
        """
        Update the hash context with hashed data.
        """
    def digest(self) -> bytes:
        """
        Returns the digest of hashed data.
        """
