# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_sls.client import Client as GatewayClientClient
from alibabacloud_sls20201230 import models as sls_20201230_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client: SPIClient = None

    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-southeast-1': 'sls.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou': 'sls.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'sls.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'sls.cn-huhehaote.aliyuncs.com',
            'cn-shanghai': 'sls.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'sls.cn-shenzhen.aliyuncs.com',
            'cn-zhangjiakou': 'sls.cn-zhangjiakou.aliyuncs.com',
            'eu-central-1': 'sls.eu-central-1.aliyuncs.com'
        }

    def create_consumer_group(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(project, logstore, request, headers, runtime)

    async def create_consumer_group_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_consumer_group_with_options_async(project, logstore, request, headers, runtime)

    def create_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_log_store(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_log_store_with_options(project, request, headers, runtime)

    async def create_log_store_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_log_store_with_options_async(project, request, headers, runtime)

    def create_log_store_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def create_log_store_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_project(
        self,
        request: sls_20201230_models.CreateProjectRequest,
    ) -> sls_20201230_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: sls_20201230_models.CreateProjectRequest,
    ) -> sls_20201230_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: sls_20201230_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: sls_20201230_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_saved_search(
        self,
        request: sls_20201230_models.CreateSavedSearchRequest,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_saved_search_with_options(request, headers, runtime)

    async def create_saved_search_async(
        self,
        request: sls_20201230_models.CreateSavedSearchRequest,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_saved_search_with_options_async(request, headers, runtime)

    def create_saved_search_with_options(
        self,
        request: sls_20201230_models.CreateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def create_saved_search_with_options_async(
        self,
        request: sls_20201230_models.CreateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(project, logstore, consumer_group, headers, runtime)

    async def delete_consumer_group_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_with_options_async(project, logstore, consumer_group, headers, runtime)

    def delete_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        consumer_group = OpenApiUtilClient.get_encode_param(consumer_group)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        consumer_group = OpenApiUtilClient.get_encode_param(consumer_group)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_project(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project, headers, runtime)

    async def delete_project_async(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project, headers, runtime)

    def delete_project_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_saved_search(
        self,
        project: str,
        savedsearch_name: str,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_saved_search_with_options(project, savedsearch_name, headers, runtime)

    async def delete_saved_search_async(
        self,
        project: str,
        savedsearch_name: str,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_saved_search_with_options_async(project, savedsearch_name, headers, runtime)

    def delete_saved_search_with_options(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        host_map = {}
        host_map['project'] = project
        savedsearch_name = OpenApiUtilClient.get_encode_param(savedsearch_name)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_saved_search_with_options_async(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        host_map = {}
        host_map['project'] = project
        savedsearch_name = OpenApiUtilClient.get_encode_param(savedsearch_name)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_log_store(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_with_options(project, logstore, headers, runtime)

    async def get_log_store_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_log_store_with_options_async(project, logstore, headers, runtime)

    def get_log_store_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogStoreResponse:
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def get_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogStoreResponse:
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_project(
        self,
        project: str,
    ) -> sls_20201230_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project, headers, runtime)

    async def get_project_async(
        self,
        project: str,
    ) -> sls_20201230_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project, headers, runtime)

    def get_project_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_consumer_group(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_with_options(project, logstore, headers, runtime)

    async def list_consumer_group_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumer_group_with_options_async(project, logstore, headers, runtime)

    def list_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_log_stores(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
    ) -> sls_20201230_models.ListLogStoresResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_stores_with_options(project, request, headers, runtime)

    async def list_log_stores_async(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
    ) -> sls_20201230_models.ListLogStoresResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_log_stores_with_options_async(project, request, headers, runtime)

    def list_log_stores_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListLogStoresResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogStoresResponse(),
            self.execute(params, req, runtime)
        )

    async def list_log_stores_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListLogStoresResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogStoresResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_project(
        self,
        request: sls_20201230_models.ListProjectRequest,
    ) -> sls_20201230_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    async def list_project_async(
        self,
        request: sls_20201230_models.ListProjectRequest,
    ) -> sls_20201230_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_with_options_async(request, headers, runtime)

    def list_project_with_options(
        self,
        request: sls_20201230_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.project_name):
            query['projectName'] = request.project_name
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: sls_20201230_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.project_name):
            query['projectName'] = request.project_name
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_saved_search(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_saved_search_with_options(project, request, headers, runtime)

    async def list_saved_search_async(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_saved_search_with_options_async(project, request, headers, runtime)

    def list_saved_search_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def list_saved_search_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_consumer_group(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def update_consumer_group_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_consumer_group_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def update_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        consumer_group = OpenApiUtilClient.get_encode_param(consumer_group)
        body = {}
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        consumer_group = OpenApiUtilClient.get_encode_param(consumer_group)
        body = {}
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_log_store(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_with_options(project, logstore, request, headers, runtime)

    async def update_log_store_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_log_store_with_options_async(project, logstore, request, headers, runtime)

    def update_log_store_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def update_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_project(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
    ) -> sls_20201230_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project, request, headers, runtime)

    async def update_project_async(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
    ) -> sls_20201230_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(project, request, headers, runtime)

    def update_project_with_options(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateProjectResponse(),
            await self.execute_async(params, req, runtime)
        )