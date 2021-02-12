import requests
import json


class NewsApi:

    def __init__(self):
        self.category = "general"
        self.country = "in"
        self.url = 'http://newsapi.org/v2/top-headlines?' \
                   'country={}&category={}&pageSize=100' \
                   '&apiKey=d96a0e4156864617a36161e44c25b906'.format(self.country, self.category)

    @staticmethod
    def get_static_news(query, language, sort_by):
        url = "https://newsapi.org/v2/everything?q={}&language={}&sortBy={}&pageSize=100&a" \
              "piKey=d96a0e4156864617a36161e44c25b906" \
            .format(query, language, sort_by)
        response = requests.get(url)
        response = response.json()
        if response['status'] == 'ok':
            return response
        else:
            return {"articles": []}

    def get_news(self):
        response = requests.get(self.url)
        print(self.url)
        response = response.json()

        if response['status'] == 'ok':
            return response
        else:
            return {"articles": []}

    def set_country_or_category(self, value):
        country_list = "ae ar at au be bg br ca ch cn co cu cz de eg " \
                       "fr gb gr hk hu id ie il in it jp kr lt lv ma " \
                       "mx my ng nl no nz ph pl pt ro rs ru sa se sg " \
                       "si sk th tr tw ua us ve za".split(" ")
        category_list = "business entertainment general health science sports technology".split(" ")
        if value in country_list:
            self.country = value
        elif value in category_list:
            self.category = value
        else:
            pass
        self.url = 'http://newsapi.org/v2/top-headlines?' \
                   'country={}&category={}&pageSize=100' \
                   '&apiKey=d96a0e4156864617a36161e44c25b906'.format(self.country, self.category)


if __name__ == '__main__':
    pass
