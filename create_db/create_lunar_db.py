import sqlite3
from pathlib import Path


DB_FILE = Path(__file__).with_name("lunar_earth_analogs.db")


PLACES = [
    {
        "name": "Cinder Lake Crater Field",
        "country_region": "Arizona, USA",
        "latitude": 35.26,
        "longitude": -111.60,
        "temperature_min_c": -20,
        "temperature_max_c": 35,
        "pressure_min_kpa": 75,
        "pressure_max_kpa": 85,
        "rocky_score": 4,
        "cold_score": 2,
        "low_pressure_score": 1,
        "terrain_keywords": "rocky basaltic cinder crater volcanic regolith",
        "temperature": "-20 to +35 C; strong diurnal range",
        "temperature_measurement": "Thermal infrared; field thermometers; DEM models",
        "terrain": "Basaltic cinder plain; artificial crater field",
        "elevation_slope_topography": "Approx. 2,100 m; crater rims; shallow depressions",
        "geological_composition": "Basaltic cinders; scoria; volcanic glass; pyroxene; olivine; plagioclase",
        "rock_minerals_spectral": "Dark mafic surface; iron-bearing minerals; basalt VNIR",
        "surface_features": "Engineered impact craters; ejecta-like rims; cinder regolith",
        "water_ice": "No permanent ice; episodic snow",
        "atmospheric_conditions": "Earth atmosphere; 75-85 kPa; N2-O2; dry air",
        "lunar_match": "Mare basalt; cratered regolith; astronaut training"
    },
    {
        "name": "Meteor Crater",
        "country_region": "Arizona, USA",
        "latitude": 35.03,
        "longitude": -111.02,
        "temperature_min_c": -20,
        "temperature_max_c": 40,
        "pressure_min_kpa": 80,
        "pressure_max_kpa": 85,
        "rocky_score": 5,
        "cold_score": 2,
        "low_pressure_score": 1,
        "terrain_keywords": "rocky impact crater ejecta steep rim breccia",
        "temperature": "-20 to +40 C; dry climate",
        "temperature_measurement": "Weather stations; thermal infrared",
        "terrain": "Bowl-shaped impact crater; steep rim; ejecta blanket",
        "elevation_slope_topography": "Approx. 1,740 m; 1.2 km diameter; 170 m depth",
        "geological_composition": "Shocked sandstone; limestone; breccia; iron meteorite fragments",
        "rock_minerals_spectral": "Quartz; calcite; impact melt; shock features",
        "surface_features": "Preserved crater; raised rim; ejecta; overturned strata",
        "water_ice": "No permanent ice; limited groundwater",
        "atmospheric_conditions": "Earth atmosphere; approx. 80 kPa; N2-O2",
        "lunar_match": "Impact morphology; ejecta stratigraphy"
    },
    {
        "name": "Mauna Kea Summit",
        "country_region": "Hawaii, USA",
        "latitude": 19.82,
        "longitude": -155.47,
        "temperature_min_c": -10,
        "temperature_max_c": 20,
        "pressure_min_kpa": 60,
        "pressure_max_kpa": 65,
        "rocky_score": 4,
        "cold_score": 4,
        "low_pressure_score": 4,
        "terrain_keywords": "rocky basalt volcanic cinder cone lava rough",
        "temperature": "-10 to +20 C; strong radiative cooling",
        "temperature_measurement": "Weather stations; infrared thermometry; satellite thermal",
        "terrain": "High-altitude volcanic summit; cinder cones; lava plains",
        "elevation_slope_topography": "4,205 m; shield slopes; summit cones",
        "geological_composition": "Basalt; hawaiite; scoria; ash; olivine; pyroxene; plagioclase",
        "rock_minerals_spectral": "Mafic volcanic spectra; Fe-bearing silicates",
        "surface_features": "Cinder cones; lava flows; volcanic pits",
        "water_ice": "Seasonal snow; no permanent surface ice",
        "atmospheric_conditions": "Earth atmosphere; approx. 60 kPa; low humidity; high UV",
        "lunar_match": "Highland volcanic terrain; cinder cones"
    },
    {
        "name": "McMurdo Dry Valleys",
        "country_region": "Victoria Land, Antarctica",
        "latitude": -77.50,
        "longitude": 162.00,
        "temperature_min_c": -66,
        "temperature_max_c": 12,
        "pressure_min_kpa": 65,
        "pressure_max_kpa": 100,
        "rocky_score": 5,
        "cold_score": 5,
        "low_pressure_score": 2,
        "terrain_keywords": "rocky exposed bedrock gravel dry valley glacial",
        "temperature": "-66 to +12 C; cold-desert conditions",
        "temperature_measurement": "Weather stations; thermal infrared; ground sensors",
        "terrain": "Hyper-arid polar valleys; exposed bedrock; gravel plains",
        "elevation_slope_topography": "Sea level to >2,000 m; steep walls; valley floors",
        "geological_composition": "Granite; gneiss; volcanic rocks; glacial till; evaporite salts",
        "rock_minerals_spectral": "Quartz; feldspar; mica; iron oxides; salt crusts",
        "surface_features": "Dry valleys; glacial channels; moraines; patterned ground",
        "water_ice": "Buried ice; glaciers; frozen lakes; brines",
        "atmospheric_conditions": "Earth atmosphere; 65-100 kPa; cold dry air; katabatic winds",
        "lunar_match": "Cold aridity; exposed regolith; ice-related processes"
    },
    {
        "name": "Atacama Desert",
        "country_region": "Northern Chile",
        "latitude": -23.00,
        "longitude": -69.00,
        "temperature_min_c": -6,
        "temperature_max_c": 40,
        "pressure_min_kpa": 55,
        "pressure_max_kpa": 95,
        "rocky_score": 4,
        "cold_score": 3,
        "low_pressure_score": 3,
        "terrain_keywords": "rocky hyper-arid gravel volcanic salt flat dry channel",
        "temperature": "-6 to +40 C; intense solar heating",
        "temperature_measurement": "Weather stations; radiometers; satellite thermal",
        "terrain": "Hyper-arid desert; gravel plains; volcanic plateaus; salt flats",
        "elevation_slope_topography": "Approx. 500-4,500 m; basins; Andean slopes",
        "geological_composition": "Basalt; andesite; ignimbrite; gypsum; halite; sulfates; clays",
        "rock_minerals_spectral": "Iron oxides; sulfates; chlorides; smectite; evaporites",
        "surface_features": "Dry channels; alluvial fans; volcanic cones; salt polygons",
        "water_ice": "No permanent lowland ice; subsurface moisture",
        "atmospheric_conditions": "Earth atmosphere; 55-95 kPa; very low humidity",
        "lunar_match": "Extreme dryness; salts; dry-channel morphology"
    }
]


