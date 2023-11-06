"""
Suppose that you’d like to implement a cookie jar in which to store cookies.
In a file called jar.py, implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity,
which represents the maximum number of cookies that can fit in the cookie jar.
 If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

__str__ should return a str with n  🍪, where n is the number of cookies in the cookie jar.
For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

deposit should add n cookies to the cookie jar. If adding that many would exceed the
 cookie jar’s capacity, though, deposit should instead raise a ValueError.

withdraw should remove n cookies from the cookie jar. Nom nom nom.
If there aren’t that many cookies in the cookie jar, though, withdraw
should instead raise a ValueError.

capacity should return the cookie jar’s capacity.

size should return the number of cookies actually in the cookie jar.

Structure your class per the below. You may not alter these methods’ parameters,
but you may add your own methods.

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

"""
def main():
    jar1 = Jar()
    print(jar1)

    jar1.deposit(6)
    print(jar1)

    jar1.withdraw(5)
    print(jar1)

    jar1.deposit(4)
    print(jar1)

    print(jar1.capacity)

    print(jar1.size)




class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity must be a positive integer')
        self._capacity = capacity
        self.cookies_now = 0


    def __str__(self):
        #return f"{self.cookies_now}"
        return self.cookies_now * '🍪'

    def deposit(self, n):
        if self.capacity < n + self.cookies_now:
            raise ValueError("Not enough capacity")
        else:
            self.cookies_now += n

    def withdraw(self, n):
        if n > self.cookies_now:
            raise ValueError("Not enough cookies to withdraw")
        else:
            self.cookies_now -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity > self._capacity:
            raise ValueError("Cookies can't exceed {self._capacity}")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self.cookies_now

if __name__ == "__main__":
    main()