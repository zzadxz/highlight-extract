import sqlite3
import os

db_path = os.path.expanduser('~/Library/Containers/com.apple.iBooksX/Data/Documents/AEAnnotation/AEAnnotation_v10312011_1727_local.sqlite')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = "SELECT ZANNOTATIONSELECTEDTEXT FROM ZAEANNOTATION WHERE ZANNOTATIONSELECTEDTEXT IS NOT NULL"

cursor.execute(query)

results = cursor.fetchall()

with open('highlights.txt', 'w') as file:
    for row in results:
        if row[0]:
            file.write(f"{row[0]}\n")

conn.close()

print("Highlights have been extracted to highlights.txt")
