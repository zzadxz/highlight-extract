from setuptools import setup

APP = ['extract_highlights.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['sqlite3', 'os', 'textwrap', 'tkinter'],
    'includes': ['sqlite3', 'os', 'textwrap', 'tkinter'],
    'plist': {
        'CFBundleName': 'Highlight Extractor',
        'CFBundleDisplayName': 'Highlight Extractor',
        'CFBundleGetInfoString': 'Extract highlights from iBooks',
        'CFBundleIdentifier': 'com.yourcompany.highlightextractor',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
        'NSHighResolutionCapable': 'True',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
