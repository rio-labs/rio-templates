from __future__ import annotations

import typing as t
from pathlib import Path

import rio

from . import components as comps
from . import data_models, theme


def on_session_start(sess: rio.Session) -> None:
    # Determine which layout to use
    if sess.window_width < 60:
        layout = data_models.PageLayout(
            device="mobile",
        )
    else:
        layout = data_models.PageLayout(
            device="desktop",
        )

    # Attach the layout to the session
    sess.attach(layout)



# Create the Rio app
app = rio.App(
    name='Crypto Dashboard',
    # This function will be called each time a user connects
    on_session_start=on_session_start,
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

