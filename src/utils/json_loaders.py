import json
import pandas as pd


def is_json_line(line: str) -> bool:
    '''Test to see is each line in file is empty, JSON or an array'''
    line = line.strip()
    if not line:
        return False
    return line.startswith("{") or line.startswith("[")

def load_variable_json(raw_data_path:str, verbose:bool = True) -> pd.DataFrame:
    '''Process variably formed JSON files'''
    with open(raw_data_path, 'r') as f:
        raw = f.read().strip()

    # Try properly formed JSON
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, dict):
            data = [parsed]
        elif isinstance(parsed, list):
            data = parsed
        else:
            data = [parsed]
        if verbose:
            print(f"[load_variable_json] parsed as properly formed JSON from: {raw_data_path}")
        return pd.DataFrame(data)
    except json.JSONDecodeError:
        pass

    # Try JSON lines format
    lines = [ln.strip() for ln in raw.splitlines() if is_json_line(ln)]
    json_line_objects = []
    json_line_objects_ok = True
    for line in lines:
        try:
            obj = json.loads(line)
            json_line_objects.append(obj)
        except json.JSONDecodeError:
            json_line_objects_ok = False
            break
    if json_line_objects_ok and json_line_objects:
        if verbose:
             print(f"[load_variable_json] parsed as JSONL (one JSON object per line) from: {raw_data_path}")
        return pd.DataFrame(json_line_objects)
    
    # Improperly formed JSON (end of line commas)
    cleaned = raw

    # Strip trailing commas at end of file
    while cleaned.endswith(","):
        cleaned = cleaned[:-1].rstrip()

    cleaned = "[" + cleaned + "]"
    data = json.loads(cleaned)

    if verbose:
        print(f"[load_variable_json] Parsed as 'concatenated JSON objects with commas' from: {raw_data_path}")

    return pd.DataFrame(data)