# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gpdb20190620 import models as gpdb_20190620_models
from alibabacloud_tea_util import models as util_models


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
            'cn-beijing': 'gpdb.aliyuncs.com',
            'cn-hangzhou': 'gpdb.aliyuncs.com',
            'cn-shanghai': 'gpdb.aliyuncs.com',
            'cn-shenzhen': 'gpdb.aliyuncs.com',
            'cn-hongkong': 'gpdb.aliyuncs.com',
            'ap-southeast-1': 'gpdb.aliyuncs.com',
            'us-west-1': 'gpdb.aliyuncs.com',
            'us-east-1': 'gpdb.aliyuncs.com',
            'cn-hangzhou-finance': 'gpdb.aliyuncs.com',
            'cn-shanghai-finance-1': 'gpdb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'gpdb.aliyuncs.com',
            'cn-qingdao': 'gpdb.aliyuncs.com',
            'cn-north-2-gov-1': 'gpdb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('gpdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_dbinstance_for_dms_with_options(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceForDmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.DescribeDBInstanceForDmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.DescribeDBInstanceForDmsResponse(),
            self.do_rpcrequest('DescribeDBInstanceForDms', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_for_dms_with_options_async(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceForDmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.DescribeDBInstanceForDmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.DescribeDBInstanceForDmsResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceForDms', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_for_dms(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceForDmsRequest,
    ) -> gpdb_20190620_models.DescribeDBInstanceForDmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_for_dms_with_options(request, runtime)

    async def describe_dbinstance_for_dms_async(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceForDmsRequest,
    ) -> gpdb_20190620_models.DescribeDBInstanceForDmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_for_dms_with_options_async(request, runtime)

    def describe_dbinstance_security_ips_with_options(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.DescribeDBInstanceSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.DescribeDBInstanceSecurityIpsResponse(),
            self.do_rpcrequest('DescribeDBInstanceSecurityIps', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_security_ips_with_options_async(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.DescribeDBInstanceSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.DescribeDBInstanceSecurityIpsResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceSecurityIps', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_security_ips(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceSecurityIpsRequest,
    ) -> gpdb_20190620_models.DescribeDBInstanceSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_security_ips_with_options(request, runtime)

    async def describe_dbinstance_security_ips_async(
        self,
        request: gpdb_20190620_models.DescribeDBInstanceSecurityIpsRequest,
    ) -> gpdb_20190620_models.DescribeDBInstanceSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_security_ips_with_options_async(request, runtime)

    def describe_dbinstances_for_dms_with_options(
        self,
        request: gpdb_20190620_models.DescribeDBInstancesForDmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.DescribeDBInstancesForDmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.DescribeDBInstancesForDmsResponse(),
            self.do_rpcrequest('DescribeDBInstancesForDms', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_for_dms_with_options_async(
        self,
        request: gpdb_20190620_models.DescribeDBInstancesForDmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.DescribeDBInstancesForDmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.DescribeDBInstancesForDmsResponse(),
            await self.do_rpcrequest_async('DescribeDBInstancesForDms', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_for_dms(
        self,
        request: gpdb_20190620_models.DescribeDBInstancesForDmsRequest,
    ) -> gpdb_20190620_models.DescribeDBInstancesForDmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_for_dms_with_options(request, runtime)

    async def describe_dbinstances_for_dms_async(
        self,
        request: gpdb_20190620_models.DescribeDBInstancesForDmsRequest,
    ) -> gpdb_20190620_models.DescribeDBInstancesForDmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_for_dms_with_options_async(request, runtime)

    def modify_dbinstance_security_ips_with_options(
        self,
        request: gpdb_20190620_models.ModifyDBInstanceSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.ModifyDBInstanceSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.ModifyDBInstanceSecurityIpsResponse(),
            self.do_rpcrequest('ModifyDBInstanceSecurityIps', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_security_ips_with_options_async(
        self,
        request: gpdb_20190620_models.ModifyDBInstanceSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20190620_models.ModifyDBInstanceSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20190620_models.ModifyDBInstanceSecurityIpsResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceSecurityIps', '2019-06-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_security_ips(
        self,
        request: gpdb_20190620_models.ModifyDBInstanceSecurityIpsRequest,
    ) -> gpdb_20190620_models.ModifyDBInstanceSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_security_ips_with_options(request, runtime)

    async def modify_dbinstance_security_ips_async(
        self,
        request: gpdb_20190620_models.ModifyDBInstanceSecurityIpsRequest,
    ) -> gpdb_20190620_models.ModifyDBInstanceSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_security_ips_with_options_async(request, runtime)
