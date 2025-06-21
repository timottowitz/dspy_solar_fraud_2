import difflib
from dataclasses import dataclass
from typing import List

@dataclass
class RetrievedDocument:
    long_text: str

class SimpleRetriever:
    """A lightweight in-memory retriever for Example objects."""
    def __init__(self, examples: List):
        self.examples = examples

    def __call__(self, query: str, k: int = 1):
        scored = sorted(
            self.examples,
            key=lambda ex: difflib.SequenceMatcher(None, query.lower(), getattr(ex, "content", str(ex)).lower()).ratio(),
            reverse=True,
        )
        return [RetrievedDocument(long_text=getattr(ex, "content", str(ex))) for ex in scored[:k]]
