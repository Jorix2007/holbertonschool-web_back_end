#!/usr/bin/env python3
"""Utility to calculate slice bounds for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Computes the starting and ending indices
    for a given page number and items per page.
    """
    offset = (page - 1) * page_size
    limit = offset + page_size

    return offset, limit
