from sympy import symbols, Matrix
import tkinter as tk


def get_forces():
    known_forces = int(known_forces_entry.get())
    unknown_forces = int(unknown_forces_entry.get())
    return known_forces, unknown_forces


def resolve_known_force():
    position_vector = known_force_vector_entry.get()
    i_component, j_component, k_component = map(
        float, position_vector.split(','))
    components = Matrix([[i_component], [j_component], [k_component]])

    magnitude = float(known_force_magnitude_entry.get())
    unit_vector = components / components.norm()  # Calculate unit vector

    known_force = magnitude * unit_vector  # Calculate known force as vector

    return known_force


def resolve_unknown_force():
    position_vector = unknown_force_vector_entry.get()
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

    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, "Unknown forces:\n")
    for i, unknown_force in enumerate(unknown_forces):
        result_text.insert(tk.END, f"Force {i+1}: {unknown_force}\n")


# Create the UI
root = tk.Tk()
root.title("Equilibrium Solver")

# Labels
known_forces_label = tk.Label(root, text="Number of known forces:")
known_forces_label.grid(row=0, column=0, sticky=tk.W)
unknown_forces_label = tk.Label(root, text="Number of unknown forces:")
unknown_forces_label.grid(row=1, column=0, sticky=tk.W)
known_force_vector_label = tk.Label(
    root, text="Position vector of known force (in i, j, k format):")
known_force_vector_label.grid(row=2, column=0, sticky=tk.W)
known_force_magnitude_label = tk.Label(root, text="Magnitude of known force:")
known_force_magnitude_label.grid(row=3, column=0, sticky=tk.W)
unknown_force_vector_label = tk.Label(
    root, text="Position vector of unknown force (in i, j, k format):")
unknown_force_vector_label.grid(row=4, column=0, sticky=tk.W)

# Entry fields
known_forces_entry = tk.Entry(root)
known_forces_entry.grid(row=0, column=1)
unknown_forces_entry = tk.Entry(root)
unknown_forces_entry.grid(row=1, column=1)
known_force_vector_entry = tk.Entry(root)
known_force_vector_entry.grid(row=2, column=1)
known_force_magnitude_entry = tk.Entry(root)
known_force_magnitude_entry.grid(row=3, column=1)
unknown_force_vector_entry = tk.Entry(root)
unknown_force_vector_entry.grid(row=4, column=1)

# Solve button
solve_button = tk.Button(root, text="Solve", command=solve_equilibrium)
solve_button.grid(row=5, column=0, columnspan=2)

# Result text
result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=6, column=0, columnspan=2)

root.mainloop()
