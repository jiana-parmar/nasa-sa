import os
import sqlite3


def _query_best_match(rocky_score, temperature_min_c, pressure_min_kpa, dbfile):
    DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), dbfile)

    with sqlite3.connect(DB_FILE) as connection:
        connection.row_factory = sqlite3.Row

        query = """
            SELECT *
            FROM analog_places
            WHERE rocky_score >= ?
            AND temperature_min_c <= ?
            AND pressure_min_kpa <= ?
            ORDER BY
                ABS(temperature_min_c - ?) +
                ABS(pressure_min_kpa - ?) +
                ABS(rocky_score - ?)
            LIMIT 1
        """

        return connection.execute(
            query,
            (
                rocky_score,
                temperature_min_c,
                pressure_min_kpa,
                temperature_min_c,
                pressure_min_kpa,
                rocky_score,
            ),
        ).fetchone()


def prompt_user_input():
    planet = input("Choose, Moon or Mars: ").strip().lower()
    if planet not in ["moon", "mars"]:
        raise ValueError("Choose between Moon or Mars only.")
    
    terrain = input("Terrain [very rocky/rocky]: ").strip().lower()
    if terrain == "very rocky":
        rocky_score = 5
    elif terrain == "rocky": 
        rocky_score = 4 #Cinder Lake Arizona - Moon #McMurdo - Mars
    else:
        raise ValueError("Choose terrain between rocky/very rocky only.")
    
    temperature = input("Temperature [very very cold/very cold/cold/normal]: ").strip().lower()
    if temperature == "very very cold":
        temperature_min_c = -66.0 #McMurdo - Mars
    elif temperature == "very cold":
        temperature_min_c = -20.0 #Cinder Lake Arizona - Moon
    elif temperature == "cold":
        temperature_min_c = -10.0
    elif temperature == "normal":
        temperature_min_c = -6.0
    else:
        raise ValueError("Choose temperature between very very cold/very cold/cold/normal only.")
    
    pressure = input("Pressure [very low/low/normal/high/very high]: ").strip().lower()
    if pressure == "very low":
        pressure_min_kpa = 55 
    elif pressure == "low":
        pressure_min_kpa = 60
    elif pressure == "normal":
        pressure_min_kpa = 65 #McMurdo - Mars
    elif pressure == "high":
        pressure_min_kpa = 75 #Cinder Lake Arizona - Moon
    elif pressure == "very high":
        pressure_min_kpa = 80
    else:
        raise ValueError("Choose pressure between very low/low/normal/high/very high only.")

    if planet == "moon":
        return moon(rocky_score, temperature_min_c, pressure_min_kpa, planet)
    if planet == "mars":
        return mars(rocky_score, temperature_min_c, pressure_min_kpa, planet)
    
    
def moon(rocky_score, temperature_min_c, pressure_min_kpa, planet):
    result = _query_best_match(rocky_score, temperature_min_c, pressure_min_kpa, dbfile="lunar_earth_analogs.db")
    if result is None:
        return None
    return dict(result), planet


def mars(rocky_score, temperature_min_c, pressure_min_kpa, planet):
    result = _query_best_match(rocky_score, temperature_min_c, pressure_min_kpa, dbfile="mars_earth_analogs.db")
    if result is None:
        return None
    return dict(result), planet

def main():
    try:
        result, planet = prompt_user_input()
        if result is None:
            print("\nNo matching Earth area was found.")
            return

        print("\nRecommended Earth analog: \n")
        print(f"Area: {result['name']}")
        print(f"Region: {result['country_region']}")
        print(f"Coordinates: {result['latitude']}, {result['longitude']}")
        if result['rocky_score'] == 5:
            print(f"Terrain: very rocky; {result['terrain']}")
        elif result['rocky_score'] == 4:
            print(f"Terrain: rocky; {result['terrain']}")
        print(f"Temperature: {result['temperature']}")
        print(f"Atmosphere: {result['atmospheric_conditions']}")
        if planet == "moon":
            print(f"Reason: {result['lunar_match']}")
        elif planet == "mars":
            print(f"Reason: {result['mars_match']}")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()