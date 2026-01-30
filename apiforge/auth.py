class BearerAuth:
    def __init__(self, token: str):
        self.token = token

    def headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.token}"
        }