MOON_REFERENCE = {
    "temperature": "-173 to +127 C; extreme diurnal variation; vacuum heating",
    "terrain": "Impact-cratered highlands; basaltic maria; mountains; plains; rilles",
    "geological_composition": "Anorthosite; basalt; breccia; impact melt; regolith",
    "surface_features": "Impact craters; maria; ejecta; wrinkle ridges; rilles; lava tubes",
    "water_ice": "Polar ice; hydration; hydroxyl; impact-delivered volatiles",
    "atmospheric_conditions": "Exosphere; ultra-low pressure; He; Ar; Ne; Na; K"
}


def create_database():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.executescript("""
            DROP TABLE IF EXISTS analog_places;
            DROP TABLE IF EXISTS moon_reference;

            CREATE TABLE analog_places (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country_region TEXT NOT NULL,
                latitude REAL,
                longitude REAL,

                temperature_min_c REAL,
                temperature_max_c REAL,
                pressure_min_kpa REAL,
                pressure_max_kpa REAL,

                rocky_score INTEGER,
                cold_score INTEGER,
                low_pressure_score INTEGER,

                terrain_keywords TEXT,
                temperature TEXT,
                temperature_measurement TEXT,
                terrain TEXT,
                elevation_slope_topography TEXT,
                geological_composition TEXT,
                rock_minerals_spectral TEXT,
                surface_features TEXT,
                water_ice TEXT,
                atmospheric_conditions TEXT,
                lunar_match TEXT
            );

            CREATE TABLE moon_reference (
                characteristic TEXT PRIMARY KEY,
                description TEXT NOT NULL
            );
        """)

        place_columns = [
            "name",
            "country_region",
            "latitude",
            "longitude",
            "temperature_min_c",
            "temperature_max_c",
            "pressure_min_kpa",
            "pressure_max_kpa",
            "rocky_score",
            "cold_score",
            "low_pressure_score",
            "terrain_keywords",
            "temperature",
            "temperature_measurement",
            "terrain",
            "elevation_slope_topography",
            "geological_composition",
            "rock_minerals_spectral",
            "surface_features",
            "water_ice",
            "atmospheric_conditions",
            "lunar_match"
        ]

        placeholders = ", ".join(["?"] * len(place_columns))
        columns = ", ".join(place_columns)

        values = [
            tuple(place[column] for column in place_columns)
            for place in PLACES
        ]

        cursor.executemany(
            f"""
            INSERT INTO analog_places ({columns})
            VALUES ({placeholders})
            """,
            values
        )

        cursor.executemany(
            """
            INSERT INTO moon_reference
            (characteristic, description)
            VALUES (?, ?)
            """,
            MOON_REFERENCE.items()
        )

        connection.commit()

    print(f"Database created successfully:\n{DB_FILE}")

if __name__ == "__main__":
    create_database()