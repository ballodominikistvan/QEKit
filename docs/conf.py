import os
import sys
# Hozzáadjuk a projekt gyökerét (QEKit/) a Python útvonalhoz, 
# hogy a Sphinx be tudja importálni a 'qekit' csomagot
sys.path.insert(0, os.path.abspath('..'))

project = 'QEKit'
copyright = '2026, Dominik Istvan Ballo'
author = 'Dominik Istvan Ballo'
release = '0.1.0'

# EZEKET A BŐVÍTMÉNYEKET MINDENKÉPP ADD HOZZÁ:
extensions = [
    'sphinx.ext.autodoc',      # Kiolvassa a docstringeket
    'sphinx.ext.napoleon',     # Támogatja a Google/NumPy stílusú docstringeket
    'sphinx.ext.viewcode',     # Linkeli a forráskódot a dokumentációból
    'myst_parser'              # Lehetővé teszi Markdown (.md) fájlok használatát
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# A Read the Docs téma beállítása:
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']