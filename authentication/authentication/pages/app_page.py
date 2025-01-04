from __future__ import annotations

import typing as t
from dataclasses import KW_ONLY, field

import rio

from .. import components as comps
from .. import data_models


def guard(event: rio.GuardEvent) -> str | None:
    # This website allows access to sensitive information. Enforce stringent
    # access control to all in-app pages.

    # Check if the user is authenticated by looking for a user session
    try:
        event.session[data_models.AppUser]

    except KeyError:
        # User is not logged in, redirect to the login page
        return "/"

    # User is logged in, no redirection needed
    return None


@rio.page(
    name="App",
    url_segment="app",
    guard=guard,
)
class InnerAppPage(rio.Component):
    def build(self) -> rio.Component:
        return rio.PageView(
            grow_y=True,
        )

