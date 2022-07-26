"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.  # noqa: E501

    The version of the OpenAPI document: 1.0.172
    Contact: support@infobip.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from infobip_api_client.api_client import ApiClient, Endpoint as _Endpoint
from infobip_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from infobip_api_client.model.sms_api_exception import SmsApiException
from infobip_api_client.model.sms_bulk_request import SmsBulkRequest
from infobip_api_client.model.sms_bulk_response import SmsBulkResponse
from infobip_api_client.model.sms_bulk_status_response import SmsBulkStatusResponse
from infobip_api_client.model.sms_update_status_request import SmsUpdateStatusRequest


class ScheduledSmsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_scheduled_sms_messages(self, bulk_id, **kwargs):
            """Get scheduled SMS messages  # noqa: E501

            See the status and the scheduled time of your SMS messages.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_scheduled_sms_messages(bulk_id, async_req=True)
            >>> result = thread.get()

            Args:
                bulk_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SmsBulkResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["bulk_id"] = bulk_id
            return self.call_with_http_info(**kwargs)

        self.get_scheduled_sms_messages = _Endpoint(
            settings={
                "response_type": (SmsBulkResponse,),
                "auth": ["APIKeyHeader", "Basic", "IBSSOTokenHeader", "OAuth2"],
                "endpoint_path": "/sms/1/bulks",
                "operation_id": "get_scheduled_sms_messages",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "bulk_id",
                ],
                "required": [
                    "bulk_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "bulk_id": (str,),
                },
                "attribute_map": {
                    "bulk_id": "bulkId",
                },
                "location_map": {
                    "bulk_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "application/xml"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_scheduled_sms_messages,
        )

        def __get_scheduled_sms_messages_status(self, bulk_id, **kwargs):
            """Get scheduled SMS messages status  # noqa: E501

            See the status of scheduled messages.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_scheduled_sms_messages_status(bulk_id, async_req=True)
            >>> result = thread.get()

            Args:
                bulk_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SmsBulkStatusResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["bulk_id"] = bulk_id
            return self.call_with_http_info(**kwargs)

        self.get_scheduled_sms_messages_status = _Endpoint(
            settings={
                "response_type": (SmsBulkStatusResponse,),
                "auth": ["APIKeyHeader", "Basic", "IBSSOTokenHeader", "OAuth2"],
                "endpoint_path": "/sms/1/bulks/status",
                "operation_id": "get_scheduled_sms_messages_status",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "bulk_id",
                ],
                "required": [
                    "bulk_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "bulk_id": (str,),
                },
                "attribute_map": {
                    "bulk_id": "bulkId",
                },
                "location_map": {
                    "bulk_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "application/xml"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_scheduled_sms_messages_status,
        )

        def __reschedule_sms_messages(self, bulk_id, **kwargs):
            """Reschedule SMS messages  # noqa: E501

            Change the date and time for sending scheduled messages.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.reschedule_sms_messages(bulk_id, async_req=True)
            >>> result = thread.get()

            Args:
                bulk_id (str):

            Keyword Args:
                sms_bulk_request (SmsBulkRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SmsBulkResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["bulk_id"] = bulk_id
            return self.call_with_http_info(**kwargs)

        self.reschedule_sms_messages = _Endpoint(
            settings={
                "response_type": (SmsBulkResponse,),
                "auth": ["APIKeyHeader", "Basic", "IBSSOTokenHeader", "OAuth2"],
                "endpoint_path": "/sms/1/bulks",
                "operation_id": "reschedule_sms_messages",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "bulk_id",
                    "sms_bulk_request",
                ],
                "required": [
                    "bulk_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "bulk_id": (str,),
                    "sms_bulk_request": (SmsBulkRequest,),
                },
                "attribute_map": {
                    "bulk_id": "bulkId",
                },
                "location_map": {
                    "bulk_id": "query",
                    "sms_bulk_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "application/xml"],
                "content_type": ["application/json", "application/xml"],
            },
            api_client=api_client,
            callable=__reschedule_sms_messages,
        )

        def __update_scheduled_sms_messages_status(self, bulk_id, **kwargs):
            """Update scheduled SMS messages status  # noqa: E501

            Change status or completely cancel sending of scheduled messages.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_scheduled_sms_messages_status(bulk_id, async_req=True)
            >>> result = thread.get()

            Args:
                bulk_id (str):

            Keyword Args:
                sms_update_status_request (SmsUpdateStatusRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SmsBulkStatusResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["bulk_id"] = bulk_id
            return self.call_with_http_info(**kwargs)

        self.update_scheduled_sms_messages_status = _Endpoint(
            settings={
                "response_type": (SmsBulkStatusResponse,),
                "auth": ["APIKeyHeader", "Basic", "IBSSOTokenHeader", "OAuth2"],
                "endpoint_path": "/sms/1/bulks/status",
                "operation_id": "update_scheduled_sms_messages_status",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "bulk_id",
                    "sms_update_status_request",
                ],
                "required": [
                    "bulk_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "bulk_id": (str,),
                    "sms_update_status_request": (SmsUpdateStatusRequest,),
                },
                "attribute_map": {
                    "bulk_id": "bulkId",
                },
                "location_map": {
                    "bulk_id": "query",
                    "sms_update_status_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "application/xml"],
                "content_type": ["application/json", "application/xml"],
            },
            api_client=api_client,
            callable=__update_scheduled_sms_messages_status,
        )
