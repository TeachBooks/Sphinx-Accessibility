# -*- coding: utf-8 -*-
"""
sphinx_accessibility
~~~~~~~~~~~~~~~~~~~~

Sphinx extension that provides accessibility features.

"""

from sphinx.application import Sphinx
from typing import Any, Dict, Set, Union, cast
from pathlib import Path
from sphinx.util.fileutil import copy_asset

def setup(app: Sphinx) -> Dict[str, Any]:
    
    app.connect("builder-inited", set_asset_files)  # event order - 2
    app.connect("build-finished", copy_asset_files)  # event order - 16

    return {
        "version": "builtin",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def set_asset_files(app: Sphinx) -> None:
    """Sets the asset files for the codex extension"""

    # app.add_js_file(None, body=f"let dualButtonTextual = '{translate('Textual')}';")
    
    app.add_js_file("Accessibility.js")
    app.add_css_file("HighContrast.css")
    app.add_css_file("OpenDyslexic.css")
    app.add_css_file("SVGstyling.css")

def copy_asset_files(app: Sphinx, exc: Union[bool, Exception]):
    """Copies required assets for formating in HTML"""

    html_assets_dir = Path(__file__).parent.joinpath("assets", "html").absolute()
    asset_files = list(html_assets_dir.glob("*"))
    if exc is None:
        for path in asset_files:
            copy_asset(str(path), str(Path(app.outdir).joinpath("_static").absolute()))