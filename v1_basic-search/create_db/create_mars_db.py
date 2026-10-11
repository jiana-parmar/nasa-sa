import sqlite3
from pathlib import Path


DB_FILE = Path(__file__).with_name("mars_earth_analogs.db")


PLACES = [
    {
        "name": "Atacama Desert",
        "country_region": "Northern Chile",
        "latitude": -23.00,
        "longitude": -69.00,
        "temperature_min_c": -20,
        "temperature_max_c": 40,
        "pressure_min_kpa": 55,
        "pressure_max_kpa": 95,
        "rocky_score": 5,
        "cold_score": 3,
        "dryness_score": 5,
        "low_pressure_score": 3,
        "terrain_keywords": "rocky hyper-arid gravel volcanic salt flat dry channel",
        "temperature": "-20 to +40 C; high diurnal range; intense solar heating",
        "temperature_measurement": "Automatic weather stations; radiometers; satellite thermal products",
        "terrain": "Hyper-arid desert; gravel plains; volcanic plateaus; salt flats",
        "elevation_slope_topography": "Approx. 500-4,500 m; broad basins; steep Andean slopes",
        "geological_composition": "Basalt; andesite; ignimbrite; gypsum; halite; sulfates; clays",
        "rock_minerals_spectral": "Iron oxides; sulfates; chlorides; smectite; evaporite spectra",
        "surface_features": "Dry channels; alluvial fans; volcanic cones; yardangs; salt polygons",
        "water_ice": "No permanent lowland ice; shallow subsurface moisture; high-altitude snow",
        "atmospheric_conditions": "Earth atmosphere; 55-95 kPa by elevation; very low humidity; high UV; dust",
        "mars_match": "Hyper-aridity; oxidized minerals; salt deposits; dry channels; Mars soil analog"
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
        "dryness_score": 5,
        "low_pressure_score": 2,
        "terrain_keywords": "rocky cold hyper-arid dry valley exposed bedrock gravel glacier",
        "temperature": "-66 to +12 C; extreme cold; strong seasonal variation",
        "temperature_measurement": "Automatic weather stations; thermal infrared; ground sensors",
        "terrain": "Hyper-arid polar valleys; exposed bedrock; gravel plains; glaciers",
        "elevation_slope_topography": "Sea level to >2,000 m; steep mountain walls; valley floors",
        "geological_composition": "Granite; gneiss; volcanic rocks; glacial till; evaporite salts",
        "rock_minerals_spectral": "Quartz; feldspar; mica; iron oxides; salt crusts",
        "surface_features": "Dry valleys; glacial channels; moraines; patterned ground; permafrost",
        "water_ice": "Buried ice; glaciers; frozen lakes; brines; permafrost",
        "atmospheric_conditions": "Earth atmosphere; 65-100 kPa; cold dry air; katabatic winds",
        "mars_match": "Cold desert; permafrost; exposed bedrock; ice-related surface processes"
    },
    {
        "name": "Rio Tinto Mining District",
        "country_region": "Andalusia, Spain",
        "latitude": 37.69,
        "longitude": -6.56,
        "temperature_min_c": 0,
        "temperature_max_c": 40,
        "pressure_min_kpa": 95,
        "pressure_max_kpa": 102,
        "rocky_score": 5,
        "cold_score": 2,
        "dryness_score": 4,
        "low_pressure_score": 1,
        "terrain_keywords": "rocky acidic iron oxide sulfur mineral river channel mine",
        "temperature": "Approx. 0 to +40 C; seasonal Mediterranean range",
        "temperature_measurement": "Meteorological stations; field thermometry; thermal imagery",
        "terrain": "Rugged mining landscape; exposed rock; acidic drainage channels",
        "elevation_slope_topography": "Approx. 200-500 m; dissected hills; mine pits; channel slopes",
        "geological_composition": "Pyrite; hematite; goethite; jarosite; iron sulfates; acidic sediments",
        "rock_minerals_spectral": "Strong ferric iron; sulfate minerals; red-orange spectral signatures",
        "surface_features": "Open pits; waste piles; acidic streams; eroded channels; terraces",
        "water_ice": "Liquid acidic water; no ice; seasonal moisture",
        "atmospheric_conditions": "Earth atmosphere; approx. 100 kPa; humid to dry seasonal air",
        "mars_match": "Iron oxidation; sulfate minerals; acidic aqueous alteration; Mars geochemistry"
    },
    {
        "name": "Haughton Crater",
        "country_region": "Devon Island, Canada",
        "latitude": 75.37,
        "longitude": -89.68,
        "temperature_min_c": -40,
        "temperature_max_c": 10,
        "pressure_min_kpa": 85,
        "pressure_max_kpa": 102,
        "rocky_score": 5,
        "cold_score": 5,
        "dryness_score": 4,
        "low_pressure_score": 2,
        "terrain_keywords": "rocky cold impact crater breccia permafrost arctic dry",
        "temperature": "-40 to +10 C; polar desert; long winter",
        "temperature_measurement": "Automatic weather stations; permafrost sensors; thermal imagery",
        "terrain": "Impact crater; polar desert; exposed bedrock; permafrost terrain",
        "elevation_slope_topography": "Approx. 300 m; 23 km crater; central peak; rim slopes",
        "geological_composition": "Impact breccia; shocked carbonate rocks; melt rocks; clay minerals",
        "rock_minerals_spectral": "Carbonates; clays; impact-altered minerals; weathered rock spectra",
        "surface_features": "Impact crater; central uplift; ejecta; gullies; channels; patterned ground",
        "water_ice": "Permafrost; subsurface ice; seasonal snow; ice-cemented ground",
        "atmospheric_conditions": "Earth atmosphere; 85-102 kPa; cold polar air; seasonal winds",
        "mars_match": "Impact crater; permafrost; cold desert; ice-cemented regolith"
    },
    {
        "name": "Icelandic Volcanic Highlands",
        "country_region": "Iceland",
        "latitude": 64.90,
        "longitude": -18.80,
        "temperature_min_c": -25,
        "temperature_max_c": 15,
        "pressure_min_kpa": 75,
        "pressure_max_kpa": 102,
        "rocky_score": 5,
        "cold_score": 4,
        "dryness_score": 3,
        "low_pressure_score": 2,
        "terrain_keywords": "rocky basalt volcanic lava ash crater glacier channel",
        "temperature": "-25 to +15 C; cold subarctic; strong seasonal variation",
        "temperature_measurement": "Weather stations; ground sensors; satellite thermal products",
        "terrain": "Basaltic lava fields; volcanic deserts; ash plains; glaciers",
        "elevation_slope_topography": "Approx. 500-2,000 m; lava plateaus; volcanic cones; steep valleys",
        "geological_composition": "Basalt; tephra; volcanic ash; olivine; pyroxene; plagioclase",
        "rock_minerals_spectral": "Mafic mineral spectra; basalt; volcanic glass; iron-bearing silicates",
        "surface_features": "Craters; lava flows; fissures; ash plains; meltwater channels",
        "water_ice": "Glaciers; seasonal snow; subglacial water; permafrost locally",
        "atmospheric_conditions": "Earth atmosphere; 75-102 kPa; cold; windy; humid to dry",
        "mars_match": "Basaltic lava; volcanic landforms; cold terrain; channels; ice interactions"
    }
]


