from sqlmodel import SQLModel, create_engine
from .config import settings
import os

engine = create_engine(settings.db_url, echo=False)

def _ensure_sqlite_dir() -> None:
    url = settings.db_url
    if url.startswith("sqlite:///"):
        path = url.replace("sqlite:///", "")
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)


def init_db() -> None:
    from .models.memory_event import MemoryEvent
    from .models.soulpack_meta import SoulpackMeta
    _ensure_sqlite_dir()
    SQLModel.metadata.create_all(engine)