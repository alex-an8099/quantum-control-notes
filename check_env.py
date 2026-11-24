"""Print the versions of the packages used in these notes."""

from importlib import metadata
import sys

PACKAGES = ["numpy", "scipy", "matplotlib", "jupyterlab", "qutip", "qcodes", "pyvisa-sim"]


def main() -> int:
    print(f"Python {sys.version.split()[0]}")
    missing = []
    for name in PACKAGES:
        try:
            print(f"  {name:<12} {metadata.version(name)}")
        except metadata.PackageNotFoundError:
            print(f"  {name:<12} NOT INSTALLED")
            missing.append(name)
    if missing:
        print("\nMissing: " + ", ".join(missing))
        print("Run: pip install -r requirements.txt")
        return 1
    print("\nAll packages are installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
