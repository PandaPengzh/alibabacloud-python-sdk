# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiplugin20220112 import models as pai_plugin_20220112_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('paiplugin', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_signature(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        """
        注册签名。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_signature_with_options(request, headers, runtime)

    async def create_signature_async(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        """
        注册签名。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_signature_with_options_async(request, headers, runtime)

    def create_signature_with_options(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_signature_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        """
        注册模板。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        """
        注册模板。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_signature(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        """
        删除签名。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_signature_with_options(id, headers, runtime)

    async def delete_signature_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        """
        删除签名。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_signature_with_options_async(id, headers, runtime)

    def delete_signature_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_signature_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        """
        删除模板
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(id, headers, runtime)

    async def delete_template_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        """
        删除模板
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(id, headers, runtime)

    def delete_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_config(self) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        """
        获取短信配置。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_message_config_with_options(headers, runtime)

    async def get_message_config_async(self) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        """
        获取短信配置。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_message_config_with_options_async(headers, runtime)

    def get_message_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMessageConfig',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/messageConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetMessageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMessageConfig',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/messageConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetMessageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_signature(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        """
        获取签名详情。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_signature_with_options(id, headers, runtime)

    async def get_signature_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        """
        获取签名详情。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_signature_with_options_async(id, headers, runtime)

    def get_signature_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_signature_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        """
        获取模板详情。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(id, headers, runtime)

    async def get_template_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        """
        获取模板详情。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(id, headers, runtime)

    def get_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(self) -> pai_plugin_20220112_models.GetUserResponse:
        """
        获取账号状态。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(headers, runtime)

    async def get_user_async(self) -> pai_plugin_20220112_models.GetUserResponse:
        """
        获取账号状态。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(headers, runtime)

    def get_user_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetUserResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetUserResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message_metrics(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        """
        获取短信发送统计列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_message_metrics_with_options(request, headers, runtime)

    async def list_message_metrics_async(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        """
        获取短信发送统计列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_message_metrics_with_options_async(request, headers, runtime)

    def list_message_metrics_with_options(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessageMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessageMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_metrics_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessageMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessageMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messages(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        """
        查询短信发送详情列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_messages_with_options(request, headers, runtime)

    async def list_messages_async(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        """
        查询短信发送详情列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_messages_with_options_async(request, headers, runtime)

    def list_messages_with_options(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datetime):
            query['Datetime'] = request.datetime
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messages_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datetime):
            query['Datetime'] = request.datetime
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_signatures(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        """
        获取签名列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_signatures_with_options(request, headers, runtime)

    async def list_signatures_async(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        """
        获取签名列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_signatures_with_options_async(request, headers, runtime)

    def list_signatures_with_options(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSignatures',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_signatures_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSignatures',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        """
        获取模板列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        """
        获取模板列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        """
        发送短信。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_message_with_options(request, headers, runtime)

    async def send_message_async(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        """
        发送短信。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_message_with_options_async(request, headers, runtime)

    def send_message_with_options(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.out_ids):
            body['OutIds'] = request.out_ids
        if not UtilClient.is_unset(request.phone_numbers):
            body['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.schedule_id):
            body['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.sms_up_extend_codes):
            body['SmsUpExtendCodes'] = request.sms_up_extend_codes
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_params):
            body['TemplateParams'] = request.template_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.out_ids):
            body['OutIds'] = request.out_ids
        if not UtilClient.is_unset(request.phone_numbers):
            body['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.schedule_id):
            body['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.sms_up_extend_codes):
            body['SmsUpExtendCodes'] = request.sms_up_extend_codes
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_params):
            body['TemplateParams'] = request.template_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_report(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        """
        短信回执。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sms_report_with_options(request, headers, runtime)

    async def sms_report_async(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        """
        短信回执。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sms_report_with_options_async(request, headers, runtime)

    def sms_report_with_options(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsReport',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_report_with_options_async(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsReport',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_up(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        """
        短信上行。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sms_up_with_options(request, headers, runtime)

    async def sms_up_async(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        """
        短信上行。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sms_up_with_options_async(request, headers, runtime)

    def sms_up_with_options(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsUp',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsUpResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_up_with_options_async(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsUp',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsUpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_report_url(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        """
        更新回执Url。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_report_url_with_options(request, headers, runtime)

    async def update_report_url_async(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        """
        更新回执Url。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_report_url_with_options_async(request, headers, runtime)

    def update_report_url_with_options(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/reportUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateReportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_report_url_with_options_async(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/reportUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateReportUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_upload_url(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        """
        更新上行Url。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_upload_url_with_options(request, headers, runtime)

    async def update_upload_url_async(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        """
        更新上行Url。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_upload_url_with_options_async(request, headers, runtime)

    def update_upload_url_with_options(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUploadUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/uploadUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_upload_url_with_options_async(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUploadUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/uploadUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )
