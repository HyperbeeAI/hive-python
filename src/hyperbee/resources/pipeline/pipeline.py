# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from openai import _legacy_response
from openai._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from openai._utils import required_args, maybe_transform
from openai._compat import cached_property
from openai._resource import SyncAPIResource, AsyncAPIResource
from openai._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from openai._streaming import Stream, AsyncStream
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionToolParam,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    completion_create_params,
)
from openai._base_client import (
    make_request_options,
)

__all__ = ["Pipeline"]


class Pipeline(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        return CompletionsWithRawResponse(self)
    
    
    @required_args(["task_id", "query", "candidate_labels"])
    def __call__(
        self,
        *,
        model: Union[
            str,
            Literal[
                "hive",
            ],
        ],
        task_id: Literal["classification"] | NotGiven = NOT_GIVEN,
        query: Optional[str] | NotGiven = NOT_GIVEN,
        candidate_labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
                  
        return self._post(
            "/pipeline",
            body=maybe_transform(
                {
                    "messages": [{"role": "user","content": ""}],
                    "model": model,
                    "task_id": task_id,
                    "query": query,
                    "candidate_labels": candidate_labels,
                },
                completion_create_params.CompletionCreateParams,
            ),
            
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )