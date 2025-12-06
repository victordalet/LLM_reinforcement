from typing import List


class ParserManager:

    @staticmethod
    def get_between(text: str, start: str, end: str, filter_to_remove=None) -> List[str]:
        results = []
        start_len = len(start)
        end_len = len(end)
        start_idx = 0

        while True:
            start_idx = text.find(start, start_idx)
            if start_idx == -1:
                break
            start_idx += start_len
            end_idx = text.find(end, start_idx)
            if end_idx == -1:
                break
            results.append(text[start_idx:end_idx])
            start_idx = end_idx + end_len

        for item in results.copy():
            if filter_to_remove and filter_to_remove in item:
                results.remove(item)

        return results


