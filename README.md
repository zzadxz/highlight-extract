# Highlight Extractor

Highlight Extractor is an application designed to extract highlights from iBooks and Apple Books and save them to a text file. This tool is particularly useful for readers who want to keep an organzied record of their highlights for future reference. NLP is intended to be added in future updates. Stay tuned!

## Features

- Extracts highlights from iBooks
- Organizes highlights by book and color
- Saves the extracted highlights to a text file
- Easy-to-use graphical interface

## Requirements

- Python 3.x
- Tkinter

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required Python packages:
    ```sh
    pip install tk
    ```
3. Download or clone the repository.

## Usage

1. **Running the Script:**

    You can run the script directly using Python:
    ```sh
    python extract_highlights.py
    ```

2. **Using the GUI:**

    - Open the application.
    - Click on the "Browse..." button to select the output file where the highlights will be saved.
    - Click on the "Extract Highlights" button to start the extraction process.
    - A success message will be displayed once the highlights have been extracted and saved.


## Code Overview

### `extract_highlights.py`

This script performs the following tasks:
- Connects to the iBooks SQLite database to retrieve highlights.
- Organizes the highlights by book ID and color.
- Saves the organized highlights to a specified text file.
- Provides a graphical interface for selecting the output file and running the extraction process.

### Functions

- `extract_highlights(output_path)`: Connects to the SQLite database, retrieves highlights, organizes them, and saves them to the specified output file.
- `select_output_file()`: Opens a file dialog to select the output file.
- `run_extraction()`: Initiates the highlight extraction process and displays success or error messages.

### Graphical Interface

The graphical interface is built using Tkinter. It provides an easy-to-use interface for selecting the output file and starting the extraction process.

Enjoy using Highlight Extractor to keep track of your Apple Books highlights!
