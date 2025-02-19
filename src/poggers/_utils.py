from typing import List, Tuple
from datetime import datetime
from pathlib import Path

import pandas as pd

from .options import PoggerOptions


def parse_filename_to_unix(path: Path):
    parts = path.stem.split("_")

    timestamp1_str = parts[1]
    timestamp2_str = parts[2]
    
    dt_format = "%y%m%d%H%M%S"
    timestamp1 = datetime.strptime(timestamp1_str, dt_format)
    timestamp2 = datetime.strptime(timestamp2_str, dt_format)
    
    unix_timestamp1 = int(timestamp1.timestamp()) + 7200
    unix_timestamp2 = int(timestamp2.timestamp()) + 7200
    
    return unix_timestamp1, unix_timestamp2

def get_scan_timestamps(fill: int) -> List[Tuple[int, int]]:
    # FIXME: This should not have a hardcoded path
    options = PoggerOptions()
    vdm_fill_path = (options.vdm_path / str(fill)).absolute()
    if not vdm_fill_path.exists():
        print(f"No scans found for fill '{fill}' in '{options.vdm_path.absolute().as_posix()}'. If this is not expected verify the 'vdm_path' option is set to the correct value.")
        return []

    return [parse_filename_to_unix(path) for path in vdm_fill_path.glob("*.hd5")]

def filter_scan_timestamps(df: pd.DataFrame, scan_timestamps: List[Tuple[int, int]]) -> pd.DataFrame:
    filter_condition = pd.Series(False, index=df.index)
    for start, end in scan_timestamps:
        filter_condition |= (df["time"] >= start) & (df["time"] <= end)
    return df[~filter_condition]
