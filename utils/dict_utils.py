from typing import Any, Dict, List


class DictUtils:

    @staticmethod
    def sort_list_dicts(list_of_dicts: List[Dict[str, Any]], key: str):
        if list_of_dicts and key in list_of_dicts[0]:
            list_of_dicts = sorted(list_of_dicts, key=lambda x: x[key])
        return list_of_dicts
