from src.commons.data_manager import DataManager
from src.commons.parser_manager import ParserManager
from src.commons.request_manager import RequestManager
from typing import List


class ScrapperCoachHunter:

    @staticmethod
    def scrap_article(url: str) -> List[dict]:
        articles: List[dict] = []
        data = RequestManager.get(url) or ""
        blocks = ParserManager.get_between(data, '<div class="exo2">', "</div>")
        for b in blocks:
            raw_title = ""
            title_blocks = ParserManager.get_between(b, "<h4>", "</h4>")
            if title_blocks:
                raw_title = ParserManager.strip_tags(title_blocks[0])
            content = ""
            content_blocks = ParserManager.get_between(
                b, '<figcaption class="descEx">', "</figcaption>"
            )
            if content_blocks:
                content = ParserManager.strip_tags(content_blocks[0])

            images = ParserManager.get_between(b, 'src="', '"')
            image = images[0] if images else ""

            if raw_title or content or image:
                articles.append(
                    {"title": raw_title, "content": content, "pictures_urls": [image]}
                )

        return articles

    def run(self):
        articles = self.scrap_article("https://www.coach-hunter.com/exercice")
        DataManager.save_json(articles, "dataset/coach_hunter.json")


if __name__ == "__main__":
    DataManager.create_directory("dataset")
    ScrapperCoachHunter().run()
