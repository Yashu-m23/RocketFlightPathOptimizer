### atmosphere.py

def get_air_density(altitude):
    if altitude < 11000:
        return 1.225 * (1 - 0.0000225577 * altitude) ** 4.2561
    elif altitude < 25000:
        return 0.36391 * np.exp(-0.000157688 * (altitude - 11000))
    else:
        return 0.08803 * (altitude / 25000) ** -34.1632
