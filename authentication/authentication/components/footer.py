from __future__ import annotations

from dataclasses import KW_ONLY, field
import typing as t

import rio

from .. import components as comps

class Footer(rio.Component):
    """
    A simple, static component which displays a footer with the company name and
    website name.
    """

    def build(self) -> rio.Component:
        return rio.Card(
            content=rio.Column(
                rio.Icon("rio/logo:fill", min_width=5, min_height=5),
                rio.Text("Buzzwordz Inc.", justify="center"),
                rio.Text(
                    "Hyper Dyper Website",
                    style="dim",
                ),
                spacing=1,
                margin=2,
                align_x=0.5,
            ),
            color="hud",
            corner_radius=0,
        )

