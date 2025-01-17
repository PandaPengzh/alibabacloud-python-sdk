# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_governance20210120 import models as governance_20210120_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('governance', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def enroll_account_with_options(
        self,
        request: governance_20210120_models.EnrollAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.EnrollAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.payer_account_uid):
            query['PayerAccountUid'] = request.payer_account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnrollAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.EnrollAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def enroll_account_with_options_async(
        self,
        request: governance_20210120_models.EnrollAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.EnrollAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.payer_account_uid):
            query['PayerAccountUid'] = request.payer_account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnrollAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.EnrollAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enroll_account(
        self,
        request: governance_20210120_models.EnrollAccountRequest,
    ) -> governance_20210120_models.EnrollAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.enroll_account_with_options(request, runtime)

    async def enroll_account_async(
        self,
        request: governance_20210120_models.EnrollAccountRequest,
    ) -> governance_20210120_models.EnrollAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enroll_account_with_options_async(request, runtime)

    def get_account_factory_baseline_with_options(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_factory_baseline_with_options_async(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_factory_baseline(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_factory_baseline_with_options(request, runtime)

    async def get_account_factory_baseline_async(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_factory_baseline_with_options_async(request, runtime)

    def get_enrolled_account_with_options(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnrolledAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetEnrolledAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enrolled_account_with_options_async(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnrolledAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetEnrolledAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enrolled_account(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_enrolled_account_with_options(request, runtime)

    async def get_enrolled_account_async(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_enrolled_account_with_options_async(request, runtime)

    def list_account_factory_baselines_with_options(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountFactoryBaselines',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListAccountFactoryBaselinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_factory_baselines_with_options_async(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountFactoryBaselines',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListAccountFactoryBaselinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_factory_baselines(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_account_factory_baselines_with_options(request, runtime)

    async def list_account_factory_baselines_async(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_account_factory_baselines_with_options_async(request, runtime)

    def list_enrolled_accounts_with_options(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnrolledAccounts',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEnrolledAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enrolled_accounts_with_options_async(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnrolledAccounts',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEnrolledAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enrolled_accounts(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_enrolled_accounts_with_options(request, runtime)

    async def list_enrolled_accounts_async(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_enrolled_accounts_with_options_async(request, runtime)
