def second_law(force, mass, acc):
    output_force = 0
    output_mass = 0
    output_acc = 0
    if force == "x":
        output_force = mass * acc
        return output_force
    elif mass == "x":
        output_mass = force / acc
        return output_mass
    elif acc == "x":
        output_acc = force / mass
        return output_acc
