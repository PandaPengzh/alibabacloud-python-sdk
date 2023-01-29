# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbfs20200418 import models as dbfs20200418_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'dbfs.aliyuncs.com',
            'cn-beijing-finance-1': 'dbfs.aliyuncs.com',
            'cn-beijing-finance-pop': 'dbfs.aliyuncs.com',
            'cn-beijing-gov-1': 'dbfs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dbfs.aliyuncs.com',
            'cn-edge-1': 'dbfs.aliyuncs.com',
            'cn-fujian': 'dbfs.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dbfs.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dbfs.aliyuncs.com',
            'cn-hangzhou-finance': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dbfs.aliyuncs.com',
            'cn-hangzhou-test-306': 'dbfs.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dbfs.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dbfs.aliyuncs.com',
            'cn-north-2-gov-1': 'dbfs.aliyuncs.com',
            'cn-qingdao-nebula': 'dbfs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dbfs.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dbfs.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbfs.aliyuncs.com',
            'cn-shanghai-inner': 'dbfs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dbfs.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbfs.aliyuncs.com',
            'cn-shenzhen-inner': 'dbfs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dbfs.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dbfs.aliyuncs.com',
            'cn-wuhan': 'dbfs.aliyuncs.com',
            'cn-wulanchabu': 'dbfs.aliyuncs.com',
            'cn-yushanfang': 'dbfs.aliyuncs.com',
            'cn-zhangbei': 'dbfs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dbfs.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dbfs.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dbfs.aliyuncs.com',
            'eu-west-1-oxs': 'dbfs.aliyuncs.com',
            'rus-west-1-pop': 'dbfs.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbfs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_tags_batch_with_options(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbfs_list):
            query['DbfsList'] = request.dbfs_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_batch_with_options_async(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbfs_list):
            query['DbfsList'] = request.dbfs_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags_batch(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_batch_with_options(request, runtime)

    async def add_tags_batch_async(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_batch_with_options_async(request, runtime)

    def apply_auto_snapshot_policy_with_options(
        self,
        tmp_req: dbfs20200418_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ApplyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.ApplyAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbfs_ids):
            request.dbfs_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbfs_ids, 'DbfsIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbfs_ids_shrink):
            query['DbfsIds'] = request.dbfs_ids_shrink
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ApplyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_auto_snapshot_policy_with_options_async(
        self,
        tmp_req: dbfs20200418_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ApplyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.ApplyAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbfs_ids):
            request.dbfs_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbfs_ids, 'DbfsIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbfs_ids_shrink):
            query['DbfsIds'] = request.dbfs_ids_shrink
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ApplyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_auto_snapshot_policy(
        self,
        request: dbfs20200418_models.ApplyAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.ApplyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    async def apply_auto_snapshot_policy_async(
        self,
        request: dbfs20200418_models.ApplyAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.ApplyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_auto_snapshot_policy_with_options_async(request, runtime)

    def attach_dbfs_with_options(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_mode):
            query['AttachMode'] = request.attach_mode
        if not UtilClient.is_unset(request.attach_point):
            query['AttachPoint'] = request.attach_point
        if not UtilClient.is_unset(request.ecsinstance_id):
            query['ECSInstanceId'] = request.ecsinstance_id
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_url):
            query['ServerUrl'] = request.server_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_mode):
            query['AttachMode'] = request.attach_mode
        if not UtilClient.is_unset(request.attach_point):
            query['AttachPoint'] = request.attach_point
        if not UtilClient.is_unset(request.ecsinstance_id):
            query['ECSInstanceId'] = request.ecsinstance_id
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_url):
            query['ServerUrl'] = request.server_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_dbfs(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_dbfs_with_options(request, runtime)

    async def attach_dbfs_async(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_dbfs_with_options_async(request, runtime)

    def cancel_auto_snapshot_policy_with_options(
        self,
        tmp_req: dbfs20200418_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CancelAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.CancelAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbfs_ids):
            request.dbfs_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbfs_ids, 'DbfsIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbfs_ids_shrink):
            query['DbfsIds'] = request.dbfs_ids_shrink
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CancelAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_auto_snapshot_policy_with_options_async(
        self,
        tmp_req: dbfs20200418_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CancelAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.CancelAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbfs_ids):
            request.dbfs_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbfs_ids, 'DbfsIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbfs_ids_shrink):
            query['DbfsIds'] = request.dbfs_ids_shrink
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CancelAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_auto_snapshot_policy(
        self,
        request: dbfs20200418_models.CancelAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.CancelAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    async def cancel_auto_snapshot_policy_async(
        self,
        request: dbfs20200418_models.CancelAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.CancelAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_auto_snapshot_policy_with_options_async(request, runtime)

    def create_auto_snapshot_policy_with_options(
        self,
        tmp_req: dbfs20200418_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.CreateAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.repeat_weekdays):
            request.repeat_weekdays_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_weekdays, 'RepeatWeekdays', 'json')
        if not UtilClient.is_unset(tmp_req.time_points):
            request.time_points_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.time_points, 'TimePoints', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_weekdays_shrink):
            query['RepeatWeekdays'] = request.repeat_weekdays_shrink
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points_shrink):
            query['TimePoints'] = request.time_points_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_snapshot_policy_with_options_async(
        self,
        tmp_req: dbfs20200418_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.CreateAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.repeat_weekdays):
            request.repeat_weekdays_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_weekdays, 'RepeatWeekdays', 'json')
        if not UtilClient.is_unset(tmp_req.time_points):
            request.time_points_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.time_points, 'TimePoints', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_weekdays_shrink):
            query['RepeatWeekdays'] = request.repeat_weekdays_shrink
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points_shrink):
            query['TimePoints'] = request.time_points_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_snapshot_policy(
        self,
        request: dbfs20200418_models.CreateAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.CreateAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    async def create_auto_snapshot_policy_async(
        self,
        request: dbfs20200418_models.CreateAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.CreateAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_snapshot_policy_with_options_async(request, runtime)

    def create_dbfs_with_options(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advanced_features):
            query['AdvancedFeatures'] = request.advanced_features
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_snapshot):
            query['DeleteSnapshot'] = request.delete_snapshot
        if not UtilClient.is_unset(request.enable_raid):
            query['EnableRaid'] = request.enable_raid
        if not UtilClient.is_unset(request.encryption):
            query['Encryption'] = request.encryption
        if not UtilClient.is_unset(request.fs_name):
            query['FsName'] = request.fs_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.raid_stripe_unit_number):
            query['RaidStripeUnitNumber'] = request.raid_stripe_unit_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size_g):
            query['SizeG'] = request.size_g
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.used_scene):
            query['UsedScene'] = request.used_scene
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advanced_features):
            query['AdvancedFeatures'] = request.advanced_features
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_snapshot):
            query['DeleteSnapshot'] = request.delete_snapshot
        if not UtilClient.is_unset(request.enable_raid):
            query['EnableRaid'] = request.enable_raid
        if not UtilClient.is_unset(request.encryption):
            query['Encryption'] = request.encryption
        if not UtilClient.is_unset(request.fs_name):
            query['FsName'] = request.fs_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.raid_stripe_unit_number):
            query['RaidStripeUnitNumber'] = request.raid_stripe_unit_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size_g):
            query['SizeG'] = request.size_g
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.used_scene):
            query['UsedScene'] = request.used_scene
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbfs(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbfs_with_options(request, runtime)

    async def create_dbfs_async(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbfs_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_auto_snapshot_policy_with_options(
        self,
        request: dbfs20200418_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_snapshot_policy_with_options_async(
        self,
        request: dbfs20200418_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_snapshot_policy(
        self,
        request: dbfs20200418_models.DeleteAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.DeleteAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    async def delete_auto_snapshot_policy_async(
        self,
        request: dbfs20200418_models.DeleteAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.DeleteAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_snapshot_policy_with_options_async(request, runtime)

    def delete_dbfs_with_options(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbfs(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbfs_with_options(request, runtime)

    async def delete_dbfs_async(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbfs_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_tags_batch_with_options(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbfs_list):
            query['DbfsList'] = request.dbfs_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tags_batch_with_options_async(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbfs_list):
            query['DbfsList'] = request.dbfs_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tags_batch(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tags_batch_with_options(request, runtime)

    async def delete_tags_batch_async(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tags_batch_with_options_async(request, runtime)

    def describe_dbfs_specifications_with_options(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.ecs_instance_type):
            query['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbfsSpecifications',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbfs_specifications_with_options_async(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.ecs_instance_type):
            query['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbfsSpecifications',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbfs_specifications(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbfs_specifications_with_options(request, runtime)

    async def describe_dbfs_specifications_async(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbfs_specifications_with_options_async(request, runtime)

    def describe_instance_types_with_options(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_types_with_options_async(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeInstanceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_types(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    async def describe_instance_types_async(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_types_with_options_async(request, runtime)

    def detach_dbfs_with_options(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecsinstance_id):
            query['ECSInstanceId'] = request.ecsinstance_id
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecsinstance_id):
            query['ECSInstanceId'] = request.ecsinstance_id
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_dbfs(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_dbfs_with_options(request, runtime)

    async def detach_dbfs_async(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_dbfs_with_options_async(request, runtime)

    def get_auto_snapshot_policy_with_options(
        self,
        request: dbfs20200418_models.GetAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_snapshot_policy_with_options_async(
        self,
        request: dbfs20200418_models.GetAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_snapshot_policy(
        self,
        request: dbfs20200418_models.GetAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.GetAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_snapshot_policy_with_options(request, runtime)

    async def get_auto_snapshot_policy_async(
        self,
        request: dbfs20200418_models.GetAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.GetAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_snapshot_policy_with_options_async(request, runtime)

    def get_dbfs_with_options(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dbfs(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
    ) -> dbfs20200418_models.GetDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dbfs_with_options(request, runtime)

    async def get_dbfs_async(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
    ) -> dbfs20200418_models.GetDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dbfs_with_options_async(request, runtime)

    def get_service_linked_role_with_options(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_linked_role_with_options_async(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_linked_role(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_with_options(request, runtime)

    async def get_service_linked_role_async(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_linked_role_with_options_async(request, runtime)

    def get_snapshot_link_with_options(
        self,
        request: dbfs20200418_models.GetSnapshotLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetSnapshotLinkResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotLink',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetSnapshotLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_snapshot_link_with_options_async(
        self,
        request: dbfs20200418_models.GetSnapshotLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetSnapshotLinkResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotLink',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetSnapshotLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_snapshot_link(
        self,
        request: dbfs20200418_models.GetSnapshotLinkRequest,
    ) -> dbfs20200418_models.GetSnapshotLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_snapshot_link_with_options(request, runtime)

    async def get_snapshot_link_async(
        self,
        request: dbfs20200418_models.GetSnapshotLinkRequest,
    ) -> dbfs20200418_models.GetSnapshotLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_snapshot_link_with_options_async(request, runtime)

    def list_auto_snapshot_policies_with_options(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListAutoSnapshotPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoSnapshotPolicies',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListAutoSnapshotPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_snapshot_policies_with_options_async(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListAutoSnapshotPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoSnapshotPolicies',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListAutoSnapshotPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_snapshot_policies(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPoliciesRequest,
    ) -> dbfs20200418_models.ListAutoSnapshotPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auto_snapshot_policies_with_options(request, runtime)

    async def list_auto_snapshot_policies_async(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPoliciesRequest,
    ) -> dbfs20200418_models.ListAutoSnapshotPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_snapshot_policies_with_options_async(request, runtime)

    def list_auto_snapshot_policy_applied_dbfs_with_options(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoSnapshotPolicyAppliedDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_snapshot_policy_applied_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoSnapshotPolicyAppliedDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_snapshot_policy_applied_dbfs(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsRequest,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auto_snapshot_policy_applied_dbfs_with_options(request, runtime)

    async def list_auto_snapshot_policy_applied_dbfs_async(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsRequest,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyAppliedDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_snapshot_policy_applied_dbfs_with_options_async(request, runtime)

    def list_auto_snapshot_policy_unapplied_dbfs_with_options(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoSnapshotPolicyUnappliedDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_snapshot_policy_unapplied_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoSnapshotPolicyUnappliedDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_snapshot_policy_unapplied_dbfs(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsRequest,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auto_snapshot_policy_unapplied_dbfs_with_options(request, runtime)

    async def list_auto_snapshot_policy_unapplied_dbfs_async(
        self,
        request: dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsRequest,
    ) -> dbfs20200418_models.ListAutoSnapshotPolicyUnappliedDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_snapshot_policy_unapplied_dbfs_with_options_async(request, runtime)

    def list_dbfs_with_options(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbfs(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
    ) -> dbfs20200418_models.ListDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_with_options(request, runtime)

    async def list_dbfs_async(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
    ) -> dbfs20200418_models.ListDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbfs_with_options_async(request, runtime)

    def list_dbfs_attachable_ecs_instances_with_options(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachableEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbfs_attachable_ecs_instances_with_options_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachableEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbfs_attachable_ecs_instances(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_attachable_ecs_instances_with_options(request, runtime)

    async def list_dbfs_attachable_ecs_instances_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbfs_attachable_ecs_instances_with_options_async(request, runtime)

    def list_dbfs_attached_ecs_instances_with_options(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachedEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbfs_attached_ecs_instances_with_options_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachedEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbfs_attached_ecs_instances(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_attached_ecs_instances_with_options(request, runtime)

    async def list_dbfs_attached_ecs_instances_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbfs_attached_ecs_instances_with_options_async(request, runtime)

    def list_snapshot_with_options(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshot(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_snapshot_with_options(request, runtime)

    async def list_snapshot_async(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshot_with_options_async(request, runtime)

    def list_snapshot_links_with_options(
        self,
        request: dbfs20200418_models.ListSnapshotLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotLinksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshotLinks',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotLinksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshot_links_with_options_async(
        self,
        request: dbfs20200418_models.ListSnapshotLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotLinksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshotLinks',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotLinksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshot_links(
        self,
        request: dbfs20200418_models.ListSnapshotLinksRequest,
    ) -> dbfs20200418_models.ListSnapshotLinksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_snapshot_links_with_options(request, runtime)

    async def list_snapshot_links_async(
        self,
        request: dbfs20200418_models.ListSnapshotLinksRequest,
    ) -> dbfs20200418_models.ListSnapshotLinksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshot_links_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_with_options(
        self,
        tmp_req: dbfs20200418_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.ModifyAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.repeat_weekdays):
            request.repeat_weekdays_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_weekdays, 'RepeatWeekdays', 'json')
        if not UtilClient.is_unset(tmp_req.time_points):
            request.time_points_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.time_points, 'TimePoints', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_weekdays_shrink):
            query['RepeatWeekdays'] = request.repeat_weekdays_shrink
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points_shrink):
            query['TimePoints'] = request.time_points_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ModifyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_snapshot_policy_with_options_async(
        self,
        tmp_req: dbfs20200418_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = dbfs20200418_models.ModifyAutoSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.repeat_weekdays):
            request.repeat_weekdays_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repeat_weekdays, 'RepeatWeekdays', 'json')
        if not UtilClient.is_unset(tmp_req.time_points):
            request.time_points_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.time_points, 'TimePoints', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_weekdays_shrink):
            query['RepeatWeekdays'] = request.repeat_weekdays_shrink
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points_shrink):
            query['TimePoints'] = request.time_points_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ModifyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_snapshot_policy(
        self,
        request: dbfs20200418_models.ModifyAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    async def modify_auto_snapshot_policy_async(
        self,
        request: dbfs20200418_models.ModifyAutoSnapshotPolicyRequest,
    ) -> dbfs20200418_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_snapshot_policy_with_options_async(request, runtime)

    def modify_snapshot_attribute_with_options(
        self,
        request: dbfs20200418_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySnapshotAttribute',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ModifySnapshotAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_snapshot_attribute_with_options_async(
        self,
        request: dbfs20200418_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySnapshotAttribute',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ModifySnapshotAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_snapshot_attribute(
        self,
        request: dbfs20200418_models.ModifySnapshotAttributeRequest,
    ) -> dbfs20200418_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_attribute_with_options(request, runtime)

    async def modify_snapshot_attribute_async(
        self,
        request: dbfs20200418_models.ModifySnapshotAttributeRequest,
    ) -> dbfs20200418_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_snapshot_attribute_with_options_async(request, runtime)

    def rename_dbfs_with_options(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.fs_name):
            query['FsName'] = request.fs_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.fs_name):
            query['FsName'] = request.fs_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_dbfs(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_dbfs_with_options(request, runtime)

    async def rename_dbfs_async(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_dbfs_with_options_async(request, runtime)

    def resize_dbfs_with_options(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.new_size_g):
            query['NewSizeG'] = request.new_size_g
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.new_size_g):
            query['NewSizeG'] = request.new_size_g
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_dbfs(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_dbfs_with_options(request, runtime)

    async def resize_dbfs_async(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_dbfs_with_options_async(request, runtime)

    def tag_dbfs_with_options(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.TagDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbfs_id):
            query['DbfsId'] = request.dbfs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.TagDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbfs_id):
            query['DbfsId'] = request.dbfs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_dbfs(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
    ) -> dbfs20200418_models.TagDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_dbfs_with_options(request, runtime)

    async def tag_dbfs_async(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
    ) -> dbfs20200418_models.TagDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_dbfs_with_options_async(request, runtime)

    def update_dbfs_with_options(
        self,
        request: dbfs20200418_models.UpdateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.UpdateDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advanced_features):
            query['AdvancedFeatures'] = request.advanced_features
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_scene):
            query['UsedScene'] = request.used_scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.UpdateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.UpdateDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advanced_features):
            query['AdvancedFeatures'] = request.advanced_features
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_scene):
            query['UsedScene'] = request.used_scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dbfs(
        self,
        request: dbfs20200418_models.UpdateDbfsRequest,
    ) -> dbfs20200418_models.UpdateDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dbfs_with_options(request, runtime)

    async def update_dbfs_async(
        self,
        request: dbfs20200418_models.UpdateDbfsRequest,
    ) -> dbfs20200418_models.UpdateDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dbfs_with_options_async(request, runtime)
