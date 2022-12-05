from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print(key)

# with open("mykey.key", "wb") as mykey:
#     mykey.write(key)

with open("mykey.key", "rb") as mykey:
    key = mykey.read()

print(key)

f = Fernet(key)

with open("sample.txt", "rb") as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open("sample_encrypted.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print(encrypted)
