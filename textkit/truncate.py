def truncate(text: str, width: int) -> str:
    if width < 1:
        raise ValueError(f"width must be at least 1, got {width}")
    if len(text) <= width:
        return text
    return text[: width - 1].rstrip() + "…"
