import os

def rename_mp3_files(directory):
    # Liste aller MP3-Dateien im angegebenen Verzeichnis
    files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    
    # Dateien sortieren, um sicherzustellen, dass sie in der gewünschten Reihenfolge umbenannt werden
    files.sort()
    
    # Dateien umbenennen
    for count, filename in enumerate(files, start=1):
        # Neues Dateinamenformat mit führenden Nullen
        new_name = f"{count:03}.mp3"
        
        # Vollständige Pfade für Quell- und Zieldateien
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        
        # Datei umbenennen
        os.rename(src, dst)
        print(f"Renamed '{filename}' to '{new_name}'")

# Verzeichnis mit dem Speicherort des Skripts angeben
rename_mp3_files(os.getcwd())