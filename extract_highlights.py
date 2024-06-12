import sqlite3
import os
import textwrap

db_path = os.path.expanduser(
    '~/Library/Containers/com.apple.iBooksX/Data/Documents/AEAnnotation/AEAnnotation_v10312011_1727_local.sqlite')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = """
SELECT 
    ZANNOTATIONASSETID AS BookID, 
    ZANNOTATIONSELECTEDTEXT AS Highlight,
    ZANNOTATIONSTYLE AS Color
FROM ZAEANNOTATION 
WHERE ZANNOTATIONSELECTEDTEXT IS NOT NULL
ORDER BY BookID, Color;
"""

cursor.execute(query)
results = cursor.fetchall()
conn.close()

color_mapping = {
    0: 'Yellow',
    1: 'Green',
    2: 'Blue',
    3: 'Pink',
    4: 'Purple',
    5: 'Underline'
}

organized_highlights = {}
for row in results:
    book_id, highlight, color_code = row
    color = color_mapping.get(color_code, 'Unknown')

    if book_id not in organized_highlights:
        organized_highlights[book_id] = {}

    if color not in organized_highlights[book_id]:
        organized_highlights[book_id][color] = []

    organized_highlights[book_id][color].append(highlight)

divider = "------------"
with open('organized_highlights.txt', 'w') as file:
    first_book = True
    for book_id, colors in organized_highlights.items():
        if not first_book:
            file.write(f"\n{divider}\n")
        first_book = False
        file.write(f"\nBook ID: {book_id}\n")
        for color, highlights in colors.items():
            file.write(f"  {color} Highlights:\n")
            for highlight in highlights:
                wrapped_highlight = textwrap.fill(highlight, width=80)
                file.write(f"    - {wrapped_highlight}\n")

print("Organized highlights have been extracted to organized_highlights.txt")
