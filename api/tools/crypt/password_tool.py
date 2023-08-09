import bcrypt

class PasswordCrypter:
    salt_gen = bcrypt.gensalt(rounds=6)

    @classmethod
    def encrypt(cls, pw: str) -> str:
        byte_pw = pw.encode()
        byte_res = bcrypt.hashpw(password= byte_pw, salt = cls.salt_gen)
        return byte_res.decode()

    @classmethod
    def verify(cls, pw: str, hash: str) -> bool:
        byte_pw = pw.encode()
        byte_hash = hash.encode()
        return bcrypt.checkpw(byte_pw,byte_hash)