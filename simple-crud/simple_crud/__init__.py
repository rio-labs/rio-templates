from __future__ import annotations

import typing as t
from pathlib import Path

import rio

from . import components as comps
from . import persistence


def on_app_start(app: rio.App) -> None:
    """
    A function that runs when the app is started.
    """
    # Create a persistence instance. This class hides the gritty details of
    # database interaction from the app.
    pers = persistence.Persistence()

    # Now attach it to the session. This way, the persistence instance is
    # available to all components using `self.session[persistence.Persistence]`
    app.default_attachments.append(pers)



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
    mode="light",
)


# Create the Rio app
app = rio.App(
    name='Simple CRUD',
    # This function will be called once the app is ready.
    #
    # `rio run` will also call it again each time the app is reloaded.
    on_app_start=on_app_start,
    theme=theme,
    assets_dir=Path(__file__).parent / "assets",
)

