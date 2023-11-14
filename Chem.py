def ideal_gas_law():
    # Define the variables
    r = 0.0821  # Ideal gas constant

    # Ask the user which variable they want to solve for
    unknown = input(
        "Which variable do you want to solve for? (p, v, n, t, d, Mu, or m): ")

    # Solve for the unknown variable
    if unknown == "p":
        t = float(input("Enter the temperature in Kelvin: "))
        v = float(input("Enter the volume in liters: "))
        n = float(input("Enter the number of moles: "))
        p = (n * r * t) / v
        print("The pressure is", p, "atm.")
    elif unknown == "v":
        t = float(input("Enter the temperature in Kelvin: "))
        p = float(input("Enter the pressure in atm: "))
        n = float(input("Enter the number of moles: "))
        v = (n * r * t) / p
        print("The volume is", v, "liters.")
    elif unknown == "n":
        t = float(input("Enter the temperature in Kelvin: "))
        p = float(input("Enter the pressure in atm: "))
        v = float(input("Enter the volume in liters: "))
        n = (p * v) / (r * t)
        print("The number of moles is", n)
    elif unknown == "t":
        p = float(input("Enter the pressure in atm: "))
        v = float(input("Enter the volume in liters: "))
        n = float(input("Enter the number of moles: "))
        t = (p * v) / (n * r)
        print("The temperature is", t, "Kelvin.")
    elif unknown == "d":
        p = float(input("Enter the pressure in atm: "))
        t = float(input("Enter the temperature in Kelvin: "))
        m = float(input("Enter the molar mass in g/mol: "))
        d = (p * m) / (r * t)
        print("The gas density is", d, "g/L.")
    elif unknown == "Mu":
        p = float(input("Enter the pressure in atm: "))
        t = float(input("Enter the temperature in Kelvin: "))
        m = float(input("Enter the mass of gas in grams: "))
        v = float(input("Enter the volume in liters: "))
        Mu = (m * r * t) / (p * v)
        print("The molar mass is", Mu, "g/mol.")
    elif unknown == "m":
        v = float(input("Enter the volume in liters: "))
        Mu = float(input("Enter the molar mass in g/mol: "))
        t = float(input("Enter the temperature in Kelvin: "))
        p = float(input("Enter the pressure in atm: "))
        m = v * p * Mu / (r * t)
        print("The mass of gas is", Mu, "grams.")
    else:
        print("Invalid input. Please enter p, v, n, t, d, M, or m.")


def pressure_converter():
    # Define the variables
    atm_to_pascal = 101325
    mmHg_to_pascal = 133.322
    torr_to_pascal = 133.322

    # Ask the user which unit the pressure is given in
    from_unit = input(
        "Enter the unit of the pressure you want to convert (atm, mmHg, torr, or pascal): ")
    while from_unit not in ["atm", "mmHg", "torr", "pascal"]:
        from_unit = input(
            "Invalid input. Please enter atm, mmHg, torr, or pascal: ")

    # Ask the user which unit the pressure needs to be converted to
    to_unit = input(
        "Enter the unit of the pressure you want to convert to (atm, mmHg, torr, or pascal): ")
    while to_unit not in ["atm", "mmHg", "torr", "pascal"]:
        to_unit = input(
            "Invalid input. Please enter atm, mmHg, torr, or pascal: ")

    # Ask the user for the pressure value
    pressure = float(input("Enter the pressure value: "))

    # Convert the pressure to pascal
    if from_unit == "atm":
        pressure_pascal = pressure * atm_to_pascal
    elif from_unit == "mmHg":
        pressure_pascal = pressure * mmHg_to_pascal
    elif from_unit == "torr":
        pressure_pascal = pressure * torr_to_pascal
    else:
        pressure_pascal = pressure

    # Convert the pressure from pascal to the desired unit
    if to_unit == "atm":
        pressure_final = pressure_pascal / atm_to_pascal
    elif to_unit == "mmHg":
        pressure_final = pressure_pascal / mmHg_to_pascal
    elif to_unit == "torr":
        pressure_final = pressure_pascal / torr_to_pascal
    else:
        pressure_final = pressure_pascal

    # Print the final pressure value
    print("The pressure is", pressure_final, to_unit + ".")


