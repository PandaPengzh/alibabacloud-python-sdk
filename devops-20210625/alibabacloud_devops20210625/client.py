# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devops20210625 import models as devops_20210625_models
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
        self._endpoint = self.get_endpoint('devops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_flow_tag(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_with_options(organization_id, request, headers, runtime)

    async def create_flow_tag_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_flow_tag_with_options_async(organization_id, request, headers, runtime)

    def create_flow_tag_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_tag_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_tag_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_group_with_options(organization_id, request, headers, runtime)

    async def create_flow_tag_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_flow_tag_group_with_options_async(organization_id, request, headers, runtime)

    def create_flow_tag_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_host_group_with_options(organization_id, request, headers, runtime)

    async def create_host_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_host_group_with_options_async(organization_id, request, headers, runtime)

    def create_host_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_member_with_options(organization_id, resource_type, resource_id, request, headers, runtime)

    async def create_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_member_with_options_async(organization_id, resource_type, resource_id, request, headers, runtime)

    def create_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ssh_key(
        self,
        organization_id: str,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(organization_id, headers, runtime)

    async def create_ssh_key_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ssh_key_with_options_async(organization_id, headers, runtime)

    def create_ssh_key_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/sshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ssh_key_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/sshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_variable_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_variable_group_with_options(organization_id, request, headers, runtime)

    async def create_variable_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_variable_group_with_options_async(organization_id, request, headers, runtime)

    def create_variable_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_variable_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_tag(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_with_options(organization_id, id, headers, runtime)

    async def delete_flow_tag_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_flow_tag_with_options_async(organization_id, id, headers, runtime)

    def delete_flow_tag_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tags/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_tag_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tags/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_tag_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_group_with_options(organization_id, id, headers, runtime)

    async def delete_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_flow_tag_group_with_options_async(organization_id, id, headers, runtime)

    def delete_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_host_group_with_options(organization_id, id, headers, runtime)

    async def delete_host_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_host_group_with_options_async(organization_id, id, headers, runtime)

    def delete_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    async def delete_pipeline_async(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_with_options_async(organization_id, pipeline_id, headers, runtime)

    def delete_pipeline_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_member_with_options(organization_id, resource_type, resource_id, account_id, headers, runtime)

    async def delete_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_member_with_options_async(organization_id, resource_type, resource_id, account_id, headers, runtime)

    def delete_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members/{account_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members/{account_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_variable_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_variable_group_with_options(organization_id, id, headers, runtime)

    async def delete_variable_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_variable_group_with_options_async(organization_id, id, headers, runtime)

    def delete_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups/{id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def frozen_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.frozen_workspace_with_options(workspace_id, headers, runtime)

    async def frozen_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.frozen_workspace_with_options_async(workspace_id, headers, runtime)

    def frozen_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{workspace_id}/frozen',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def frozen_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{workspace_id}/frozen',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_tag_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_flow_tag_group_with_options(organization_id, id, headers, runtime)

    async def get_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_flow_tag_group_with_options_async(organization_id, id, headers, runtime)

    def get_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_host_group_with_options(organization_id, id, headers, runtime)

    async def get_host_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_host_group_with_options_async(organization_id, id, headers, runtime)

    def get_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetHostGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetHostGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organization_member(
        self,
        organization_id: str,
        account_id: str,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_member_with_options(organization_id, account_id, headers, runtime)

    async def get_organization_member_async(
        self,
        organization_id: str,
        account_id: str,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_organization_member_with_options_async(organization_id, account_id, headers, runtime)

    def get_organization_member_with_options(
        self,
        organization_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/members/{account_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organization_member_with_options_async(
        self,
        organization_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/members/{account_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    async def get_pipeline_async(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(organization_id, pipeline_id, headers, runtime)

    def get_pipeline_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    async def get_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def get_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_info(
        self,
        organization_id: str,
        project_id: str,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_info_with_options(organization_id, project_id, headers, runtime)

    async def get_project_info_async(
        self,
        organization_id: str,
        project_id: str,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_info_with_options_async(organization_id, project_id, headers, runtime)

    def get_project_info_with_options(
        self,
        organization_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/project/{project_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_info_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/project/{project_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def get_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def get_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_variable_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_variable_group_with_options(organization_id, id, headers, runtime)

    async def get_variable_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_variable_group_with_options_async(organization_id, id, headers, runtime)

    def get_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_id, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{workspace_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{workspace_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_tag_groups(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_tag_groups_with_options(organization_id, headers, runtime)

    async def list_flow_tag_groups_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_tag_groups_with_options_async(organization_id, headers, runtime)

    def list_flow_tag_groups_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowTagGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListFlowTagGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_tag_groups_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowTagGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListFlowTagGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_host_groups_with_options(organization_id, request, headers, runtime)

    async def list_host_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_host_groups_with_options_async(organization_id, request, headers, runtime)

    def list_host_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_members(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organization_members_with_options(organization_id, request, headers, runtime)

    async def list_organization_members_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_organization_members_with_options_async(organization_id, request, headers, runtime)

    def list_organization_members_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_members_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_runs(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_runs_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_runs_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_runs_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_runs_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
    ) -> devops_20210625_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(organization_id, request, headers, runtime)

    async def list_pipelines_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
    ) -> devops_20210625_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(organization_id, request, headers, runtime)

    def list_pipelines_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_members(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_members_with_options(organization_id, project_id, request, headers, runtime)

    async def list_project_members_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_members_with_options_async(organization_id, project_id, request, headers, runtime)

    def list_project_members_with_options(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/projects/{project_id}/listMembers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_members_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/projects/{project_id}/listMembers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_members(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_members_with_options(organization_id, resource_type, resource_id, headers, runtime)

    async def list_resource_members_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_members_with_options_async(organization_id, resource_type, resource_id, headers, runtime)

    def list_resource_members_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_members_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_connections(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_connections_with_options(organization_id, request, headers, runtime)

    async def list_service_connections_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_connections_with_options_async(organization_id, request, headers, runtime)

    def list_service_connections_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/serviceConnections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_connections_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/serviceConnections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variable_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_variable_groups_with_options(organization_id, request, headers, runtime)

    async def list_variable_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_variable_groups_with_options_async(organization_id, request, headers, runtime)

    def list_variable_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variable_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: devops_20210625_models.ListWorkspacesRequest,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: devops_20210625_models.ListWorkspacesRequest,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: devops_20210625_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: devops_20210625_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_pipeline_job_run_with_options(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    async def log_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_pipeline_job_run_with_options_async(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    def log_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipeline/{pipeline_id}/pipelineRun/{pipeline_run_id}/job/{job_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipeline/{pipeline_id}/pipelineRun/{pipeline_run_id}/job/{job_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def log_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def log_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/machine/{machine_sn}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/machine/{machine_sn}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pass_pipeline_validate(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pass_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def pass_pipeline_validate_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pass_pipeline_validate_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def pass_pipeline_validate_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/pass',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def pass_pipeline_validate_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/pass',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refuse_pipeline_validate(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refuse_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def refuse_pipeline_validate_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refuse_pipeline_validate_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def refuse_pipeline_validate_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/refuse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def refuse_pipeline_validate_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/refuse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_workspace_with_options(workspace_id, headers, runtime)

    async def release_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_workspace_with_options_async(workspace_id, headers, runtime)

    def release_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{workspace_id}/release',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{workspace_id}/release',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_ssh_key(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_ssh_key_with_options(organization_id, headers, runtime)

    async def reset_ssh_key_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reset_ssh_key_with_options_async(organization_id, headers, runtime)

    def reset_ssh_key_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/sshKey',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_ssh_key_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/sshKey',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def resume_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def resume_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def retry_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def retry_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def retry_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def retry_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/machine/{machine_sn}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/machine/{machine_sn}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def skip_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.skip_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def skip_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def skip_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.skip_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def skip_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/machine/{machine_sn}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/machine/{machine_sn}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_run_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def start_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_pipeline_run_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def start_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/{organization_id}/pipelines/{pipeline_id}/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/{organization_id}/pipelines/{pipeline_id}/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def stop_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def stop_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/jobs/{job_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    async def stop_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_pipeline_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def stop_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/pipelineRuns/{pipeline_run_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def stop_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def stop_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/deploy/{deploy_order_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_tag(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_with_options(organization_id, id, request, headers, runtime)

    async def update_flow_tag_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_flow_tag_with_options_async(organization_id, id, request, headers, runtime)

    def update_flow_tag_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tags/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_tag_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tags/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_tag_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_group_with_options(organization_id, id, request, headers, runtime)

    async def update_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_flow_tag_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/flow/tagGroups/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_host_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_host_group_with_options(organization_id, id, request, headers, runtime)

    async def update_host_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_host_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/hostGroups/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_base_info(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_base_info_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def update_pipeline_base_info_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_base_info_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def update_pipeline_base_info_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['envId'] = request.env_id
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.tag_list):
            query['tagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineBaseInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/baseInfo',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_base_info_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['envId'] = request.env_id
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.tag_list):
            query['tagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineBaseInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/pipelines/{pipeline_id}/baseInfo',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_member_with_options(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    async def update_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_member_with_options_async(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    def update_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members/{account_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/{resource_type}/{resource_id}/members/{account_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_variable_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_variable_group_with_options(organization_id, id, request, headers, runtime)

    async def update_variable_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_variable_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{organization_id}/variableGroups/{id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )
