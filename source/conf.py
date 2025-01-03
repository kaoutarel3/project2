# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'project2'
copyright = '2024, kaoutar_wissal'
author = 'kaoutar_wissal'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'prev_next_buttons_location': 'bottom',  # Options: 'bottom', 'top', 'both', None
    'style_nav_header_background': '#070637',  # Optional: Customize navigation header color
    'collapse_navigation': False,  # Ensures the menu doesn't collapse
    'navigation_depth': 1,
}
html_title = "Stu(dying)"
