from pathlib import Path

import psycopg

from src.extractors.abstract_extractor import AbstractExtractor
from src.utils import postgresql

DSN = ""


class PostgreSQLExtractor(AbstractExtractor):
    """Extractor for PostgreSQL."""

    def extract(self, table_name: str) -> list[dict]:
        """Extract data from PostgreSQL.

        Args:
            table_name (str): Name of the table.
        """
        try:
            self.logger.info("Attempting to connect to the PostgreSQL service.")
            with psycopg.connect(DSN, row_factory=psycopg.rows.dict_row) as connection:
                self.logger.info("Connecting to the PostgreSQL service.")
                with connection.cursor() as cursor:
                    self.logger.info(
                        f"Attempting to download everything from : {table_name}."
                    )
                    cursor.execute(
                        "SELECT * FROM %s;",
                        (table_name,),
                    )
                rows = cursor.fetchall()
                self.logger.info(f"Number of rows downloaded : {len(rows)}.")
                return rows
        except Exception as e:
            self.logger.error(f"Error PostgreSQL extractor: {e}.")
            raise
