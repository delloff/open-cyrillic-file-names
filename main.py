import transliterate
import os

old_path = os.path.join("D:\Books", "Название на русском.xlsx")
new_path = os.path.join("D:\Books", transliterate.translit('Название на русском.xlsx'.replace(' ','_'), reversed=True))

os.rename(old_path, new_path)

os.system(new_path)

if not os.path.isfile(old_path):
    os.rename(new_path, old_path)
