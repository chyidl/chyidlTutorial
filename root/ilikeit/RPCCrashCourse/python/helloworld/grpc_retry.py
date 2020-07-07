# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import time
import logging
from decouple import config
from grpc import StatusCode
from grpc._channel import _Rendezvous, _UnaryUnaryMultiCallable


logger = logging.getLogger(__name__)


# The maximum number of retries
_MAX_RETRIES_BY_CODE = {
    # Internal errors. This means that some invariants expected by the
    # underlying system have been broken. This error code is reserved for
    # serious errors
    StatusCode.INTERNAL: config('GRPC_RETRY_INTERNAL', default=1, cast=int),
    # The operation was aborted, typically due to a concurrency issue such as a
    # sequencer check failure or transaction abort. See the guidelines above for
    # deciding between FAILED_PRECONDITION, ABORTED, and UNAVAILABLE.
    StatusCode.ABORTED: config('GRPC_RETRY_ABPRTED', default=3, cast=int),
    # The service is currently unavailble. this is most likely a transient
    # condition, which can be corrected by retrying with a backoff. Not that it
    # is not always safe to retry non-idempotent operations.
    StatusCode.UNAVAILABLE: config('GRPC_RETRY_UNAVAILABLE', default=5,
        cast=int),
    # The deadline expired before the operation could complete. For operations
    # that change the state of the system, this error may be returned even if
    # the operation has completed successfully. For example, a successful
    # response from a server could have been delayed long.
    StatusCode.DEADLINE_EXCEEDED: config('GRPC_RETRY_DEADLINE_EXCEEDED',
        default=5, cast=int),
}

# The minimum seconds (float) of sleeping
_MIN_SLEEPING = config('GRPC_RETRY_MIN_SLEEPING', default=0.015625, cast=float)
_MAX_SLEEPING = config('GRPC_RETRY_MAX_SLEEPING', default=1.0, cast=float)


class RetriesExceeded(Exception):
    """docstring for RetriesExceeded"""
    pass


def retry(f, transactional=False):
    def wraps(*args, **kwargs):
        retries = 0
        while True:
            try:
                return f(*args, **kwargs)
            #except _Rendezvous as e:
            except Exception as e:
                code = e.code()

                max_retries = _MAX_RETRIES_BY_CODE.get(code)
                if max_retries is None or transactional and code == StatusCode.ABABORTED:
                    raise

                if retries > max_retries:
                    raise RetriesExceeded(e)

                backoff = min(_MIN_SLEEPING * 2 ** retries, _MAX_SLEEPING)
                logger.error("sleeping %r for %r before retrying failed request...", backoff, code)

                retries += 1
                time.sleep(backoff)
    return wraps


def retrying_stub_methods(obj):
    for key, attr in obj.__dict__.items():
        if isinstance(attr, _UnaryUnaryMultiCallable):
            setattr(obj, key, retry(attr))

