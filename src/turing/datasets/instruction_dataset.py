from typing import Union
from pathlib import Path
from datasets import load_dataset

class InstructionDataset:
    def __init__(
        self, 
        path: Union[str, Path]
    ):
        self.data = load_dataset(path)
        self._validate()
    
    def _validate(self):
        # check is hf dataset has train split and if it has column text, and if there are any other - it should be target
        assert "train" in self.data, "The dataset should have a train split"
        assert "text" in self.data["train"].column_names, "The dataset should have a column named text"
        assert "target" in self.data["train"].column_names, "The dataset should have a column named target"
        assert "instruction" in self.data["train"].column_names, "The dataset should have a column named instruction"
        assert len(self.data["train"].column_names) == 3, "The dataset should have only three columns, instruction, text and target"

    def __len__(self):
        return len(self.data["train"])

    def __iter__(self):
        return iter(self.data["train"])

    def __getitem__(self, idx):
        return self.data["train"][idx]
