import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Snap:
    snap_id: str
    url: str
    create_time: str
    file_type: str
    locale: str
    duration: str
    snapMediaInfo: str


class SnapJSONEncoder(json.JSONEncoder):
    def default(self, o: Snap):
        return asdict(o)
