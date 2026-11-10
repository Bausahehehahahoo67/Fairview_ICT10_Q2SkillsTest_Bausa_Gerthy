from pyscript import document
nonmets = {
    "Hydrogen": ("H", 1, 1.008),
    "Helium": ("He", 2, 4.0026),
    "Carbon": ("C", 6, 12.011),
    "Nitrogen": ("N", 7, 14.007),
    "Oxygen": ("O", 8, 15.999),
    "Fluorine": ("F", 9, 18.998),
    "Neon": ("Ne", 10, 20.180),
    "Phosphorus": ("P", 15, 30.974),
    "Sulfur": ("S", 16, 32.06),
    "Chlorine": ("Cl", 17, 35.45),
    "Argon": ("Ar", 18, 39.948),
    "Selenium": ("Se", 34, 78.971),
    "Bromine": ("Br", 35, 79.904),
    "Krypton": ("Kr", 36, 83.798),
    "Iodine": ("I", 53, 126.90),
    "Xenon": ("Xe", 54, 131.29),
    "Radon": ("Rn", 86, 222.0)
}
# The full names represent Keys, the tuples are values describing (symbols index 0, atomic numbers index 1, atomic weight index 2)

def locate_element(e): #defining my own function, which is to locate elements
    Element = document.getElementById("nonmets").value #collects user input
    result = nonmets.get(Element, ("Element not found", "-","-")) #validates user input if it matches anything in "nonmets" databse, other wise results to fallback
    document.getElementById("data_name").innerText = Element #gets name
    document.getElementById("data_symbol").innerText = result[0] #gets index 0
    document.getElementById("data_number").innerText = result[1] #gets index 1
    document.getElementById("data_weight").innerText = result[2] #gets index 2