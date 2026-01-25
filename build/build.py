from builder.ini import *
from builder.ini import INIO

def build(backup: bool = True, p: str) -> dict[str, str] | dict[str, dict[str, str]] | list[str] | None:
  path = ""
  ini = INIO(path)
  ini.load()

  if not ini.data:
    return { "error": "1" }

  if backup:
    ini.backup(p)
  else:
    pass
