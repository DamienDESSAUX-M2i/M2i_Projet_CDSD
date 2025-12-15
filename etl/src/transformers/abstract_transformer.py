from abc import ABC


class AbstractTransformer(ABC):
    """Abstract class for loaders."""

    def __init__(self, logger):
        self.logger = logger
