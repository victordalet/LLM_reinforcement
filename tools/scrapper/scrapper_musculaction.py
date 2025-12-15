from src.commons.data_manager import DataManager
from src.commons.parser_manager import ParserManager
from src.commons.request_manager import RequestManager


class ScrapperMusculaction:

    @staticmethod
    def scrap_link():
        url = "https://www.musculaction.com/exercices-musculation.htm"
        data = RequestManager.get(url)
        urls = ParserManager.get_between(
            data, '<li><a href="https://www.musculaction.com/', '">'
        )
        for i in range(len(urls)):
            urls[i] = "https://www.musculaction.com/" + urls[i]
        return urls

    @staticmethod
    def scrap_article(url: str) -> dict:
        data = RequestManager.get(url)
        title_parts = ParserManager.get_between(data, '<h1 class="h1grand">', "</h1>")
        if not title_parts:
            title_parts = ParserManager.get_between(data, "<title>", "</title>")
        title = title_parts[0].strip()
        content_parts = ParserManager.get_between(data, "<p>", "</p>")
        content = "\n".join([p.strip() for p in content_parts])
        picture_parts = ParserManager.get_between(data, 'src="images/', '.jpg"')
        picture_url = ""
        if len(picture_parts) >= 2:
            picture_url = (
                "https://www.musculaction.com/images/" + picture_parts[1] + ".jpg"
            )
        return {"title": title, "content": content, "pictures_urls": [picture_url]}

    def run(self):
        urls = self.scrap_link()

        articles = []
        for url in urls:
            article = self.scrap_article(url)
            articles.append(article)
        DataManager.save_json(articles, "dataset/musculaction.json")


if __name__ == "__main__":
    DataManager.create_directory("dataset")
    ScrapperMusculaction().run()
