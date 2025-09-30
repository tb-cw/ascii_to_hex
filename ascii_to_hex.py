#!/usr/bin/env python3
"""
ascii_to_64bit_hex.py

Dieses Skript wandelt einen ASCII-String in einen 64-Bit Hex-Wert um.
Der Benutzer wird an der Kommandozeile nach dem ASCII-String gefragt.
Falls der String kürzer oder länger als 8 Zeichen ist, wird eine Warnung ausgegeben.
"""

# Eingabe vom Benutzer abfragen
ascii_input = input("Bitte einen ASCII-String eingeben (8 Zeichen = 64 Bit): ")

# Länge prüfen und ggf. Warnung ausgeben
if len(ascii_input) < 8:
    print("Warnung: Der String ist kürzer als 8 Zeichen. Das Ergebnis wird nicht 64 Bit sein.")
elif len(ascii_input) > 8:
    print("Warnung: Der String ist länger als 8 Zeichen. Es werden nur die ersten 8 Zeichen für 64 Bit verwendet.")
    ascii_input = ascii_input[:8]  # nur die ersten 8 Zeichen verwenden

# Umwandlung in Hex
hex_output = '0x' + ''.join(f'{ord(c):02X}' for c in ascii_input)

# Ergebnis ausgeben
print(f"ASCII: {ascii_input}")
print(f"Hex  : {hex_output}")
