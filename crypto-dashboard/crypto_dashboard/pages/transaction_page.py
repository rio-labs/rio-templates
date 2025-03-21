from __future__ import annotations

import typing as t
from dataclasses import KW_ONLY, field

import rio

from .. import components as comps


@rio.page(
    name="Transactions",
    url_segment="transactions",
)
class TransactionPage(rio.Component):
    """
    HELP US IMPROVE THIS TEMPLATE
    """

    def build(self) -> rio.Component:
        return comps.ContributionWanted(
            align_x=0.5,
            align_y=0.5,
            grow_x=True,
        )

