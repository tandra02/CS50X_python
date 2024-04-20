class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > self.capacity or self._size + n > self.capacity:
            raise ValueError('Too many cookies, exceeds capacity')
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError('No cookies left to remove from jar.')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

if __name__=="__main__":
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    print(jar)

