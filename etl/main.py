import logging
from pathlib import Path

from src.pipelines.etl_pipeline import ETLPipeline
from src.utils.config import etl_config, minio_config
from src.utils.logger import setup_logger
from src.utils.minio import make_buckeks


def main() -> None:
    log_dir = Path("/app/logs")
    if not log_dir.exists():
        log_dir.mkdir()
    logger_path = log_dir / "app.log"
    logger: logging.Logger = setup_logger(
        name="log", path=logger_path, level=logging.INFO
    )

    print("Minio config : ", minio_config)
    make_buckeks(logger=logger)

    etl_pipeline = ETLPipeline(config=etl_config, logger=logger)
    etl_pipeline.run()


if __name__ == "__main__":
    main()
