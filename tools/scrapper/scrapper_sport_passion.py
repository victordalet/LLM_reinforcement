from src.commons.data_manager import DataManager
from src.commons.parser_manager import ParserManager
from src.commons.request_manager import RequestManager


class ScrapperSportPassion:

    @staticmethod
    def scrap_link():
        url = "https://www.sport-passion.fr/categories/conseils-fitness-minceur.php"
        data = RequestManager.get(url)

        urls = ParserManager.get_between(data, "/conseils/", ".php")
        for i in range(len(urls)):
            urls[i] = "https://www.sport-passion.fr/conseils/" + urls[i] + ".php"
        return urls

    @staticmethod
    def scrap_article(url: str) -> dict:
        data = RequestManager.get(url)
        title = ParserManager.get_between(data, "<title>", "</title>")[0]
        content_parts = ParserManager.get_between(data, "<p>", "</p>")
        for i in range(len(content_parts)):
            content_parts[i] = ParserManager.strip_tags(content_parts[i])
        content = "\n".join(content_parts)
        pictures_urls = ParserManager.get_between(
            data, "pictures/", '"', filter_to_remove="/"
        )
        for i in range(len(pictures_urls)):
            full_pic_url = "https://www.sport-passion.fr/pictures/" + pictures_urls[i]
            pictures_urls[i] = full_pic_url
        return {"title": title, "content": content, "pictures_urls": pictures_urls}

    def run(self):
        urls = self.scrap_link()
        articles = []
        for url in urls:
            article = self.scrap_article(url)
            articles.append(article)
        DataManager.save_json(articles, "dataset/sport_passion_articles.json")


if __name__ == "__main__":
    DataManager.create_directory("dataset")
    ScrapperSportPassion().run()
