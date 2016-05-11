# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import os
import sys
import builtins

from xonsh import __version__ as XONSH_VERSION
from xonsh.environ import DEFAULT_DOCS, Env
from xonsh.xontribs import xontrib_metadata

sys.path.insert(0, os.path.dirname(__file__))

# -- General configuration -----------------------------------------------------

# Documentation is being built on readthedocs, this will be true.
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.pngmath',
              'sphinx.ext.inheritance_diagram', 'sphinx.ext.viewcode',
              #'sphinx.ext.autosummary',
              'numpydoc', 'cmdhelp',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'xonsh'
copyright = u'2015, Anthony Scopatz'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = XONSH_VERSION.rsplit('.',1)[0]

# The full version, including alpha/beta/rc tags.
release = XONSH_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
#pygments_style = 'friendly'
#pygments_style = 'bw'
#pygments_style = 'fruity'
#pygments_style = 'manni'
#pygments_style = 'tango'
#pygments_style = 'pastie'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'default'
#html_theme = 'altered_nature'
#html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
if not on_rtd:
    import cloud_sptheme as csp

    html_theme = 'cloud'

    html_theme_options = {
        'max_width': '1250px',
        'minimal_width': '700px',
        'relbarbgcolor': '#000000',
        'footerbgcolor': '#FFFFE7',
        'sidebarwidth': '322px',
        'sidebarbgcolor': '#e7e7ff',
        #'googleanalytics_id': 'UA-41934829-1',
        'stickysidebar': False,
        'highlighttoc': False,
        'externalrefs': False,
        'collapsiblesidebar': True,
        'default_layout_text_size': "100%",  # prevents division by zero error
        }

    # Add any paths that contain custom themes here, relative to this directory.
    html_theme_path = ["_theme", csp.get_theme_dir()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/ascii_conch_part_color_tight.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/magic_conch.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = "numpy_friendly.css"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'xonshdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'xonsh.tex', u'xonsh documentation',
   u'Anthony Scopatz', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

#Autodocumentation Flags
autodoc_member_order = "groupwise"
autoclass_content = "both"
autosummary_generate = []

# Prevent numpy from making silly tables
numpydoc_show_class_members = False


#
# Auto-generate some docs
#

def make_envvars():
    env = Env()
    vars = sorted(DEFAULT_DOCS.keys())
    s = ('.. list-table::\n'
         '    :header-rows: 0\n\n')
    table = []
    ncol = 3
    row = '    {0} - :ref:`${1} <{2}>`'
    for i, var in enumerate(vars):
        star = '*' if i%ncol == 0 else ' '
        table.append(row.format(star, var, var.lower()))
    table.extend(['      -']*((ncol - len(vars)%ncol)%ncol))
    s += '\n'.join(table) + '\n\n'
    s += ('Listing\n'
          '-------\n\n')
    sec = ('.. _{low}:\n\n'
           '{title}\n'
           '{under}\n'
           '{docstr}\n\n'
           '**configurable:** {configurable}\n\n'
           '**default:** {default}\n\n'
           '-------\n\n')
    for var in vars:
        title = '$' + var
        under = '.' * len(title)
        vd = env.get_docs(var)
        s += sec.format(low=var.lower(), title=title, under=under,
                        docstr=vd.docstr, configurable=vd.configurable,
                        default=vd.default)
    s = s[:-9]
    fname = os.path.join(os.path.dirname(__file__), 'envvarsbody')
    with open(fname, 'w') as f:
        f.write(s)


def make_xontribs():
    md = xontrib_metadata()
    names = sorted(d['name'] for d in md['xontribs'] if 'name' in d)
    s = ('.. list-table::\n'
         '    :header-rows: 0\n\n')
    table = []
    ncol = 3
    row = '    {0} - :ref:`{1} <{2}>`'
    for i, name in enumerate(names):
        star = '*' if i%ncol == 0 else ' '
        table.append(row.format(star, name, name.lower()))
    table.extend(['      -']*((ncol - len(vars)%ncol)%ncol))
    s += '\n'.join(table) + '\n\n'
    s += ('Information\n'
          '-----------\n\n')
    sec = ('.. _{low}:\n\n'
           '{title}\n'
           '{under}\n'
           '**Website:** {url}\n\n'
           '**Package:** {pkg}\n\n'
           '{desc}\n\n'
           '{inst}'
           '-------\n\n')
    for name in names:
        for d in md['xontribs']:
            if d.get('name', None) == name:
                break
        title = name
        under = '.' * len(title)
        desc = d.get('description', '')
        if not isinstance(desc, str):
            desc = ''.join(desc)
        pkgname = d.get('package', None)
        if pkgname is None:
            pkg = 'unknown'
            inst = ''
        else:
            pd = md['packages'].get(pkgname, {})
            pkg = pkgname
            if 'url' in pd:
                pkg = '`{0} <{1}>`_'.format(pkg, pd['url'])
            if 'license' in pd:
                pkg = pkg + ', ' + pd['license']
            inst = ''
            for k, v in sorted(pd.get('install', {}).items()):
                cmd = "\n    $ ".join(v.split('\n'))
                inst += ('**Install with {k}:**\n\n'
                         '.. code-block:: xonshcon\n\n'
                         '    $ {cmd}'
                         '\n\n').format(k=k, cmd=cmd)
        s += sec.format(low=name.lower(), title=title, under=under,
                        url=d.get('url', 'unknown'), desc=desc,
                        pkg=pkg, inst=inst)
    s = s[:-9]
    fname = os.path.join(os.path.dirname(__file__), 'xontribsbody')
    with open(fname, 'w') as f:
        f.write(s)


make_envvars()
make_xontribs()

builtins.__xonsh_history__= None
