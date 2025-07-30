# utils/pagination.py
async def fetch_all_paginated(fetch_fn, page_size=50, max_pages=10):
    all_results = []
    offset = 0

    for _ in range(max_pages):
        page = await fetch_fn(limit=page_size, offset=offset)
        if not page:
            break
        all_results.extend(page)
        offset += page_size

    return all_results
