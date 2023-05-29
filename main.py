import random
class PasswordGenerator:
    def __init__(self, length, characters):
        self.length = length
        self.characters = characters
    def generate_password(self):
        password = ""
        for _ in range(self.length):
            password += random.choice(self.characters)
        return password
length = 8
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
generator = PasswordGenerator(length, characters)
password1 = generator.generate_password()
print(password1)Z
password2 = generator.generate_password()
print(password2)
