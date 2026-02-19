"""
FastAPI applications module.
"""
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Type, Union

from fastapi.routing import APIRouter
from fastapi.types import ASGIApp


class FastAPI:
    """
    The main FastAPI class.
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[Any]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = None,
        **extra: Any,
    ) -> None:
        self.debug = debug
        self.title = title
        self.description = description
        self.version = version
        self.openapi_url = openapi_url
        self.openapi_tags = openapi_tags
        self.servers = servers
        self.docs_url = docs_url
        self.redoc_url = redoc_url
        self.swagger_ui_oauth2_redirect_url = swagger_ui_oauth2_redirect_url
        self.extra = extra
        self.routes = routes or []
        self.router = APIRouter()

    def add_route(
        self,
        path: str,
        route: Any,
        *,
        include_in_schema: bool = True,
    ) -> None:
        self.router.add_route(path, route, include_in_schema=include_in_schema)

    def include_router(
        self,
        router: Any,
        *,
        prefix: str = "",
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[Any]] = None,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        default_response_class: Optional[Type[Any]] = None,
        include_in_schema: bool = True,
    ) -> None:
        self.router.include_router(
            router,
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            responses=responses,
            default_response_class=default_response_class,
            include_in_schema=include_in_schema,
        )
