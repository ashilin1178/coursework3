import json


class CommentssDAO:

    def load_data(self):
        """
        загружает все комментарии из файла comments.json
        :return:
        """
        with open("data/comments.json", "r", encoding="utf-8") as file:
            comments = json.load(file)
        return comments

    def get_comments_by_post_id(self, post_id):
        """
        возвращает все комментарии поста
        :param post_id:
        :return:
        """
        comments = self.load_data()
        comments_post = []

        try:
            for comment in comments:
                if post_id == comment["post_id"]:
                    comments_post.append(comment)

            return comments_post
        except ValueError:
            "К этому посту еще нет комментариев"
