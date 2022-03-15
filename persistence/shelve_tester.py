import shelve
from person import Person


with shelve.open("shelve_db") as x:
    # x["class"] = Person("Smb", "engineer", 500)
    print(x["class"].tax)
