from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LabelItem:
    qrcode: str
    lines: list[str]

    def serialize(self) -> str:
        return "\n".join(self.lines)
