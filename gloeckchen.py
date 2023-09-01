import os

# Pfad zum Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Pfad zum Ordner "CD" auf dem Desktop
cd_path = os.path.join(desktop_path, "CD")

# Erstelle den Ordner "CD", wenn er nicht vorhanden ist
os.makedirs(cd_path, exist_ok=True)

while True:
    spawnname = input("Spawnname (oder 'exit' zum Beenden): ")

    if spawnname.lower() == 'exit':
        break

    # Erstelle den Ordner für den Spawnnamen im "CD"-Ordner
    spawn_folder = os.path.join(cd_path, spawnname)
    os.makedirs(spawn_folder, exist_ok=True)

    # Erstelle die "data" und "stream" Ordner
    data_folder = os.path.join(spawn_folder, "data")
    stream_folder = os.path.join(spawn_folder, "stream")
    os.makedirs(data_folder, exist_ok=True)
    os.makedirs(stream_folder, exist_ok=True)

    # Erstelle die "_resource.lua" Datei
    resource_lua = os.path.join(spawn_folder, "_resource.lua")
    with open(resource_lua, "w") as file:
        file.write('''fx_version 'adamant'
game 'gta5'

description "ein Fantastisches Fahrzeug von Gloeckchen"
author "Made with <3 by mrgloeckchen"

files {
    'data/handling.meta',
    'data/dlctext.meta',
    'data/vehicles.meta',
    'data/carvariations.meta',
}

data_file 'HANDLING_FILE' 'data/handling.meta'
data_file 'DLCTEXT_FILE' 'data/dlctext.meta'
data_file 'VEHICLE_METADATA_FILE' 'data/vehicles.meta'
data_file 'VEHICLE_VARIATION_FILE' 'data/carvariations.meta'
''')

    print(f"Ordner für '{spawnname}' wurde erstellt.")

print("Das Programm wurde beendet.")
