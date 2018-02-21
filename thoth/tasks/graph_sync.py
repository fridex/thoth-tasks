"""Sync packages stored on the remote distributed FS to the graph database."""

from .base import BaseTask


class GraphSyncTask(BaseTask):
    """Sync packages stored on the remote distributed FS to the graph database."""

    def run(self, node_args: dict) -> None:
        raise NotImplementedError
