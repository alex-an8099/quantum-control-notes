"""Check the hand calculations in 01-linear-algebra.md with NumPy.

Run after doing the exercises by hand:
    python 01-foundations/linear_algebra_check.py
"""

import numpy as np

np.set_printoptions(precision=3, suppress=True)

# Basis states and common matrices
ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
CNOT = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]],
    dtype=complex,
)


def dagger(m: np.ndarray) -> np.ndarray:
    """Conjugate transpose."""
    return m.conj().T


def is_unitary(m: np.ndarray) -> bool:
    return np.allclose(dagger(m) @ m, np.eye(m.shape[0]))


def is_hermitian(m: np.ndarray) -> bool:
    return np.allclose(m, dagger(m))


def show(title: str, value) -> None:
    print(f"\n[{title}]")
    print(value)


def exercise_1() -> None:
    """Inner product and normalization of a complex vector."""
    psi = np.array([1, 1j], dtype=complex)
    norm = np.sqrt(np.vdot(psi, psi).real)  # vdot conjugates the first argument
    psi_n = psi / norm
    show("1a <psi|psi> for psi = (1, i)", np.vdot(psi, psi))
    show("1b normalized psi", psi_n)
    show("1c probabilities |<0|psi>|^2, |<1|psi>|^2",
         np.array([abs(np.vdot(ket0, psi_n)) ** 2, abs(np.vdot(ket1, psi_n)) ** 2]))


def exercise_2() -> None:
    """Unitary and Hermitian checks."""
    for name, m in [("X", X), ("Y", Y), ("Z", Z), ("H", H)]:
        print(f"  {name}: unitary={is_unitary(m)}, hermitian={is_hermitian(m)}")
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    print(f"  S: unitary={is_unitary(S)}, hermitian={is_hermitian(S)}")
    show("2b H|0>", H @ ket0)
    show("2c H H", H @ H)


def exercise_3() -> None:
    """Eigenvalues and eigenvectors of X."""
    vals, vecs = np.linalg.eigh(X)
    show("3a eigenvalues of X", vals)
    show("3b eigenvectors of X (columns)", vecs)


def exercise_4() -> None:
    """Tensor products and CNOT."""
    ket01 = np.kron(ket0, ket1)
    show("4a |0> (x) |1>", ket01)
    show("4b X (x) I", np.kron(X, I).real)
    plus = H @ ket0
    bell = CNOT @ np.kron(plus, ket0)
    show("4c CNOT (H|0> (x) |0>)", bell)
    # A product state reshaped to 2x2 has rank 1; an entangled state has rank 2.
    print(f"  rank of 4c as 2x2 matrix = {np.linalg.matrix_rank(bell.reshape(2, 2))}")


def main() -> None:
    print("Exercise 1"); exercise_1()
    print("\nExercise 2"); exercise_2()
    print("\nExercise 3"); exercise_3()
    print("\nExercise 4"); exercise_4()


if __name__ == "__main__":
    main()