def molecular_geometry():
    # Define the variables
    atoms = {"H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10, "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20, "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30, "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40, "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50, "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58,
             "Pr": 59, "Nd": 60, "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70, "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80, "Tl": 81, "Pb": 82, "Bi": 83, "Th": 90, "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100, "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109, "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118}
    valence_electrons = {"H": 1, "He": 2, "Li": 1, "Be": 2, "B": 3, "C": 4, "N": 5, "O": 6, "F": 7, "Ne": 8, "Na": 1, "Mg": 2, "Al": 3, "Si": 4, "P": 5, "S": 6, "Cl": 7, "Ar": 8, "K": 1, "Ca": 2, "Sc": 3, "Ti": 4, "V": 5, "Cr": 6, "Mn": 7, "Fe": 8, "Co": 9, "Ni": 10, "Cu": 11, "Zn": 12, "Ga": 3, "Ge": 4, "As": 5, "Se": 6, "Br": 7, "Kr": 8, "Rb": 1, "Sr": 2, "Y": 3, "Zr": 4, "Nb": 5, "Mo": 6, "Tc": 7, "Ru": 8, "Rh": 9, "Pd": 10, "Ag": 11, "Cd": 12, "In": 3, "Sn": 4, "Sb": 5, "Te": 6, "I": 7, "Xe": 8, "Cs": 1, "Ba": 2,
                         "La": 3, "Ce": 4, "Pr": 5, "Nd": 6, "Pm": 7, "Sm": 8, "Eu": 9, "Gd": 10, "Tb": 11, "Dy": 12, "Ho": 13, "Er": 14, "Tm": 15, "Yb": 16, "Lu": 17, "Hf": 4, "Ta": 5, "W": 6, "Re": 7, "Os": 8, "Ir": 9, "Pt": 10, "Au": 11, "Hg": 12, "Tl": 3, "Pb": 4, "Bi": 5, "Th": 4, "Pa": 5, "U": 6, "Np": 5, "Pu": 6, "Am": 7, "Cm": 6, "Bk": 7, "Cf": 6, "Es": 7, "Fm": 8, "Md": 9, "No": 10, "Lr": 3, "Rf": 4, "Db": 5, "Sg": 6, "Bh": 7, "Hs": 8, "Mt": 9, "Ds": 10, "Rg": 11, "Cn": 12, "Nh": 5, "Fl": 6, "Mc": 7, "Lv": 8, "Ts": 9, "Og": 10}
    electron_pairs = {"1": "linear", "2": "linear", "3": "trigonal planar",
                      "4": "tetrahedral", "5": "trigonal bipyramidal", "6": "octahedral"}

    # Ask the user for the chemical formula
    formula = input("Enter the chemical formula: ")

    # Calculate the number of valence electrons
    valence_electrons_total = 0
    for atom in atoms:
        count = formula.count(atom)
        valence_electrons_total += count * valence_electrons[atom]

    # Calculate the number of electron pairs
    electron_pairs_total = valence_electrons_total // 2

    # Calculate the number of lone electron pairs
    lone_electron_pairs = electron_pairs_total - len(formula)

    # Determine the molecular geometry and electron-pair geometry
    if lone_electron_pairs == 0:
        electron_pairs_str = str(electron_pairs_total)
        molecular_geometry = electron_pairs[electron_pairs_str]
        electron_pair_geometry = electron_pairs[electron_pairs_str]
    elif lone_electron_pairs == 1:
        electron_pairs_str = str(electron_pairs_total)
        if electron_pairs_total == 3:
            molecular_geometry = "trigonal pyramidal"
            electron_pair_geometry = "tetrahedral"
        else:
            molecular_geometry = "bent"
            electron_pair_geometry = "tetrahedral"
    elif lone_electron_pairs == 2:
        electron_pairs_str = str(electron_pairs_total)
        if electron_pairs_total == 4:
            molecular_geometry = "bent"
            electron_pair_geometry = "tetrahedral"
        elif electron_pairs_total == 5:
            molecular_geometry = "linear"
            electron_pair_geometry = "trigonal bipyramidal"
        else:
            molecular_geometry = "unknown"
            electron_pair_geometry = "unknown"
    elif lone_electron_pairs == 3:
        electron_pairs_str = str(electron_pairs_total)
        if electron_pairs_total == 5:
            molecular_geometry = "trigonal pyramidal"
            electron_pair_geometry = "trigonal bipyramidal"
        elif electron_pairs_total == 6:
            molecular_geometry = "linear"
            electron_pair_geometry = "octahedral"
        else:
            molecular_geometry = "unknown"
            electron_pair_geometry = "unknown"
    elif lone_electron_pairs == 4:
        electron_pairs_str = str(electron_pairs_total)
        if electron_pairs_total == 6:
            molecular_geometry = "bent"
            electron_pair_geometry = "octahedral"
        else:
            molecular_geometry = "unknown"
            electron_pair_geometry = "unknown"
    else:
        molecular_geometry = "unknown"
        electron_pair_geometry = "unknown"

    # Print the molecular geometry and electron-pair geometry
    print("The electron-pair geometry is", electron_pair_geometry)
    print("The molecular geometry is", molecular_geometry)


while True:
    # Ask the user which function they want to perform
    choice = input(
        "Enter 1 to use the ideal gas law function, 2 to convert from mmHg to atm, 3 to calculate molecular geometry, or 0 to exit: ")

    if choice == "1":
        ideal_gas_law()
    elif choice == "2":
        pressure_converter()
    elif choice == "3":
        molecular_geometry()
    elif choice == "0":
        break
    else:
        print("Invalid input. Please enter 1, 2, 3, or 0.")
