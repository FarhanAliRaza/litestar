from typing import Any, Dict, List, Optional

from openapi_schema_pydantic import Example, ExternalDocumentation
from pydantic.fields import Field, Undefined
from pydantic.typing import NoArgAnyCallable


def Parameter(  # pylint: disable=too-many-locals
    *,
    header: Optional[str] = None,
    cookie: Optional[str] = None,
    query: Optional[str] = None,
    examples: Optional[List[Example]] = None,
    external_docs: Optional[ExternalDocumentation] = None,
    content_encoding: Optional[str] = None,
    required: bool = True,
    default: Any = Undefined,
    default_factory: Optional[NoArgAnyCallable] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    const: Optional[bool] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    multiple_of: Optional[float] = None,
    min_items: Optional[int] = None,
    max_items: Optional[int] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None
) -> Any:
    """
    Creates a pydantic FieldInfo instance with an extra kwargs,
    used for both parameter parsing and OpenAPI schema generation.
    """
    extra: Dict[str, Any] = {}
    extra.update(header=header)
    extra.update(cookie=cookie)
    extra.update(query=query)
    extra.update(required=required)
    extra.update(examples=examples)
    extra.update(external_docs=external_docs)
    extra.update(content_encoding=content_encoding)
    return Field(
        default,
        default_factory=default_factory,
        alias="",
        title=title,
        description=description,
        const=const,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        multiple_of=multiple_of,
        min_items=min_items,
        max_items=max_items,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        **extra,
    )
