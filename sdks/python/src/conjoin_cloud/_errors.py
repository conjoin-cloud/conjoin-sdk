from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ValidationFieldError:
    message: str
    path: str


class ConjoinError(Exception):
    status: int
    code: str
    param: str | None
    details: Any
    request_id: str | None

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status: int = 0,
        param: str | None = None,
        details: Any = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        self.param = param
        self.details = details
        self.request_id = request_id


class ConjoinApiError(ConjoinError):
    pass


class ConjoinAuthenticationError(ConjoinApiError):
    pass


class ConjoinPermissionDeniedError(ConjoinApiError):
    pass


class ConjoinNotFoundError(ConjoinApiError):
    pass


class ConjoinConflictError(ConjoinApiError):
    pass


class ConjoinValidationError(ConjoinApiError):
    errors: tuple[ValidationFieldError, ...]

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status: int,
        errors: Sequence[ValidationFieldError] = (),
        param: str | None = None,
        details: Any = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status=status,
            param=param,
            details=details,
            request_id=request_id,
        )
        self.errors = tuple(errors)


class ConjoinRateLimitError(ConjoinApiError):
    retry_after: float | None

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status: int,
        retry_after: float | None = None,
        param: str | None = None,
        details: Any = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status=status,
            param=param,
            details=details,
            request_id=request_id,
        )
        self.retry_after = retry_after


class ConjoinInternalServerError(ConjoinApiError):
    pass


class ConjoinResponseError(ConjoinError):
    def __init__(self, message: str, *, status: int, request_id: str | None = None) -> None:
        super().__init__(message, code="invalid_response", status=status, request_id=request_id)


class ConjoinNetworkError(ConjoinError):
    def __init__(self, message: str, *, request_id: str | None = None) -> None:
        super().__init__(message, code="network_error", request_id=request_id)


class ConjoinTimeoutError(ConjoinError):
    def __init__(self, message: str, *, request_id: str | None = None) -> None:
        super().__init__(message, code="timeout_error", request_id=request_id)


class ConjoinConfigurationError(ConjoinError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="configuration_error")


class ConjoinStorageError(ConjoinError):
    storage_url: str
    upload_mode: str | None

    def __init__(
        self,
        message: str,
        *,
        status: int,
        storage_url: str,
        upload_mode: str | None = None,
    ) -> None:
        super().__init__(message, code="storage_error", status=status)
        self.storage_url = storage_url
        self.upload_mode = upload_mode
