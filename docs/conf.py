import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'QEKit'
copyright = '2026 Dominik Istvan Ballo'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser'
]

html_theme = 'sphinx_rtd_theme'