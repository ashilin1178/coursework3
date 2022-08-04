import json
import string


class PostsDAO:

    def load_data(self):
        """
        загружает все посты из файла data.json
        :return:
        """
        with open("data/data.json", "r", encoding="utf-8") as file:
            posts = json.load(file)
        return posts

    def get_all(self):
        """
        выводит все посты
        :return:
        """
        return self.load_data()

    def get_posts_by_user(self, poster_name):
        """
        возвращает все посты автора
        :param poster_name:
        :return:
        """
        posts = self.load_data()
        posts_user = []

        try:
            for post in posts:
                if poster_name == post['poster_name']:
                    posts_user.append(post)

            return posts_user
        except ValueError:
            "Такого пользователя не существует"

    def search_for_posts(self, query):
        """
        возвращает список постов по ключевому слову
        :param query:
        :return:
        """
        posts = self.load_data()
        query_posts = []
        query_lower = query.lower()

        for post in posts:
            # переводим в нижний регистр, удаляем знаки препинания из поста и преобразуем строку в список разделитель
            # пробел
            words_post = post["content"].lower().translate(str.maketrans('', '', string.punctuation)).split(" ")
            if query_lower in words_post:
                query_posts.append(post)

        return query_posts
