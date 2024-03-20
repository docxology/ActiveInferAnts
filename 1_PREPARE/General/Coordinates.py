import sys
import math
# Add the qrays.py module from Math4Wisdom to the system path for importing
sys.path.append('../../9_OTHER/repos/Synergetics/m4w')
from qrays import Vector, Qvector

class VectorAdapter:
    """
    A class to adapt between XYZ and IVM (quadray) coordinate systems using Vector and Qvector.
    """
    def __init__(self, coords, coord_type='xyz'):
        """
        Initialize the VectorAdapter with coordinates and coordinate type ('xyz' or 'ivm').

        Args:
            coords (tuple): The coordinates to be adapted.
            coord_type (str, optional): The type of coordinates ('xyz' or 'ivm'). Defaults to 'xyz'.
        """
        self.coord_type = coord_type
        if coord_type == 'xyz':
            self.vector = Vector(coords)
            self.qvector = self.vector.quadray()  # Convert XYZ to quadray coordinates
        elif coord_type == 'ivm':
            self.qvector = Qvector(coords)
            self.vector = self.qvector.xyz  # Convert quadray to XYZ coordinates
        else:
            raise ValueError(f"Invalid coordinate type specified: {coord_type}")

    def to_xyz(self):
        """Converts the stored coordinates to XYZ format."""
        if self.coord_type != 'xyz':
            self.vector = self.qvector.xyz  # Convert quadray to XYZ coordinates
            self.coord_type = 'xyz'
        return self.vector

    def to_ivm(self):
        """Converts the stored coordinates to IVM (quadray) format."""
        if self.coord_type != 'ivm':
            self.qvector = self.vector.quadray()  # Convert XYZ to quadray coordinates
            self.coord_type = 'ivm'
        return self.qvector

    def __repr__(self):
        """Representation of the VectorAdapter showing both XYZ and IVM coordinates."""
        if self.coord_type == 'xyz':
            x, y, z = self.vector.xyz
            return f"XYZ Vector(x={x:.2f}, y={y:.2f}, z={z:.2f})"
        else:
            a, b, c, d = self.qvector.coords
            return f"IVM Vector(a={a:.2f}, b={b:.2f}, c={c:.2f}, d={d:.2f})"

    def __add__(self, other):
        """Implements addition of two vectors."""
        new_vector = self.vector + other.to_xyz()
        return VectorAdapter(new_vector.xyz, 'xyz')

    def __sub__(self, other):
        """Implements subtraction of two vectors."""
        new_vector = self.vector - other.to_xyz()
        return VectorAdapter(new_vector.xyz, 'xyz')

    def __mul__(self, scalar):
        """Implements scalar multiplication of a vector."""
        new_vector = self.vector * scalar
        return VectorAdapter(new_vector.xyz, 'xyz')

    def __truediv__(self, scalar):
        """Implements scalar division of a vector."""
        new_vector = self.vector / scalar
        return VectorAdapter(new_vector.xyz, 'xyz')

    def dot(self, other):
        """Calculates the dot product with another vector."""
        return self.vector.dot(other.to_xyz())

    def cross(self, other):
        """Calculates the cross product with another vector."""
        new_vector = self.vector.cross(other.to_xyz())
        return VectorAdapter(new_vector.xyz, 'xyz')

    def length(self):
        """Returns the length of the vector."""
        return self.vector.length()

    def angle_with(self, other):
        """Calculates the angle with another vector."""
        return self.vector.angle(other.to_xyz())

    def spherical(self):
        """Returns the spherical coordinates of the vector."""
        return self.vector.spherical()

    def quadray(self):
        """Returns the quadray (IVM) coordinates of the vector."""
        return self.qvector.coords

    def __format__(self, format_spec):
        """Custom format specification for printing."""
        if self.coord_type == 'xyz':
            return f"{self.vector.__str__():{format_spec}}"
        else:
            return f"{self.qvector.__str__():{format_spec}}"

if __name__ == "__main__":
    headers = ["Operation", "Initial Vector", "Converted Vector"]
    test_vectors = [
        {"description": "XYZ to IVM", "vector": VectorAdapter((1.0, 2.0, 3.0), 'xyz'), "conversion_method": "to_ivm"},
        {"description": "IVM to XYZ", "vector": VectorAdapter((1, 1, 1, 1), 'ivm'), "conversion_method": "to_xyz"},
        {"description": "Vector Addition (XYZ) and Convert to IVM", "vector": VectorAdapter((1.0, 0.0, 0.0), 'xyz') + VectorAdapter((0.0, 1.0, 0.0), 'xyz'), "conversion_method": "to_ivm"},
    ]

    # Formatting table header
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "+" + "-" * (len(header_line) - 2) + "+"
    print(header_line)
    print(separator_line)

    # Processing and displaying each test vector
    for test_vector in test_vectors:
        initial_vector = test_vector["vector"]
        conversion_method = test_vector["conversion_method"]
        converted_vector = getattr(initial_vector, conversion_method)()
        print(f"| {test_vector['description']:30} | {initial_vector:20} | {converted_vector} |")

    # Calculating and displaying dot product and angle
    vec_ivm = VectorAdapter((1, 1, 1, 1), 'ivm')
    vec2_xyz = VectorAdapter((0.0, 1.0, 0.0), 'xyz')
    dot_product = vec_ivm.dot(vec2_xyz)
    angle = vec_ivm.angle_with(vec2_xyz)
    angle_display = f"{angle:.2f} degrees" if not math.isnan(angle) else "NaN"
    print(f"| {'Dot Product and Angle':30} | {'vec_ivm & vec2_xyz':20} | {dot_product}, {angle_display} |")
