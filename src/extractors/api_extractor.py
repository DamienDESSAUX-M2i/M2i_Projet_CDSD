import logging
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from src.extractors.abstract_extractor import AbstractExtractor


class APIExtractor(AbstractExtractor):
    """Loader API REST."""

    def __init__(
        self,
        logger: logging.Logger,
        base_url: str,
        api_key: str = None,
        timeout: int = 10,
        retry_strategy: Retry = Retry(total=3, backoff_factor=1),
    ):
        super().__init__(logger)
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.retry_strategy = retry_strategy

    def extract(self, endpoint, params: dict[str, Any] = {}) -> requests.Response:
        """Extrait données d'une API"""
        try:
            self.logger.info(
                f"Attempting to extract data from {self.base_url}/{endpoint}."
            )

            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            with requests.Session() as session:
                adapter = HTTPAdapter(max_retries=self.retry_strategy)
                session.mount("http://", adapter)
                session.mount("https://", adapter)

                response = session.get(
                    url=f"{self.base_url}/{endpoint}",
                    params=params,
                    headers=headers,
                    timeout=self.timeout,
                )

            response.raise_for_status()
            data = response.json()

            self.logger.info("Extraction completed.")
            return data
        except Exception as e:
            self.logger.error(f"API Extractor Error : {e}")
            raise
