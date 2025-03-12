from __future__ import annotations

import typing as t
from dataclasses import KW_ONLY, field

import rio

from .. import components as comps
from .. import data_models


class ContributionWanted(rio.Component):
    """
    The ContributionWanted class is a component of a dashboard application, designed to
    display a message for contributors.

    ## Attributes

    `message`: The message for contributors.
    """

    def build(self) -> rio.Component:
        """
        Creates a message for contributors.
        """
        # Set the margin and minimum width based on the device
        device = self.session[data_models.PageLayout].device

        if device == "desktop":
            margin = 5
            min_width = 40
        else:
            margin = 2
            min_width = self.session.window_width - 2

        return rio.Card(
            rio.Markdown(
                """
# Contribution Wanted! :)
                
Would you like to help us improve this template or share your ideas? Feel free
to get in touch with us [GitHub
issue](https://github.com/rio-labs/rio/issues/217)!

We would love to hear from you! 🚀
""",
                margin=margin,
            ),
            min_width=min_width,
        )

