# -*- coding: utf-8 -*-
#
# UBC EOAS MOAD Group documentation Sphinx builder configuration file.
#
# This file does only contain a selection of the most common options.
# For a full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

import datetime


# -- Project information -----------------------------------------------------

project = 'UBC MOAD Docs'
author = 'The UBC EOAS MOAD Group and The University of British Columbia'
copyright_years = (
    "2018"
    if datetime.date.today().year == 2018
    else f"2018-{datetime.date.today():%Y}"
)
copyright = f"{copyright_years}, {author}"

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'nemocmd':
        ('http://nemo-cmd.readthedocs.io/en/latest/', None),
    'salishseacmd':
        ('http://salishseacmd.readthedocs.io/en/latest/', None),
    "salishseadocs":
        ("https://salishsea-meopar-docs.readthedocs.io/en/latest/", None),
}

# Private GitHub repositories that linkcheck will ignore
linkcheck_ignore = [
    'https://github.com/SalishSeaCast/NEMO-3.6-code',
    'https://github.com/SalishSeaCast/rpn-to-gemlam',
    'https://github.com/SalishSeaCast/XIOS-2',
    'https://github.com/UBC-MOAD/ariane-2.2.8-code',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/UBC_EOAS_favicon.ico"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
