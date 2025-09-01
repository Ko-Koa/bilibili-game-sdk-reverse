from typing import TypeAlias, Literal, TypedDict, Any, NotRequired

RequestMethod: TypeAlias = Literal["GET", "POST", "PUT", "DELETE"]


class BiliRequest(TypedDict):
    param: NotRequired[dict[str, Any] | None]
    data: NotRequired[dict[str, Any] | str | None]
    json: NotRequired[dict[str, Any] | None]
    headers: NotRequired[dict[str, Any] | None]
    cookies: NotRequired[dict[str, Any] | None]
    proxy: NotRequired[dict[str, Any] | None]
    timeout: NotRequired[int | None]
    verify: NotRequired[bool | None]
