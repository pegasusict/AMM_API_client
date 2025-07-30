def build_offset_args(limit: int = 20, offset: int = 0) -> dict:
    return {"limit": limit, "offset": offset}


def build_search_args(query: str, limit: int = 20) -> dict:
    return {"query": query, "limit": limit}
