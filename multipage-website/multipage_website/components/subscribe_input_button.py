from __future__ import annotations

import typing as t
from dataclasses import KW_ONLY, field

import rio

from .. import components as comps


class SubscribeInputButton(rio.Component):
    """
    A component for collecting email subscriptions.
    """

    def build(self) -> rio.Component:
        """
        Constructs the subscription input and button component.

        The component consists of:
        - A pill-styled text input field for email input.
        - A rounded "Subscribe" button with hover and ripple effects.
        """
        return rio.Stack(
            # Email input field
            rio.TextInput(
                "",
                label="Enter your email address",
                style="pill",
                min_height=3,
                align_y=0,
            ),
            # Subscribe button
            rio.Rectangle(
                content=rio.Text(
                    "Subscribe",
                    style=rio.TextStyle(
                        font_size=0.75,
                        fill=self.session.theme.background_color,
                    ),
                    selectable=False,  # Make the text non-selectable
                    margin=0.5,
                ),
                fill=self.session.theme.primary_color,
                hover_fill=self.session.theme.primary_color.darker(0.2),
                transition_time=0.1,  # Smooth transition for hover effects
                corner_radius=99999,  # Fully rounded corners for the button
                # Add a pointer cursor and ripple effect on hover
                cursor=rio.CursorStyle.POINTER,
                ripple=True,
                # Align and add margin
                align_x=1,
                align_y=0.5,
                margin_right=0.5,
            ),
        )

