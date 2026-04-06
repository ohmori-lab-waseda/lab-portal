project = "大森研ポータル"
copyright = "2025, 大森研究室"
author = "大森峻一"
release = "2025"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "ja"

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["custom.js"]

html_title = "大森研究室ポータル"
html_short_title = "大森研究室"

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    "light_css_variables": {
        "color-brand-primary": "#1a5276",
        "color-brand-content": "#1a5276",
        "color-highlight-on-target": "#e8f4f8",
    },
    "dark_css_variables": {
        "color-brand-primary": "#5dade2",
        "color-brand-content": "#5dade2",
    },
    "footer_icons": [],
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
