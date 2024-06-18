import sqlite3
import os
import textwrap
import tkinter as tk
from tkinter import filedialog, messagebox


def extract_highlights(output_path):
    db_path = os.path.expanduser(
        '~/Library/Containers/com.apple.iBooksX/Data/Documents/AEAnnotation/AEAnnotation_v10312011_1727_local.sqlite')
    if not os.path.exists(db_path):
        messagebox.showerror("Error", f"Database file not found at {db_path}.")
        return

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
    with open(output_path, 'w') as file:
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


def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, file_path)


def run_extraction():
    output_path = output_path_entry.get()
    if not output_path:
        messagebox.showerror("Error", "Please select an output file.")
        return
    extract_highlights(output_path)
    messagebox.showinfo("Success", "Highlights have been extracted successfully.")


app = tk.Tk()
app.title("Highlight Extractor")

tk.Label(app, text="Output File:").grid(row=0, column=0, padx=10, pady=10)
output_path_entry = tk.Entry(app, width=50)
output_path_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse...", command=select_output_file).grid(row=0, column=2, padx=10, pady=10)

tk.Button(app, text="Extract Highlights", command=run_extraction).grid(row=1, columnspan=3, padx=10, pady=20)

app.mainloop()
