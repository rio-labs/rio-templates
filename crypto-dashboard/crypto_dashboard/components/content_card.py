from __future__ import annotations

from dataclasses import KW_ONLY, field
import typing as t

import rio

from .. import components as comps

class ContentCard(rio.Component):
    """
    A component that represents a card with a header and content.


    ## Attributes:

    `header`: The text to display as the card's header.

    `content`: The content component to display within the card.
    """

    header: str
    content: rio.Component

    def build(self) -> rio.Component:
        return rio.Card(
            content=rio.Column(
                # Add header with bold font
                rio.Text(
                    self.header,
                    style=rio.TextStyle(
                        font_size=1.5,
                        font_weight="bold",
                    ),
                ),
                # Add content
                self.content,
                # Fill up remaining space with a spacer, therefore all cards
                # have the same height
                rio.Spacer(),
                spacing=1,
                margin=1,
            ),
        )

