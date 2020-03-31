class Vector:
    """
    Represent a vector in multidimensional space
    """

    def __init__(self, d):
        self._coords = [0]*d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value"""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]+other[j]
        return result

    def __eq__(self, other):
        """
        Return True if vector has same co ordinates as other.
        """
        return self._coords == other._coords
    def __ne__(self,other):
        """
        Return True if vector from other
        """
        return not self == other
    def __str__(self):
        """
        Produce string representation of vector.
        """
        return '<'+str(self._coords)[1:-1]