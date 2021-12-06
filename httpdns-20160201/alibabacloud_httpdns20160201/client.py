# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_httpdns20160201 import models as httpdns_20160201_models
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
        self._endpoint = self.get_endpoint('httpdns', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_domain_with_options(
        self,
        request: httpdns_20160201_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.AddDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.AddDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_with_options_async(
        self,
        request: httpdns_20160201_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.AddDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.AddDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain(
        self,
        request: httpdns_20160201_models.AddDomainRequest,
    ) -> httpdns_20160201_models.AddDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_domain_with_options(request, runtime)

    async def add_domain_async(
        self,
        request: httpdns_20160201_models.AddDomainRequest,
    ) -> httpdns_20160201_models.AddDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: httpdns_20160201_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: httpdns_20160201_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: httpdns_20160201_models.DeleteDomainRequest,
    ) -> httpdns_20160201_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: httpdns_20160201_models.DeleteDomainRequest,
    ) -> httpdns_20160201_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: httpdns_20160201_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: httpdns_20160201_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: httpdns_20160201_models.DescribeDomainsRequest,
    ) -> httpdns_20160201_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: httpdns_20160201_models.DescribeDomainsRequest,
    ) -> httpdns_20160201_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def get_account_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.GetAccountInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountInfo',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.GetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.GetAccountInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountInfo',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.GetAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_info(self) -> httpdns_20160201_models.GetAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_info_with_options(runtime)

    async def get_account_info_async(self) -> httpdns_20160201_models.GetAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_info_with_options_async(runtime)

    def get_resolve_count_summary_with_options(
        self,
        request: httpdns_20160201_models.GetResolveCountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.GetResolveCountSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Granularity'] = request.granularity
        query['TimeSpan'] = request.time_span
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetResolveCountSummary',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.GetResolveCountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resolve_count_summary_with_options_async(
        self,
        request: httpdns_20160201_models.GetResolveCountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.GetResolveCountSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Granularity'] = request.granularity
        query['TimeSpan'] = request.time_span
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetResolveCountSummary',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.GetResolveCountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resolve_count_summary(
        self,
        request: httpdns_20160201_models.GetResolveCountSummaryRequest,
    ) -> httpdns_20160201_models.GetResolveCountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resolve_count_summary_with_options(request, runtime)

    async def get_resolve_count_summary_async(
        self,
        request: httpdns_20160201_models.GetResolveCountSummaryRequest,
    ) -> httpdns_20160201_models.GetResolveCountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resolve_count_summary_with_options_async(request, runtime)

    def get_resolve_statistics_with_options(
        self,
        request: httpdns_20160201_models.GetResolveStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.GetResolveStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['Granularity'] = request.granularity
        query['ProtocolName'] = request.protocol_name
        query['TimeSpan'] = request.time_span
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetResolveStatistics',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.GetResolveStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resolve_statistics_with_options_async(
        self,
        request: httpdns_20160201_models.GetResolveStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.GetResolveStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['Granularity'] = request.granularity
        query['ProtocolName'] = request.protocol_name
        query['TimeSpan'] = request.time_span
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetResolveStatistics',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.GetResolveStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resolve_statistics(
        self,
        request: httpdns_20160201_models.GetResolveStatisticsRequest,
    ) -> httpdns_20160201_models.GetResolveStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resolve_statistics_with_options(request, runtime)

    async def get_resolve_statistics_async(
        self,
        request: httpdns_20160201_models.GetResolveStatisticsRequest,
    ) -> httpdns_20160201_models.GetResolveStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resolve_statistics_with_options_async(request, runtime)

    def list_domains_with_options(
        self,
        request: httpdns_20160201_models.ListDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.ListDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: httpdns_20160201_models.ListDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> httpdns_20160201_models.ListDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            httpdns_20160201_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: httpdns_20160201_models.ListDomainsRequest,
    ) -> httpdns_20160201_models.ListDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    async def list_domains_async(
        self,
        request: httpdns_20160201_models.ListDomainsRequest,
    ) -> httpdns_20160201_models.ListDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_domains_with_options_async(request, runtime)
