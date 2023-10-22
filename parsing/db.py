"""Database functions."""
import contextlib
from typing import Any, Iterator, Callable, Protocol

import sqlite3

class Connection(Protocol):
    """Generic db connection object"""
    def cursor(self) -> Any:
        """Retrieve cursor object"""
        raise NotImplementedError
    def commit(self) -> Any:
        """commit transaction."""
        raise NotImplementedError
    def rollback(self) -> Any:
        """rollback transaction."""
        raise NotImplementedError

class Cursor(Protocol):
    """Generic db cursor object."""
    def execute(self, *args, **kwargs) -> Any:
        """Execute a single query"""
        raise NotImplementedError

    def executemany(self, *args, **kwargs) -> Any:
        """Run query with many params."""
        raise NotImplementedError

    def fetchone(self, *args, **kwargs):
        """Fetch single result if present, or `None`."""
        raise NotImplementedError

    def fetchmany(self, *args, **kwargs):
        """Fetch many results if present or `None`."""
        raise NotImplementedError

    def fetchall(self, *args, **kwargs):
        """Fetch all results if present or `None`."""
        raise NotImplementedError

@contextlib.contextmanager
def connection(db_path: str,
               row_factory: Callable = sqlite3.Row) -> Iterator[Connection]:
    """Get connection to sqlite3 database."""
    conn = sqlite3.connect(db_path)
    try:
        conn.row_factory = row_factory
        conn.execute("PRAGMA foreign_keys = ON")
        yield conn
        conn.commit()
    except sqlite3.Error as exc:
        conn.rollback()
        raise exc
    finally:
        conn.close()

@contextlib.contextmanager
def cursor(conn: Connection) -> Iterator[Cursor]:
    """Get a cursor from connection."""
    cur = conn.cursor()
    try:
        yield conn.cursor()
        conn.commit()
    except sqlite3.Error as exc:
        conn.rollback()
        raise exc
    finally:
        cur.close()
