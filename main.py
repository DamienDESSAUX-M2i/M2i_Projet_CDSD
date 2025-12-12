import logging

from src.pipelines.etl_pipeline import ETLPipeline
from src.utils.config import etl_config
from src.utils.logger import setup_logger
from src.utils.minio import make_buckeks


def main() -> None:
    logger_path = "./logs/app.log"
    logger: logging.Logger = setup_logger(
        name="log", path=logger_path, level=logging.INFO
    )

    # make_buckeks(logger=logger)

    etl_pipeline = ETLPipeline(config=etl_config, logger=logger)
    etl_pipeline.run()


if __name__ == "__main__":
    main()
