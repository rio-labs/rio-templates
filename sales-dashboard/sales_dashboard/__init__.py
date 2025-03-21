from __future__ import annotations

import typing as t
from pathlib import Path

import pandas as pd

import rio

from . import components as comps
from . import data_models, persistence


def on_app_start(app: rio.App) -> None:
    """
    A function that runs when the app is started.
    """
    # Create a persistence instance. This class hides the gritty details of
    # database interaction from the app.
    pers = persistence.Persistence(
        csv_path=Path(__file__).parent / "assets" / "sales_data.csv",
        start_date=pd.Timestamp("2024-02-01"),
    )

    # Now attach it to the session. This way, the persistence instance is
    # available to all components using `self.session[persistence.Persistence]`
    app.default_attachments.append(pers)


def on_session_start(sess: rio.Session) -> None:
    # Determine which layout to use
    if sess.window_width < 60:
        layout = data_models.PageLayout(
            device="mobile",
            margin_app=0.5,
            margin_in_card=1,
            grow_x_content=False,
            grow_y_content=False,
        )
        # Calculate the minimum height of the content
        layout.min_width_content = (
            sess.window_width
            - 2 * layout.margin_app
            - 2 * layout.margin_in_card
        )

    else:
        layout = data_models.PageLayout(
            device="desktop",
            margin_app=4,
            margin_in_card=1,
            grow_x_content=True,
            grow_y_content=True,
        )

    # Attach the layout to the session
    sess.attach(layout)



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
    name='Sales Dashboard',
    # This function will be called once the app is ready.
    #
    # `rio run` will also call it again each time the app is reloaded.
    on_app_start=on_app_start,
    # This function will be called each time a user connects
    on_session_start=on_session_start,
    theme=theme,
    assets_dir=Path(__file__).parent / "assets",
)

