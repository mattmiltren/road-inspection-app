"""
NLEX Defect Inspection Tool - Step 2
Converts coordinates as shown on the DrivePro 250 footage (e.g. "E120 36.1045")
into decimal degrees (e.g. 120.601742), which you can then feed into your
existing km-station converter.
"""

def dmm_to_decimal(coord_str):
    coord_str = coord_str.strip()
    direction = coord_str[0].upper()
    rest = coord_str[1:].strip()
    degree_str, minute_str = rest.split()
    degree = float(degree_str)
    minute = float(minute_str)
    decimal = degree + minute / 60

    if direction in ("S", "W"):
        decimal = -decimal

    return decimal


def main():
    print("=== NLEX Coordinate Converter (Degrees-Minutes to Decimal Degrees) ===")
    print("Type the coordinates exactly as shown on the footage overlay.")
    print("Example Longitude: E120 36.1045")
    print("Example Latitude:  N15 11.0486")
    print("Type 'q' at any time to quit.\n")

    while True:
        e_input = input("Enter Longitude (E...): ")
        if e_input.strip().lower() == "q":
            break

        n_input = input("Enter Latitude  (N...): ")
        if n_input.strip().lower() == "q":
            break

        try:
            longitude = dmm_to_decimal(e_input)
            latitude = dmm_to_decimal(n_input)
            print(f"\n  Longitude (decimal): {longitude:.6f}")
            print(f"  Latitude  (decimal): {latitude:.6f}\n")
        except Exception:
            print("\n  Couldn't read that. Please type it exactly like: E120 36.1045\n")


if __name__ == "__main__":
    main()
