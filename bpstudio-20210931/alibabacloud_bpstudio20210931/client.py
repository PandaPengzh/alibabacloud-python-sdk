# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bpstudio20210931 import models as bpstudio_20210931_models
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
        self._endpoint = self.get_endpoint('bpstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_resource_group_with_options(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        tmp_req: bpstudio_20210931_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        if not UtilClient.is_unset(tmp_req.variables):
            request.variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        body = {}
        if not UtilClient.is_unset(request.area_id):
            body['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        if not UtilClient.is_unset(request.instances_shrink):
            body['Instances'] = request.instances_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.variables_shrink):
            body['Variables'] = request.variables_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        if not UtilClient.is_unset(tmp_req.variables):
            request.variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        body = {}
        if not UtilClient.is_unset(request.area_id):
            body['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        if not UtilClient.is_unset(request.instances_shrink):
            body['Instances'] = request.instances_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.variables_shrink):
            body['Variables'] = request.variables_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: bpstudio_20210931_models.CreateApplicationRequest,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: bpstudio_20210931_models.CreateApplicationRequest,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def deploy_application_with_options(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeployApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_application_with_options(request, runtime)

    async def deploy_application_async(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_application_with_options_async(request, runtime)

    def execute_operation_async_with_options(
        self,
        tmp_req: bpstudio_20210931_models.ExecuteOperationASyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ExecuteOperationASyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteOperationASync',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ExecuteOperationASyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_operation_async_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.ExecuteOperationASyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ExecuteOperationASyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteOperationASync',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ExecuteOperationASyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_operation_async(
        self,
        request: bpstudio_20210931_models.ExecuteOperationASyncRequest,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_operation_async_with_options(request, runtime)

    async def execute_operation_async_async(
        self,
        request: bpstudio_20210931_models.ExecuteOperationASyncRequest,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_operation_async_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_execute_operation_result_with_options(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation_id):
            body['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExecuteOperationResult',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetExecuteOperationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execute_operation_result_with_options_async(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation_id):
            body['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExecuteOperationResult',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetExecuteOperationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execute_operation_result(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_execute_operation_result_with_options(request, runtime)

    async def get_execute_operation_result_async(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_execute_operation_result_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def list_application_with_options(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_application_with_options(request, runtime)

    async def list_application_async(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_application_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_template_with_options(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_list):
            body['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_with_options_async(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_list):
            body['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_template_with_options(request, runtime)

    async def list_template_async(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_template_with_options_async(request, runtime)

    def release_application_with_options(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReleaseApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReleaseApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_application(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_application_with_options(request, runtime)

    async def release_application_async(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_application_with_options_async(request, runtime)

    def validate_application_with_options(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValidateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValidateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_application(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_application_with_options(request, runtime)

    async def validate_application_async(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_application_with_options_async(request, runtime)

    def valuate_application_with_options(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValuateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def valuate_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValuateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valuate_application(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.valuate_application_with_options(request, runtime)

    async def valuate_application_async(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.valuate_application_with_options_async(request, runtime)
