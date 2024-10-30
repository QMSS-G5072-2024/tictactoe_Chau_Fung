# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tictactoe_fc2786'
copyright = '2024, Fung Chau'
author = 'Fung Chau'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# Enable the necessary extensions
extensions = [
    'sphinx.ext.autodoc',           # Automatically document modules
    'sphinx.ext.napoleon',           # Supports NumPy-style docstrings
    'myst_nb',                       # Supports Markdown and Jupyter notebooks
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
]

# Specify the directory for AutoAPI
autoapi_dirs = ['../src']

# Templates and excluded patterns
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']




