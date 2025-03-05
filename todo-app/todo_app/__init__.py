from __future__ import annotations

import typing as t
from pathlib import Path

import rio

from . import components as comps
from . import data_models

# Define a theme for Rio to use.
#
# You can modify the colors here to adapt the appearance of your app or website.
# The most important parameters are listed, but more are available! You can find
# them all in the docs
#
# https://rio.dev/docs/api/theme
theme = rio.Theme.from_colors(
    primary_color=rio.Color.from_hex("01dffdff"),
    secondary_color=rio.Color.from_hex("0083ffff"),
    mode="dark",
)


# Create the Rio app
app = rio.App(
    name='Todo App',
    default_attachments=[data_models.TodoAppSettings()],
    theme=theme,
    assets_dir=Path(__file__).parent / "assets",
)

