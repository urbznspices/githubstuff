from sympy import symbols, Matrix


def get_forces():
    known_forces = int(input("Enter the number of known forces: "))
    unknown_forces = int(input("Enter the number of unknown forces: "))
    return known_forces, unknown_forces


def resolve_known_force():
    position_vector = input(
        "Enter the position vector of the force (in i, j, k format): ")
    i_component, j_component, k_component = map(
        float, position_vector.split(','))
    components = Matrix([[i_component], [j_component], [k_component]])

    magnitude = float(input("Enter the magnitude of the known force: "))
    unit_vector = components / components.norm()  # Calculate unit vector

    known_force = magnitude * unit_vector  # Calculate known force as vector

    return known_force


def resolve_unknown_force():
    position_vector = input(
        "Enter the position vector of the force (in i, j, k format): ")
    i_component, j_component, k_component = map(
        float, position_vector.split(','))
    components = Matrix([[i_component], [j_component], [k_component]])

    unit_vector = components / components.norm()  # Calculate unit vector

    return unit_vector


def append_unit_vectors(*unit_vectors):
    appended_vectors = Matrix.hstack(*unit_vectors)
    return appended_vectors


def create_augmented_matrix(unknown_vectors, known_force):
    negative_known_force = -known_force
    augmented_matrix = Matrix.hstack(unknown_vectors, negative_known_force)
    return augmented_matrix


def solve_unknown_forces(augmented_matrix):
    rref_matrix = augmented_matrix.rref()[0]
    unknown_forces = rref_matrix[:, -1]
    return unknown_forces


def solve_equilibrium():
    known_forces, unknown_forces = get_forces()

    for _ in range(known_forces):
        known_force = resolve_known_force()

    unknown_vectors = []
    for _ in range(unknown_forces):
        unknown_vector = resolve_unknown_force()
        unknown_vectors.append(unknown_vector)

    augmented_matrix = create_augmented_matrix(
        append_unit_vectors(*unknown_vectors), known_force)

    unknown_forces = solve_unknown_forces(augmented_matrix)

    print("Unknown forces:")
    for i, unknown_force in enumerate(unknown_forces):
        print(f"Force {i+1}: {unknown_force}")


solve_equilibrium()
