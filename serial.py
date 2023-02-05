"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start-1
        self.show = self.start

    def generate(self):
        """
        Increments the self.show count, so that we leave
        the self.start value untouched for future use
        """
        self.show += 1 
        return self.show

    def reset(self):
        """
        Sets self.show to the untouched self.start value
        """
        self.show = self.start