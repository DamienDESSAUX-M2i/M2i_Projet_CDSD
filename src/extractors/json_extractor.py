import json
from pathlib import Path
from typing import Any

from src.extractors.abstract_extractor import AbstractExtractor


class JSONExtractor(AbstractExtractor):
    """Extractor for a CSV file."""

    def extract(self, file_path: Path, **kwargs) -> dict[str, Any]:
        """Extract data from a JSON file.

        Args:
            file_path (Path): Path of the JSON file.

        Returns:
            dict[str, Any]: Data extract from the JSON file.
        """
        try:
            self.logger.info(f"Attempting to extract data from {file_path}.")
            with open(file=file_path, mode="r", encoding="utf-8") as file:
                dict_data = json.load(fp=file, **kwargs)
            self.logger.info(f"Extraction completed : {len(dict_data)} data extract.")
            return dict_data
        except Exception as e:
            self.logger.error(f"Error JSON extractor: {e}.")
            raise