MARS_REFERENCE = {
    "temperature": "Average approx. -59 C; extremes approx. -153 to +20 C",
    "temperature_measurement": "Orbiter thermal instruments; rover meteorological stations",
    "terrain": "Rocky deserts; impact craters; volcanoes; canyons; dunes; plains",
    "elevation_slope_topography": "Global relief; Olympus Mons; Valles Marineris; cratered highlands",
    "geological_composition": "Basalt; iron oxides; sulfates; clays; carbonates; dust; regolith",
    "rock_minerals_spectral": "Ferric oxides; pyroxene; olivine; sulfates; phyllosilicates; CRISM spectra",
    "surface_features": "Impact craters; volcanoes; dunes; channels; deltas; gullies; yardangs",
    "water_ice": "Polar ice; subsurface ice; hydrated minerals; ancient lakebeds; brines",
    "atmospheric_conditions": "Approx. 0.6 kPa; CO2 approx. 95%; N2 approx. 2.6%; Ar approx. 1.9%",
    "environment": "Cold; dry; dusty; thin atmosphere; high radiation; frequent dust activity"
}


def create_database():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.executescript("""
            DROP TABLE IF EXISTS analog_places;
            DROP TABLE IF EXISTS mars_reference;

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
                dryness_score INTEGER,
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
                mars_match TEXT
            );

            CREATE TABLE mars_reference (
                characteristic TEXT PRIMARY KEY,
                description TEXT NOT NULL
            );
        """)

        columns = [
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
            "dryness_score",
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
            "mars_match"
        ]

        column_text = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(columns))

        values = [
            tuple(place[column] for column in columns)
            for place in PLACES
        ]

        cursor.executemany(
            f"""
            INSERT INTO analog_places ({column_text})
            VALUES ({placeholders})
            """,
            values
        )

        cursor.executemany(
            """
            INSERT INTO mars_reference
            (characteristic, description)
            VALUES (?, ?)
            """,
            MARS_REFERENCE.items()
        )

        connection.commit()

    print(f"Database created successfully: {DB_FILE}")


def find_earth_area(
    terrain="rocky",
    maximum_temperature=0,
    maximum_pressure=70,
    minimum_rockiness=4,
    minimum_dryness=3
):
    terrain_words = terrain.lower().split()

    with sqlite3.connect(DB_FILE) as connection:
        connection.row_factory = sqlite3.Row

        query = """
            SELECT *
            FROM analog_places
            WHERE rocky_score >= ?
            AND dryness_score >= ?
            AND temperature_min_c <= ?
            AND pressure_min_kpa <= ?
            ORDER BY
                ABS(temperature_min_c - ?) +
                ABS(pressure_min_kpa - ?) +
                ABS(dryness_score - ?)
            LIMIT 1
        """

        result = connection.execute(
            query,
            (
                minimum_rockiness,
                minimum_dryness,
                maximum_temperature,
                maximum_pressure,
                maximum_temperature,
                maximum_pressure,
                minimum_dryness
            )
        ).fetchone()

        if result is None:
            return None

        terrain_text = result["terrain_keywords"].lower()

        if not any(word in terrain_text for word in terrain_words):
            return None

        return dict(result)


if __name__ == "__main__":
    create_database()
