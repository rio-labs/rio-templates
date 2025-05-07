from __future__ import annotations

import typing as t
from pathlib import Path

import rio

from . import components as comps
from . import theme

# Create the Rio app
app = rio.App(
    name='Dashboard Better Name',
    # You can optionally provide a root component for the app. By default,
    # Rio's default navigation is used. By providing your own component, you
    # can create components which stay put while the user navigates between
    # pages, such as a navigation bar or footer.
    #
    # When you do this, make sure your component contains a `rio.PageView`
    # so the currently active page is still visible.
    build=comps.RootComponent,
    # You can also provide a custom theme for the app. This theme will
    # override Rio's default.
    theme=theme.THEME,
    assets_dir=Path(__file__).parent / "assets",
)

