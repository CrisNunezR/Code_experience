class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity must be a positive int')
        self.size = capacity    #initial nunmber of cookies in jar = capacity
        self.capacity = capacity

    def __str__(self):
        return f"{self.size}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Cannot exceed jar's capacity")
        else:
            self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Cannot withdraw more than current cookies in jar")
        else:
            self.size = self.size - n #if jar holds enough cookies, allow withdrawal

    #@property
    #def capacity(self):
    #    return f"{self.capacity}"

    #@property
    #def size(self):
    #    ...


def main():

    #define an instance of Jar
    jar = Jar(12)

    #test jar's capacity
    print(str(jar.capacity))

    #test withdrawal
    jar.withdraw(2)
    print(str(jar))

    #test deposit
    jar.deposit(1)

    #test str function
    print(str(jar))

main()