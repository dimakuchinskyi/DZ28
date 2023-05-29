class PrimeGenerator:
    def __init__(self):
        self.current = 2
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    def generate(self):
        while True:
            try:
                if self.is_prime(self.current):
                    yield self.current
                self.current += 1
            except KeyboardInterrupt:
                print("Generation interrupted!")
                return
