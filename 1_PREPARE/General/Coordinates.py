from qrays import Vector, Qvector

class VectorAdapter:
    def __init__(self, coords, coord_type='xyz'):
        self.coord_type = coord_type
        if coord_type == 'xyz':
            self.vector = Vector(coords)
            self.qvector = Qvector.from_xyz(*coords)
        elif coord_type == 'ivm':
            self.qvector = Qvector(coords)
            self.vector = Vector.from_ivm(*coords)
        else:
            raise ValueError(f"Invalid coordinate type specified: {coord_type}")

    def to_xyz(self):
        if self.coord_type != 'xyz':
            self.vector = Vector.from_ivm(*self.qvector.coords)
            self.coord_type = 'xyz'
        return self.vector

    def to_ivm(self):
        if self.coord_type != 'ivm':
            self.qvector = Qvector.from_xyz(*self.vector.xyz)
            self.coord_type = 'ivm'
        return self.qvector

    def __repr__(self):
        return f"XYZ: {self.to_xyz()}, IVM: {self.to_ivm()}"

    def __add__(self, other):
        new_vector = self.vector + other.to_xyz()
        return VectorAdapter(new_vector.xyz, 'xyz')

    def __sub__(self, other):
        new_vector = self.vector - other.to_xyz()
        return VectorAdapter(new_vector.xyz, 'xyz')

    def __mul__(self, scalar):
        new_vector = self.vector * scalar
        return VectorAdapter(new_vector.xyz, 'xyz')

    def __truediv__(self, scalar):
        new_vector = self.vector / scalar
        return VectorAdapter(new_vector.xyz, 'xyz')

    def dot(self, other):
        return self.vector.dot(other.to_xyz())

    def cross(self, other):
        new_vector = self.vector.cross(other.to_xyz())
        return VectorAdapter(new_vector.xyz, 'xyz')

    def length(self):
        return self.vector.length()

    def angle_with(self, other):
        return self.vector.angle(other.to_xyz())

    def spherical(self):
        return self.vector.spherical()

    def quadray(self):
        return self.qvector.coords

# Test Cases

if __name__ == "__main__":
    # Example 1: Convert XYZ to IVM
    xyz_coords = (1.0, 2.0, 3.0)
    vec_xyz = VectorAdapter(xyz_coords, 'xyz')
    print(f"XYZ to IVM: {vec_xyz} to {vec_xyz.to_ivm().coords}")

    # Example 2: Convert IVM to XYZ
    ivm_coords = (1, 1, 1, 1)
    vec_ivm = VectorAdapter(ivm_coords, 'ivm')
    print(f"IVM to XYZ: {vec_ivm} to {vec_ivm.to_xyz().xyz}")

    # Example 3: Vector addition in XYZ, result in IVM
    vec1_xyz = VectorAdapter((1.0, 0.0, 0.0), 'xyz')
    vec2_xyz = VectorAdapter((0.0, 1.0, 0.0), 'xyz')
    result_addition = vec1_xyz + vec2_xyz
    print(f"Vector Addition (XYZ to IVM): {result_addition} to {result_addition.to_ivm().coords}")

    # Example 4: Dot product and angle between vectors in different systems
    vec1_ivm = VectorAdapter((1, 0, 0, 0), 'ivm')
    vec2_xyz = VectorAdapter((0.0, 1.0, 0.0), 'xyz')
    dot_product = vec1_ivm.dot(vec2_xyz)
    angle = vec1_ivm.angle_with(vec2_xyz)
    print(f"Dot Product: {dot_product}, Angle: {angle} degrees")