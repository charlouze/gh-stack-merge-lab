import re
import unicodedata

_SEPARATORS = re.compile(r"[\W_]+")


def slugify(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    without_accents = "".join(c for c in decomposed if not unicodedata.combining(c))
    return _SEPARATORS.sub("-", without_accents.lower()).strip("-")
