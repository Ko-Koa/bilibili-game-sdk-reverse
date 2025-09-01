import json


class Response(object):
    def __init__(
        self,
        response,
        url: str,
        status_code: int,
        content: bytes,
        headers: dict,
        cookies: dict,
        encoding: str,
    ) -> None:
        self.response = response
        self.url = url
        self.status_code = status_code
        self.content = content
        self.headers = headers
        self.cookies = cookies
        self.encoding = encoding
        self.encoding_errors = "strict"
        self._html = None
        self._text = None

    @property
    def text(self):
        if self._text is None:
            if not self.content:
                self._text = ""
            else:
                self._text = self.content.decode(
                    self.encoding, errors=self.encoding_errors
                )
        return self._text

    def json(self):
        return json.loads(self.text)
