# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_btripopen20220520 import models as btrip_open_20220520_models
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
        self._endpoint = self.get_endpoint('btripopen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def access_token_with_options(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccessToken',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/btrip-open-auth/v1/access-token/action/take',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def access_token_with_options_async(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccessToken',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/btrip-open-auth/v1/access-token/action/take',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def access_token(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.access_token_with_options(request, headers, runtime)

    async def access_token_async(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.access_token_with_options_async(request, headers, runtime)

    def add_invoice_entity_with_options(
        self,
        tmp_req: btrip_open_20220520_models.AddInvoiceEntityRequest,
        headers: btrip_open_20220520_models.AddInvoiceEntityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AddInvoiceEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.AddInvoiceEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        body = {}
        if not UtilClient.is_unset(request.entities_shrink):
            body['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddInvoiceEntity',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/entities',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AddInvoiceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_invoice_entity_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.AddInvoiceEntityRequest,
        headers: btrip_open_20220520_models.AddInvoiceEntityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AddInvoiceEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.AddInvoiceEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        body = {}
        if not UtilClient.is_unset(request.entities_shrink):
            body['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddInvoiceEntity',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/entities',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AddInvoiceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_invoice_entity(
        self,
        request: btrip_open_20220520_models.AddInvoiceEntityRequest,
    ) -> btrip_open_20220520_models.AddInvoiceEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AddInvoiceEntityHeaders()
        return self.add_invoice_entity_with_options(request, headers, runtime)

    async def add_invoice_entity_async(
        self,
        request: btrip_open_20220520_models.AddInvoiceEntityRequest,
    ) -> btrip_open_20220520_models.AddInvoiceEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AddInvoiceEntityHeaders()
        return await self.add_invoice_entity_with_options_async(request, headers, runtime)

    def address_get_with_options(
        self,
        request: btrip_open_20220520_models.AddressGetRequest,
        headers: btrip_open_20220520_models.AddressGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AddressGetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['action_type'] = request.action_type
        if not UtilClient.is_unset(request.car_scenes_code):
            query['car_scenes_code'] = request.car_scenes_code
        if not UtilClient.is_unset(request.itinerary_id):
            query['itinerary_id'] = request.itinerary_id
        if not UtilClient.is_unset(request.phone):
            query['phone'] = request.phone
        if not UtilClient.is_unset(request.sub_corp_id):
            query['sub_corp_id'] = request.sub_corp_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddressGet',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/open/v1/address',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AddressGetResponse(),
            self.call_api(params, req, runtime)
        )

    async def address_get_with_options_async(
        self,
        request: btrip_open_20220520_models.AddressGetRequest,
        headers: btrip_open_20220520_models.AddressGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AddressGetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['action_type'] = request.action_type
        if not UtilClient.is_unset(request.car_scenes_code):
            query['car_scenes_code'] = request.car_scenes_code
        if not UtilClient.is_unset(request.itinerary_id):
            query['itinerary_id'] = request.itinerary_id
        if not UtilClient.is_unset(request.phone):
            query['phone'] = request.phone
        if not UtilClient.is_unset(request.sub_corp_id):
            query['sub_corp_id'] = request.sub_corp_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddressGet',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/open/v1/address',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AddressGetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def address_get(
        self,
        request: btrip_open_20220520_models.AddressGetRequest,
    ) -> btrip_open_20220520_models.AddressGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AddressGetHeaders()
        return self.address_get_with_options(request, headers, runtime)

    async def address_get_async(
        self,
        request: btrip_open_20220520_models.AddressGetRequest,
    ) -> btrip_open_20220520_models.AddressGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AddressGetHeaders()
        return await self.address_get_with_options_async(request, headers, runtime)

    def airport_search_with_options(
        self,
        request: btrip_open_20220520_models.AirportSearchRequest,
        headers: btrip_open_20220520_models.AirportSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AirportSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AirportSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/airport',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AirportSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def airport_search_with_options_async(
        self,
        request: btrip_open_20220520_models.AirportSearchRequest,
        headers: btrip_open_20220520_models.AirportSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AirportSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AirportSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/airport',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AirportSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def airport_search(
        self,
        request: btrip_open_20220520_models.AirportSearchRequest,
    ) -> btrip_open_20220520_models.AirportSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AirportSearchHeaders()
        return self.airport_search_with_options(request, headers, runtime)

    async def airport_search_async(
        self,
        request: btrip_open_20220520_models.AirportSearchRequest,
    ) -> btrip_open_20220520_models.AirportSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AirportSearchHeaders()
        return await self.airport_search_with_options_async(request, headers, runtime)

    def all_base_city_info_query_with_options(
        self,
        headers: btrip_open_20220520_models.AllBaseCityInfoQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AllBaseCityInfoQueryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_access_token):
            real_headers['x-acs-btrip-access-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='AllBaseCityInfoQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/code',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AllBaseCityInfoQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def all_base_city_info_query_with_options_async(
        self,
        headers: btrip_open_20220520_models.AllBaseCityInfoQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AllBaseCityInfoQueryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_access_token):
            real_headers['x-acs-btrip-access-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='AllBaseCityInfoQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/code',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AllBaseCityInfoQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def all_base_city_info_query(self) -> btrip_open_20220520_models.AllBaseCityInfoQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AllBaseCityInfoQueryHeaders()
        return self.all_base_city_info_query_with_options(headers, runtime)

    async def all_base_city_info_query_async(self) -> btrip_open_20220520_models.AllBaseCityInfoQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.AllBaseCityInfoQueryHeaders()
        return await self.all_base_city_info_query_with_options_async(headers, runtime)

    def apply_add_with_options(
        self,
        tmp_req: btrip_open_20220520_models.ApplyAddRequest,
        headers: btrip_open_20220520_models.ApplyAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyAddResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.ApplyAddShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.external_traveler_list):
            request.external_traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_list, 'external_traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.external_traveler_standard):
            request.external_traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_standard, 'external_traveler_standard', 'json')
        if not UtilClient.is_unset(tmp_req.hotel_share):
            request.hotel_share_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_share, 'hotel_share', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_list):
            request.itinerary_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_list, 'itinerary_list', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_set_list):
            request.itinerary_set_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_set_list, 'itinerary_set_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_list):
            request.traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_list, 'traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_standard):
            request.traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_standard, 'traveler_standard', 'json')
        query = {}
        if not UtilClient.is_unset(request.international_flight_cabins):
            query['international_flight_cabins'] = request.international_flight_cabins
        body = {}
        if not UtilClient.is_unset(request.budget):
            body['budget'] = request.budget
        if not UtilClient.is_unset(request.budget_merge):
            body['budget_merge'] = request.budget_merge
        if not UtilClient.is_unset(request.corp_name):
            body['corp_name'] = request.corp_name
        if not UtilClient.is_unset(request.depart_id):
            body['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.depart_name):
            body['depart_name'] = request.depart_name
        if not UtilClient.is_unset(request.extend_field):
            body['extend_field'] = request.extend_field
        if not UtilClient.is_unset(request.external_traveler_list_shrink):
            body['external_traveler_list'] = request.external_traveler_list_shrink
        if not UtilClient.is_unset(request.external_traveler_standard_shrink):
            body['external_traveler_standard'] = request.external_traveler_standard_shrink
        if not UtilClient.is_unset(request.flight_budget):
            body['flight_budget'] = request.flight_budget
        if not UtilClient.is_unset(request.hotel_budget):
            body['hotel_budget'] = request.hotel_budget
        if not UtilClient.is_unset(request.hotel_share_shrink):
            body['hotel_share'] = request.hotel_share_shrink
        if not UtilClient.is_unset(request.itinerary_list_shrink):
            body['itinerary_list'] = request.itinerary_list_shrink
        if not UtilClient.is_unset(request.itinerary_rule):
            body['itinerary_rule'] = request.itinerary_rule
        if not UtilClient.is_unset(request.itinerary_set_list_shrink):
            body['itinerary_set_list'] = request.itinerary_set_list_shrink
        if not UtilClient.is_unset(request.limit_traveler):
            body['limit_traveler'] = request.limit_traveler
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            body['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.thirdpart_business_id):
            body['thirdpart_business_id'] = request.thirdpart_business_id
        if not UtilClient.is_unset(request.thirdpart_depart_id):
            body['thirdpart_depart_id'] = request.thirdpart_depart_id
        if not UtilClient.is_unset(request.together_book_rule):
            body['together_book_rule'] = request.together_book_rule
        if not UtilClient.is_unset(request.train_budget):
            body['train_budget'] = request.train_budget
        if not UtilClient.is_unset(request.traveler_list_shrink):
            body['traveler_list'] = request.traveler_list_shrink
        if not UtilClient.is_unset(request.traveler_standard_shrink):
            body['traveler_standard'] = request.traveler_standard_shrink
        if not UtilClient.is_unset(request.trip_cause):
            body['trip_cause'] = request.trip_cause
        if not UtilClient.is_unset(request.trip_day):
            body['trip_day'] = request.trip_day
        if not UtilClient.is_unset(request.trip_title):
            body['trip_title'] = request.trip_title
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.union_no):
            body['union_no'] = request.union_no
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_budget):
            body['vehicle_budget'] = request.vehicle_budget
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_add_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.ApplyAddRequest,
        headers: btrip_open_20220520_models.ApplyAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyAddResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.ApplyAddShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.external_traveler_list):
            request.external_traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_list, 'external_traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.external_traveler_standard):
            request.external_traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_standard, 'external_traveler_standard', 'json')
        if not UtilClient.is_unset(tmp_req.hotel_share):
            request.hotel_share_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_share, 'hotel_share', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_list):
            request.itinerary_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_list, 'itinerary_list', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_set_list):
            request.itinerary_set_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_set_list, 'itinerary_set_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_list):
            request.traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_list, 'traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_standard):
            request.traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_standard, 'traveler_standard', 'json')
        query = {}
        if not UtilClient.is_unset(request.international_flight_cabins):
            query['international_flight_cabins'] = request.international_flight_cabins
        body = {}
        if not UtilClient.is_unset(request.budget):
            body['budget'] = request.budget
        if not UtilClient.is_unset(request.budget_merge):
            body['budget_merge'] = request.budget_merge
        if not UtilClient.is_unset(request.corp_name):
            body['corp_name'] = request.corp_name
        if not UtilClient.is_unset(request.depart_id):
            body['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.depart_name):
            body['depart_name'] = request.depart_name
        if not UtilClient.is_unset(request.extend_field):
            body['extend_field'] = request.extend_field
        if not UtilClient.is_unset(request.external_traveler_list_shrink):
            body['external_traveler_list'] = request.external_traveler_list_shrink
        if not UtilClient.is_unset(request.external_traveler_standard_shrink):
            body['external_traveler_standard'] = request.external_traveler_standard_shrink
        if not UtilClient.is_unset(request.flight_budget):
            body['flight_budget'] = request.flight_budget
        if not UtilClient.is_unset(request.hotel_budget):
            body['hotel_budget'] = request.hotel_budget
        if not UtilClient.is_unset(request.hotel_share_shrink):
            body['hotel_share'] = request.hotel_share_shrink
        if not UtilClient.is_unset(request.itinerary_list_shrink):
            body['itinerary_list'] = request.itinerary_list_shrink
        if not UtilClient.is_unset(request.itinerary_rule):
            body['itinerary_rule'] = request.itinerary_rule
        if not UtilClient.is_unset(request.itinerary_set_list_shrink):
            body['itinerary_set_list'] = request.itinerary_set_list_shrink
        if not UtilClient.is_unset(request.limit_traveler):
            body['limit_traveler'] = request.limit_traveler
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            body['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.thirdpart_business_id):
            body['thirdpart_business_id'] = request.thirdpart_business_id
        if not UtilClient.is_unset(request.thirdpart_depart_id):
            body['thirdpart_depart_id'] = request.thirdpart_depart_id
        if not UtilClient.is_unset(request.together_book_rule):
            body['together_book_rule'] = request.together_book_rule
        if not UtilClient.is_unset(request.train_budget):
            body['train_budget'] = request.train_budget
        if not UtilClient.is_unset(request.traveler_list_shrink):
            body['traveler_list'] = request.traveler_list_shrink
        if not UtilClient.is_unset(request.traveler_standard_shrink):
            body['traveler_standard'] = request.traveler_standard_shrink
        if not UtilClient.is_unset(request.trip_cause):
            body['trip_cause'] = request.trip_cause
        if not UtilClient.is_unset(request.trip_day):
            body['trip_day'] = request.trip_day
        if not UtilClient.is_unset(request.trip_title):
            body['trip_title'] = request.trip_title
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.union_no):
            body['union_no'] = request.union_no
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_budget):
            body['vehicle_budget'] = request.vehicle_budget
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_add(
        self,
        request: btrip_open_20220520_models.ApplyAddRequest,
    ) -> btrip_open_20220520_models.ApplyAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyAddHeaders()
        return self.apply_add_with_options(request, headers, runtime)

    async def apply_add_async(
        self,
        request: btrip_open_20220520_models.ApplyAddRequest,
    ) -> btrip_open_20220520_models.ApplyAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyAddHeaders()
        return await self.apply_add_with_options_async(request, headers, runtime)

    def apply_approve_with_options(
        self,
        request: btrip_open_20220520_models.ApplyApproveRequest,
        headers: btrip_open_20220520_models.ApplyApproveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyApproveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_id):
            body['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.note):
            body['note'] = request.note
        if not UtilClient.is_unset(request.operate_time):
            body['operate_time'] = request.operate_time
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyApprove',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip/action/approve',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyApproveResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_approve_with_options_async(
        self,
        request: btrip_open_20220520_models.ApplyApproveRequest,
        headers: btrip_open_20220520_models.ApplyApproveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyApproveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_id):
            body['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.note):
            body['note'] = request.note
        if not UtilClient.is_unset(request.operate_time):
            body['operate_time'] = request.operate_time
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyApprove',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip/action/approve',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyApproveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_approve(
        self,
        request: btrip_open_20220520_models.ApplyApproveRequest,
    ) -> btrip_open_20220520_models.ApplyApproveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyApproveHeaders()
        return self.apply_approve_with_options(request, headers, runtime)

    async def apply_approve_async(
        self,
        request: btrip_open_20220520_models.ApplyApproveRequest,
    ) -> btrip_open_20220520_models.ApplyApproveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyApproveHeaders()
        return await self.apply_approve_with_options_async(request, headers, runtime)

    def apply_invoice_task_with_options(
        self,
        tmp_req: btrip_open_20220520_models.ApplyInvoiceTaskRequest,
        headers: btrip_open_20220520_models.ApplyInvoiceTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyInvoiceTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.ApplyInvoiceTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.invoice_task_list):
            request.invoice_task_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_task_list, 'invoice_task_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.bill_date):
            body['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.invoice_task_list_shrink):
            body['invoice_task_list'] = request.invoice_task_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyInvoiceTask',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/apply-invoice-task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyInvoiceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_invoice_task_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.ApplyInvoiceTaskRequest,
        headers: btrip_open_20220520_models.ApplyInvoiceTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyInvoiceTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.ApplyInvoiceTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.invoice_task_list):
            request.invoice_task_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_task_list, 'invoice_task_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.bill_date):
            body['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.invoice_task_list_shrink):
            body['invoice_task_list'] = request.invoice_task_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyInvoiceTask',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/apply-invoice-task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyInvoiceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_invoice_task(
        self,
        request: btrip_open_20220520_models.ApplyInvoiceTaskRequest,
    ) -> btrip_open_20220520_models.ApplyInvoiceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyInvoiceTaskHeaders()
        return self.apply_invoice_task_with_options(request, headers, runtime)

    async def apply_invoice_task_async(
        self,
        request: btrip_open_20220520_models.ApplyInvoiceTaskRequest,
    ) -> btrip_open_20220520_models.ApplyInvoiceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyInvoiceTaskHeaders()
        return await self.apply_invoice_task_with_options_async(request, headers, runtime)

    def apply_list_query_with_options(
        self,
        request: btrip_open_20220520_models.ApplyListQueryRequest,
        headers: btrip_open_20220520_models.ApplyListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.gmt_modified):
            query['gmt_modified'] = request.gmt_modified
        if not UtilClient.is_unset(request.only_shang_lv_apply):
            query['only_shang_lv_apply'] = request.only_shang_lv_apply
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.union_no):
            query['union_no'] = request.union_no
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trips',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyListQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_list_query_with_options_async(
        self,
        request: btrip_open_20220520_models.ApplyListQueryRequest,
        headers: btrip_open_20220520_models.ApplyListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.gmt_modified):
            query['gmt_modified'] = request.gmt_modified
        if not UtilClient.is_unset(request.only_shang_lv_apply):
            query['only_shang_lv_apply'] = request.only_shang_lv_apply
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.union_no):
            query['union_no'] = request.union_no
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trips',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyListQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_list_query(
        self,
        request: btrip_open_20220520_models.ApplyListQueryRequest,
    ) -> btrip_open_20220520_models.ApplyListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyListQueryHeaders()
        return self.apply_list_query_with_options(request, headers, runtime)

    async def apply_list_query_async(
        self,
        request: btrip_open_20220520_models.ApplyListQueryRequest,
    ) -> btrip_open_20220520_models.ApplyListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyListQueryHeaders()
        return await self.apply_list_query_with_options_async(request, headers, runtime)

    def apply_modify_with_options(
        self,
        tmp_req: btrip_open_20220520_models.ApplyModifyRequest,
        headers: btrip_open_20220520_models.ApplyModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyModifyResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.ApplyModifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.external_traveler_list):
            request.external_traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_list, 'external_traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.external_traveler_standard):
            request.external_traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_standard, 'external_traveler_standard', 'json')
        if not UtilClient.is_unset(tmp_req.hotel_share):
            request.hotel_share_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_share, 'hotel_share', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_list):
            request.itinerary_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_list, 'itinerary_list', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_set_list):
            request.itinerary_set_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_set_list, 'itinerary_set_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_list):
            request.traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_list, 'traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_standard):
            request.traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_standard, 'traveler_standard', 'json')
        body = {}
        if not UtilClient.is_unset(request.budget):
            body['budget'] = request.budget
        if not UtilClient.is_unset(request.budget_merge):
            body['budget_merge'] = request.budget_merge
        if not UtilClient.is_unset(request.corp_name):
            body['corp_name'] = request.corp_name
        if not UtilClient.is_unset(request.depart_id):
            body['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.depart_name):
            body['depart_name'] = request.depart_name
        if not UtilClient.is_unset(request.extend_field):
            body['extend_field'] = request.extend_field
        if not UtilClient.is_unset(request.external_traveler_list_shrink):
            body['external_traveler_list'] = request.external_traveler_list_shrink
        if not UtilClient.is_unset(request.external_traveler_standard_shrink):
            body['external_traveler_standard'] = request.external_traveler_standard_shrink
        if not UtilClient.is_unset(request.flight_budget):
            body['flight_budget'] = request.flight_budget
        if not UtilClient.is_unset(request.hotel_budget):
            body['hotel_budget'] = request.hotel_budget
        if not UtilClient.is_unset(request.hotel_share_shrink):
            body['hotel_share'] = request.hotel_share_shrink
        if not UtilClient.is_unset(request.itinerary_list_shrink):
            body['itinerary_list'] = request.itinerary_list_shrink
        if not UtilClient.is_unset(request.itinerary_rule):
            body['itinerary_rule'] = request.itinerary_rule
        if not UtilClient.is_unset(request.itinerary_set_list_shrink):
            body['itinerary_set_list'] = request.itinerary_set_list_shrink
        if not UtilClient.is_unset(request.limit_traveler):
            body['limit_traveler'] = request.limit_traveler
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            body['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.thirdpart_business_id):
            body['thirdpart_business_id'] = request.thirdpart_business_id
        if not UtilClient.is_unset(request.thirdpart_depart_id):
            body['thirdpart_depart_id'] = request.thirdpart_depart_id
        if not UtilClient.is_unset(request.together_book_rule):
            body['together_book_rule'] = request.together_book_rule
        if not UtilClient.is_unset(request.train_budget):
            body['train_budget'] = request.train_budget
        if not UtilClient.is_unset(request.traveler_list_shrink):
            body['traveler_list'] = request.traveler_list_shrink
        if not UtilClient.is_unset(request.traveler_standard_shrink):
            body['traveler_standard'] = request.traveler_standard_shrink
        if not UtilClient.is_unset(request.trip_cause):
            body['trip_cause'] = request.trip_cause
        if not UtilClient.is_unset(request.trip_day):
            body['trip_day'] = request.trip_day
        if not UtilClient.is_unset(request.trip_title):
            body['trip_title'] = request.trip_title
        if not UtilClient.is_unset(request.union_no):
            body['union_no'] = request.union_no
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_budget):
            body['vehicle_budget'] = request.vehicle_budget
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_modify_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.ApplyModifyRequest,
        headers: btrip_open_20220520_models.ApplyModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyModifyResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.ApplyModifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.external_traveler_list):
            request.external_traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_list, 'external_traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.external_traveler_standard):
            request.external_traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_traveler_standard, 'external_traveler_standard', 'json')
        if not UtilClient.is_unset(tmp_req.hotel_share):
            request.hotel_share_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_share, 'hotel_share', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_list):
            request.itinerary_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_list, 'itinerary_list', 'json')
        if not UtilClient.is_unset(tmp_req.itinerary_set_list):
            request.itinerary_set_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.itinerary_set_list, 'itinerary_set_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_list):
            request.traveler_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_list, 'traveler_list', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_standard):
            request.traveler_standard_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_standard, 'traveler_standard', 'json')
        body = {}
        if not UtilClient.is_unset(request.budget):
            body['budget'] = request.budget
        if not UtilClient.is_unset(request.budget_merge):
            body['budget_merge'] = request.budget_merge
        if not UtilClient.is_unset(request.corp_name):
            body['corp_name'] = request.corp_name
        if not UtilClient.is_unset(request.depart_id):
            body['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.depart_name):
            body['depart_name'] = request.depart_name
        if not UtilClient.is_unset(request.extend_field):
            body['extend_field'] = request.extend_field
        if not UtilClient.is_unset(request.external_traveler_list_shrink):
            body['external_traveler_list'] = request.external_traveler_list_shrink
        if not UtilClient.is_unset(request.external_traveler_standard_shrink):
            body['external_traveler_standard'] = request.external_traveler_standard_shrink
        if not UtilClient.is_unset(request.flight_budget):
            body['flight_budget'] = request.flight_budget
        if not UtilClient.is_unset(request.hotel_budget):
            body['hotel_budget'] = request.hotel_budget
        if not UtilClient.is_unset(request.hotel_share_shrink):
            body['hotel_share'] = request.hotel_share_shrink
        if not UtilClient.is_unset(request.itinerary_list_shrink):
            body['itinerary_list'] = request.itinerary_list_shrink
        if not UtilClient.is_unset(request.itinerary_rule):
            body['itinerary_rule'] = request.itinerary_rule
        if not UtilClient.is_unset(request.itinerary_set_list_shrink):
            body['itinerary_set_list'] = request.itinerary_set_list_shrink
        if not UtilClient.is_unset(request.limit_traveler):
            body['limit_traveler'] = request.limit_traveler
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            body['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.thirdpart_business_id):
            body['thirdpart_business_id'] = request.thirdpart_business_id
        if not UtilClient.is_unset(request.thirdpart_depart_id):
            body['thirdpart_depart_id'] = request.thirdpart_depart_id
        if not UtilClient.is_unset(request.together_book_rule):
            body['together_book_rule'] = request.together_book_rule
        if not UtilClient.is_unset(request.train_budget):
            body['train_budget'] = request.train_budget
        if not UtilClient.is_unset(request.traveler_list_shrink):
            body['traveler_list'] = request.traveler_list_shrink
        if not UtilClient.is_unset(request.traveler_standard_shrink):
            body['traveler_standard'] = request.traveler_standard_shrink
        if not UtilClient.is_unset(request.trip_cause):
            body['trip_cause'] = request.trip_cause
        if not UtilClient.is_unset(request.trip_day):
            body['trip_day'] = request.trip_day
        if not UtilClient.is_unset(request.trip_title):
            body['trip_title'] = request.trip_title
        if not UtilClient.is_unset(request.union_no):
            body['union_no'] = request.union_no
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_budget):
            body['vehicle_budget'] = request.vehicle_budget
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_modify(
        self,
        request: btrip_open_20220520_models.ApplyModifyRequest,
    ) -> btrip_open_20220520_models.ApplyModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyModifyHeaders()
        return self.apply_modify_with_options(request, headers, runtime)

    async def apply_modify_async(
        self,
        request: btrip_open_20220520_models.ApplyModifyRequest,
    ) -> btrip_open_20220520_models.ApplyModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyModifyHeaders()
        return await self.apply_modify_with_options_async(request, headers, runtime)

    def apply_query_with_options(
        self,
        request: btrip_open_20220520_models.ApplyQueryRequest,
        headers: btrip_open_20220520_models.ApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.apply_show_id):
            query['apply_show_id'] = request.apply_show_id
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_query_with_options_async(
        self,
        request: btrip_open_20220520_models.ApplyQueryRequest,
        headers: btrip_open_20220520_models.ApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.apply_show_id):
            query['apply_show_id'] = request.apply_show_id
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/biz-trip',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ApplyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_query(
        self,
        request: btrip_open_20220520_models.ApplyQueryRequest,
    ) -> btrip_open_20220520_models.ApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyQueryHeaders()
        return self.apply_query_with_options(request, headers, runtime)

    async def apply_query_async(
        self,
        request: btrip_open_20220520_models.ApplyQueryRequest,
    ) -> btrip_open_20220520_models.ApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ApplyQueryHeaders()
        return await self.apply_query_with_options_async(request, headers, runtime)

    def btrip_bill_info_adjust_with_options(
        self,
        request: btrip_open_20220520_models.BtripBillInfoAdjustRequest,
        headers: btrip_open_20220520_models.BtripBillInfoAdjustHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.BtripBillInfoAdjustResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.primary_id):
            body['primary_id'] = request.primary_id
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_department_id):
            body['third_part_department_id'] = request.third_part_department_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        if not UtilClient.is_unset(request.third_part_project_id):
            body['third_part_project_id'] = request.third_part_project_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BtripBillInfoAdjust',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/bill/v1/info/action/adjust',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.BtripBillInfoAdjustResponse(),
            self.call_api(params, req, runtime)
        )

    async def btrip_bill_info_adjust_with_options_async(
        self,
        request: btrip_open_20220520_models.BtripBillInfoAdjustRequest,
        headers: btrip_open_20220520_models.BtripBillInfoAdjustHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.BtripBillInfoAdjustResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.primary_id):
            body['primary_id'] = request.primary_id
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_department_id):
            body['third_part_department_id'] = request.third_part_department_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        if not UtilClient.is_unset(request.third_part_project_id):
            body['third_part_project_id'] = request.third_part_project_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BtripBillInfoAdjust',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/bill/v1/info/action/adjust',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.BtripBillInfoAdjustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def btrip_bill_info_adjust(
        self,
        request: btrip_open_20220520_models.BtripBillInfoAdjustRequest,
    ) -> btrip_open_20220520_models.BtripBillInfoAdjustResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.BtripBillInfoAdjustHeaders()
        return self.btrip_bill_info_adjust_with_options(request, headers, runtime)

    async def btrip_bill_info_adjust_async(
        self,
        request: btrip_open_20220520_models.BtripBillInfoAdjustRequest,
    ) -> btrip_open_20220520_models.BtripBillInfoAdjustResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.BtripBillInfoAdjustHeaders()
        return await self.btrip_bill_info_adjust_with_options_async(request, headers, runtime)

    def car_apply_add_with_options(
        self,
        request: btrip_open_20220520_models.CarApplyAddRequest,
        headers: btrip_open_20220520_models.CarApplyAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarApplyAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['cause'] = request.cause
        if not UtilClient.is_unset(request.city):
            body['city'] = request.city
        if not UtilClient.is_unset(request.date):
            body['date'] = request.date
        if not UtilClient.is_unset(request.finished_date):
            body['finished_date'] = request.finished_date
        if not UtilClient.is_unset(request.project_code):
            body['project_code'] = request.project_code
        if not UtilClient.is_unset(request.project_name):
            body['project_name'] = request.project_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['third_part_apply_id'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        if not UtilClient.is_unset(request.times_total):
            body['times_total'] = request.times_total
        if not UtilClient.is_unset(request.times_type):
            body['times_type'] = request.times_type
        if not UtilClient.is_unset(request.times_used):
            body['times_used'] = request.times_used
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CarApplyAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/car',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarApplyAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def car_apply_add_with_options_async(
        self,
        request: btrip_open_20220520_models.CarApplyAddRequest,
        headers: btrip_open_20220520_models.CarApplyAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarApplyAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['cause'] = request.cause
        if not UtilClient.is_unset(request.city):
            body['city'] = request.city
        if not UtilClient.is_unset(request.date):
            body['date'] = request.date
        if not UtilClient.is_unset(request.finished_date):
            body['finished_date'] = request.finished_date
        if not UtilClient.is_unset(request.project_code):
            body['project_code'] = request.project_code
        if not UtilClient.is_unset(request.project_name):
            body['project_name'] = request.project_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['third_part_apply_id'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        if not UtilClient.is_unset(request.times_total):
            body['times_total'] = request.times_total
        if not UtilClient.is_unset(request.times_type):
            body['times_type'] = request.times_type
        if not UtilClient.is_unset(request.times_used):
            body['times_used'] = request.times_used
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CarApplyAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/car',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarApplyAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def car_apply_add(
        self,
        request: btrip_open_20220520_models.CarApplyAddRequest,
    ) -> btrip_open_20220520_models.CarApplyAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarApplyAddHeaders()
        return self.car_apply_add_with_options(request, headers, runtime)

    async def car_apply_add_async(
        self,
        request: btrip_open_20220520_models.CarApplyAddRequest,
    ) -> btrip_open_20220520_models.CarApplyAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarApplyAddHeaders()
        return await self.car_apply_add_with_options_async(request, headers, runtime)

    def car_apply_modify_with_options(
        self,
        request: btrip_open_20220520_models.CarApplyModifyRequest,
        headers: btrip_open_20220520_models.CarApplyModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarApplyModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operate_time):
            body['operate_time'] = request.operate_time
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['third_part_apply_id'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CarApplyModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/car',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarApplyModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def car_apply_modify_with_options_async(
        self,
        request: btrip_open_20220520_models.CarApplyModifyRequest,
        headers: btrip_open_20220520_models.CarApplyModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarApplyModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operate_time):
            body['operate_time'] = request.operate_time
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['third_part_apply_id'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CarApplyModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/car',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarApplyModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def car_apply_modify(
        self,
        request: btrip_open_20220520_models.CarApplyModifyRequest,
    ) -> btrip_open_20220520_models.CarApplyModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarApplyModifyHeaders()
        return self.car_apply_modify_with_options(request, headers, runtime)

    async def car_apply_modify_async(
        self,
        request: btrip_open_20220520_models.CarApplyModifyRequest,
    ) -> btrip_open_20220520_models.CarApplyModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarApplyModifyHeaders()
        return await self.car_apply_modify_with_options_async(request, headers, runtime)

    def car_apply_query_with_options(
        self,
        request: btrip_open_20220520_models.CarApplyQueryRequest,
        headers: btrip_open_20220520_models.CarApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.created_end_at):
            query['created_end_at'] = request.created_end_at
        if not UtilClient.is_unset(request.created_start_at):
            query['created_start_at'] = request.created_start_at
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.third_part_apply_id):
            query['third_part_apply_id'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/car',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarApplyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def car_apply_query_with_options_async(
        self,
        request: btrip_open_20220520_models.CarApplyQueryRequest,
        headers: btrip_open_20220520_models.CarApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.created_end_at):
            query['created_end_at'] = request.created_end_at
        if not UtilClient.is_unset(request.created_start_at):
            query['created_start_at'] = request.created_start_at
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.third_part_apply_id):
            query['third_part_apply_id'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/car',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarApplyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def car_apply_query(
        self,
        request: btrip_open_20220520_models.CarApplyQueryRequest,
    ) -> btrip_open_20220520_models.CarApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarApplyQueryHeaders()
        return self.car_apply_query_with_options(request, headers, runtime)

    async def car_apply_query_async(
        self,
        request: btrip_open_20220520_models.CarApplyQueryRequest,
    ) -> btrip_open_20220520_models.CarApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarApplyQueryHeaders()
        return await self.car_apply_query_with_options_async(request, headers, runtime)

    def car_bill_settlement_query_with_options(
        self,
        request: btrip_open_20220520_models.CarBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.CarBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarBillSettlementQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def car_bill_settlement_query_with_options_async(
        self,
        request: btrip_open_20220520_models.CarBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.CarBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarBillSettlementQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def car_bill_settlement_query(
        self,
        request: btrip_open_20220520_models.CarBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.CarBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarBillSettlementQueryHeaders()
        return self.car_bill_settlement_query_with_options(request, headers, runtime)

    async def car_bill_settlement_query_async(
        self,
        request: btrip_open_20220520_models.CarBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.CarBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarBillSettlementQueryHeaders()
        return await self.car_bill_settlement_query_with_options_async(request, headers, runtime)

    def car_order_list_query_with_options(
        self,
        request: btrip_open_20220520_models.CarOrderListQueryRequest,
        headers: btrip_open_20220520_models.CarOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarOrderListQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def car_order_list_query_with_options_async(
        self,
        request: btrip_open_20220520_models.CarOrderListQueryRequest,
        headers: btrip_open_20220520_models.CarOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarOrderListQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def car_order_list_query(
        self,
        request: btrip_open_20220520_models.CarOrderListQueryRequest,
    ) -> btrip_open_20220520_models.CarOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarOrderListQueryHeaders()
        return self.car_order_list_query_with_options(request, headers, runtime)

    async def car_order_list_query_async(
        self,
        request: btrip_open_20220520_models.CarOrderListQueryRequest,
    ) -> btrip_open_20220520_models.CarOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarOrderListQueryHeaders()
        return await self.car_order_list_query_with_options_async(request, headers, runtime)

    def car_order_query_with_options(
        self,
        request: btrip_open_20220520_models.CarOrderQueryRequest,
        headers: btrip_open_20220520_models.CarOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.sub_order_id):
            query['sub_order_id'] = request.sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarOrderQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def car_order_query_with_options_async(
        self,
        request: btrip_open_20220520_models.CarOrderQueryRequest,
        headers: btrip_open_20220520_models.CarOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.sub_order_id):
            query['sub_order_id'] = request.sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CarOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarOrderQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def car_order_query(
        self,
        request: btrip_open_20220520_models.CarOrderQueryRequest,
    ) -> btrip_open_20220520_models.CarOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarOrderQueryHeaders()
        return self.car_order_query_with_options(request, headers, runtime)

    async def car_order_query_async(
        self,
        request: btrip_open_20220520_models.CarOrderQueryRequest,
    ) -> btrip_open_20220520_models.CarOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarOrderQueryHeaders()
        return await self.car_order_query_with_options_async(request, headers, runtime)

    def car_scene_query_with_options(
        self,
        headers: btrip_open_20220520_models.CarSceneQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarSceneQueryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='CarSceneQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarSceneQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def car_scene_query_with_options_async(
        self,
        headers: btrip_open_20220520_models.CarSceneQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CarSceneQueryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='CarSceneQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/car/v1/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CarSceneQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def car_scene_query(self) -> btrip_open_20220520_models.CarSceneQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarSceneQueryHeaders()
        return self.car_scene_query_with_options(headers, runtime)

    async def car_scene_query_async(self) -> btrip_open_20220520_models.CarSceneQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CarSceneQueryHeaders()
        return await self.car_scene_query_with_options_async(headers, runtime)

    def city_search_with_options(
        self,
        request: btrip_open_20220520_models.CitySearchRequest,
        headers: btrip_open_20220520_models.CitySearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CitySearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CitySearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/city',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CitySearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def city_search_with_options_async(
        self,
        request: btrip_open_20220520_models.CitySearchRequest,
        headers: btrip_open_20220520_models.CitySearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CitySearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CitySearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/city',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CitySearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def city_search(
        self,
        request: btrip_open_20220520_models.CitySearchRequest,
    ) -> btrip_open_20220520_models.CitySearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CitySearchHeaders()
        return self.city_search_with_options(request, headers, runtime)

    async def city_search_async(
        self,
        request: btrip_open_20220520_models.CitySearchRequest,
    ) -> btrip_open_20220520_models.CitySearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CitySearchHeaders()
        return await self.city_search_with_options_async(request, headers, runtime)

    def common_apply_query_with_options(
        self,
        request: btrip_open_20220520_models.CommonApplyQueryRequest,
        headers: btrip_open_20220520_models.CommonApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CommonApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.biz_category):
            query['biz_category'] = request.biz_category
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommonApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/common',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CommonApplyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def common_apply_query_with_options_async(
        self,
        request: btrip_open_20220520_models.CommonApplyQueryRequest,
        headers: btrip_open_20220520_models.CommonApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CommonApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.biz_category):
            query['biz_category'] = request.biz_category
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommonApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/common',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CommonApplyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def common_apply_query(
        self,
        request: btrip_open_20220520_models.CommonApplyQueryRequest,
    ) -> btrip_open_20220520_models.CommonApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CommonApplyQueryHeaders()
        return self.common_apply_query_with_options(request, headers, runtime)

    async def common_apply_query_async(
        self,
        request: btrip_open_20220520_models.CommonApplyQueryRequest,
    ) -> btrip_open_20220520_models.CommonApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CommonApplyQueryHeaders()
        return await self.common_apply_query_with_options_async(request, headers, runtime)

    def common_apply_sync_with_options(
        self,
        request: btrip_open_20220520_models.CommonApplySyncRequest,
        headers: btrip_open_20220520_models.CommonApplySyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CommonApplySyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.biz_category):
            query['biz_category'] = request.biz_category
        if not UtilClient.is_unset(request.remark):
            query['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.thirdparty_flow_id):
            query['thirdparty_flow_id'] = request.thirdparty_flow_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommonApplySync',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/syn-common',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CommonApplySyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def common_apply_sync_with_options_async(
        self,
        request: btrip_open_20220520_models.CommonApplySyncRequest,
        headers: btrip_open_20220520_models.CommonApplySyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CommonApplySyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.biz_category):
            query['biz_category'] = request.biz_category
        if not UtilClient.is_unset(request.remark):
            query['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.thirdparty_flow_id):
            query['thirdparty_flow_id'] = request.thirdparty_flow_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommonApplySync',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/syn-common',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CommonApplySyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def common_apply_sync(
        self,
        request: btrip_open_20220520_models.CommonApplySyncRequest,
    ) -> btrip_open_20220520_models.CommonApplySyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CommonApplySyncHeaders()
        return self.common_apply_sync_with_options(request, headers, runtime)

    async def common_apply_sync_async(
        self,
        request: btrip_open_20220520_models.CommonApplySyncRequest,
    ) -> btrip_open_20220520_models.CommonApplySyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CommonApplySyncHeaders()
        return await self.common_apply_sync_with_options_async(request, headers, runtime)

    def corp_auth_link_info_query_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CorpAuthLinkInfoQueryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CorpAuthLinkInfoQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/corp-authority-link/v1/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CorpAuthLinkInfoQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def corp_auth_link_info_query_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CorpAuthLinkInfoQueryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CorpAuthLinkInfoQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/corp-authority-link/v1/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CorpAuthLinkInfoQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def corp_auth_link_info_query(self) -> btrip_open_20220520_models.CorpAuthLinkInfoQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.corp_auth_link_info_query_with_options(headers, runtime)

    async def corp_auth_link_info_query_async(self) -> btrip_open_20220520_models.CorpAuthLinkInfoQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.corp_auth_link_info_query_with_options_async(headers, runtime)

    def corp_token_with_options(
        self,
        request: btrip_open_20220520_models.CorpTokenRequest,
        headers: btrip_open_20220520_models.CorpTokenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CorpTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        if not UtilClient.is_unset(request.corp_id):
            query['corp_id'] = request.corp_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_access_token):
            real_headers['x-acs-btrip-access-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CorpToken',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/btrip-open-auth/v1/corp-token/action/take',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CorpTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def corp_token_with_options_async(
        self,
        request: btrip_open_20220520_models.CorpTokenRequest,
        headers: btrip_open_20220520_models.CorpTokenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CorpTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        if not UtilClient.is_unset(request.corp_id):
            query['corp_id'] = request.corp_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_access_token):
            real_headers['x-acs-btrip-access-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CorpToken',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/btrip-open-auth/v1/corp-token/action/take',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CorpTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def corp_token(
        self,
        request: btrip_open_20220520_models.CorpTokenRequest,
    ) -> btrip_open_20220520_models.CorpTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CorpTokenHeaders()
        return self.corp_token_with_options(request, headers, runtime)

    async def corp_token_async(
        self,
        request: btrip_open_20220520_models.CorpTokenRequest,
    ) -> btrip_open_20220520_models.CorpTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CorpTokenHeaders()
        return await self.corp_token_with_options_async(request, headers, runtime)

    def cost_center_delete_with_options(
        self,
        request: btrip_open_20220520_models.CostCenterDeleteRequest,
        headers: btrip_open_20220520_models.CostCenterDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.thirdpart_id):
            query['thirdpart_id'] = request.thirdpart_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CostCenterDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/delete-costcenter',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def cost_center_delete_with_options_async(
        self,
        request: btrip_open_20220520_models.CostCenterDeleteRequest,
        headers: btrip_open_20220520_models.CostCenterDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.thirdpart_id):
            query['thirdpart_id'] = request.thirdpart_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CostCenterDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/delete-costcenter',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cost_center_delete(
        self,
        request: btrip_open_20220520_models.CostCenterDeleteRequest,
    ) -> btrip_open_20220520_models.CostCenterDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterDeleteHeaders()
        return self.cost_center_delete_with_options(request, headers, runtime)

    async def cost_center_delete_async(
        self,
        request: btrip_open_20220520_models.CostCenterDeleteRequest,
    ) -> btrip_open_20220520_models.CostCenterDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterDeleteHeaders()
        return await self.cost_center_delete_with_options_async(request, headers, runtime)

    def cost_center_modify_with_options(
        self,
        request: btrip_open_20220520_models.CostCenterModifyRequest,
        headers: btrip_open_20220520_models.CostCenterModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_no):
            body['alipay_no'] = request.alipay_no
        if not UtilClient.is_unset(request.number):
            body['number'] = request.number
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CostCenterModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/modify-costcenter',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def cost_center_modify_with_options_async(
        self,
        request: btrip_open_20220520_models.CostCenterModifyRequest,
        headers: btrip_open_20220520_models.CostCenterModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_no):
            body['alipay_no'] = request.alipay_no
        if not UtilClient.is_unset(request.number):
            body['number'] = request.number
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CostCenterModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/modify-costcenter',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cost_center_modify(
        self,
        request: btrip_open_20220520_models.CostCenterModifyRequest,
    ) -> btrip_open_20220520_models.CostCenterModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterModifyHeaders()
        return self.cost_center_modify_with_options(request, headers, runtime)

    async def cost_center_modify_async(
        self,
        request: btrip_open_20220520_models.CostCenterModifyRequest,
    ) -> btrip_open_20220520_models.CostCenterModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterModifyHeaders()
        return await self.cost_center_modify_with_options_async(request, headers, runtime)

    def cost_center_query_with_options(
        self,
        request: btrip_open_20220520_models.CostCenterQueryRequest,
        headers: btrip_open_20220520_models.CostCenterQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_org_entity):
            query['need_org_entity'] = request.need_org_entity
        if not UtilClient.is_unset(request.thirdpart_id):
            query['thirdpart_id'] = request.thirdpart_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CostCenterQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/costcenter',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def cost_center_query_with_options_async(
        self,
        request: btrip_open_20220520_models.CostCenterQueryRequest,
        headers: btrip_open_20220520_models.CostCenterQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_org_entity):
            query['need_org_entity'] = request.need_org_entity
        if not UtilClient.is_unset(request.thirdpart_id):
            query['thirdpart_id'] = request.thirdpart_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CostCenterQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/costcenter',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cost_center_query(
        self,
        request: btrip_open_20220520_models.CostCenterQueryRequest,
    ) -> btrip_open_20220520_models.CostCenterQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterQueryHeaders()
        return self.cost_center_query_with_options(request, headers, runtime)

    async def cost_center_query_async(
        self,
        request: btrip_open_20220520_models.CostCenterQueryRequest,
    ) -> btrip_open_20220520_models.CostCenterQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterQueryHeaders()
        return await self.cost_center_query_with_options_async(request, headers, runtime)

    def cost_center_save_with_options(
        self,
        request: btrip_open_20220520_models.CostCenterSaveRequest,
        headers: btrip_open_20220520_models.CostCenterSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterSaveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_no):
            body['alipay_no'] = request.alipay_no
        if not UtilClient.is_unset(request.number):
            body['number'] = request.number
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CostCenterSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/save-costcenter',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def cost_center_save_with_options_async(
        self,
        request: btrip_open_20220520_models.CostCenterSaveRequest,
        headers: btrip_open_20220520_models.CostCenterSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CostCenterSaveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_no):
            body['alipay_no'] = request.alipay_no
        if not UtilClient.is_unset(request.number):
            body['number'] = request.number
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CostCenterSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/save-costcenter',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CostCenterSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cost_center_save(
        self,
        request: btrip_open_20220520_models.CostCenterSaveRequest,
    ) -> btrip_open_20220520_models.CostCenterSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterSaveHeaders()
        return self.cost_center_save_with_options(request, headers, runtime)

    async def cost_center_save_async(
        self,
        request: btrip_open_20220520_models.CostCenterSaveRequest,
    ) -> btrip_open_20220520_models.CostCenterSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CostCenterSaveHeaders()
        return await self.cost_center_save_with_options_async(request, headers, runtime)

    def create_sub_corp_with_options(
        self,
        request: btrip_open_20220520_models.CreateSubCorpRequest,
        headers: btrip_open_20220520_models.CreateSubCorpHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CreateSubCorpResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.outer_corp_id):
            body['outer_corp_id'] = request.outer_corp_id
        if not UtilClient.is_unset(request.outer_corp_name):
            body['outer_corp_name'] = request.outer_corp_name
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubCorp',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/sub_corps/v1/corps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CreateSubCorpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sub_corp_with_options_async(
        self,
        request: btrip_open_20220520_models.CreateSubCorpRequest,
        headers: btrip_open_20220520_models.CreateSubCorpHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.CreateSubCorpResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.outer_corp_id):
            body['outer_corp_id'] = request.outer_corp_id
        if not UtilClient.is_unset(request.outer_corp_name):
            body['outer_corp_name'] = request.outer_corp_name
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubCorp',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/sub_corps/v1/corps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.CreateSubCorpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sub_corp(
        self,
        request: btrip_open_20220520_models.CreateSubCorpRequest,
    ) -> btrip_open_20220520_models.CreateSubCorpResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CreateSubCorpHeaders()
        return self.create_sub_corp_with_options(request, headers, runtime)

    async def create_sub_corp_async(
        self,
        request: btrip_open_20220520_models.CreateSubCorpRequest,
    ) -> btrip_open_20220520_models.CreateSubCorpResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.CreateSubCorpHeaders()
        return await self.create_sub_corp_with_options_async(request, headers, runtime)

    def delete_invoice_entity_with_options(
        self,
        tmp_req: btrip_open_20220520_models.DeleteInvoiceEntityRequest,
        headers: btrip_open_20220520_models.DeleteInvoiceEntityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.DeleteInvoiceEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.DeleteInvoiceEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        query = {}
        if not UtilClient.is_unset(request.del_all):
            query['del_all'] = request.del_all
        if not UtilClient.is_unset(request.entities_shrink):
            query['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInvoiceEntity',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/entities',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.DeleteInvoiceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_invoice_entity_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.DeleteInvoiceEntityRequest,
        headers: btrip_open_20220520_models.DeleteInvoiceEntityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.DeleteInvoiceEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.DeleteInvoiceEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        query = {}
        if not UtilClient.is_unset(request.del_all):
            query['del_all'] = request.del_all
        if not UtilClient.is_unset(request.entities_shrink):
            query['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInvoiceEntity',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/entities',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.DeleteInvoiceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_invoice_entity(
        self,
        request: btrip_open_20220520_models.DeleteInvoiceEntityRequest,
    ) -> btrip_open_20220520_models.DeleteInvoiceEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.DeleteInvoiceEntityHeaders()
        return self.delete_invoice_entity_with_options(request, headers, runtime)

    async def delete_invoice_entity_async(
        self,
        request: btrip_open_20220520_models.DeleteInvoiceEntityRequest,
    ) -> btrip_open_20220520_models.DeleteInvoiceEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.DeleteInvoiceEntityHeaders()
        return await self.delete_invoice_entity_with_options_async(request, headers, runtime)

    def department_save_with_options(
        self,
        tmp_req: btrip_open_20220520_models.DepartmentSaveRequest,
        headers: btrip_open_20220520_models.DepartmentSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.DepartmentSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.DepartmentSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.depart_list):
            request.depart_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.depart_list, 'depart_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.depart_list_shrink):
            body['depart_list'] = request.depart_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DepartmentSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/department/v1/department',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.DepartmentSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def department_save_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.DepartmentSaveRequest,
        headers: btrip_open_20220520_models.DepartmentSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.DepartmentSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.DepartmentSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.depart_list):
            request.depart_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.depart_list, 'depart_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.depart_list_shrink):
            body['depart_list'] = request.depart_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DepartmentSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/department/v1/department',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.DepartmentSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def department_save(
        self,
        request: btrip_open_20220520_models.DepartmentSaveRequest,
    ) -> btrip_open_20220520_models.DepartmentSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.DepartmentSaveHeaders()
        return self.department_save_with_options(request, headers, runtime)

    async def department_save_async(
        self,
        request: btrip_open_20220520_models.DepartmentSaveRequest,
    ) -> btrip_open_20220520_models.DepartmentSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.DepartmentSaveHeaders()
        return await self.department_save_with_options_async(request, headers, runtime)

    def entity_add_with_options(
        self,
        tmp_req: btrip_open_20220520_models.EntityAddRequest,
        headers: btrip_open_20220520_models.EntityAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EntityAddResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.EntityAddShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_dolist):
            request.entity_dolist_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_dolist, 'entity_d_o_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.entity_dolist_shrink):
            body['entity_d_o_list'] = request.entity_dolist_shrink
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EntityAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/add-entity',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EntityAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def entity_add_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.EntityAddRequest,
        headers: btrip_open_20220520_models.EntityAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EntityAddResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.EntityAddShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_dolist):
            request.entity_dolist_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_dolist, 'entity_d_o_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.entity_dolist_shrink):
            body['entity_d_o_list'] = request.entity_dolist_shrink
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EntityAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/add-entity',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EntityAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def entity_add(
        self,
        request: btrip_open_20220520_models.EntityAddRequest,
    ) -> btrip_open_20220520_models.EntityAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EntityAddHeaders()
        return self.entity_add_with_options(request, headers, runtime)

    async def entity_add_async(
        self,
        request: btrip_open_20220520_models.EntityAddRequest,
    ) -> btrip_open_20220520_models.EntityAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EntityAddHeaders()
        return await self.entity_add_with_options_async(request, headers, runtime)

    def entity_delete_with_options(
        self,
        tmp_req: btrip_open_20220520_models.EntityDeleteRequest,
        headers: btrip_open_20220520_models.EntityDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EntityDeleteResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.EntityDeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_dolist):
            request.entity_dolist_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_dolist, 'entity_d_o_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.del_all):
            query['del_all'] = request.del_all
        if not UtilClient.is_unset(request.thirdpart_id):
            query['thirdpart_id'] = request.thirdpart_id
        body = {}
        if not UtilClient.is_unset(request.entity_dolist_shrink):
            body['entity_d_o_list'] = request.entity_dolist_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EntityDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/entity/action/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EntityDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def entity_delete_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.EntityDeleteRequest,
        headers: btrip_open_20220520_models.EntityDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EntityDeleteResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.EntityDeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_dolist):
            request.entity_dolist_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_dolist, 'entity_d_o_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.del_all):
            query['del_all'] = request.del_all
        if not UtilClient.is_unset(request.thirdpart_id):
            query['thirdpart_id'] = request.thirdpart_id
        body = {}
        if not UtilClient.is_unset(request.entity_dolist_shrink):
            body['entity_d_o_list'] = request.entity_dolist_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EntityDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/entity/action/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EntityDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def entity_delete(
        self,
        request: btrip_open_20220520_models.EntityDeleteRequest,
    ) -> btrip_open_20220520_models.EntityDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EntityDeleteHeaders()
        return self.entity_delete_with_options(request, headers, runtime)

    async def entity_delete_async(
        self,
        request: btrip_open_20220520_models.EntityDeleteRequest,
    ) -> btrip_open_20220520_models.EntityDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EntityDeleteHeaders()
        return await self.entity_delete_with_options_async(request, headers, runtime)

    def entity_set_with_options(
        self,
        tmp_req: btrip_open_20220520_models.EntitySetRequest,
        headers: btrip_open_20220520_models.EntitySetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EntitySetResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.EntitySetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_dolist):
            request.entity_dolist_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_dolist, 'entity_d_o_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.entity_dolist_shrink):
            body['entity_d_o_list'] = request.entity_dolist_shrink
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EntitySet',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/set-entity',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EntitySetResponse(),
            self.call_api(params, req, runtime)
        )

    async def entity_set_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.EntitySetRequest,
        headers: btrip_open_20220520_models.EntitySetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EntitySetResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.EntitySetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_dolist):
            request.entity_dolist_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_dolist, 'entity_d_o_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.entity_dolist_shrink):
            body['entity_d_o_list'] = request.entity_dolist_shrink
        if not UtilClient.is_unset(request.thirdpart_id):
            body['thirdpart_id'] = request.thirdpart_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EntitySet',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/set-entity',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EntitySetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def entity_set(
        self,
        request: btrip_open_20220520_models.EntitySetRequest,
    ) -> btrip_open_20220520_models.EntitySetResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EntitySetHeaders()
        return self.entity_set_with_options(request, headers, runtime)

    async def entity_set_async(
        self,
        request: btrip_open_20220520_models.EntitySetRequest,
    ) -> btrip_open_20220520_models.EntitySetResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EntitySetHeaders()
        return await self.entity_set_with_options_async(request, headers, runtime)

    def estimated_price_query_with_options(
        self,
        request: btrip_open_20220520_models.EstimatedPriceQueryRequest,
        headers: btrip_open_20220520_models.EstimatedPriceQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EstimatedPriceQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arr_city):
            query['arr_city'] = request.arr_city
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.dep_city):
            query['dep_city'] = request.dep_city
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.itinerary_id):
            query['itinerary_id'] = request.itinerary_id
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.sub_corp_id):
            query['sub_corp_id'] = request.sub_corp_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EstimatedPriceQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/estimated-price',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EstimatedPriceQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def estimated_price_query_with_options_async(
        self,
        request: btrip_open_20220520_models.EstimatedPriceQueryRequest,
        headers: btrip_open_20220520_models.EstimatedPriceQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.EstimatedPriceQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arr_city):
            query['arr_city'] = request.arr_city
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.dep_city):
            query['dep_city'] = request.dep_city
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.itinerary_id):
            query['itinerary_id'] = request.itinerary_id
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.sub_corp_id):
            query['sub_corp_id'] = request.sub_corp_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EstimatedPriceQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/costcenter/v1/estimated-price',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.EstimatedPriceQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def estimated_price_query(
        self,
        request: btrip_open_20220520_models.EstimatedPriceQueryRequest,
    ) -> btrip_open_20220520_models.EstimatedPriceQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EstimatedPriceQueryHeaders()
        return self.estimated_price_query_with_options(request, headers, runtime)

    async def estimated_price_query_async(
        self,
        request: btrip_open_20220520_models.EstimatedPriceQueryRequest,
    ) -> btrip_open_20220520_models.EstimatedPriceQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.EstimatedPriceQueryHeaders()
        return await self.estimated_price_query_with_options_async(request, headers, runtime)

    def exceed_apply_sync_with_options(
        self,
        request: btrip_open_20220520_models.ExceedApplySyncRequest,
        headers: btrip_open_20220520_models.ExceedApplySyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ExceedApplySyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.biz_category):
            query['biz_category'] = request.biz_category
        if not UtilClient.is_unset(request.remark):
            query['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.thirdparty_flow_id):
            query['thirdparty_flow_id'] = request.thirdparty_flow_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExceedApplySync',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/syn-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ExceedApplySyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def exceed_apply_sync_with_options_async(
        self,
        request: btrip_open_20220520_models.ExceedApplySyncRequest,
        headers: btrip_open_20220520_models.ExceedApplySyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ExceedApplySyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.biz_category):
            query['biz_category'] = request.biz_category
        if not UtilClient.is_unset(request.remark):
            query['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.thirdparty_flow_id):
            query['thirdparty_flow_id'] = request.thirdparty_flow_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExceedApplySync',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/syn-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ExceedApplySyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exceed_apply_sync(
        self,
        request: btrip_open_20220520_models.ExceedApplySyncRequest,
    ) -> btrip_open_20220520_models.ExceedApplySyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ExceedApplySyncHeaders()
        return self.exceed_apply_sync_with_options(request, headers, runtime)

    async def exceed_apply_sync_async(
        self,
        request: btrip_open_20220520_models.ExceedApplySyncRequest,
    ) -> btrip_open_20220520_models.ExceedApplySyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ExceedApplySyncHeaders()
        return await self.exceed_apply_sync_with_options_async(request, headers, runtime)

    def flight_bill_settlement_query_with_options(
        self,
        request: btrip_open_20220520_models.FlightBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.FlightBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/flight/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightBillSettlementQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_bill_settlement_query_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.FlightBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/flight/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightBillSettlementQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_bill_settlement_query(
        self,
        request: btrip_open_20220520_models.FlightBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.FlightBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightBillSettlementQueryHeaders()
        return self.flight_bill_settlement_query_with_options(request, headers, runtime)

    async def flight_bill_settlement_query_async(
        self,
        request: btrip_open_20220520_models.FlightBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.FlightBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightBillSettlementQueryHeaders()
        return await self.flight_bill_settlement_query_with_options_async(request, headers, runtime)

    def flight_cancel_order_with_options(
        self,
        request: btrip_open_20220520_models.FlightCancelOrderRequest,
        headers: btrip_open_20220520_models.FlightCancelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightCancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightCancelOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightCancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_cancel_order_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightCancelOrderRequest,
        headers: btrip_open_20220520_models.FlightCancelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightCancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightCancelOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightCancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_cancel_order(
        self,
        request: btrip_open_20220520_models.FlightCancelOrderRequest,
    ) -> btrip_open_20220520_models.FlightCancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightCancelOrderHeaders()
        return self.flight_cancel_order_with_options(request, headers, runtime)

    async def flight_cancel_order_async(
        self,
        request: btrip_open_20220520_models.FlightCancelOrderRequest,
    ) -> btrip_open_20220520_models.FlightCancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightCancelOrderHeaders()
        return await self.flight_cancel_order_with_options_async(request, headers, runtime)

    def flight_create_order_with_options(
        self,
        tmp_req: btrip_open_20220520_models.FlightCreateOrderRequest,
        headers: btrip_open_20220520_models.FlightCreateOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightCreateOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightCreateOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_info):
            request.contact_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_info, 'contact_info', 'json')
        if not UtilClient.is_unset(tmp_req.order_attr):
            request.order_attr_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_attr, 'order_attr', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_info_list):
            request.traveler_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_info_list, 'traveler_info_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.arr_airport_code):
            body['arr_airport_code'] = request.arr_airport_code
        if not UtilClient.is_unset(request.arr_city_code):
            body['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.auto_pay):
            body['auto_pay'] = request.auto_pay
        if not UtilClient.is_unset(request.buyer_name):
            body['buyer_name'] = request.buyer_name
        if not UtilClient.is_unset(request.buyer_unique_key):
            body['buyer_unique_key'] = request.buyer_unique_key
        if not UtilClient.is_unset(request.contact_info_shrink):
            body['contact_info'] = request.contact_info_shrink
        if not UtilClient.is_unset(request.dep_airport_code):
            body['dep_airport_code'] = request.dep_airport_code
        if not UtilClient.is_unset(request.dep_city_code):
            body['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_date):
            body['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.order_attr_shrink):
            body['order_attr'] = request.order_attr_shrink
        if not UtilClient.is_unset(request.order_params):
            body['order_params'] = request.order_params
        if not UtilClient.is_unset(request.ota_item_id):
            body['ota_item_id'] = request.ota_item_id
        if not UtilClient.is_unset(request.price):
            body['price'] = request.price
        if not UtilClient.is_unset(request.receipt_address):
            body['receipt_address'] = request.receipt_address
        if not UtilClient.is_unset(request.receipt_target):
            body['receipt_target'] = request.receipt_target
        if not UtilClient.is_unset(request.receipt_title):
            body['receipt_title'] = request.receipt_title
        if not UtilClient.is_unset(request.traveler_info_list_shrink):
            body['traveler_info_list'] = request.traveler_info_list_shrink
        if not UtilClient.is_unset(request.trip_type):
            body['trip_type'] = request.trip_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FlightCreateOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightCreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_create_order_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.FlightCreateOrderRequest,
        headers: btrip_open_20220520_models.FlightCreateOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightCreateOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightCreateOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_info):
            request.contact_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_info, 'contact_info', 'json')
        if not UtilClient.is_unset(tmp_req.order_attr):
            request.order_attr_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_attr, 'order_attr', 'json')
        if not UtilClient.is_unset(tmp_req.traveler_info_list):
            request.traveler_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_info_list, 'traveler_info_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.arr_airport_code):
            body['arr_airport_code'] = request.arr_airport_code
        if not UtilClient.is_unset(request.arr_city_code):
            body['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.auto_pay):
            body['auto_pay'] = request.auto_pay
        if not UtilClient.is_unset(request.buyer_name):
            body['buyer_name'] = request.buyer_name
        if not UtilClient.is_unset(request.buyer_unique_key):
            body['buyer_unique_key'] = request.buyer_unique_key
        if not UtilClient.is_unset(request.contact_info_shrink):
            body['contact_info'] = request.contact_info_shrink
        if not UtilClient.is_unset(request.dep_airport_code):
            body['dep_airport_code'] = request.dep_airport_code
        if not UtilClient.is_unset(request.dep_city_code):
            body['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_date):
            body['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.order_attr_shrink):
            body['order_attr'] = request.order_attr_shrink
        if not UtilClient.is_unset(request.order_params):
            body['order_params'] = request.order_params
        if not UtilClient.is_unset(request.ota_item_id):
            body['ota_item_id'] = request.ota_item_id
        if not UtilClient.is_unset(request.price):
            body['price'] = request.price
        if not UtilClient.is_unset(request.receipt_address):
            body['receipt_address'] = request.receipt_address
        if not UtilClient.is_unset(request.receipt_target):
            body['receipt_target'] = request.receipt_target
        if not UtilClient.is_unset(request.receipt_title):
            body['receipt_title'] = request.receipt_title
        if not UtilClient.is_unset(request.traveler_info_list_shrink):
            body['traveler_info_list'] = request.traveler_info_list_shrink
        if not UtilClient.is_unset(request.trip_type):
            body['trip_type'] = request.trip_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FlightCreateOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightCreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_create_order(
        self,
        request: btrip_open_20220520_models.FlightCreateOrderRequest,
    ) -> btrip_open_20220520_models.FlightCreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightCreateOrderHeaders()
        return self.flight_create_order_with_options(request, headers, runtime)

    async def flight_create_order_async(
        self,
        request: btrip_open_20220520_models.FlightCreateOrderRequest,
    ) -> btrip_open_20220520_models.FlightCreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightCreateOrderHeaders()
        return await self.flight_create_order_with_options_async(request, headers, runtime)

    def flight_exceed_apply_query_with_options(
        self,
        request: btrip_open_20220520_models.FlightExceedApplyQueryRequest,
        headers: btrip_open_20220520_models.FlightExceedApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightExceedApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightExceedApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/flight-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightExceedApplyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_exceed_apply_query_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightExceedApplyQueryRequest,
        headers: btrip_open_20220520_models.FlightExceedApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightExceedApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightExceedApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/flight-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightExceedApplyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_exceed_apply_query(
        self,
        request: btrip_open_20220520_models.FlightExceedApplyQueryRequest,
    ) -> btrip_open_20220520_models.FlightExceedApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightExceedApplyQueryHeaders()
        return self.flight_exceed_apply_query_with_options(request, headers, runtime)

    async def flight_exceed_apply_query_async(
        self,
        request: btrip_open_20220520_models.FlightExceedApplyQueryRequest,
    ) -> btrip_open_20220520_models.FlightExceedApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightExceedApplyQueryHeaders()
        return await self.flight_exceed_apply_query_with_options_async(request, headers, runtime)

    def flight_itinerary_scan_query_with_options(
        self,
        request: btrip_open_20220520_models.FlightItineraryScanQueryRequest,
        headers: btrip_open_20220520_models.FlightItineraryScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightItineraryScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightItineraryScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/flight-itinerary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightItineraryScanQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_itinerary_scan_query_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightItineraryScanQueryRequest,
        headers: btrip_open_20220520_models.FlightItineraryScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightItineraryScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightItineraryScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/flight-itinerary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightItineraryScanQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_itinerary_scan_query(
        self,
        request: btrip_open_20220520_models.FlightItineraryScanQueryRequest,
    ) -> btrip_open_20220520_models.FlightItineraryScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightItineraryScanQueryHeaders()
        return self.flight_itinerary_scan_query_with_options(request, headers, runtime)

    async def flight_itinerary_scan_query_async(
        self,
        request: btrip_open_20220520_models.FlightItineraryScanQueryRequest,
    ) -> btrip_open_20220520_models.FlightItineraryScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightItineraryScanQueryHeaders()
        return await self.flight_itinerary_scan_query_with_options_async(request, headers, runtime)

    def flight_listing_search_with_options(
        self,
        request: btrip_open_20220520_models.FlightListingSearchRequest,
        headers: btrip_open_20220520_models.FlightListingSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightListingSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airline_code):
            query['airline_code'] = request.airline_code
        if not UtilClient.is_unset(request.arr_city_code):
            query['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.cabin_class):
            query['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.dep_city_code):
            query['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightListingSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/flight/action/listing-search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightListingSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_listing_search_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightListingSearchRequest,
        headers: btrip_open_20220520_models.FlightListingSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightListingSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airline_code):
            query['airline_code'] = request.airline_code
        if not UtilClient.is_unset(request.arr_city_code):
            query['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.cabin_class):
            query['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.dep_city_code):
            query['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightListingSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/flight/action/listing-search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightListingSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_listing_search(
        self,
        request: btrip_open_20220520_models.FlightListingSearchRequest,
    ) -> btrip_open_20220520_models.FlightListingSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightListingSearchHeaders()
        return self.flight_listing_search_with_options(request, headers, runtime)

    async def flight_listing_search_async(
        self,
        request: btrip_open_20220520_models.FlightListingSearchRequest,
    ) -> btrip_open_20220520_models.FlightListingSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightListingSearchHeaders()
        return await self.flight_listing_search_with_options_async(request, headers, runtime)

    def flight_order_detail_info_with_options(
        self,
        request: btrip_open_20220520_models.FlightOrderDetailInfoRequest,
        headers: btrip_open_20220520_models.FlightOrderDetailInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOrderDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOrderDetailInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOrderDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_order_detail_info_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightOrderDetailInfoRequest,
        headers: btrip_open_20220520_models.FlightOrderDetailInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOrderDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOrderDetailInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOrderDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_order_detail_info(
        self,
        request: btrip_open_20220520_models.FlightOrderDetailInfoRequest,
    ) -> btrip_open_20220520_models.FlightOrderDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOrderDetailInfoHeaders()
        return self.flight_order_detail_info_with_options(request, headers, runtime)

    async def flight_order_detail_info_async(
        self,
        request: btrip_open_20220520_models.FlightOrderDetailInfoRequest,
    ) -> btrip_open_20220520_models.FlightOrderDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOrderDetailInfoHeaders()
        return await self.flight_order_detail_info_with_options_async(request, headers, runtime)

    def flight_order_list_query_with_options(
        self,
        request: btrip_open_20220520_models.FlightOrderListQueryRequest,
        headers: btrip_open_20220520_models.FlightOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/flight/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOrderListQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_order_list_query_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightOrderListQueryRequest,
        headers: btrip_open_20220520_models.FlightOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/flight/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOrderListQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_order_list_query(
        self,
        request: btrip_open_20220520_models.FlightOrderListQueryRequest,
    ) -> btrip_open_20220520_models.FlightOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOrderListQueryHeaders()
        return self.flight_order_list_query_with_options(request, headers, runtime)

    async def flight_order_list_query_async(
        self,
        request: btrip_open_20220520_models.FlightOrderListQueryRequest,
    ) -> btrip_open_20220520_models.FlightOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOrderListQueryHeaders()
        return await self.flight_order_list_query_with_options_async(request, headers, runtime)

    def flight_order_query_with_options(
        self,
        request: btrip_open_20220520_models.FlightOrderQueryRequest,
        headers: btrip_open_20220520_models.FlightOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/flight/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOrderQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_order_query_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightOrderQueryRequest,
        headers: btrip_open_20220520_models.FlightOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/flight/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOrderQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_order_query(
        self,
        request: btrip_open_20220520_models.FlightOrderQueryRequest,
    ) -> btrip_open_20220520_models.FlightOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOrderQueryHeaders()
        return self.flight_order_query_with_options(request, headers, runtime)

    async def flight_order_query_async(
        self,
        request: btrip_open_20220520_models.FlightOrderQueryRequest,
    ) -> btrip_open_20220520_models.FlightOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOrderQueryHeaders()
        return await self.flight_order_query_with_options_async(request, headers, runtime)

    def flight_ota_search_with_options(
        self,
        request: btrip_open_20220520_models.FlightOtaSearchRequest,
        headers: btrip_open_20220520_models.FlightOtaSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOtaSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airline_code):
            query['airline_code'] = request.airline_code
        if not UtilClient.is_unset(request.arr_city_code):
            query['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.cabin_class):
            query['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.carrier_flight_no):
            query['carrier_flight_no'] = request.carrier_flight_no
        if not UtilClient.is_unset(request.dep_city_code):
            query['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.flight_no):
            query['flight_no'] = request.flight_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOtaSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/flight/action/ota-search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOtaSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_ota_search_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightOtaSearchRequest,
        headers: btrip_open_20220520_models.FlightOtaSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightOtaSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airline_code):
            query['airline_code'] = request.airline_code
        if not UtilClient.is_unset(request.arr_city_code):
            query['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.cabin_class):
            query['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.carrier_flight_no):
            query['carrier_flight_no'] = request.carrier_flight_no
        if not UtilClient.is_unset(request.dep_city_code):
            query['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.flight_no):
            query['flight_no'] = request.flight_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightOtaSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/flight/action/ota-search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightOtaSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_ota_search(
        self,
        request: btrip_open_20220520_models.FlightOtaSearchRequest,
    ) -> btrip_open_20220520_models.FlightOtaSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOtaSearchHeaders()
        return self.flight_ota_search_with_options(request, headers, runtime)

    async def flight_ota_search_async(
        self,
        request: btrip_open_20220520_models.FlightOtaSearchRequest,
    ) -> btrip_open_20220520_models.FlightOtaSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightOtaSearchHeaders()
        return await self.flight_ota_search_with_options_async(request, headers, runtime)

    def flight_pay_order_with_options(
        self,
        tmp_req: btrip_open_20220520_models.FlightPayOrderRequest,
        headers: btrip_open_20220520_models.FlightPayOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightPayOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightPayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_pay_price):
            body['corp_pay_price'] = request.corp_pay_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.personal_pay_price):
            body['personal_pay_price'] = request.personal_pay_price
        if not UtilClient.is_unset(request.total_pay_price):
            body['total_pay_price'] = request.total_pay_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FlightPayOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/pay',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_pay_order_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.FlightPayOrderRequest,
        headers: btrip_open_20220520_models.FlightPayOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightPayOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightPayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_pay_price):
            body['corp_pay_price'] = request.corp_pay_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.personal_pay_price):
            body['personal_pay_price'] = request.personal_pay_price
        if not UtilClient.is_unset(request.total_pay_price):
            body['total_pay_price'] = request.total_pay_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FlightPayOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/order/action/pay',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_pay_order(
        self,
        request: btrip_open_20220520_models.FlightPayOrderRequest,
    ) -> btrip_open_20220520_models.FlightPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightPayOrderHeaders()
        return self.flight_pay_order_with_options(request, headers, runtime)

    async def flight_pay_order_async(
        self,
        request: btrip_open_20220520_models.FlightPayOrderRequest,
    ) -> btrip_open_20220520_models.FlightPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightPayOrderHeaders()
        return await self.flight_pay_order_with_options_async(request, headers, runtime)

    def flight_refund_apply_with_options(
        self,
        tmp_req: btrip_open_20220520_models.FlightRefundApplyRequest,
        headers: btrip_open_20220520_models.FlightRefundApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightRefundApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightRefundApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_segment_info_list):
            request.passenger_segment_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_segment_info_list, 'passenger_segment_info_list', 'json')
        if not UtilClient.is_unset(tmp_req.refund_voucher_info):
            request.refund_voucher_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_voucher_info, 'refund_voucher_info', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_refund_price):
            body['corp_refund_price'] = request.corp_refund_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            body['dis_sub_order_id'] = request.dis_sub_order_id
        if not UtilClient.is_unset(request.display_refund_money):
            body['display_refund_money'] = request.display_refund_money
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_voluntary):
            body['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.item_unit_ids):
            body['item_unit_ids'] = request.item_unit_ids
        if not UtilClient.is_unset(request.passenger_segment_info_list_shrink):
            body['passenger_segment_info_list'] = request.passenger_segment_info_list_shrink
        if not UtilClient.is_unset(request.personal_refund_price):
            body['personal_refund_price'] = request.personal_refund_price
        if not UtilClient.is_unset(request.reason_detail):
            body['reason_detail'] = request.reason_detail
        if not UtilClient.is_unset(request.reason_type):
            body['reason_type'] = request.reason_type
        if not UtilClient.is_unset(request.refund_voucher_info_shrink):
            body['refund_voucher_info'] = request.refund_voucher_info_shrink
        if not UtilClient.is_unset(request.session_id):
            body['session_id'] = request.session_id
        if not UtilClient.is_unset(request.total_refund_price):
            body['total_refund_price'] = request.total_refund_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FlightRefundApply',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/refund/action/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightRefundApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_refund_apply_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.FlightRefundApplyRequest,
        headers: btrip_open_20220520_models.FlightRefundApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightRefundApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightRefundApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_segment_info_list):
            request.passenger_segment_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_segment_info_list, 'passenger_segment_info_list', 'json')
        if not UtilClient.is_unset(tmp_req.refund_voucher_info):
            request.refund_voucher_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_voucher_info, 'refund_voucher_info', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_refund_price):
            body['corp_refund_price'] = request.corp_refund_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            body['dis_sub_order_id'] = request.dis_sub_order_id
        if not UtilClient.is_unset(request.display_refund_money):
            body['display_refund_money'] = request.display_refund_money
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_voluntary):
            body['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.item_unit_ids):
            body['item_unit_ids'] = request.item_unit_ids
        if not UtilClient.is_unset(request.passenger_segment_info_list_shrink):
            body['passenger_segment_info_list'] = request.passenger_segment_info_list_shrink
        if not UtilClient.is_unset(request.personal_refund_price):
            body['personal_refund_price'] = request.personal_refund_price
        if not UtilClient.is_unset(request.reason_detail):
            body['reason_detail'] = request.reason_detail
        if not UtilClient.is_unset(request.reason_type):
            body['reason_type'] = request.reason_type
        if not UtilClient.is_unset(request.refund_voucher_info_shrink):
            body['refund_voucher_info'] = request.refund_voucher_info_shrink
        if not UtilClient.is_unset(request.session_id):
            body['session_id'] = request.session_id
        if not UtilClient.is_unset(request.total_refund_price):
            body['total_refund_price'] = request.total_refund_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FlightRefundApply',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/refund/action/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightRefundApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_refund_apply(
        self,
        request: btrip_open_20220520_models.FlightRefundApplyRequest,
    ) -> btrip_open_20220520_models.FlightRefundApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightRefundApplyHeaders()
        return self.flight_refund_apply_with_options(request, headers, runtime)

    async def flight_refund_apply_async(
        self,
        request: btrip_open_20220520_models.FlightRefundApplyRequest,
    ) -> btrip_open_20220520_models.FlightRefundApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightRefundApplyHeaders()
        return await self.flight_refund_apply_with_options_async(request, headers, runtime)

    def flight_refund_detail_with_options(
        self,
        request: btrip_open_20220520_models.FlightRefundDetailRequest,
        headers: btrip_open_20220520_models.FlightRefundDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightRefundDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            query['dis_sub_order_id'] = request.dis_sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightRefundDetail',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/refund/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightRefundDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_refund_detail_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightRefundDetailRequest,
        headers: btrip_open_20220520_models.FlightRefundDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightRefundDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            query['dis_sub_order_id'] = request.dis_sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightRefundDetail',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/refund/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightRefundDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_refund_detail(
        self,
        request: btrip_open_20220520_models.FlightRefundDetailRequest,
    ) -> btrip_open_20220520_models.FlightRefundDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightRefundDetailHeaders()
        return self.flight_refund_detail_with_options(request, headers, runtime)

    async def flight_refund_detail_async(
        self,
        request: btrip_open_20220520_models.FlightRefundDetailRequest,
    ) -> btrip_open_20220520_models.FlightRefundDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightRefundDetailHeaders()
        return await self.flight_refund_detail_with_options_async(request, headers, runtime)

    def flight_refund_pre_cal_with_options(
        self,
        tmp_req: btrip_open_20220520_models.FlightRefundPreCalRequest,
        headers: btrip_open_20220520_models.FlightRefundPreCalHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightRefundPreCalResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightRefundPreCalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.passenger_segment_info_list):
            request.passenger_segment_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_segment_info_list, 'passenger_segment_info_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            query['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.passenger_segment_info_list_shrink):
            query['passenger_segment_info_list'] = request.passenger_segment_info_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightRefundPreCal',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/refund/action/pre-cal',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightRefundPreCalResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_refund_pre_cal_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.FlightRefundPreCalRequest,
        headers: btrip_open_20220520_models.FlightRefundPreCalHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightRefundPreCalResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.FlightRefundPreCalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.passenger_segment_info_list):
            request.passenger_segment_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_segment_info_list, 'passenger_segment_info_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            query['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.passenger_segment_info_list_shrink):
            query['passenger_segment_info_list'] = request.passenger_segment_info_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightRefundPreCal',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/refund/action/pre-cal',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightRefundPreCalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_refund_pre_cal(
        self,
        request: btrip_open_20220520_models.FlightRefundPreCalRequest,
    ) -> btrip_open_20220520_models.FlightRefundPreCalResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightRefundPreCalHeaders()
        return self.flight_refund_pre_cal_with_options(request, headers, runtime)

    async def flight_refund_pre_cal_async(
        self,
        request: btrip_open_20220520_models.FlightRefundPreCalRequest,
    ) -> btrip_open_20220520_models.FlightRefundPreCalResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightRefundPreCalHeaders()
        return await self.flight_refund_pre_cal_with_options_async(request, headers, runtime)

    def flight_search_list_with_options(
        self,
        request: btrip_open_20220520_models.FlightSearchListRequest,
        headers: btrip_open_20220520_models.FlightSearchListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightSearchListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airline_code):
            query['airline_code'] = request.airline_code
        if not UtilClient.is_unset(request.arr_city_code):
            query['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.arr_city_name):
            query['arr_city_name'] = request.arr_city_name
        if not UtilClient.is_unset(request.arr_date):
            query['arr_date'] = request.arr_date
        if not UtilClient.is_unset(request.cabin_class):
            query['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.dep_city_code):
            query['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_city_name):
            query['dep_city_name'] = request.dep_city_name
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.flight_no):
            query['flight_no'] = request.flight_no
        if not UtilClient.is_unset(request.need_multi_class_price):
            query['need_multi_class_price'] = request.need_multi_class_price
        if not UtilClient.is_unset(request.transfer_city_code):
            query['transfer_city_code'] = request.transfer_city_code
        if not UtilClient.is_unset(request.transfer_flight_no):
            query['transfer_flight_no'] = request.transfer_flight_no
        if not UtilClient.is_unset(request.transfer_leave_date):
            query['transfer_leave_date'] = request.transfer_leave_date
        if not UtilClient.is_unset(request.trip_type):
            query['trip_type'] = request.trip_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightSearchList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/huge/dtb-flight/v1/flight/action/search-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightSearchListResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_search_list_with_options_async(
        self,
        request: btrip_open_20220520_models.FlightSearchListRequest,
        headers: btrip_open_20220520_models.FlightSearchListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.FlightSearchListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airline_code):
            query['airline_code'] = request.airline_code
        if not UtilClient.is_unset(request.arr_city_code):
            query['arr_city_code'] = request.arr_city_code
        if not UtilClient.is_unset(request.arr_city_name):
            query['arr_city_name'] = request.arr_city_name
        if not UtilClient.is_unset(request.arr_date):
            query['arr_date'] = request.arr_date
        if not UtilClient.is_unset(request.cabin_class):
            query['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.dep_city_code):
            query['dep_city_code'] = request.dep_city_code
        if not UtilClient.is_unset(request.dep_city_name):
            query['dep_city_name'] = request.dep_city_name
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.flight_no):
            query['flight_no'] = request.flight_no
        if not UtilClient.is_unset(request.need_multi_class_price):
            query['need_multi_class_price'] = request.need_multi_class_price
        if not UtilClient.is_unset(request.transfer_city_code):
            query['transfer_city_code'] = request.transfer_city_code
        if not UtilClient.is_unset(request.transfer_flight_no):
            query['transfer_flight_no'] = request.transfer_flight_no
        if not UtilClient.is_unset(request.transfer_leave_date):
            query['transfer_leave_date'] = request.transfer_leave_date
        if not UtilClient.is_unset(request.trip_type):
            query['trip_type'] = request.trip_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightSearchList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/huge/dtb-flight/v1/flight/action/search-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.FlightSearchListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_search_list(
        self,
        request: btrip_open_20220520_models.FlightSearchListRequest,
    ) -> btrip_open_20220520_models.FlightSearchListResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightSearchListHeaders()
        return self.flight_search_list_with_options(request, headers, runtime)

    async def flight_search_list_async(
        self,
        request: btrip_open_20220520_models.FlightSearchListRequest,
    ) -> btrip_open_20220520_models.FlightSearchListResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.FlightSearchListHeaders()
        return await self.flight_search_list_with_options_async(request, headers, runtime)

    def group_depart_save_with_options(
        self,
        tmp_req: btrip_open_20220520_models.GroupDepartSaveRequest,
        headers: btrip_open_20220520_models.GroupDepartSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.GroupDepartSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.GroupDepartSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_corp_id_list):
            request.sub_corp_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_corp_id_list, 'sub_corp_id_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.dept_name):
            body['dept_name'] = request.dept_name
        if not UtilClient.is_unset(request.manager_ids):
            body['manager_ids'] = request.manager_ids
        if not UtilClient.is_unset(request.outer_dept_id):
            body['outer_dept_id'] = request.outer_dept_id
        if not UtilClient.is_unset(request.outer_dept_pid):
            body['outer_dept_pid'] = request.outer_dept_pid
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.sub_corp_id_list_shrink):
            body['sub_corp_id_list'] = request.sub_corp_id_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupDepartSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/sub_corps/v1/departs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.GroupDepartSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def group_depart_save_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.GroupDepartSaveRequest,
        headers: btrip_open_20220520_models.GroupDepartSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.GroupDepartSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.GroupDepartSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_corp_id_list):
            request.sub_corp_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_corp_id_list, 'sub_corp_id_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.dept_name):
            body['dept_name'] = request.dept_name
        if not UtilClient.is_unset(request.manager_ids):
            body['manager_ids'] = request.manager_ids
        if not UtilClient.is_unset(request.outer_dept_id):
            body['outer_dept_id'] = request.outer_dept_id
        if not UtilClient.is_unset(request.outer_dept_pid):
            body['outer_dept_pid'] = request.outer_dept_pid
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.sub_corp_id_list_shrink):
            body['sub_corp_id_list'] = request.sub_corp_id_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupDepartSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/sub_corps/v1/departs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.GroupDepartSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def group_depart_save(
        self,
        request: btrip_open_20220520_models.GroupDepartSaveRequest,
    ) -> btrip_open_20220520_models.GroupDepartSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.GroupDepartSaveHeaders()
        return self.group_depart_save_with_options(request, headers, runtime)

    async def group_depart_save_async(
        self,
        request: btrip_open_20220520_models.GroupDepartSaveRequest,
    ) -> btrip_open_20220520_models.GroupDepartSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.GroupDepartSaveHeaders()
        return await self.group_depart_save_with_options_async(request, headers, runtime)

    def group_user_save_with_options(
        self,
        tmp_req: btrip_open_20220520_models.GroupUserSaveRequest,
        headers: btrip_open_20220520_models.GroupUserSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.GroupUserSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.GroupUserSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_corp_id_list):
            request.sub_corp_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_corp_id_list, 'sub_corp_id_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.job_no):
            body['job_no'] = request.job_no
        if not UtilClient.is_unset(request.leave_status):
            body['leave_status'] = request.leave_status
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.real_name_en):
            body['real_name_en'] = request.real_name_en
        if not UtilClient.is_unset(request.sub_corp_id_list_shrink):
            body['sub_corp_id_list'] = request.sub_corp_id_list_shrink
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupUserSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/sub_corps/v1/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.GroupUserSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def group_user_save_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.GroupUserSaveRequest,
        headers: btrip_open_20220520_models.GroupUserSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.GroupUserSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.GroupUserSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_corp_id_list):
            request.sub_corp_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_corp_id_list, 'sub_corp_id_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.job_no):
            body['job_no'] = request.job_no
        if not UtilClient.is_unset(request.leave_status):
            body['leave_status'] = request.leave_status
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.real_name_en):
            body['real_name_en'] = request.real_name_en
        if not UtilClient.is_unset(request.sub_corp_id_list_shrink):
            body['sub_corp_id_list'] = request.sub_corp_id_list_shrink
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupUserSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/sub_corps/v1/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.GroupUserSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def group_user_save(
        self,
        request: btrip_open_20220520_models.GroupUserSaveRequest,
    ) -> btrip_open_20220520_models.GroupUserSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.GroupUserSaveHeaders()
        return self.group_user_save_with_options(request, headers, runtime)

    async def group_user_save_async(
        self,
        request: btrip_open_20220520_models.GroupUserSaveRequest,
    ) -> btrip_open_20220520_models.GroupUserSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.GroupUserSaveHeaders()
        return await self.group_user_save_with_options_async(request, headers, runtime)

    def hotel_bill_settlement_query_with_options(
        self,
        request: btrip_open_20220520_models.HotelBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.HotelBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/hotel/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelBillSettlementQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_bill_settlement_query_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.HotelBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/hotel/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelBillSettlementQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_bill_settlement_query(
        self,
        request: btrip_open_20220520_models.HotelBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.HotelBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelBillSettlementQueryHeaders()
        return self.hotel_bill_settlement_query_with_options(request, headers, runtime)

    async def hotel_bill_settlement_query_async(
        self,
        request: btrip_open_20220520_models.HotelBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.HotelBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelBillSettlementQueryHeaders()
        return await self.hotel_bill_settlement_query_with_options_async(request, headers, runtime)

    def hotel_exceed_apply_query_with_options(
        self,
        request: btrip_open_20220520_models.HotelExceedApplyQueryRequest,
        headers: btrip_open_20220520_models.HotelExceedApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelExceedApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelExceedApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/hotel-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelExceedApplyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_exceed_apply_query_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelExceedApplyQueryRequest,
        headers: btrip_open_20220520_models.HotelExceedApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelExceedApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelExceedApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/hotel-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelExceedApplyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_exceed_apply_query(
        self,
        request: btrip_open_20220520_models.HotelExceedApplyQueryRequest,
    ) -> btrip_open_20220520_models.HotelExceedApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelExceedApplyQueryHeaders()
        return self.hotel_exceed_apply_query_with_options(request, headers, runtime)

    async def hotel_exceed_apply_query_async(
        self,
        request: btrip_open_20220520_models.HotelExceedApplyQueryRequest,
    ) -> btrip_open_20220520_models.HotelExceedApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelExceedApplyQueryHeaders()
        return await self.hotel_exceed_apply_query_with_options_async(request, headers, runtime)

    def hotel_goods_query_with_options(
        self,
        request: btrip_open_20220520_models.HotelGoodsQueryRequest,
        headers: btrip_open_20220520_models.HotelGoodsQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelGoodsQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adult_num):
            query['adult_num'] = request.adult_num
        if not UtilClient.is_unset(request.agreement_price):
            query['agreement_price'] = request.agreement_price
        if not UtilClient.is_unset(request.begin_date):
            query['begin_date'] = request.begin_date
        if not UtilClient.is_unset(request.breakfast_included):
            query['breakfast_included'] = request.breakfast_included
        if not UtilClient.is_unset(request.btrip_user_id):
            query['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.city_code):
            query['city_code'] = request.city_code
        if not UtilClient.is_unset(request.end_date):
            query['end_date'] = request.end_date
        if not UtilClient.is_unset(request.hotel_id):
            query['hotel_id'] = request.hotel_id
        if not UtilClient.is_unset(request.pay_over_type):
            query['pay_over_type'] = request.pay_over_type
        if not UtilClient.is_unset(request.payment_type):
            query['payment_type'] = request.payment_type
        if not UtilClient.is_unset(request.special_invoice):
            query['special_invoice'] = request.special_invoice
        if not UtilClient.is_unset(request.super_man):
            query['super_man'] = request.super_man
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelGoodsQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/hotel-goods',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelGoodsQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_goods_query_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelGoodsQueryRequest,
        headers: btrip_open_20220520_models.HotelGoodsQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelGoodsQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adult_num):
            query['adult_num'] = request.adult_num
        if not UtilClient.is_unset(request.agreement_price):
            query['agreement_price'] = request.agreement_price
        if not UtilClient.is_unset(request.begin_date):
            query['begin_date'] = request.begin_date
        if not UtilClient.is_unset(request.breakfast_included):
            query['breakfast_included'] = request.breakfast_included
        if not UtilClient.is_unset(request.btrip_user_id):
            query['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.city_code):
            query['city_code'] = request.city_code
        if not UtilClient.is_unset(request.end_date):
            query['end_date'] = request.end_date
        if not UtilClient.is_unset(request.hotel_id):
            query['hotel_id'] = request.hotel_id
        if not UtilClient.is_unset(request.pay_over_type):
            query['pay_over_type'] = request.pay_over_type
        if not UtilClient.is_unset(request.payment_type):
            query['payment_type'] = request.payment_type
        if not UtilClient.is_unset(request.special_invoice):
            query['special_invoice'] = request.special_invoice
        if not UtilClient.is_unset(request.super_man):
            query['super_man'] = request.super_man
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelGoodsQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/hotel-goods',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelGoodsQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_goods_query(
        self,
        request: btrip_open_20220520_models.HotelGoodsQueryRequest,
    ) -> btrip_open_20220520_models.HotelGoodsQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelGoodsQueryHeaders()
        return self.hotel_goods_query_with_options(request, headers, runtime)

    async def hotel_goods_query_async(
        self,
        request: btrip_open_20220520_models.HotelGoodsQueryRequest,
    ) -> btrip_open_20220520_models.HotelGoodsQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelGoodsQueryHeaders()
        return await self.hotel_goods_query_with_options_async(request, headers, runtime)

    def hotel_index_info_with_options(
        self,
        request: btrip_open_20220520_models.HotelIndexInfoRequest,
        headers: btrip_open_20220520_models.HotelIndexInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelIndexInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_code):
            query['city_code'] = request.city_code
        if not UtilClient.is_unset(request.hotel_status):
            query['hotel_status'] = request.hotel_status
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelIndexInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/index-infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelIndexInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_index_info_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelIndexInfoRequest,
        headers: btrip_open_20220520_models.HotelIndexInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelIndexInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_code):
            query['city_code'] = request.city_code
        if not UtilClient.is_unset(request.hotel_status):
            query['hotel_status'] = request.hotel_status
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelIndexInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/index-infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelIndexInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_index_info(
        self,
        request: btrip_open_20220520_models.HotelIndexInfoRequest,
    ) -> btrip_open_20220520_models.HotelIndexInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelIndexInfoHeaders()
        return self.hotel_index_info_with_options(request, headers, runtime)

    async def hotel_index_info_async(
        self,
        request: btrip_open_20220520_models.HotelIndexInfoRequest,
    ) -> btrip_open_20220520_models.HotelIndexInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelIndexInfoHeaders()
        return await self.hotel_index_info_with_options_async(request, headers, runtime)

    def hotel_order_cancel_with_options(
        self,
        request: btrip_open_20220520_models.HotelOrderCancelRequest,
        headers: btrip_open_20220520_models.HotelOrderCancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderCancelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderCancel',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_order_cancel_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelOrderCancelRequest,
        headers: btrip_open_20220520_models.HotelOrderCancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderCancelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderCancel',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_order_cancel(
        self,
        request: btrip_open_20220520_models.HotelOrderCancelRequest,
    ) -> btrip_open_20220520_models.HotelOrderCancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderCancelHeaders()
        return self.hotel_order_cancel_with_options(request, headers, runtime)

    async def hotel_order_cancel_async(
        self,
        request: btrip_open_20220520_models.HotelOrderCancelRequest,
    ) -> btrip_open_20220520_models.HotelOrderCancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderCancelHeaders()
        return await self.hotel_order_cancel_with_options_async(request, headers, runtime)

    def hotel_order_create_with_options(
        self,
        tmp_req: btrip_open_20220520_models.HotelOrderCreateRequest,
        headers: btrip_open_20220520_models.HotelOrderCreateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderCreateResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelOrderCreateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.invoice_info):
            request.invoice_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_info, 'invoice_info', 'json')
        if not UtilClient.is_unset(tmp_req.occupant_info_list):
            request.occupant_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.occupant_info_list, 'occupant_info_list', 'json')
        if not UtilClient.is_unset(tmp_req.promotion_info):
            request.promotion_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.promotion_info, 'promotion_info', 'json')
        body = {}
        if not UtilClient.is_unset(request.btrip_user_id):
            body['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.check_in):
            body['check_in'] = request.check_in
        if not UtilClient.is_unset(request.check_out):
            body['check_out'] = request.check_out
        if not UtilClient.is_unset(request.contract_email):
            body['contract_email'] = request.contract_email
        if not UtilClient.is_unset(request.contract_name):
            body['contract_name'] = request.contract_name
        if not UtilClient.is_unset(request.contract_phone):
            body['contract_phone'] = request.contract_phone
        if not UtilClient.is_unset(request.corp_pay_price):
            body['corp_pay_price'] = request.corp_pay_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.invoice_info_shrink):
            body['invoice_info'] = request.invoice_info_shrink
        if not UtilClient.is_unset(request.item_id):
            body['item_id'] = request.item_id
        if not UtilClient.is_unset(request.itinerary_no):
            body['itinerary_no'] = request.itinerary_no
        if not UtilClient.is_unset(request.occupant_info_list_shrink):
            body['occupant_info_list'] = request.occupant_info_list_shrink
        if not UtilClient.is_unset(request.person_pay_price):
            body['person_pay_price'] = request.person_pay_price
        if not UtilClient.is_unset(request.promotion_info_shrink):
            body['promotion_info'] = request.promotion_info_shrink
        if not UtilClient.is_unset(request.rate_plan_id):
            body['rate_plan_id'] = request.rate_plan_id
        if not UtilClient.is_unset(request.room_id):
            body['room_id'] = request.room_id
        if not UtilClient.is_unset(request.room_num):
            body['room_num'] = request.room_num
        if not UtilClient.is_unset(request.seller_id):
            body['seller_id'] = request.seller_id
        if not UtilClient.is_unset(request.shid):
            body['shid'] = request.shid
        if not UtilClient.is_unset(request.total_order_price):
            body['total_order_price'] = request.total_order_price
        if not UtilClient.is_unset(request.validate_res_key):
            body['validate_res_key'] = request.validate_res_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotelOrderCreate',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_order_create_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.HotelOrderCreateRequest,
        headers: btrip_open_20220520_models.HotelOrderCreateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderCreateResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelOrderCreateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.invoice_info):
            request.invoice_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_info, 'invoice_info', 'json')
        if not UtilClient.is_unset(tmp_req.occupant_info_list):
            request.occupant_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.occupant_info_list, 'occupant_info_list', 'json')
        if not UtilClient.is_unset(tmp_req.promotion_info):
            request.promotion_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.promotion_info, 'promotion_info', 'json')
        body = {}
        if not UtilClient.is_unset(request.btrip_user_id):
            body['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.check_in):
            body['check_in'] = request.check_in
        if not UtilClient.is_unset(request.check_out):
            body['check_out'] = request.check_out
        if not UtilClient.is_unset(request.contract_email):
            body['contract_email'] = request.contract_email
        if not UtilClient.is_unset(request.contract_name):
            body['contract_name'] = request.contract_name
        if not UtilClient.is_unset(request.contract_phone):
            body['contract_phone'] = request.contract_phone
        if not UtilClient.is_unset(request.corp_pay_price):
            body['corp_pay_price'] = request.corp_pay_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.invoice_info_shrink):
            body['invoice_info'] = request.invoice_info_shrink
        if not UtilClient.is_unset(request.item_id):
            body['item_id'] = request.item_id
        if not UtilClient.is_unset(request.itinerary_no):
            body['itinerary_no'] = request.itinerary_no
        if not UtilClient.is_unset(request.occupant_info_list_shrink):
            body['occupant_info_list'] = request.occupant_info_list_shrink
        if not UtilClient.is_unset(request.person_pay_price):
            body['person_pay_price'] = request.person_pay_price
        if not UtilClient.is_unset(request.promotion_info_shrink):
            body['promotion_info'] = request.promotion_info_shrink
        if not UtilClient.is_unset(request.rate_plan_id):
            body['rate_plan_id'] = request.rate_plan_id
        if not UtilClient.is_unset(request.room_id):
            body['room_id'] = request.room_id
        if not UtilClient.is_unset(request.room_num):
            body['room_num'] = request.room_num
        if not UtilClient.is_unset(request.seller_id):
            body['seller_id'] = request.seller_id
        if not UtilClient.is_unset(request.shid):
            body['shid'] = request.shid
        if not UtilClient.is_unset(request.total_order_price):
            body['total_order_price'] = request.total_order_price
        if not UtilClient.is_unset(request.validate_res_key):
            body['validate_res_key'] = request.validate_res_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotelOrderCreate',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_order_create(
        self,
        request: btrip_open_20220520_models.HotelOrderCreateRequest,
    ) -> btrip_open_20220520_models.HotelOrderCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderCreateHeaders()
        return self.hotel_order_create_with_options(request, headers, runtime)

    async def hotel_order_create_async(
        self,
        request: btrip_open_20220520_models.HotelOrderCreateRequest,
    ) -> btrip_open_20220520_models.HotelOrderCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderCreateHeaders()
        return await self.hotel_order_create_with_options_async(request, headers, runtime)

    def hotel_order_detail_info_with_options(
        self,
        request: btrip_open_20220520_models.HotelOrderDetailInfoRequest,
        headers: btrip_open_20220520_models.HotelOrderDetailInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderDetailInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_order_detail_info_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelOrderDetailInfoRequest,
        headers: btrip_open_20220520_models.HotelOrderDetailInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderDetailInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_order_detail_info(
        self,
        request: btrip_open_20220520_models.HotelOrderDetailInfoRequest,
    ) -> btrip_open_20220520_models.HotelOrderDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderDetailInfoHeaders()
        return self.hotel_order_detail_info_with_options(request, headers, runtime)

    async def hotel_order_detail_info_async(
        self,
        request: btrip_open_20220520_models.HotelOrderDetailInfoRequest,
    ) -> btrip_open_20220520_models.HotelOrderDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderDetailInfoHeaders()
        return await self.hotel_order_detail_info_with_options_async(request, headers, runtime)

    def hotel_order_list_query_with_options(
        self,
        request: btrip_open_20220520_models.HotelOrderListQueryRequest,
        headers: btrip_open_20220520_models.HotelOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/hotel/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderListQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_order_list_query_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelOrderListQueryRequest,
        headers: btrip_open_20220520_models.HotelOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/hotel/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderListQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_order_list_query(
        self,
        request: btrip_open_20220520_models.HotelOrderListQueryRequest,
    ) -> btrip_open_20220520_models.HotelOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderListQueryHeaders()
        return self.hotel_order_list_query_with_options(request, headers, runtime)

    async def hotel_order_list_query_async(
        self,
        request: btrip_open_20220520_models.HotelOrderListQueryRequest,
    ) -> btrip_open_20220520_models.HotelOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderListQueryHeaders()
        return await self.hotel_order_list_query_with_options_async(request, headers, runtime)

    def hotel_order_pay_with_options(
        self,
        request: btrip_open_20220520_models.HotelOrderPayRequest,
        headers: btrip_open_20220520_models.HotelOrderPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderPayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.btrip_order_id):
            body['btrip_order_id'] = request.btrip_order_id
        if not UtilClient.is_unset(request.btrip_user_id):
            body['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.company_pay_fee):
            body['company_pay_fee'] = request.company_pay_fee
        if not UtilClient.is_unset(request.person_pay_fee):
            body['person_pay_fee'] = request.person_pay_fee
        if not UtilClient.is_unset(request.third_pay_account):
            body['third_pay_account'] = request.third_pay_account
        if not UtilClient.is_unset(request.third_trade_no):
            body['third_trade_no'] = request.third_trade_no
        if not UtilClient.is_unset(request.total_price):
            body['total_price'] = request.total_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotelOrderPay',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/pay',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderPayResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_order_pay_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelOrderPayRequest,
        headers: btrip_open_20220520_models.HotelOrderPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderPayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.btrip_order_id):
            body['btrip_order_id'] = request.btrip_order_id
        if not UtilClient.is_unset(request.btrip_user_id):
            body['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.company_pay_fee):
            body['company_pay_fee'] = request.company_pay_fee
        if not UtilClient.is_unset(request.person_pay_fee):
            body['person_pay_fee'] = request.person_pay_fee
        if not UtilClient.is_unset(request.third_pay_account):
            body['third_pay_account'] = request.third_pay_account
        if not UtilClient.is_unset(request.third_trade_no):
            body['third_trade_no'] = request.third_trade_no
        if not UtilClient.is_unset(request.total_price):
            body['total_price'] = request.total_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotelOrderPay',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/pay',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderPayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_order_pay(
        self,
        request: btrip_open_20220520_models.HotelOrderPayRequest,
    ) -> btrip_open_20220520_models.HotelOrderPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderPayHeaders()
        return self.hotel_order_pay_with_options(request, headers, runtime)

    async def hotel_order_pay_async(
        self,
        request: btrip_open_20220520_models.HotelOrderPayRequest,
    ) -> btrip_open_20220520_models.HotelOrderPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderPayHeaders()
        return await self.hotel_order_pay_with_options_async(request, headers, runtime)

    def hotel_order_pre_validate_with_options(
        self,
        tmp_req: btrip_open_20220520_models.HotelOrderPreValidateRequest,
        headers: btrip_open_20220520_models.HotelOrderPreValidateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderPreValidateResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelOrderPreValidateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.daily_list):
            request.daily_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.daily_list, 'daily_list', 'json')
        if not UtilClient.is_unset(tmp_req.occupant_info_list):
            request.occupant_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.occupant_info_list, 'occupant_info_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.btrip_user_id):
            query['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.check_in):
            query['check_in'] = request.check_in
        if not UtilClient.is_unset(request.check_out):
            query['check_out'] = request.check_out
        if not UtilClient.is_unset(request.daily_list_shrink):
            query['daily_list'] = request.daily_list_shrink
        if not UtilClient.is_unset(request.item_id):
            query['item_id'] = request.item_id
        if not UtilClient.is_unset(request.number_of_adults_per_room):
            query['number_of_adults_per_room'] = request.number_of_adults_per_room
        if not UtilClient.is_unset(request.occupant_info_list_shrink):
            query['occupant_info_list'] = request.occupant_info_list_shrink
        if not UtilClient.is_unset(request.rate_plan_id):
            query['rate_plan_id'] = request.rate_plan_id
        if not UtilClient.is_unset(request.room_id):
            query['room_id'] = request.room_id
        if not UtilClient.is_unset(request.room_num):
            query['room_num'] = request.room_num
        if not UtilClient.is_unset(request.search_room_price):
            query['search_room_price'] = request.search_room_price
        if not UtilClient.is_unset(request.seller_id):
            query['seller_id'] = request.seller_id
        if not UtilClient.is_unset(request.shid):
            query['shid'] = request.shid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderPreValidate',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/pre-validate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderPreValidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_order_pre_validate_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.HotelOrderPreValidateRequest,
        headers: btrip_open_20220520_models.HotelOrderPreValidateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderPreValidateResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelOrderPreValidateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.daily_list):
            request.daily_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.daily_list, 'daily_list', 'json')
        if not UtilClient.is_unset(tmp_req.occupant_info_list):
            request.occupant_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.occupant_info_list, 'occupant_info_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.btrip_user_id):
            query['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.check_in):
            query['check_in'] = request.check_in
        if not UtilClient.is_unset(request.check_out):
            query['check_out'] = request.check_out
        if not UtilClient.is_unset(request.daily_list_shrink):
            query['daily_list'] = request.daily_list_shrink
        if not UtilClient.is_unset(request.item_id):
            query['item_id'] = request.item_id
        if not UtilClient.is_unset(request.number_of_adults_per_room):
            query['number_of_adults_per_room'] = request.number_of_adults_per_room
        if not UtilClient.is_unset(request.occupant_info_list_shrink):
            query['occupant_info_list'] = request.occupant_info_list_shrink
        if not UtilClient.is_unset(request.rate_plan_id):
            query['rate_plan_id'] = request.rate_plan_id
        if not UtilClient.is_unset(request.room_id):
            query['room_id'] = request.room_id
        if not UtilClient.is_unset(request.room_num):
            query['room_num'] = request.room_num
        if not UtilClient.is_unset(request.search_room_price):
            query['search_room_price'] = request.search_room_price
        if not UtilClient.is_unset(request.seller_id):
            query['seller_id'] = request.seller_id
        if not UtilClient.is_unset(request.shid):
            query['shid'] = request.shid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderPreValidate',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/orders/action/pre-validate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderPreValidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_order_pre_validate(
        self,
        request: btrip_open_20220520_models.HotelOrderPreValidateRequest,
    ) -> btrip_open_20220520_models.HotelOrderPreValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderPreValidateHeaders()
        return self.hotel_order_pre_validate_with_options(request, headers, runtime)

    async def hotel_order_pre_validate_async(
        self,
        request: btrip_open_20220520_models.HotelOrderPreValidateRequest,
    ) -> btrip_open_20220520_models.HotelOrderPreValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderPreValidateHeaders()
        return await self.hotel_order_pre_validate_with_options_async(request, headers, runtime)

    def hotel_order_query_with_options(
        self,
        request: btrip_open_20220520_models.HotelOrderQueryRequest,
        headers: btrip_open_20220520_models.HotelOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/hotel/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_order_query_with_options_async(
        self,
        request: btrip_open_20220520_models.HotelOrderQueryRequest,
        headers: btrip_open_20220520_models.HotelOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/hotel/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelOrderQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_order_query(
        self,
        request: btrip_open_20220520_models.HotelOrderQueryRequest,
    ) -> btrip_open_20220520_models.HotelOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderQueryHeaders()
        return self.hotel_order_query_with_options(request, headers, runtime)

    async def hotel_order_query_async(
        self,
        request: btrip_open_20220520_models.HotelOrderQueryRequest,
    ) -> btrip_open_20220520_models.HotelOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelOrderQueryHeaders()
        return await self.hotel_order_query_with_options_async(request, headers, runtime)

    def hotel_room_info_with_options(
        self,
        tmp_req: btrip_open_20220520_models.HotelRoomInfoRequest,
        headers: btrip_open_20220520_models.HotelRoomInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelRoomInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelRoomInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_ids):
            request.room_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_ids, 'room_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.room_ids_shrink):
            query['room_ids'] = request.room_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelRoomInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/room-infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelRoomInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_room_info_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.HotelRoomInfoRequest,
        headers: btrip_open_20220520_models.HotelRoomInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelRoomInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelRoomInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_ids):
            request.room_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_ids, 'room_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.room_ids_shrink):
            query['room_ids'] = request.room_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelRoomInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/room-infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelRoomInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_room_info(
        self,
        request: btrip_open_20220520_models.HotelRoomInfoRequest,
    ) -> btrip_open_20220520_models.HotelRoomInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelRoomInfoHeaders()
        return self.hotel_room_info_with_options(request, headers, runtime)

    async def hotel_room_info_async(
        self,
        request: btrip_open_20220520_models.HotelRoomInfoRequest,
    ) -> btrip_open_20220520_models.HotelRoomInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelRoomInfoHeaders()
        return await self.hotel_room_info_with_options_async(request, headers, runtime)

    def hotel_search_with_options(
        self,
        tmp_req: btrip_open_20220520_models.HotelSearchRequest,
        headers: btrip_open_20220520_models.HotelSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelSearchResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelSearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.brand_code):
            request.brand_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.brand_code, 'brand_code', 'json')
        if not UtilClient.is_unset(tmp_req.shids):
            request.shids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shids, 'shids', 'json')
        query = {}
        if not UtilClient.is_unset(request.adult_num):
            query['adult_num'] = request.adult_num
        if not UtilClient.is_unset(request.brand_code_shrink):
            query['brand_code'] = request.brand_code_shrink
        if not UtilClient.is_unset(request.btrip_user_id):
            query['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.check_in_date):
            query['check_in_date'] = request.check_in_date
        if not UtilClient.is_unset(request.check_out_date):
            query['check_out_date'] = request.check_out_date
        if not UtilClient.is_unset(request.city_code):
            query['city_code'] = request.city_code
        if not UtilClient.is_unset(request.dir):
            query['dir'] = request.dir
        if not UtilClient.is_unset(request.distance):
            query['distance'] = request.distance
        if not UtilClient.is_unset(request.district_code):
            query['district_code'] = request.district_code
        if not UtilClient.is_unset(request.hotel_star):
            query['hotel_star'] = request.hotel_star
        if not UtilClient.is_unset(request.is_protocol):
            query['is_protocol'] = request.is_protocol
        if not UtilClient.is_unset(request.key_words):
            query['key_words'] = request.key_words
        if not UtilClient.is_unset(request.location):
            query['location'] = request.location
        if not UtilClient.is_unset(request.max_price):
            query['max_price'] = request.max_price
        if not UtilClient.is_unset(request.min_price):
            query['min_price'] = request.min_price
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.pay_over_type):
            query['pay_over_type'] = request.pay_over_type
        if not UtilClient.is_unset(request.payment_type):
            query['payment_type'] = request.payment_type
        if not UtilClient.is_unset(request.shids_shrink):
            query['shids'] = request.shids_shrink
        if not UtilClient.is_unset(request.sort_code):
            query['sort_code'] = request.sort_code
        if not UtilClient.is_unset(request.super_man):
            query['super_man'] = request.super_man
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/hotels/action/search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_search_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.HotelSearchRequest,
        headers: btrip_open_20220520_models.HotelSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelSearchResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelSearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.brand_code):
            request.brand_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.brand_code, 'brand_code', 'json')
        if not UtilClient.is_unset(tmp_req.shids):
            request.shids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shids, 'shids', 'json')
        query = {}
        if not UtilClient.is_unset(request.adult_num):
            query['adult_num'] = request.adult_num
        if not UtilClient.is_unset(request.brand_code_shrink):
            query['brand_code'] = request.brand_code_shrink
        if not UtilClient.is_unset(request.btrip_user_id):
            query['btrip_user_id'] = request.btrip_user_id
        if not UtilClient.is_unset(request.check_in_date):
            query['check_in_date'] = request.check_in_date
        if not UtilClient.is_unset(request.check_out_date):
            query['check_out_date'] = request.check_out_date
        if not UtilClient.is_unset(request.city_code):
            query['city_code'] = request.city_code
        if not UtilClient.is_unset(request.dir):
            query['dir'] = request.dir
        if not UtilClient.is_unset(request.distance):
            query['distance'] = request.distance
        if not UtilClient.is_unset(request.district_code):
            query['district_code'] = request.district_code
        if not UtilClient.is_unset(request.hotel_star):
            query['hotel_star'] = request.hotel_star
        if not UtilClient.is_unset(request.is_protocol):
            query['is_protocol'] = request.is_protocol
        if not UtilClient.is_unset(request.key_words):
            query['key_words'] = request.key_words
        if not UtilClient.is_unset(request.location):
            query['location'] = request.location
        if not UtilClient.is_unset(request.max_price):
            query['max_price'] = request.max_price
        if not UtilClient.is_unset(request.min_price):
            query['min_price'] = request.min_price
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.pay_over_type):
            query['pay_over_type'] = request.pay_over_type
        if not UtilClient.is_unset(request.payment_type):
            query['payment_type'] = request.payment_type
        if not UtilClient.is_unset(request.shids_shrink):
            query['shids'] = request.shids_shrink
        if not UtilClient.is_unset(request.sort_code):
            query['sort_code'] = request.sort_code
        if not UtilClient.is_unset(request.super_man):
            query['super_man'] = request.super_man
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/hotels/action/search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_search(
        self,
        request: btrip_open_20220520_models.HotelSearchRequest,
    ) -> btrip_open_20220520_models.HotelSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelSearchHeaders()
        return self.hotel_search_with_options(request, headers, runtime)

    async def hotel_search_async(
        self,
        request: btrip_open_20220520_models.HotelSearchRequest,
    ) -> btrip_open_20220520_models.HotelSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelSearchHeaders()
        return await self.hotel_search_with_options_async(request, headers, runtime)

    def hotel_static_info_with_options(
        self,
        tmp_req: btrip_open_20220520_models.HotelStaticInfoRequest,
        headers: btrip_open_20220520_models.HotelStaticInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelStaticInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelStaticInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_ids):
            request.hotel_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_ids, 'hotel_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.hotel_ids_shrink):
            query['hotel_ids'] = request.hotel_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelStaticInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/static-infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelStaticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_static_info_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.HotelStaticInfoRequest,
        headers: btrip_open_20220520_models.HotelStaticInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.HotelStaticInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.HotelStaticInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_ids):
            request.hotel_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_ids, 'hotel_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.hotel_ids_shrink):
            query['hotel_ids'] = request.hotel_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotelStaticInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-hotel/v1/static-infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.HotelStaticInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_static_info(
        self,
        request: btrip_open_20220520_models.HotelStaticInfoRequest,
    ) -> btrip_open_20220520_models.HotelStaticInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelStaticInfoHeaders()
        return self.hotel_static_info_with_options(request, headers, runtime)

    async def hotel_static_info_async(
        self,
        request: btrip_open_20220520_models.HotelStaticInfoRequest,
    ) -> btrip_open_20220520_models.HotelStaticInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.HotelStaticInfoHeaders()
        return await self.hotel_static_info_with_options_async(request, headers, runtime)

    def ie_flight_bill_settlement_query_with_options(
        self,
        request: btrip_open_20220520_models.IeFlightBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.IeFlightBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.IeFlightBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IeFlightBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/ie-flight/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.IeFlightBillSettlementQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def ie_flight_bill_settlement_query_with_options_async(
        self,
        request: btrip_open_20220520_models.IeFlightBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.IeFlightBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.IeFlightBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IeFlightBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/ie-flight/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.IeFlightBillSettlementQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ie_flight_bill_settlement_query(
        self,
        request: btrip_open_20220520_models.IeFlightBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.IeFlightBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.IeFlightBillSettlementQueryHeaders()
        return self.ie_flight_bill_settlement_query_with_options(request, headers, runtime)

    async def ie_flight_bill_settlement_query_async(
        self,
        request: btrip_open_20220520_models.IeFlightBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.IeFlightBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.IeFlightBillSettlementQueryHeaders()
        return await self.ie_flight_bill_settlement_query_with_options_async(request, headers, runtime)

    def ins_invoice_scan_query_with_options(
        self,
        request: btrip_open_20220520_models.InsInvoiceScanQueryRequest,
        headers: btrip_open_20220520_models.InsInvoiceScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InsInvoiceScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsInvoiceScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/ins-invoice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InsInvoiceScanQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def ins_invoice_scan_query_with_options_async(
        self,
        request: btrip_open_20220520_models.InsInvoiceScanQueryRequest,
        headers: btrip_open_20220520_models.InsInvoiceScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InsInvoiceScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsInvoiceScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/ins-invoice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InsInvoiceScanQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ins_invoice_scan_query(
        self,
        request: btrip_open_20220520_models.InsInvoiceScanQueryRequest,
    ) -> btrip_open_20220520_models.InsInvoiceScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InsInvoiceScanQueryHeaders()
        return self.ins_invoice_scan_query_with_options(request, headers, runtime)

    async def ins_invoice_scan_query_async(
        self,
        request: btrip_open_20220520_models.InsInvoiceScanQueryRequest,
    ) -> btrip_open_20220520_models.InsInvoiceScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InsInvoiceScanQueryHeaders()
        return await self.ins_invoice_scan_query_with_options_async(request, headers, runtime)

    def invoice_add_with_options(
        self,
        request: btrip_open_20220520_models.InvoiceAddRequest,
        headers: btrip_open_20220520_models.InvoiceAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.bank_name):
            body['bank_name'] = request.bank_name
        if not UtilClient.is_unset(request.bank_no):
            body['bank_no'] = request.bank_no
        if not UtilClient.is_unset(request.tax_no):
            body['tax_no'] = request.tax_no
        if not UtilClient.is_unset(request.tel):
            body['tel'] = request.tel
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/add-invoice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoice_add_with_options_async(
        self,
        request: btrip_open_20220520_models.InvoiceAddRequest,
        headers: btrip_open_20220520_models.InvoiceAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.bank_name):
            body['bank_name'] = request.bank_name
        if not UtilClient.is_unset(request.bank_no):
            body['bank_no'] = request.bank_no
        if not UtilClient.is_unset(request.tax_no):
            body['tax_no'] = request.tax_no
        if not UtilClient.is_unset(request.tel):
            body['tel'] = request.tel
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/add-invoice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoice_add(
        self,
        request: btrip_open_20220520_models.InvoiceAddRequest,
    ) -> btrip_open_20220520_models.InvoiceAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceAddHeaders()
        return self.invoice_add_with_options(request, headers, runtime)

    async def invoice_add_async(
        self,
        request: btrip_open_20220520_models.InvoiceAddRequest,
    ) -> btrip_open_20220520_models.InvoiceAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceAddHeaders()
        return await self.invoice_add_with_options_async(request, headers, runtime)

    def invoice_delete_with_options(
        self,
        request: btrip_open_20220520_models.InvoiceDeleteRequest,
        headers: btrip_open_20220520_models.InvoiceDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvoiceDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoice_delete_with_options_async(
        self,
        request: btrip_open_20220520_models.InvoiceDeleteRequest,
        headers: btrip_open_20220520_models.InvoiceDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvoiceDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoice_delete(
        self,
        request: btrip_open_20220520_models.InvoiceDeleteRequest,
    ) -> btrip_open_20220520_models.InvoiceDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceDeleteHeaders()
        return self.invoice_delete_with_options(request, headers, runtime)

    async def invoice_delete_async(
        self,
        request: btrip_open_20220520_models.InvoiceDeleteRequest,
    ) -> btrip_open_20220520_models.InvoiceDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceDeleteHeaders()
        return await self.invoice_delete_with_options_async(request, headers, runtime)

    def invoice_modify_with_options(
        self,
        request: btrip_open_20220520_models.InvoiceModifyRequest,
        headers: btrip_open_20220520_models.InvoiceModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.bank_name):
            body['bank_name'] = request.bank_name
        if not UtilClient.is_unset(request.bank_no):
            body['bank_no'] = request.bank_no
        if not UtilClient.is_unset(request.tax_no):
            body['tax_no'] = request.tax_no
        if not UtilClient.is_unset(request.tel):
            body['tel'] = request.tel
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoice_modify_with_options_async(
        self,
        request: btrip_open_20220520_models.InvoiceModifyRequest,
        headers: btrip_open_20220520_models.InvoiceModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.bank_name):
            body['bank_name'] = request.bank_name
        if not UtilClient.is_unset(request.bank_no):
            body['bank_no'] = request.bank_no
        if not UtilClient.is_unset(request.tax_no):
            body['tax_no'] = request.tax_no
        if not UtilClient.is_unset(request.tel):
            body['tel'] = request.tel
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoice_modify(
        self,
        request: btrip_open_20220520_models.InvoiceModifyRequest,
    ) -> btrip_open_20220520_models.InvoiceModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceModifyHeaders()
        return self.invoice_modify_with_options(request, headers, runtime)

    async def invoice_modify_async(
        self,
        request: btrip_open_20220520_models.InvoiceModifyRequest,
    ) -> btrip_open_20220520_models.InvoiceModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceModifyHeaders()
        return await self.invoice_modify_with_options_async(request, headers, runtime)

    def invoice_rule_add_with_options(
        self,
        tmp_req: btrip_open_20220520_models.InvoiceRuleAddRequest,
        headers: btrip_open_20220520_models.InvoiceRuleAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceRuleAddResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.InvoiceRuleAddShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        body = {}
        if not UtilClient.is_unset(request.entities_shrink):
            body['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceRuleAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice-rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceRuleAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoice_rule_add_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.InvoiceRuleAddRequest,
        headers: btrip_open_20220520_models.InvoiceRuleAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceRuleAddResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.InvoiceRuleAddShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        body = {}
        if not UtilClient.is_unset(request.entities_shrink):
            body['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceRuleAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice-rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceRuleAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoice_rule_add(
        self,
        request: btrip_open_20220520_models.InvoiceRuleAddRequest,
    ) -> btrip_open_20220520_models.InvoiceRuleAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceRuleAddHeaders()
        return self.invoice_rule_add_with_options(request, headers, runtime)

    async def invoice_rule_add_async(
        self,
        request: btrip_open_20220520_models.InvoiceRuleAddRequest,
    ) -> btrip_open_20220520_models.InvoiceRuleAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceRuleAddHeaders()
        return await self.invoice_rule_add_with_options_async(request, headers, runtime)

    def invoice_rule_delete_with_options(
        self,
        tmp_req: btrip_open_20220520_models.InvoiceRuleDeleteRequest,
        headers: btrip_open_20220520_models.InvoiceRuleDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceRuleDeleteResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.InvoiceRuleDeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        query = {}
        if not UtilClient.is_unset(request.del_all):
            query['del_all'] = request.del_all
        if not UtilClient.is_unset(request.entities_shrink):
            query['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvoiceRuleDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice-rule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceRuleDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoice_rule_delete_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.InvoiceRuleDeleteRequest,
        headers: btrip_open_20220520_models.InvoiceRuleDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceRuleDeleteResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.InvoiceRuleDeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        query = {}
        if not UtilClient.is_unset(request.del_all):
            query['del_all'] = request.del_all
        if not UtilClient.is_unset(request.entities_shrink):
            query['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvoiceRuleDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice-rule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceRuleDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoice_rule_delete(
        self,
        request: btrip_open_20220520_models.InvoiceRuleDeleteRequest,
    ) -> btrip_open_20220520_models.InvoiceRuleDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceRuleDeleteHeaders()
        return self.invoice_rule_delete_with_options(request, headers, runtime)

    async def invoice_rule_delete_async(
        self,
        request: btrip_open_20220520_models.InvoiceRuleDeleteRequest,
    ) -> btrip_open_20220520_models.InvoiceRuleDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceRuleDeleteHeaders()
        return await self.invoice_rule_delete_with_options_async(request, headers, runtime)

    def invoice_rule_save_with_options(
        self,
        tmp_req: btrip_open_20220520_models.InvoiceRuleSaveRequest,
        headers: btrip_open_20220520_models.InvoiceRuleSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceRuleSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.InvoiceRuleSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        body = {}
        if not UtilClient.is_unset(request.all_employe):
            body['all_employe'] = request.all_employe
        if not UtilClient.is_unset(request.entities_shrink):
            body['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceRuleSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice-rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceRuleSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoice_rule_save_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.InvoiceRuleSaveRequest,
        headers: btrip_open_20220520_models.InvoiceRuleSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceRuleSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.InvoiceRuleSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entities):
            request.entities_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entities, 'entities', 'json')
        body = {}
        if not UtilClient.is_unset(request.all_employe):
            body['all_employe'] = request.all_employe
        if not UtilClient.is_unset(request.entities_shrink):
            body['entities'] = request.entities_shrink
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvoiceRuleSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice-rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceRuleSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoice_rule_save(
        self,
        request: btrip_open_20220520_models.InvoiceRuleSaveRequest,
    ) -> btrip_open_20220520_models.InvoiceRuleSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceRuleSaveHeaders()
        return self.invoice_rule_save_with_options(request, headers, runtime)

    async def invoice_rule_save_async(
        self,
        request: btrip_open_20220520_models.InvoiceRuleSaveRequest,
    ) -> btrip_open_20220520_models.InvoiceRuleSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceRuleSaveHeaders()
        return await self.invoice_rule_save_with_options_async(request, headers, runtime)

    def invoice_search_with_options(
        self,
        request: btrip_open_20220520_models.InvoiceSearchRequest,
        headers: btrip_open_20220520_models.InvoiceSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvoiceSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoice_search_with_options_async(
        self,
        request: btrip_open_20220520_models.InvoiceSearchRequest,
        headers: btrip_open_20220520_models.InvoiceSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.InvoiceSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvoiceSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/invoice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.InvoiceSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoice_search(
        self,
        request: btrip_open_20220520_models.InvoiceSearchRequest,
    ) -> btrip_open_20220520_models.InvoiceSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceSearchHeaders()
        return self.invoice_search_with_options(request, headers, runtime)

    async def invoice_search_async(
        self,
        request: btrip_open_20220520_models.InvoiceSearchRequest,
    ) -> btrip_open_20220520_models.InvoiceSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.InvoiceSearchHeaders()
        return await self.invoice_search_with_options_async(request, headers, runtime)

    def isv_rule_save_with_options(
        self,
        request: btrip_open_20220520_models.IsvRuleSaveRequest,
        headers: btrip_open_20220520_models.IsvRuleSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.IsvRuleSaveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.book_type):
            body['book_type'] = request.book_type
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsvRuleSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.IsvRuleSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def isv_rule_save_with_options_async(
        self,
        request: btrip_open_20220520_models.IsvRuleSaveRequest,
        headers: btrip_open_20220520_models.IsvRuleSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.IsvRuleSaveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.book_type):
            body['book_type'] = request.book_type
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsvRuleSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.IsvRuleSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def isv_rule_save(
        self,
        request: btrip_open_20220520_models.IsvRuleSaveRequest,
    ) -> btrip_open_20220520_models.IsvRuleSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.IsvRuleSaveHeaders()
        return self.isv_rule_save_with_options(request, headers, runtime)

    async def isv_rule_save_async(
        self,
        request: btrip_open_20220520_models.IsvRuleSaveRequest,
    ) -> btrip_open_20220520_models.IsvRuleSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.IsvRuleSaveHeaders()
        return await self.isv_rule_save_with_options_async(request, headers, runtime)

    def isv_user_save_with_options(
        self,
        tmp_req: btrip_open_20220520_models.IsvUserSaveRequest,
        headers: btrip_open_20220520_models.IsvUserSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.IsvUserSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.IsvUserSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_list):
            request.user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_list, 'user_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.user_list_shrink):
            body['user_list'] = request.user_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsvUserSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/isvuser/v1/isvuser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.IsvUserSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def isv_user_save_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.IsvUserSaveRequest,
        headers: btrip_open_20220520_models.IsvUserSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.IsvUserSaveResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.IsvUserSaveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_list):
            request.user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_list, 'user_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.user_list_shrink):
            body['user_list'] = request.user_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsvUserSave',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/isvuser/v1/isvuser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.IsvUserSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def isv_user_save(
        self,
        request: btrip_open_20220520_models.IsvUserSaveRequest,
    ) -> btrip_open_20220520_models.IsvUserSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.IsvUserSaveHeaders()
        return self.isv_user_save_with_options(request, headers, runtime)

    async def isv_user_save_async(
        self,
        request: btrip_open_20220520_models.IsvUserSaveRequest,
    ) -> btrip_open_20220520_models.IsvUserSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.IsvUserSaveHeaders()
        return await self.isv_user_save_with_options_async(request, headers, runtime)

    def month_bill_confirm_with_options(
        self,
        request: btrip_open_20220520_models.MonthBillConfirmRequest,
        headers: btrip_open_20220520_models.MonthBillConfirmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.MonthBillConfirmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mail_bill_date):
            body['mail_bill_date'] = request.mail_bill_date
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MonthBillConfirm',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/bill/v1/status/action/confirm',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.MonthBillConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    async def month_bill_confirm_with_options_async(
        self,
        request: btrip_open_20220520_models.MonthBillConfirmRequest,
        headers: btrip_open_20220520_models.MonthBillConfirmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.MonthBillConfirmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mail_bill_date):
            body['mail_bill_date'] = request.mail_bill_date
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MonthBillConfirm',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/bill/v1/status/action/confirm',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.MonthBillConfirmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def month_bill_confirm(
        self,
        request: btrip_open_20220520_models.MonthBillConfirmRequest,
    ) -> btrip_open_20220520_models.MonthBillConfirmResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.MonthBillConfirmHeaders()
        return self.month_bill_confirm_with_options(request, headers, runtime)

    async def month_bill_confirm_async(
        self,
        request: btrip_open_20220520_models.MonthBillConfirmRequest,
    ) -> btrip_open_20220520_models.MonthBillConfirmResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.MonthBillConfirmHeaders()
        return await self.month_bill_confirm_with_options_async(request, headers, runtime)

    def month_bill_get_with_options(
        self,
        request: btrip_open_20220520_models.MonthBillGetRequest,
        headers: btrip_open_20220520_models.MonthBillGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.MonthBillGetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_month):
            query['bill_month'] = request.bill_month
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MonthBillGet',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/open/v1/month-bill',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.MonthBillGetResponse(),
            self.call_api(params, req, runtime)
        )

    async def month_bill_get_with_options_async(
        self,
        request: btrip_open_20220520_models.MonthBillGetRequest,
        headers: btrip_open_20220520_models.MonthBillGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.MonthBillGetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_month):
            query['bill_month'] = request.bill_month
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MonthBillGet',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/open/v1/month-bill',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.MonthBillGetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def month_bill_get(
        self,
        request: btrip_open_20220520_models.MonthBillGetRequest,
    ) -> btrip_open_20220520_models.MonthBillGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.MonthBillGetHeaders()
        return self.month_bill_get_with_options(request, headers, runtime)

    async def month_bill_get_async(
        self,
        request: btrip_open_20220520_models.MonthBillGetRequest,
    ) -> btrip_open_20220520_models.MonthBillGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.MonthBillGetHeaders()
        return await self.month_bill_get_with_options_async(request, headers, runtime)

    def project_add_with_options(
        self,
        request: btrip_open_20220520_models.ProjectAddRequest,
        headers: btrip_open_20220520_models.ProjectAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ProjectAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.project_name):
            body['project_name'] = request.project_name
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProjectAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/cost/v1/project',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ProjectAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_add_with_options_async(
        self,
        request: btrip_open_20220520_models.ProjectAddRequest,
        headers: btrip_open_20220520_models.ProjectAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ProjectAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.project_name):
            body['project_name'] = request.project_name
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProjectAdd',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/cost/v1/project',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ProjectAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_add(
        self,
        request: btrip_open_20220520_models.ProjectAddRequest,
    ) -> btrip_open_20220520_models.ProjectAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ProjectAddHeaders()
        return self.project_add_with_options(request, headers, runtime)

    async def project_add_async(
        self,
        request: btrip_open_20220520_models.ProjectAddRequest,
    ) -> btrip_open_20220520_models.ProjectAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ProjectAddHeaders()
        return await self.project_add_with_options_async(request, headers, runtime)

    def project_delete_with_options(
        self,
        request: btrip_open_20220520_models.ProjectDeleteRequest,
        headers: btrip_open_20220520_models.ProjectDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ProjectDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/cost/v1/project',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ProjectDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_delete_with_options_async(
        self,
        request: btrip_open_20220520_models.ProjectDeleteRequest,
        headers: btrip_open_20220520_models.ProjectDeleteHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ProjectDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.third_part_id):
            query['third_part_id'] = request.third_part_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectDelete',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/cost/v1/project',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ProjectDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_delete(
        self,
        request: btrip_open_20220520_models.ProjectDeleteRequest,
    ) -> btrip_open_20220520_models.ProjectDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ProjectDeleteHeaders()
        return self.project_delete_with_options(request, headers, runtime)

    async def project_delete_async(
        self,
        request: btrip_open_20220520_models.ProjectDeleteRequest,
    ) -> btrip_open_20220520_models.ProjectDeleteResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ProjectDeleteHeaders()
        return await self.project_delete_with_options_async(request, headers, runtime)

    def project_modify_with_options(
        self,
        request: btrip_open_20220520_models.ProjectModifyRequest,
        headers: btrip_open_20220520_models.ProjectModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ProjectModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.project_name):
            body['project_name'] = request.project_name
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProjectModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/cost/v1/project',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ProjectModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_modify_with_options_async(
        self,
        request: btrip_open_20220520_models.ProjectModifyRequest,
        headers: btrip_open_20220520_models.ProjectModifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.ProjectModifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.project_name):
            body['project_name'] = request.project_name
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['third_part_cost_center_id'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_id):
            body['third_part_id'] = request.third_part_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['third_part_invoice_id'] = request.third_part_invoice_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProjectModify',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/cost/v1/project',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.ProjectModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_modify(
        self,
        request: btrip_open_20220520_models.ProjectModifyRequest,
    ) -> btrip_open_20220520_models.ProjectModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ProjectModifyHeaders()
        return self.project_modify_with_options(request, headers, runtime)

    async def project_modify_async(
        self,
        request: btrip_open_20220520_models.ProjectModifyRequest,
    ) -> btrip_open_20220520_models.ProjectModifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.ProjectModifyHeaders()
        return await self.project_modify_with_options_async(request, headers, runtime)

    def query_reimbursement_order_with_options(
        self,
        request: btrip_open_20220520_models.QueryReimbursementOrderRequest,
        headers: btrip_open_20220520_models.QueryReimbursementOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.QueryReimbursementOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reimb_order_no):
            query['reimb_order_no'] = request.reimb_order_no
        if not UtilClient.is_unset(request.sub_corp_id):
            query['sub_corp_id'] = request.sub_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReimbursementOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/reimbursement/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.QueryReimbursementOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_reimbursement_order_with_options_async(
        self,
        request: btrip_open_20220520_models.QueryReimbursementOrderRequest,
        headers: btrip_open_20220520_models.QueryReimbursementOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.QueryReimbursementOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reimb_order_no):
            query['reimb_order_no'] = request.reimb_order_no
        if not UtilClient.is_unset(request.sub_corp_id):
            query['sub_corp_id'] = request.sub_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReimbursementOrder',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/reimbursement/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.QueryReimbursementOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_reimbursement_order(
        self,
        request: btrip_open_20220520_models.QueryReimbursementOrderRequest,
    ) -> btrip_open_20220520_models.QueryReimbursementOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.QueryReimbursementOrderHeaders()
        return self.query_reimbursement_order_with_options(request, headers, runtime)

    async def query_reimbursement_order_async(
        self,
        request: btrip_open_20220520_models.QueryReimbursementOrderRequest,
    ) -> btrip_open_20220520_models.QueryReimbursementOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.QueryReimbursementOrderHeaders()
        return await self.query_reimbursement_order_with_options_async(request, headers, runtime)

    def sync_single_user_with_options(
        self,
        tmp_req: btrip_open_20220520_models.SyncSingleUserRequest,
        headers: btrip_open_20220520_models.SyncSingleUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.SyncSingleUserResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.SyncSingleUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.third_depart_id_list):
            request.third_depart_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_depart_id_list, 'third_depart_id_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.job_no):
            body['job_no'] = request.job_no
        if not UtilClient.is_unset(request.leave_status):
            body['leave_status'] = request.leave_status
        if not UtilClient.is_unset(request.manager_user_id):
            body['manager_user_id'] = request.manager_user_id
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.position):
            body['position'] = request.position
        if not UtilClient.is_unset(request.position_level):
            body['position_level'] = request.position_level
        if not UtilClient.is_unset(request.real_name_en):
            body['real_name_en'] = request.real_name_en
        if not UtilClient.is_unset(request.third_depart_id_list_shrink):
            body['third_depart_id_list'] = request.third_depart_id_list_shrink
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncSingleUser',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/single-user/action/sync',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.SyncSingleUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_single_user_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.SyncSingleUserRequest,
        headers: btrip_open_20220520_models.SyncSingleUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.SyncSingleUserResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.SyncSingleUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.third_depart_id_list):
            request.third_depart_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_depart_id_list, 'third_depart_id_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.job_no):
            body['job_no'] = request.job_no
        if not UtilClient.is_unset(request.leave_status):
            body['leave_status'] = request.leave_status
        if not UtilClient.is_unset(request.manager_user_id):
            body['manager_user_id'] = request.manager_user_id
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.position):
            body['position'] = request.position
        if not UtilClient.is_unset(request.position_level):
            body['position_level'] = request.position_level
        if not UtilClient.is_unset(request.real_name_en):
            body['real_name_en'] = request.real_name_en
        if not UtilClient.is_unset(request.third_depart_id_list_shrink):
            body['third_depart_id_list'] = request.third_depart_id_list_shrink
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncSingleUser',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/single-user/action/sync',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.SyncSingleUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_single_user(
        self,
        request: btrip_open_20220520_models.SyncSingleUserRequest,
    ) -> btrip_open_20220520_models.SyncSingleUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.SyncSingleUserHeaders()
        return self.sync_single_user_with_options(request, headers, runtime)

    async def sync_single_user_async(
        self,
        request: btrip_open_20220520_models.SyncSingleUserRequest,
    ) -> btrip_open_20220520_models.SyncSingleUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.SyncSingleUserHeaders()
        return await self.sync_single_user_with_options_async(request, headers, runtime)

    def sync_third_user_mapping_with_options(
        self,
        request: btrip_open_20220520_models.SyncThirdUserMappingRequest,
        headers: btrip_open_20220520_models.SyncThirdUserMappingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.SyncThirdUserMappingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_channel_type):
            body['third_channel_type'] = request.third_channel_type
        if not UtilClient.is_unset(request.third_user_id):
            body['third_user_id'] = request.third_user_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncThirdUserMapping',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/third-users/action/mapping',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.SyncThirdUserMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_third_user_mapping_with_options_async(
        self,
        request: btrip_open_20220520_models.SyncThirdUserMappingRequest,
        headers: btrip_open_20220520_models.SyncThirdUserMappingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.SyncThirdUserMappingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_channel_type):
            body['third_channel_type'] = request.third_channel_type
        if not UtilClient.is_unset(request.third_user_id):
            body['third_user_id'] = request.third_user_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncThirdUserMapping',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/third-users/action/mapping',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.SyncThirdUserMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_third_user_mapping(
        self,
        request: btrip_open_20220520_models.SyncThirdUserMappingRequest,
    ) -> btrip_open_20220520_models.SyncThirdUserMappingResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.SyncThirdUserMappingHeaders()
        return self.sync_third_user_mapping_with_options(request, headers, runtime)

    async def sync_third_user_mapping_async(
        self,
        request: btrip_open_20220520_models.SyncThirdUserMappingRequest,
    ) -> btrip_open_20220520_models.SyncThirdUserMappingResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.SyncThirdUserMappingHeaders()
        return await self.sync_third_user_mapping_with_options_async(request, headers, runtime)

    def ticket_changing_apply_with_options(
        self,
        tmp_req: btrip_open_20220520_models.TicketChangingApplyRequest,
        headers: btrip_open_20220520_models.TicketChangingApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.TicketChangingApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.modify_flight_info_list):
            request.modify_flight_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.modify_flight_info_list, 'modify_flight_info_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            body['dis_sub_order_id'] = request.dis_sub_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            body['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.modify_flight_info_list_shrink):
            body['modify_flight_info_list'] = request.modify_flight_info_list_shrink
        if not UtilClient.is_unset(request.ota_item_id):
            body['ota_item_id'] = request.ota_item_id
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        if not UtilClient.is_unset(request.session_id):
            body['session_id'] = request.session_id
        if not UtilClient.is_unset(request.whether_retry):
            body['whether_retry'] = request.whether_retry
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TicketChangingApply',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_changing_apply_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.TicketChangingApplyRequest,
        headers: btrip_open_20220520_models.TicketChangingApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.TicketChangingApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.modify_flight_info_list):
            request.modify_flight_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.modify_flight_info_list, 'modify_flight_info_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            body['dis_sub_order_id'] = request.dis_sub_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            body['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.modify_flight_info_list_shrink):
            body['modify_flight_info_list'] = request.modify_flight_info_list_shrink
        if not UtilClient.is_unset(request.ota_item_id):
            body['ota_item_id'] = request.ota_item_id
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        if not UtilClient.is_unset(request.session_id):
            body['session_id'] = request.session_id
        if not UtilClient.is_unset(request.whether_retry):
            body['whether_retry'] = request.whether_retry
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TicketChangingApply',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_changing_apply(
        self,
        request: btrip_open_20220520_models.TicketChangingApplyRequest,
    ) -> btrip_open_20220520_models.TicketChangingApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingApplyHeaders()
        return self.ticket_changing_apply_with_options(request, headers, runtime)

    async def ticket_changing_apply_async(
        self,
        request: btrip_open_20220520_models.TicketChangingApplyRequest,
    ) -> btrip_open_20220520_models.TicketChangingApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingApplyHeaders()
        return await self.ticket_changing_apply_with_options_async(request, headers, runtime)

    def ticket_changing_cancel_with_options(
        self,
        request: btrip_open_20220520_models.TicketChangingCancelRequest,
        headers: btrip_open_20220520_models.TicketChangingCancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingCancelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            query['dis_sub_order_id'] = request.dis_sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingCancel',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_changing_cancel_with_options_async(
        self,
        request: btrip_open_20220520_models.TicketChangingCancelRequest,
        headers: btrip_open_20220520_models.TicketChangingCancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingCancelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            query['dis_sub_order_id'] = request.dis_sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingCancel',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_changing_cancel(
        self,
        request: btrip_open_20220520_models.TicketChangingCancelRequest,
    ) -> btrip_open_20220520_models.TicketChangingCancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingCancelHeaders()
        return self.ticket_changing_cancel_with_options(request, headers, runtime)

    async def ticket_changing_cancel_async(
        self,
        request: btrip_open_20220520_models.TicketChangingCancelRequest,
    ) -> btrip_open_20220520_models.TicketChangingCancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingCancelHeaders()
        return await self.ticket_changing_cancel_with_options_async(request, headers, runtime)

    def ticket_changing_detail_with_options(
        self,
        request: btrip_open_20220520_models.TicketChangingDetailRequest,
        headers: btrip_open_20220520_models.TicketChangingDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            query['dis_sub_order_id'] = request.dis_sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingDetail',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_changing_detail_with_options_async(
        self,
        request: btrip_open_20220520_models.TicketChangingDetailRequest,
        headers: btrip_open_20220520_models.TicketChangingDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            query['dis_sub_order_id'] = request.dis_sub_order_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingDetail',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_changing_detail(
        self,
        request: btrip_open_20220520_models.TicketChangingDetailRequest,
    ) -> btrip_open_20220520_models.TicketChangingDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingDetailHeaders()
        return self.ticket_changing_detail_with_options(request, headers, runtime)

    async def ticket_changing_detail_async(
        self,
        request: btrip_open_20220520_models.TicketChangingDetailRequest,
    ) -> btrip_open_20220520_models.TicketChangingDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingDetailHeaders()
        return await self.ticket_changing_detail_with_options_async(request, headers, runtime)

    def ticket_changing_enquiry_with_options(
        self,
        request: btrip_open_20220520_models.TicketChangingEnquiryRequest,
        headers: btrip_open_20220520_models.TicketChangingEnquiryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingEnquiryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arr_city):
            query['arr_city'] = request.arr_city
        if not UtilClient.is_unset(request.dep_city):
            query['dep_city'] = request.dep_city
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            query['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.modify_depart_date):
            query['modify_depart_date'] = request.modify_depart_date
        if not UtilClient.is_unset(request.modify_flight_no):
            query['modify_flight_no'] = request.modify_flight_no
        if not UtilClient.is_unset(request.session_id):
            query['session_id'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingEnquiry',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/enquiry',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingEnquiryResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_changing_enquiry_with_options_async(
        self,
        request: btrip_open_20220520_models.TicketChangingEnquiryRequest,
        headers: btrip_open_20220520_models.TicketChangingEnquiryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingEnquiryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arr_city):
            query['arr_city'] = request.arr_city
        if not UtilClient.is_unset(request.dep_city):
            query['dep_city'] = request.dep_city
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            query['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.modify_depart_date):
            query['modify_depart_date'] = request.modify_depart_date
        if not UtilClient.is_unset(request.modify_flight_no):
            query['modify_flight_no'] = request.modify_flight_no
        if not UtilClient.is_unset(request.session_id):
            query['session_id'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingEnquiry',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/enquiry',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingEnquiryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_changing_enquiry(
        self,
        request: btrip_open_20220520_models.TicketChangingEnquiryRequest,
    ) -> btrip_open_20220520_models.TicketChangingEnquiryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingEnquiryHeaders()
        return self.ticket_changing_enquiry_with_options(request, headers, runtime)

    async def ticket_changing_enquiry_async(
        self,
        request: btrip_open_20220520_models.TicketChangingEnquiryRequest,
    ) -> btrip_open_20220520_models.TicketChangingEnquiryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingEnquiryHeaders()
        return await self.ticket_changing_enquiry_with_options_async(request, headers, runtime)

    def ticket_changing_flight_list_with_options(
        self,
        tmp_req: btrip_open_20220520_models.TicketChangingFlightListRequest,
        headers: btrip_open_20220520_models.TicketChangingFlightListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingFlightListResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.TicketChangingFlightListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.traveler_info_list):
            request.traveler_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_info_list, 'traveler_info_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.arr_city):
            query['arr_city'] = request.arr_city
        if not UtilClient.is_unset(request.dep_city):
            query['dep_city'] = request.dep_city
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            query['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.traveler_info_list_shrink):
            query['traveler_info_list'] = request.traveler_info_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingFlightList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/huge/dtb-flight/v1/ticket-changing-flight/action/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingFlightListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_changing_flight_list_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.TicketChangingFlightListRequest,
        headers: btrip_open_20220520_models.TicketChangingFlightListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingFlightListResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.TicketChangingFlightListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.traveler_info_list):
            request.traveler_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traveler_info_list, 'traveler_info_list', 'json')
        query = {}
        if not UtilClient.is_unset(request.arr_city):
            query['arr_city'] = request.arr_city
        if not UtilClient.is_unset(request.dep_city):
            query['dep_city'] = request.dep_city
        if not UtilClient.is_unset(request.dep_date):
            query['dep_date'] = request.dep_date
        if not UtilClient.is_unset(request.dis_order_id):
            query['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.is_voluntary):
            query['is_voluntary'] = request.is_voluntary
        if not UtilClient.is_unset(request.traveler_info_list_shrink):
            query['traveler_info_list'] = request.traveler_info_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketChangingFlightList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/huge/dtb-flight/v1/ticket-changing-flight/action/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingFlightListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_changing_flight_list(
        self,
        request: btrip_open_20220520_models.TicketChangingFlightListRequest,
    ) -> btrip_open_20220520_models.TicketChangingFlightListResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingFlightListHeaders()
        return self.ticket_changing_flight_list_with_options(request, headers, runtime)

    async def ticket_changing_flight_list_async(
        self,
        request: btrip_open_20220520_models.TicketChangingFlightListRequest,
    ) -> btrip_open_20220520_models.TicketChangingFlightListResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingFlightListHeaders()
        return await self.ticket_changing_flight_list_with_options_async(request, headers, runtime)

    def ticket_changing_pay_with_options(
        self,
        tmp_req: btrip_open_20220520_models.TicketChangingPayRequest,
        headers: btrip_open_20220520_models.TicketChangingPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingPayResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.TicketChangingPayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_pay_price):
            body['corp_pay_price'] = request.corp_pay_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            body['dis_sub_order_id'] = request.dis_sub_order_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.personal_pay_price):
            body['personal_pay_price'] = request.personal_pay_price
        if not UtilClient.is_unset(request.total_pay_price):
            body['total_pay_price'] = request.total_pay_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TicketChangingPay',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/pay',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingPayResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_changing_pay_with_options_async(
        self,
        tmp_req: btrip_open_20220520_models.TicketChangingPayRequest,
        headers: btrip_open_20220520_models.TicketChangingPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TicketChangingPayResponse:
        UtilClient.validate_model(tmp_req)
        request = btrip_open_20220520_models.TicketChangingPayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_pay_price):
            body['corp_pay_price'] = request.corp_pay_price
        if not UtilClient.is_unset(request.dis_order_id):
            body['dis_order_id'] = request.dis_order_id
        if not UtilClient.is_unset(request.dis_sub_order_id):
            body['dis_sub_order_id'] = request.dis_sub_order_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.personal_pay_price):
            body['personal_pay_price'] = request.personal_pay_price
        if not UtilClient.is_unset(request.total_pay_price):
            body['total_pay_price'] = request.total_pay_price
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TicketChangingPay',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/dtb-flight/v1/ticket-changing/action/pay',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TicketChangingPayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_changing_pay(
        self,
        request: btrip_open_20220520_models.TicketChangingPayRequest,
    ) -> btrip_open_20220520_models.TicketChangingPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingPayHeaders()
        return self.ticket_changing_pay_with_options(request, headers, runtime)

    async def ticket_changing_pay_async(
        self,
        request: btrip_open_20220520_models.TicketChangingPayRequest,
    ) -> btrip_open_20220520_models.TicketChangingPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TicketChangingPayHeaders()
        return await self.ticket_changing_pay_with_options_async(request, headers, runtime)

    def train_bill_settlement_query_with_options(
        self,
        request: btrip_open_20220520_models.TrainBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.TrainBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainBillSettlementQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def train_bill_settlement_query_with_options_async(
        self,
        request: btrip_open_20220520_models.TrainBillSettlementQueryRequest,
        headers: btrip_open_20220520_models.TrainBillSettlementQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainBillSettlementQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['period_end'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['period_start'] = request.period_start
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainBillSettlementQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v1/bill-settlement',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainBillSettlementQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def train_bill_settlement_query(
        self,
        request: btrip_open_20220520_models.TrainBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.TrainBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainBillSettlementQueryHeaders()
        return self.train_bill_settlement_query_with_options(request, headers, runtime)

    async def train_bill_settlement_query_async(
        self,
        request: btrip_open_20220520_models.TrainBillSettlementQueryRequest,
    ) -> btrip_open_20220520_models.TrainBillSettlementQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainBillSettlementQueryHeaders()
        return await self.train_bill_settlement_query_with_options_async(request, headers, runtime)

    def train_exceed_apply_query_with_options(
        self,
        request: btrip_open_20220520_models.TrainExceedApplyQueryRequest,
        headers: btrip_open_20220520_models.TrainExceedApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainExceedApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainExceedApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/train-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainExceedApplyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def train_exceed_apply_query_with_options_async(
        self,
        request: btrip_open_20220520_models.TrainExceedApplyQueryRequest,
        headers: btrip_open_20220520_models.TrainExceedApplyQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainExceedApplyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainExceedApplyQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/apply/v1/train-exceed',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainExceedApplyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def train_exceed_apply_query(
        self,
        request: btrip_open_20220520_models.TrainExceedApplyQueryRequest,
    ) -> btrip_open_20220520_models.TrainExceedApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainExceedApplyQueryHeaders()
        return self.train_exceed_apply_query_with_options(request, headers, runtime)

    async def train_exceed_apply_query_async(
        self,
        request: btrip_open_20220520_models.TrainExceedApplyQueryRequest,
    ) -> btrip_open_20220520_models.TrainExceedApplyQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainExceedApplyQueryHeaders()
        return await self.train_exceed_apply_query_with_options_async(request, headers, runtime)

    def train_order_list_query_with_options(
        self,
        request: btrip_open_20220520_models.TrainOrderListQueryRequest,
        headers: btrip_open_20220520_models.TrainOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainOrderListQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def train_order_list_query_with_options_async(
        self,
        request: btrip_open_20220520_models.TrainOrderListQueryRequest,
        headers: btrip_open_20220520_models.TrainOrderListQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainOrderListQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_apply):
            query['all_apply'] = request.all_apply
        if not UtilClient.is_unset(request.apply_id):
            query['apply_id'] = request.apply_id
        if not UtilClient.is_unset(request.depart_id):
            query['depart_id'] = request.depart_id
        if not UtilClient.is_unset(request.end_time):
            query['end_time'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['start_time'] = request.start_time
        if not UtilClient.is_unset(request.thirdpart_apply_id):
            query['thirdpart_apply_id'] = request.thirdpart_apply_id
        if not UtilClient.is_unset(request.update_end_time):
            query['update_end_time'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            query['update_start_time'] = request.update_start_time
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainOrderListQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v1/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainOrderListQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def train_order_list_query(
        self,
        request: btrip_open_20220520_models.TrainOrderListQueryRequest,
    ) -> btrip_open_20220520_models.TrainOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainOrderListQueryHeaders()
        return self.train_order_list_query_with_options(request, headers, runtime)

    async def train_order_list_query_async(
        self,
        request: btrip_open_20220520_models.TrainOrderListQueryRequest,
    ) -> btrip_open_20220520_models.TrainOrderListQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainOrderListQueryHeaders()
        return await self.train_order_list_query_with_options_async(request, headers, runtime)

    def train_order_query_with_options(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryRequest,
        headers: btrip_open_20220520_models.TrainOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainOrderQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def train_order_query_with_options_async(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryRequest,
        headers: btrip_open_20220520_models.TrainOrderQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainOrderQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainOrderQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v1/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainOrderQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def train_order_query(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryRequest,
    ) -> btrip_open_20220520_models.TrainOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainOrderQueryHeaders()
        return self.train_order_query_with_options(request, headers, runtime)

    async def train_order_query_async(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryRequest,
    ) -> btrip_open_20220520_models.TrainOrderQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainOrderQueryHeaders()
        return await self.train_order_query_with_options_async(request, headers, runtime)

    def train_order_query_v2with_options(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryV2Request,
        headers: btrip_open_20220520_models.TrainOrderQueryV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainOrderQueryV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainOrderQueryV2',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v2/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainOrderQueryV2Response(),
            self.call_api(params, req, runtime)
        )

    async def train_order_query_v2with_options_async(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryV2Request,
        headers: btrip_open_20220520_models.TrainOrderQueryV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainOrderQueryV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['order_id'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['user_id'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_corp_token):
            real_headers['x-acs-btrip-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainOrderQueryV2',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/train/v2/order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainOrderQueryV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def train_order_query_v2(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryV2Request,
    ) -> btrip_open_20220520_models.TrainOrderQueryV2Response:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainOrderQueryV2Headers()
        return self.train_order_query_v2with_options(request, headers, runtime)

    async def train_order_query_v2_async(
        self,
        request: btrip_open_20220520_models.TrainOrderQueryV2Request,
    ) -> btrip_open_20220520_models.TrainOrderQueryV2Response:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainOrderQueryV2Headers()
        return await self.train_order_query_v2with_options_async(request, headers, runtime)

    def train_station_search_with_options(
        self,
        request: btrip_open_20220520_models.TrainStationSearchRequest,
        headers: btrip_open_20220520_models.TrainStationSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainStationSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainStationSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/train',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainStationSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def train_station_search_with_options_async(
        self,
        request: btrip_open_20220520_models.TrainStationSearchRequest,
        headers: btrip_open_20220520_models.TrainStationSearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainStationSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainStationSearch',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/city/v1/train',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainStationSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def train_station_search(
        self,
        request: btrip_open_20220520_models.TrainStationSearchRequest,
    ) -> btrip_open_20220520_models.TrainStationSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainStationSearchHeaders()
        return self.train_station_search_with_options(request, headers, runtime)

    async def train_station_search_async(
        self,
        request: btrip_open_20220520_models.TrainStationSearchRequest,
    ) -> btrip_open_20220520_models.TrainStationSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainStationSearchHeaders()
        return await self.train_station_search_with_options_async(request, headers, runtime)

    def train_ticket_scan_query_with_options(
        self,
        request: btrip_open_20220520_models.TrainTicketScanQueryRequest,
        headers: btrip_open_20220520_models.TrainTicketScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainTicketScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainTicketScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/train-ticket',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainTicketScanQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def train_ticket_scan_query_with_options_async(
        self,
        request: btrip_open_20220520_models.TrainTicketScanQueryRequest,
        headers: btrip_open_20220520_models.TrainTicketScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.TrainTicketScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrainTicketScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/train-ticket',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.TrainTicketScanQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def train_ticket_scan_query(
        self,
        request: btrip_open_20220520_models.TrainTicketScanQueryRequest,
    ) -> btrip_open_20220520_models.TrainTicketScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainTicketScanQueryHeaders()
        return self.train_ticket_scan_query_with_options(request, headers, runtime)

    async def train_ticket_scan_query_async(
        self,
        request: btrip_open_20220520_models.TrainTicketScanQueryRequest,
    ) -> btrip_open_20220520_models.TrainTicketScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.TrainTicketScanQueryHeaders()
        return await self.train_ticket_scan_query_with_options_async(request, headers, runtime)

    def user_query_with_options(
        self,
        request: btrip_open_20220520_models.UserQueryRequest,
        headers: btrip_open_20220520_models.UserQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.UserQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.modified_time_greater_or_equal_than):
            query['modified_time_greater_or_equal_than'] = request.modified_time_greater_or_equal_than
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        if not UtilClient.is_unset(request.third_part_job_no):
            query['third_part_job_no'] = request.third_part_job_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/user',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.UserQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_query_with_options_async(
        self,
        request: btrip_open_20220520_models.UserQueryRequest,
        headers: btrip_open_20220520_models.UserQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.UserQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.modified_time_greater_or_equal_than):
            query['modified_time_greater_or_equal_than'] = request.modified_time_greater_or_equal_than
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        if not UtilClient.is_unset(request.third_part_job_no):
            query['third_part_job_no'] = request.third_part_job_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/user/v1/user',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.UserQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_query(
        self,
        request: btrip_open_20220520_models.UserQueryRequest,
    ) -> btrip_open_20220520_models.UserQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.UserQueryHeaders()
        return self.user_query_with_options(request, headers, runtime)

    async def user_query_async(
        self,
        request: btrip_open_20220520_models.UserQueryRequest,
    ) -> btrip_open_20220520_models.UserQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.UserQueryHeaders()
        return await self.user_query_with_options_async(request, headers, runtime)

    def vat_invoice_scan_query_with_options(
        self,
        request: btrip_open_20220520_models.VatInvoiceScanQueryRequest,
        headers: btrip_open_20220520_models.VatInvoiceScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.VatInvoiceScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VatInvoiceScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/vat-invoice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.VatInvoiceScanQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def vat_invoice_scan_query_with_options_async(
        self,
        request: btrip_open_20220520_models.VatInvoiceScanQueryRequest,
        headers: btrip_open_20220520_models.VatInvoiceScanQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.VatInvoiceScanQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        if not UtilClient.is_unset(request.bill_id):
            query['bill_id'] = request.bill_id
        if not UtilClient.is_unset(request.invoice_sub_task_id):
            query['invoice_sub_task_id'] = request.invoice_sub_task_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VatInvoiceScanQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/scan/v1/vat-invoice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.VatInvoiceScanQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vat_invoice_scan_query(
        self,
        request: btrip_open_20220520_models.VatInvoiceScanQueryRequest,
    ) -> btrip_open_20220520_models.VatInvoiceScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.VatInvoiceScanQueryHeaders()
        return self.vat_invoice_scan_query_with_options(request, headers, runtime)

    async def vat_invoice_scan_query_async(
        self,
        request: btrip_open_20220520_models.VatInvoiceScanQueryRequest,
    ) -> btrip_open_20220520_models.VatInvoiceScanQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.VatInvoiceScanQueryHeaders()
        return await self.vat_invoice_scan_query_with_options_async(request, headers, runtime)

    def wait_apply_invoice_task_detail_query_with_options(
        self,
        request: btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryRequest,
        headers: btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WaitApplyInvoiceTaskDetailQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/wait-apply-task',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def wait_apply_invoice_task_detail_query_with_options_async(
        self,
        request: btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryRequest,
        headers: btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_date):
            query['bill_date'] = request.bill_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_btrip_so_corp_token):
            real_headers['x-acs-btrip-so-corp-token'] = UtilClient.to_jsonstring(headers.x_acs_btrip_so_corp_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WaitApplyInvoiceTaskDetailQuery',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/invoice/v1/wait-apply-task',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def wait_apply_invoice_task_detail_query(
        self,
        request: btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryRequest,
    ) -> btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryHeaders()
        return self.wait_apply_invoice_task_detail_query_with_options(request, headers, runtime)

    async def wait_apply_invoice_task_detail_query_async(
        self,
        request: btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryRequest,
    ) -> btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = btrip_open_20220520_models.WaitApplyInvoiceTaskDetailQueryHeaders()
        return await self.wait_apply_invoice_task_detail_query_with_options_async(request, headers, runtime)
