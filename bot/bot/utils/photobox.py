class PhotoBox:
    @staticmethod
    def get_user_avatar(id: str) -> str:
        return f"https://photobox.cardboard.ink/user/avatar/{id}"
    @staticmethod
    def get_user_banner(id: str) -> str:
        return f"https://photobox.cardboard.ink/user/banner/{id}"
    @staticmethod
    def get_server_icon(id: str) -> str:
        return f"https://photobox.cardboard.ink/server/icon/{id}"
    @staticmethod
    def get_server_banner(id: str) -> str:
        return f"https://photobox.cardboard.ink/server/banner/{id}"
    @staticmethod
    def get_bot_icon(id: str) -> str:
        return f"https://photobox.cardboard.ink/bot/icon/{id}"
    @staticmethod
    def get_bot_banner(id: str) -> str:
        return f"https://photobox.cardboard.ink/bot/banner/{id}"
