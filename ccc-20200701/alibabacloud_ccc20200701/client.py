# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ccc20200701 import models as ccc20200701_models
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
            'ap-northeast-1': 'ccc.aliyuncs.com',
            'ap-south-1': 'ccc.aliyuncs.com',
            'ap-southeast-1': 'ccc.aliyuncs.com',
            'ap-southeast-2': 'ccc.aliyuncs.com',
            'ap-southeast-3': 'ccc.aliyuncs.com',
            'ap-southeast-5': 'ccc.aliyuncs.com',
            'cn-beijing': 'ccc.aliyuncs.com',
            'cn-chengdu': 'ccc.aliyuncs.com',
            'cn-hongkong': 'ccc.aliyuncs.com',
            'cn-huhehaote': 'ccc.aliyuncs.com',
            'cn-qingdao': 'ccc.aliyuncs.com',
            'cn-shenzhen': 'ccc.aliyuncs.com',
            'cn-zhangjiakou': 'ccc.aliyuncs.com',
            'eu-central-1': 'ccc.aliyuncs.com',
            'eu-west-1': 'ccc.aliyuncs.com',
            'me-east-1': 'ccc.aliyuncs.com',
            'us-east-1': 'ccc.aliyuncs.com',
            'us-west-1': 'ccc.aliyuncs.com',
            'cn-hangzhou-finance': 'ccc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ccc.aliyuncs.com',
            'cn-shanghai-finance-1': 'ccc.aliyuncs.com',
            'cn-north-2-gov-1': 'ccc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ccc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_campaign_with_options(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AbortCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AbortCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_campaign_with_options_async(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AbortCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AbortCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_campaign(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
    ) -> ccc20200701_models.AbortCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return self.abort_campaign_with_options(request, runtime)

    async def abort_campaign_async(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
    ) -> ccc20200701_models.AbortCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abort_campaign_with_options_async(request, runtime)

    def add_numbers_to_skill_group_with_options(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNumbersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddNumbersToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_numbers_to_skill_group_with_options_async(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNumbersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddNumbersToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_numbers_to_skill_group(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_numbers_to_skill_group_with_options(request, runtime)

    async def add_numbers_to_skill_group_async(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_numbers_to_skill_group_with_options_async(request, runtime)

    def add_personal_numbers_to_user_with_options(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPersonalNumbersToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPersonalNumbersToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_personal_numbers_to_user_with_options_async(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPersonalNumbersToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPersonalNumbersToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_personal_numbers_to_user(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_personal_numbers_to_user_with_options(request, runtime)

    async def add_personal_numbers_to_user_async(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_personal_numbers_to_user_with_options_async(request, runtime)

    def add_phone_number_to_skill_groups_with_options(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumberToSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumberToSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_phone_number_to_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumberToSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumberToSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_phone_number_to_skill_groups(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_phone_number_to_skill_groups_with_options(request, runtime)

    async def add_phone_number_to_skill_groups_async(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_number_to_skill_groups_with_options_async(request, runtime)

    def add_phone_numbers_with_options(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['InstanceId'] = request.instance_id
        query['NumberGroupId'] = request.number_group_id
        query['NumberList'] = request.number_list
        query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['InstanceId'] = request.instance_id
        query['NumberGroupId'] = request.number_group_id
        query['NumberList'] = request.number_list
        query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_phone_numbers(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_phone_numbers_with_options(request, runtime)

    async def add_phone_numbers_async(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_numbers_with_options_async(request, runtime)

    def add_skill_groups_to_user_with_options(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillLevelList'] = request.skill_level_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSkillGroupsToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSkillGroupsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_skill_groups_to_user_with_options_async(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillLevelList'] = request.skill_level_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSkillGroupsToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSkillGroupsToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_skill_groups_to_user(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_skill_groups_to_user_with_options(request, runtime)

    async def add_skill_groups_to_user_async(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_skill_groups_to_user_with_options_async(request, runtime)

    def add_users_to_skill_group_with_options(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        query['UserSkillLevelList'] = request.user_skill_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddUsersToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_to_skill_group_with_options_async(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        query['UserSkillLevelList'] = request.user_skill_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddUsersToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users_to_skill_group(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_skill_group_with_options(request, runtime)

    async def add_users_to_skill_group_async(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_users_to_skill_group_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: ccc20200701_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnswerCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AnswerCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: ccc20200701_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnswerCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AnswerCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def answer_call(
        self,
        request: ccc20200701_models.AnswerCallRequest,
    ) -> ccc20200701_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: ccc20200701_models.AnswerCallRequest,
    ) -> ccc20200701_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def assign_users_with_options(
        self,
        request: ccc20200701_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AssignUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RamIdList'] = request.ram_id_list
        query['RoleId'] = request.role_id
        query['SkillLevelList'] = request.skill_level_list
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AssignUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_users_with_options_async(
        self,
        request: ccc20200701_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AssignUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RamIdList'] = request.ram_id_list
        query['RoleId'] = request.role_id
        query['SkillLevelList'] = request.skill_level_list
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AssignUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_users(
        self,
        request: ccc20200701_models.AssignUsersRequest,
    ) -> ccc20200701_models.AssignUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_users_with_options(request, runtime)

    async def assign_users_async(
        self,
        request: ccc20200701_models.AssignUsersRequest,
    ) -> ccc20200701_models.AssignUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_users_with_options_async(request, runtime)

    def barge_in_call_with_options(
        self,
        request: ccc20200701_models.BargeInCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BargeInCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BargedUserId'] = request.barged_user_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BargeInCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BargeInCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def barge_in_call_with_options_async(
        self,
        request: ccc20200701_models.BargeInCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BargeInCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BargedUserId'] = request.barged_user_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BargeInCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BargeInCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def barge_in_call(
        self,
        request: ccc20200701_models.BargeInCallRequest,
    ) -> ccc20200701_models.BargeInCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.barge_in_call_with_options(request, runtime)

    async def barge_in_call_async(
        self,
        request: ccc20200701_models.BargeInCallRequest,
    ) -> ccc20200701_models.BargeInCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.barge_in_call_with_options_async(request, runtime)

    def blind_transfer_with_options(
        self,
        request: ccc20200701_models.BlindTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BlindTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['Transferee'] = request.transferee
        query['Transferor'] = request.transferor
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlindTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BlindTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def blind_transfer_with_options_async(
        self,
        request: ccc20200701_models.BlindTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BlindTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['Transferee'] = request.transferee
        query['Transferor'] = request.transferor
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlindTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BlindTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def blind_transfer(
        self,
        request: ccc20200701_models.BlindTransferRequest,
    ) -> ccc20200701_models.BlindTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.blind_transfer_with_options(request, runtime)

    async def blind_transfer_async(
        self,
        request: ccc20200701_models.BlindTransferRequest,
    ) -> ccc20200701_models.BlindTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.blind_transfer_with_options_async(request, runtime)

    def cancel_attended_transfer_with_options(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CancelAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CancelAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_attended_transfer(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_attended_transfer_with_options(request, runtime)

    async def cancel_attended_transfer_async(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_attended_transfer_with_options_async(request, runtime)

    def change_work_mode_with_options(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeWorkMode',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeWorkModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_work_mode_with_options_async(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeWorkMode',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeWorkModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_work_mode(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_work_mode_with_options(request, runtime)

    async def change_work_mode_async(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_work_mode_with_options_async(request, runtime)

    def coach_call_with_options(
        self,
        request: ccc20200701_models.CoachCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CoachCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CoachedUserId'] = request.coached_user_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CoachCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CoachCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def coach_call_with_options_async(
        self,
        request: ccc20200701_models.CoachCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CoachCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CoachedUserId'] = request.coached_user_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CoachCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CoachCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def coach_call(
        self,
        request: ccc20200701_models.CoachCallRequest,
    ) -> ccc20200701_models.CoachCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.coach_call_with_options(request, runtime)

    async def coach_call_async(
        self,
        request: ccc20200701_models.CoachCallRequest,
    ) -> ccc20200701_models.CoachCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.coach_call_with_options_async(request, runtime)

    def complete_attended_transfer_with_options(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CompleteAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CompleteAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_attended_transfer(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_attended_transfer_with_options(request, runtime)

    async def complete_attended_transfer_async(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_attended_transfer_with_options_async(request, runtime)

    def create_campaign_with_options(
        self,
        tmp_req: ccc20200701_models.CreateCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCampaignResponse:
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.CreateCampaignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.case_list):
            request.case_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        query['CallableTime'] = request.callable_time
        query['CaseFileKey'] = request.case_file_key
        query['CaseList'] = request.case_list_shrink
        query['ContactFlowId'] = request.contact_flow_id
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['MaxAttemptCount'] = request.max_attempt_count
        query['MinAttemptInterval'] = request.min_attempt_interval
        query['Name'] = request.name
        query['QueueId'] = request.queue_id
        query['Simulation'] = request.simulation
        query['SimulationParameters'] = request.simulation_parameters
        query['StartTime'] = request.start_time
        query['StrategyParameters'] = request.strategy_parameters
        query['StrategyType'] = request.strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_campaign_with_options_async(
        self,
        tmp_req: ccc20200701_models.CreateCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCampaignResponse:
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.CreateCampaignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.case_list):
            request.case_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        query['CallableTime'] = request.callable_time
        query['CaseFileKey'] = request.case_file_key
        query['CaseList'] = request.case_list_shrink
        query['ContactFlowId'] = request.contact_flow_id
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['MaxAttemptCount'] = request.max_attempt_count
        query['MinAttemptInterval'] = request.min_attempt_interval
        query['Name'] = request.name
        query['QueueId'] = request.queue_id
        query['Simulation'] = request.simulation
        query['SimulationParameters'] = request.simulation_parameters
        query['StartTime'] = request.start_time
        query['StrategyParameters'] = request.strategy_parameters
        query['StrategyType'] = request.strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_campaign(
        self,
        request: ccc20200701_models.CreateCampaignRequest,
    ) -> ccc20200701_models.CreateCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_campaign_with_options(request, runtime)

    async def create_campaign_async(
        self,
        request: ccc20200701_models.CreateCampaignRequest,
    ) -> ccc20200701_models.CreateCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_campaign_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AdminRamIdList'] = request.admin_ram_id_list
        query['Description'] = request.description
        query['DomainName'] = request.domain_name
        query['Name'] = request.name
        query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AdminRamIdList'] = request.admin_ram_id_list
        query['Description'] = request.description
        query['DomainName'] = request.domain_name
        query['Name'] = request.name
        query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
    ) -> ccc20200701_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
    ) -> ccc20200701_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DisplayName'] = request.display_name
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DisplayName'] = request.display_name
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_group(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ccc20200701_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DisplayName'] = request.display_name
        query['Email'] = request.email
        query['InstanceId'] = request.instance_id
        query['LoginName'] = request.login_name
        query['Mobile'] = request.mobile
        query['ResetPassword'] = request.reset_password
        query['RoleId'] = request.role_id
        query['SkillLevelList'] = request.skill_level_list
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ccc20200701_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DisplayName'] = request.display_name
        query['Email'] = request.email
        query['InstanceId'] = request.instance_id
        query['LoginName'] = request.login_name
        query['Mobile'] = request.mobile
        query['ResetPassword'] = request.reset_password
        query['RoleId'] = request.role_id
        query['SkillLevelList'] = request.skill_level_list
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: ccc20200701_models.CreateUserRequest,
    ) -> ccc20200701_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ccc20200701_models.CreateUserRequest,
    ) -> ccc20200701_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Force'] = request.force
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Force'] = request.force
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_group(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def get_call_detail_record_with_options(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallDetailRecord',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCallDetailRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_detail_record_with_options_async(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallDetailRecord',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCallDetailRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_detail_record(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_call_detail_record_with_options(request, runtime)

    async def get_call_detail_record_async(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_call_detail_record_with_options_async(request, runtime)

    def get_campaign_with_options(
        self,
        request: ccc20200701_models.GetCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_campaign_with_options_async(
        self,
        request: ccc20200701_models.GetCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_campaign(
        self,
        request: ccc20200701_models.GetCampaignRequest,
    ) -> ccc20200701_models.GetCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_campaign_with_options(request, runtime)

    async def get_campaign_async(
        self,
        request: ccc20200701_models.GetCampaignRequest,
    ) -> ccc20200701_models.GetCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_campaign_with_options_async(request, runtime)

    def get_historical_caller_report_with_options(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallingNumber'] = request.calling_number
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        query['StopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalCallerReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCallerReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_caller_report_with_options_async(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallingNumber'] = request.calling_number
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        query['StopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalCallerReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCallerReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_caller_report(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_historical_caller_report_with_options(request, runtime)

    async def get_historical_caller_report_async(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_historical_caller_report_with_options_async(request, runtime)

    def get_historical_instance_report_with_options(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalInstanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_instance_report_with_options_async(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalInstanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_instance_report(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_historical_instance_report_with_options(request, runtime)

    async def get_historical_instance_report_async(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_historical_instance_report_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: ccc20200701_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: ccc20200701_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: ccc20200701_models.GetInstanceRequest,
    ) -> ccc20200701_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: ccc20200701_models.GetInstanceRequest,
    ) -> ccc20200701_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_trending_report_with_options(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceTrendingReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_trending_report_with_options_async(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceTrendingReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_trending_report(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_trending_report_with_options(request, runtime)

    async def get_instance_trending_report_async(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_trending_report_with_options_async(request, runtime)

    def get_login_details_with_options(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetLoginDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_details_with_options_async(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetLoginDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_details(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_details_with_options(request, runtime)

    async def get_login_details_async(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_details_with_options_async(request, runtime)

    def get_mono_recording_with_options(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonoRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMonoRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mono_recording_with_options_async(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonoRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMonoRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mono_recording(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mono_recording_with_options(request, runtime)

    async def get_mono_recording_async(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mono_recording_with_options_async(request, runtime)

    def get_multi_channel_recording_with_options(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiChannelRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMultiChannelRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_channel_recording_with_options_async(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiChannelRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMultiChannelRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_channel_recording(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multi_channel_recording_with_options(request, runtime)

    async def get_multi_channel_recording_async(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_channel_recording_with_options_async(request, runtime)

    def get_number_location_with_options(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNumberLocation',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetNumberLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_number_location_with_options_async(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNumberLocation',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetNumberLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_number_location(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_number_location_with_options(request, runtime)

    async def get_number_location_async(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_number_location_with_options_async(request, runtime)

    def get_realtime_instance_states_with_options(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeInstanceStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeInstanceStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_instance_states_with_options_async(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeInstanceStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeInstanceStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_instance_states(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_instance_states_with_options(request, runtime)

    async def get_realtime_instance_states_async(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_instance_states_with_options_async(request, runtime)

    def get_turn_credentials_with_options(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnCredentials',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_turn_credentials_with_options_async(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnCredentials',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_turn_credentials(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_turn_credentials_with_options(request, runtime)

    async def get_turn_credentials_async(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_turn_credentials_with_options_async(request, runtime)

    def get_turn_server_list_with_options(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnServerList',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnServerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_turn_server_list_with_options_async(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnServerList',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnServerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_turn_server_list(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_turn_server_list_with_options(request, runtime)

    async def get_turn_server_list_async(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_turn_server_list_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: ccc20200701_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Extension'] = request.extension
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ccc20200701_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Extension'] = request.extension
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: ccc20200701_models.GetUserRequest,
    ) -> ccc20200701_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ccc20200701_models.GetUserRequest,
    ) -> ccc20200701_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: ccc20200701_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.HoldCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['Music'] = request.music
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HoldCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.HoldCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: ccc20200701_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.HoldCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['Music'] = request.music
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HoldCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.HoldCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hold_call(
        self,
        request: ccc20200701_models.HoldCallRequest,
    ) -> ccc20200701_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: ccc20200701_models.HoldCallRequest,
    ) -> ccc20200701_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def initiate_attended_transfer_with_options(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['Transferee'] = request.transferee
        query['Transferor'] = request.transferor
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitiateAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InitiateAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def initiate_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['Transferee'] = request.transferee
        query['Transferor'] = request.transferor
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitiateAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InitiateAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initiate_attended_transfer(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.initiate_attended_transfer_with_options(request, runtime)

    async def initiate_attended_transfer_async(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initiate_attended_transfer_with_options_async(request, runtime)

    def intercept_call_with_options(
        self,
        request: ccc20200701_models.InterceptCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InterceptCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['InterceptedUserId'] = request.intercepted_user_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InterceptCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InterceptCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def intercept_call_with_options_async(
        self,
        request: ccc20200701_models.InterceptCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InterceptCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['InterceptedUserId'] = request.intercepted_user_id
        query['JobId'] = request.job_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InterceptCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InterceptCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def intercept_call(
        self,
        request: ccc20200701_models.InterceptCallRequest,
    ) -> ccc20200701_models.InterceptCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.intercept_call_with_options(request, runtime)

    async def intercept_call_async(
        self,
        request: ccc20200701_models.InterceptCallRequest,
    ) -> ccc20200701_models.InterceptCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.intercept_call_with_options_async(request, runtime)

    def launch_authentication_with_options(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchAuthentication',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_authentication_with_options_async(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchAuthentication',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_authentication(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_authentication_with_options(request, runtime)

    async def launch_authentication_async(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_authentication_with_options_async(request, runtime)

    def launch_survey_with_options(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchSurvey',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchSurveyResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_survey_with_options_async(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchSurvey',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchSurveyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_survey(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_survey_with_options(request, runtime)

    async def launch_survey_async(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_survey_with_options_async(request, runtime)

    def list_agent_state_logs_with_options(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentId'] = request.agent_id
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentStateLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_state_logs_with_options_async(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentId'] = request.agent_id
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentStateLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_state_logs(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_state_logs_with_options(request, runtime)

    async def list_agent_state_logs_async(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_state_logs_with_options_async(request, runtime)

    def list_attempts_with_options(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAttemptsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAttempts',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAttemptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_attempts_with_options_async(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAttemptsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAttempts',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAttemptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_attempts(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
    ) -> ccc20200701_models.ListAttemptsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_attempts_with_options(request, runtime)

    async def list_attempts_async(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
    ) -> ccc20200701_models.ListAttemptsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_attempts_with_options_async(request, runtime)

    def list_brief_skill_groups_with_options(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBriefSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBriefSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_brief_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBriefSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBriefSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_brief_skill_groups(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_brief_skill_groups_with_options(request, runtime)

    async def list_brief_skill_groups_async(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_brief_skill_groups_with_options_async(request, runtime)

    def list_call_detail_records_with_options(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentId'] = request.agent_id
        query['CalledNumber'] = request.called_number
        query['CallingNumber'] = request.calling_number
        query['ContactDisposition'] = request.contact_disposition
        query['ContactId'] = request.contact_id
        query['ContactType'] = request.contact_type
        query['Criteria'] = request.criteria
        query['EarlyMediaStateList'] = request.early_media_state_list
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['OrderByField'] = request.order_by_field
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        query['SatisfactionList'] = request.satisfaction_list
        query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        query['SkillGroupId'] = request.skill_group_id
        query['SortOrder'] = request.sort_order
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallDetailRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_detail_records_with_options_async(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentId'] = request.agent_id
        query['CalledNumber'] = request.called_number
        query['CallingNumber'] = request.calling_number
        query['ContactDisposition'] = request.contact_disposition
        query['ContactId'] = request.contact_id
        query['ContactType'] = request.contact_type
        query['Criteria'] = request.criteria
        query['EarlyMediaStateList'] = request.early_media_state_list
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['OrderByField'] = request.order_by_field
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        query['SatisfactionList'] = request.satisfaction_list
        query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        query['SkillGroupId'] = request.skill_group_id
        query['SortOrder'] = request.sort_order
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallDetailRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_detail_records(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    async def list_call_detail_records_async(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_detail_records_with_options_async(request, runtime)

    def list_campaign_trending_report_with_options(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaignTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignTrendingReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_campaign_trending_report_with_options_async(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaignTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignTrendingReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_campaign_trending_report(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_campaign_trending_report_with_options(request, runtime)

    async def list_campaign_trending_report_async(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_campaign_trending_report_with_options_async(request, runtime)

    def list_campaigns_with_options(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActualStartTimeFrom'] = request.actual_start_time_from
        query['ActualStartTimeTo'] = request.actual_start_time_to
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PlanedStartTimeFrom'] = request.planed_start_time_from
        query['PlanedStartTimeTo'] = request.planed_start_time_to
        query['QueueId'] = request.queue_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaigns',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_campaigns_with_options_async(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActualStartTimeFrom'] = request.actual_start_time_from
        query['ActualStartTimeTo'] = request.actual_start_time_to
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PlanedStartTimeFrom'] = request.planed_start_time_from
        query['PlanedStartTimeTo'] = request.planed_start_time_to
        query['QueueId'] = request.queue_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaigns',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_campaigns(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
    ) -> ccc20200701_models.ListCampaignsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_campaigns_with_options(request, runtime)

    async def list_campaigns_async(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
    ) -> ccc20200701_models.ListCampaignsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_campaigns_with_options_async(request, runtime)

    def list_cases_with_options(
        self,
        request: ccc20200701_models.ListCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCasesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cases_with_options_async(
        self,
        request: ccc20200701_models.ListCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCasesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cases(
        self,
        request: ccc20200701_models.ListCasesRequest,
    ) -> ccc20200701_models.ListCasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cases_with_options(request, runtime)

    async def list_cases_async(
        self,
        request: ccc20200701_models.ListCasesRequest,
    ) -> ccc20200701_models.ListCasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cases_with_options_async(request, runtime)

    def list_config_items_with_options(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ObjectId'] = request.object_id
        query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListConfigItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_items_with_options_async(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ObjectId'] = request.object_id
        query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListConfigItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_items(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_items_with_options(request, runtime)

    async def list_config_items_async(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_items_with_options_async(request, runtime)

    def list_contact_flows_with_options(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContactFlows',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListContactFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contact_flows_with_options_async(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContactFlows',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListContactFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contact_flows(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_contact_flows_with_options(request, runtime)

    async def list_contact_flows_async(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_contact_flows_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: ccc20200701_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: ccc20200701_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_devices(
        self,
        request: ccc20200701_models.ListDevicesRequest,
    ) -> ccc20200701_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: ccc20200701_models.ListDevicesRequest,
    ) -> ccc20200701_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def list_historical_agent_report_with_options(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['StopTime'] = request.stop_time
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_agent_report_with_options_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['StopTime'] = request.stop_time
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_agent_report(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_historical_agent_report_with_options(request, runtime)

    async def list_historical_agent_report_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_historical_agent_report_with_options_async(request, runtime)

    def list_historical_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_skill_group_report(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_historical_skill_group_report_with_options(request, runtime)

    async def list_historical_skill_group_report_async(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_historical_skill_group_report_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: ccc20200701_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: ccc20200701_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: ccc20200701_models.ListInstancesRequest,
    ) -> ccc20200701_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: ccc20200701_models.ListInstancesRequest,
    ) -> ccc20200701_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_instances_of_user_with_options(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_of_user(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_of_user_with_options(request, runtime)

    async def list_instances_of_user_async(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_of_user_with_options_async(request, runtime)

    def list_interval_agent_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentId'] = request.agent_id
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Interval'] = request.interval
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_agent_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentId'] = request.agent_id
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Interval'] = request.interval
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_agent_report(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_interval_agent_report_with_options(request, runtime)

    async def list_interval_agent_report_async(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_agent_report_with_options_async(request, runtime)

    def list_interval_instance_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Interval'] = request.interval
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalInstanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_instance_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Interval'] = request.interval
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalInstanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_instance_report(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_interval_instance_report_with_options(request, runtime)

    async def list_interval_instance_report_async(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_instance_report_with_options_async(request, runtime)

    def list_interval_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Interval'] = request.interval
        query['SkillGroupId'] = request.skill_group_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Interval'] = request.interval
        query['SkillGroupId'] = request.skill_group_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_skill_group_report(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_interval_skill_group_report_with_options(request, runtime)

    async def list_interval_skill_group_report_async(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_skill_group_report_with_options_async(request, runtime)

    def list_ivr_tracking_details_with_options(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIvrTrackingDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIvrTrackingDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ivr_tracking_details_with_options_async(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactId'] = request.contact_id
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIvrTrackingDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIvrTrackingDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ivr_tracking_details(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ivr_tracking_details_with_options(request, runtime)

    async def list_ivr_tracking_details_async(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ivr_tracking_details_with_options_async(request, runtime)

    def list_outbound_numbers_of_user_with_options(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SkillGroupIdList'] = request.skill_group_id_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOutboundNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListOutboundNumbersOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_numbers_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SkillGroupIdList'] = request.skill_group_id_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOutboundNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListOutboundNumbersOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_numbers_of_user(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_numbers_of_user_with_options(request, runtime)

    async def list_outbound_numbers_of_user_async(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_numbers_of_user_with_options_async(request, runtime)

    def list_personal_numbers_of_user_with_options(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPersonalNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPersonalNumbersOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_personal_numbers_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPersonalNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPersonalNumbersOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_personal_numbers_of_user(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_personal_numbers_of_user_with_options(request, runtime)

    async def list_personal_numbers_of_user_async(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_personal_numbers_of_user_with_options_async(request, runtime)

    def list_phone_numbers_with_options(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Active'] = request.active
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Active'] = request.active
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_numbers(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_with_options(request, runtime)

    async def list_phone_numbers_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_numbers_with_options_async(request, runtime)

    def list_phone_numbers_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Active'] = request.active
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbersOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_numbers_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Active'] = request.active
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbersOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_numbers_of_skill_group(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_of_skill_group_with_options(request, runtime)

    async def list_phone_numbers_of_skill_group_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_numbers_of_skill_group_with_options_async(request, runtime)

    def list_privileges_of_user_with_options(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivilegesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPrivilegesOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_privileges_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivilegesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPrivilegesOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_privileges_of_user(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_privileges_of_user_with_options(request, runtime)

    async def list_privileges_of_user_async(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_privileges_of_user_with_options_async(request, runtime)

    def list_ram_users_with_options(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRamUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRamUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ram_users_with_options_async(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRamUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRamUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ram_users(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
    ) -> ccc20200701_models.ListRamUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ram_users_with_options(request, runtime)

    async def list_ram_users_async(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
    ) -> ccc20200701_models.ListRamUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ram_users_with_options_async(request, runtime)

    def list_realtime_agent_states_with_options(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentName'] = request.agent_name
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SkillGroupId'] = request.skill_group_id
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        if not UtilClient.is_unset(request.state_list):
            body['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeAgentStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeAgentStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_agent_states_with_options_async(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AgentName'] = request.agent_name
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SkillGroupId'] = request.skill_group_id
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        if not UtilClient.is_unset(request.state_list):
            body['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeAgentStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeAgentStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_agent_states(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_agent_states_with_options(request, runtime)

    async def list_realtime_agent_states_async(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_agent_states_with_options_async(request, runtime)

    def list_realtime_skill_group_states_with_options(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeSkillGroupStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeSkillGroupStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_skill_group_states_with_options_async(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeSkillGroupStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeSkillGroupStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_skill_group_states(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_skill_group_states_with_options(request, runtime)

    async def list_realtime_skill_group_states_async(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_skill_group_states_with_options_async(request, runtime)

    def list_recent_call_detail_records_with_options(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Criteria'] = request.criteria
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecentCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRecentCallDetailRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_call_detail_records_with_options_async(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Criteria'] = request.criteria
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecentCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRecentCallDetailRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_call_detail_records(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recent_call_detail_records_with_options(request, runtime)

    async def list_recent_call_detail_records_async(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recent_call_detail_records_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: ccc20200701_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: ccc20200701_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: ccc20200701_models.ListRolesRequest,
    ) -> ccc20200701_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: ccc20200701_models.ListRolesRequest,
    ) -> ccc20200701_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_sip_call_records_with_options(
        self,
        request: ccc20200701_models.ListSipCallRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSipCallRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactIdList'] = request.contact_id_list
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipCallRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSipCallRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sip_call_records_with_options_async(
        self,
        request: ccc20200701_models.ListSipCallRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSipCallRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactIdList'] = request.contact_id_list
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipCallRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSipCallRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sip_call_records(
        self,
        request: ccc20200701_models.ListSipCallRecordsRequest,
    ) -> ccc20200701_models.ListSipCallRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sip_call_records_with_options(request, runtime)

    async def list_sip_call_records_async(
        self,
        request: ccc20200701_models.ListSipCallRecordsRequest,
    ) -> ccc20200701_models.ListSipCallRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sip_call_records_with_options_async(request, runtime)

    def list_sip_traces_with_options(
        self,
        request: ccc20200701_models.ListSipTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSipTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTraces',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSipTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sip_traces_with_options_async(
        self,
        request: ccc20200701_models.ListSipTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSipTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTraces',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSipTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sip_traces(
        self,
        request: ccc20200701_models.ListSipTracesRequest,
    ) -> ccc20200701_models.ListSipTracesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sip_traces_with_options(request, runtime)

    async def list_sip_traces_async(
        self,
        request: ccc20200701_models.ListSipTracesRequest,
    ) -> ccc20200701_models.ListSipTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sip_traces_with_options_async(request, runtime)

    def list_skill_groups_with_options(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_groups(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_with_options(request, runtime)

    async def list_skill_groups_async(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_groups_with_options_async(request, runtime)

    def list_skill_levels_of_user_with_options(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillLevelsOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_levels_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillLevelsOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_levels_of_user(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_levels_of_user_with_options(request, runtime)

    async def list_skill_levels_of_user_async(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_levels_of_user_with_options_async(request, runtime)

    def list_unassigned_numbers_with_options(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUnassignedNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUnassignedNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_unassigned_numbers_with_options_async(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUnassignedNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUnassignedNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_unassigned_numbers(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_unassigned_numbers_with_options(request, runtime)

    async def list_unassigned_numbers_async(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_unassigned_numbers_with_options_async(request, runtime)

    def list_user_levels_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUserLevelsOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_levels_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['IsMember'] = request.is_member
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUserLevelsOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_levels_of_skill_group(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_levels_of_skill_group_with_options(request, runtime)

    async def list_user_levels_of_skill_group_async(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_levels_of_skill_group_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ccc20200701_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ccc20200701_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: ccc20200701_models.ListUsersRequest,
    ) -> ccc20200701_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ccc20200701_models.ListUsersRequest,
    ) -> ccc20200701_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def make_call_with_options(
        self,
        request: ccc20200701_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MakeCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['Caller'] = request.caller
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['MaskedCallee'] = request.masked_callee
        query['Tags'] = request.tags
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MakeCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_call_with_options_async(
        self,
        request: ccc20200701_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MakeCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['Caller'] = request.caller
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['MaskedCallee'] = request.masked_callee
        query['Tags'] = request.tags
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MakeCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_call(
        self,
        request: ccc20200701_models.MakeCallRequest,
    ) -> ccc20200701_models.MakeCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    async def make_call_async(
        self,
        request: ccc20200701_models.MakeCallRequest,
    ) -> ccc20200701_models.MakeCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.make_call_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_phone_number_with_options(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhoneNumber',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_phone_number_with_options_async(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContactFlowId'] = request.contact_flow_id
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhoneNumber',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_phone_number(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_number_with_options(request, runtime)

    async def modify_phone_number_async(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_phone_number_with_options_async(request, runtime)

    def modify_skill_group_with_options(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DisplayName'] = request.display_name
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DisplayName'] = request.display_name
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_skill_group(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_with_options(request, runtime)

    async def modify_skill_group_async(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_group_with_options_async(request, runtime)

    def modify_skill_levels_of_user_with_options(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillLevelList'] = request.skill_level_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillLevelsOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_skill_levels_of_user_with_options_async(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillLevelList'] = request.skill_level_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillLevelsOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_skill_levels_of_user(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_levels_of_user_with_options(request, runtime)

    async def modify_skill_levels_of_user_async(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_levels_of_user_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: ccc20200701_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Mobile'] = request.mobile
        query['RoleId'] = request.role_id
        query['UserId'] = request.user_id
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: ccc20200701_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Mobile'] = request.mobile
        query['RoleId'] = request.role_id
        query['UserId'] = request.user_id
        query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user(
        self,
        request: ccc20200701_models.ModifyUserRequest,
    ) -> ccc20200701_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: ccc20200701_models.ModifyUserRequest,
    ) -> ccc20200701_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def modify_user_levels_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        query['UserLevelList'] = request.user_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_levels_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        query['UserLevelList'] = request.user_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_levels_of_skill_group(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_levels_of_skill_group_with_options(request, runtime)

    async def modify_user_levels_of_skill_group_async(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_levels_of_skill_group_with_options_async(request, runtime)

    def monitor_call_with_options(
        self,
        request: ccc20200701_models.MonitorCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MonitorCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['MonitoredUserId'] = request.monitored_user_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MonitorCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MonitorCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def monitor_call_with_options_async(
        self,
        request: ccc20200701_models.MonitorCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MonitorCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['MonitoredUserId'] = request.monitored_user_id
        query['TimeoutSeconds'] = request.timeout_seconds
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MonitorCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MonitorCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def monitor_call(
        self,
        request: ccc20200701_models.MonitorCallRequest,
    ) -> ccc20200701_models.MonitorCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.monitor_call_with_options(request, runtime)

    async def monitor_call_async(
        self,
        request: ccc20200701_models.MonitorCallRequest,
    ) -> ccc20200701_models.MonitorCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.monitor_call_with_options_async(request, runtime)

    def mute_call_with_options(
        self,
        request: ccc20200701_models.MuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MuteCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MuteCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def mute_call_with_options_async(
        self,
        request: ccc20200701_models.MuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MuteCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MuteCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mute_call(
        self,
        request: ccc20200701_models.MuteCallRequest,
    ) -> ccc20200701_models.MuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.mute_call_with_options(request, runtime)

    async def mute_call_async(
        self,
        request: ccc20200701_models.MuteCallRequest,
    ) -> ccc20200701_models.MuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mute_call_with_options_async(request, runtime)

    def pause_campaign_with_options(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PauseCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PauseCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_campaign_with_options_async(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PauseCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PauseCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_campaign(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
    ) -> ccc20200701_models.PauseCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return self.pause_campaign_with_options(request, runtime)

    async def pause_campaign_async(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
    ) -> ccc20200701_models.PauseCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pause_campaign_with_options_async(request, runtime)

    def pick_outbound_numbers_with_options(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['Count'] = request.count
        query['InstanceId'] = request.instance_id
        query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PickOutboundNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PickOutboundNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def pick_outbound_numbers_with_options_async(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['Count'] = request.count
        query['InstanceId'] = request.instance_id
        query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PickOutboundNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PickOutboundNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pick_outbound_numbers(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.pick_outbound_numbers_with_options(request, runtime)

    async def pick_outbound_numbers_async(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pick_outbound_numbers_with_options_async(request, runtime)

    def poll_user_status_with_options(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PollUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollUserStatus',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PollUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_user_status_with_options_async(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PollUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollUserStatus',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PollUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_user_status(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
    ) -> ccc20200701_models.PollUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.poll_user_status_with_options(request, runtime)

    async def poll_user_status_async(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
    ) -> ccc20200701_models.PollUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.poll_user_status_with_options_async(request, runtime)

    def ready_for_service_with_options(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['OutboundScenario'] = request.outbound_scenario
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReadyForService',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReadyForServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def ready_for_service_with_options_async(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['OutboundScenario'] = request.outbound_scenario
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReadyForService',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReadyForServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ready_for_service(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.ready_for_service_with_options(request, runtime)

    async def ready_for_service_async(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ready_for_service_with_options_async(request, runtime)

    def register_device_with_options(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['Password'] = request.password
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['Password'] = request.password
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_device(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)

    def release_call_with_options(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReleaseCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReleaseCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_call_with_options_async(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReleaseCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReleaseCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_call(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
    ) -> ccc20200701_models.ReleaseCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_call_with_options(request, runtime)

    async def release_call_async(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
    ) -> ccc20200701_models.ReleaseCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_call_with_options_async(request, runtime)

    def remove_personal_numbers_from_user_with_options(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePersonalNumbersFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePersonalNumbersFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_personal_numbers_from_user_with_options_async(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePersonalNumbersFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePersonalNumbersFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_personal_numbers_from_user(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_personal_numbers_from_user_with_options(request, runtime)

    async def remove_personal_numbers_from_user_async(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_personal_numbers_from_user_with_options_async(request, runtime)

    def remove_phone_number_from_skill_groups_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumberFromSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_number_from_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Number'] = request.number
        query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumberFromSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_number_from_skill_groups(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_number_from_skill_groups_with_options(request, runtime)

    async def remove_phone_number_from_skill_groups_async(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_number_from_skill_groups_with_options_async(request, runtime)

    def remove_phone_numbers_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_numbers(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_with_options(request, runtime)

    async def remove_phone_numbers_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_numbers_with_options_async(request, runtime)

    def remove_phone_numbers_from_skill_group_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_numbers_from_skill_group_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NumberList'] = request.number_list
        query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_numbers_from_skill_group(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_from_skill_group_with_options(request, runtime)

    async def remove_phone_numbers_from_skill_group_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_numbers_from_skill_group_with_options_async(request, runtime)

    def remove_skill_groups_from_user_with_options(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupIdList'] = request.skill_group_id_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSkillGroupsFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveSkillGroupsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_skill_groups_from_user_with_options_async(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupIdList'] = request.skill_group_id_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSkillGroupsFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveSkillGroupsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_skill_groups_from_user(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_groups_from_user_with_options(request, runtime)

    async def remove_skill_groups_from_user_async(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_skill_groups_from_user_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
    ) -> ccc20200701_models.RemoveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
    ) -> ccc20200701_models.RemoveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def remove_users_from_skill_group_with_options(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_from_skill_group_with_options_async(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SkillGroupId'] = request.skill_group_id
        query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users_from_skill_group(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_skill_group_with_options(request, runtime)

    async def remove_users_from_skill_group_async(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_from_skill_group_with_options_async(request, runtime)

    def reset_agent_state_with_options(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAgentState',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetAgentStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_agent_state_with_options_async(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAgentState',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetAgentStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_agent_state(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_agent_state_with_options(request, runtime)

    async def reset_agent_state_async(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_agent_state_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Password'] = request.password
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Password'] = request.password
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def resume_campaign_with_options(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResumeCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_campaign_with_options_async(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResumeCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_campaign(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_campaign_with_options(request, runtime)

    async def resume_campaign_async(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_campaign_with_options_async(request, runtime)

    def retrieve_call_with_options(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RetrieveCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetrieveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RetrieveCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_call_with_options_async(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RetrieveCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetrieveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RetrieveCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_call(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
    ) -> ccc20200701_models.RetrieveCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.retrieve_call_with_options(request, runtime)

    async def retrieve_call_async(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
    ) -> ccc20200701_models.RetrieveCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retrieve_call_with_options_async(request, runtime)

    def save_rtcstats_v2with_options(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['GeneralInfo'] = request.general_info
        query['GoogAddress'] = request.goog_address
        query['InstanceId'] = request.instance_id
        query['ReceiverReport'] = request.receiver_report
        query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRTCStatsV2',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveRTCStatsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def save_rtcstats_v2with_options_async(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['GeneralInfo'] = request.general_info
        query['GoogAddress'] = request.goog_address
        query['InstanceId'] = request.instance_id
        query['ReceiverReport'] = request.receiver_report
        query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRTCStatsV2',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveRTCStatsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def save_rtcstats_v2(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.save_rtcstats_v2with_options(request, runtime)

    async def save_rtcstats_v2_async(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.save_rtcstats_v2with_options_async(request, runtime)

    def save_terminal_log_with_options(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['CallId'] = request.call_id
        query['Content'] = request.content
        query['DataType'] = request.data_type
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['MethodName'] = request.method_name
        query['Status'] = request.status
        query['UniqueRequestId'] = request.unique_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTerminalLog',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveTerminalLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_terminal_log_with_options_async(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['CallId'] = request.call_id
        query['Content'] = request.content
        query['DataType'] = request.data_type
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['MethodName'] = request.method_name
        query['Status'] = request.status
        query['UniqueRequestId'] = request.unique_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTerminalLog',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveTerminalLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_terminal_log(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_terminal_log_with_options(request, runtime)

    async def save_terminal_log_async(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_terminal_log_with_options_async(request, runtime)

    def save_web_rtcstats_with_options(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['GeneralInfo'] = request.general_info
        query['GoogAddress'] = request.goog_address
        query['InstanceId'] = request.instance_id
        query['ReceiverReport'] = request.receiver_report
        query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRTCStats',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRTCStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_web_rtcstats_with_options_async(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['GeneralInfo'] = request.general_info
        query['GoogAddress'] = request.goog_address
        query['InstanceId'] = request.instance_id
        query['ReceiverReport'] = request.receiver_report
        query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRTCStats',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRTCStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_web_rtcstats(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtcstats_with_options(request, runtime)

    async def save_web_rtcstats_async(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_web_rtcstats_with_options_async(request, runtime)

    def save_web_rtc_info_with_options(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['Content'] = request.content
        query['ContentType'] = request.content_type
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRtcInfo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRtcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_web_rtc_info_with_options_async(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['Content'] = request.content
        query['ContentType'] = request.content_type
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRtcInfo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRtcInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_web_rtc_info(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtc_info_with_options(request, runtime)

    async def save_web_rtc_info_async(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_web_rtc_info_with_options_async(request, runtime)

    def send_dtmf_signaling_with_options(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['Dtmf'] = request.dtmf
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendDtmfSignaling',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SendDtmfSignalingResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_dtmf_signaling_with_options_async(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['Dtmf'] = request.dtmf
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendDtmfSignaling',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SendDtmfSignalingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_dtmf_signaling(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_dtmf_signaling_with_options(request, runtime)

    async def send_dtmf_signaling_async(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_dtmf_signaling_with_options_async(request, runtime)

    def sign_in_group_with_options(
        self,
        request: ccc20200701_models.SignInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignInGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_in_group_with_options_async(
        self,
        request: ccc20200701_models.SignInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignInGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign_in_group(
        self,
        request: ccc20200701_models.SignInGroupRequest,
    ) -> ccc20200701_models.SignInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.sign_in_group_with_options(request, runtime)

    async def sign_in_group_async(
        self,
        request: ccc20200701_models.SignInGroupRequest,
    ) -> ccc20200701_models.SignInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sign_in_group_with_options_async(request, runtime)

    def sign_out_group_with_options(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignOutGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignOutGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignOutGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_out_group_with_options_async(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignOutGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignOutGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignOutGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign_out_group(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
    ) -> ccc20200701_models.SignOutGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.sign_out_group_with_options(request, runtime)

    async def sign_out_group_async(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
    ) -> ccc20200701_models.SignOutGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sign_out_group_with_options_async(request, runtime)

    def start_back_2back_call_with_options(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AdditionalBroker'] = request.additional_broker
        query['Broker'] = request.broker
        query['Callee'] = request.callee
        query['Caller'] = request.caller
        query['InstanceId'] = request.instance_id
        query['Tags'] = request.tags
        query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBack2BackCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartBack2BackCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_back_2back_call_with_options_async(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AdditionalBroker'] = request.additional_broker
        query['Broker'] = request.broker
        query['Callee'] = request.callee
        query['Caller'] = request.caller
        query['InstanceId'] = request.instance_id
        query['Tags'] = request.tags
        query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBack2BackCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartBack2BackCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_back_2back_call(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_back_2back_call_with_options(request, runtime)

    async def start_back_2back_call_async(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_back_2back_call_with_options_async(request, runtime)

    def start_predictive_call_with_options(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['Caller'] = request.caller
        query['ContactFlowId'] = request.contact_flow_id
        query['ContactFlowVariables'] = request.contact_flow_variables
        query['InstanceId'] = request.instance_id
        query['MaskedCallee'] = request.masked_callee
        query['SkillGroupId'] = request.skill_group_id
        query['Tags'] = request.tags
        query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPredictiveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPredictiveCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_predictive_call_with_options_async(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['Caller'] = request.caller
        query['ContactFlowId'] = request.contact_flow_id
        query['ContactFlowVariables'] = request.contact_flow_variables
        query['InstanceId'] = request.instance_id
        query['MaskedCallee'] = request.masked_callee
        query['SkillGroupId'] = request.skill_group_id
        query['Tags'] = request.tags
        query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPredictiveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPredictiveCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_predictive_call(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_predictive_call_with_options(request, runtime)

    async def start_predictive_call_async(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_predictive_call_with_options_async(request, runtime)

    def submit_campaign_with_options(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SubmitCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_campaign_with_options_async(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CampaignId'] = request.campaign_id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SubmitCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_campaign(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_campaign_with_options(request, runtime)

    async def submit_campaign_async(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_campaign_with_options_async(request, runtime)

    def take_break_with_options(
        self,
        request: ccc20200701_models.TakeBreakRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.TakeBreakResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Code'] = request.code
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TakeBreak',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.TakeBreakResponse(),
            self.call_api(params, req, runtime)
        )

    async def take_break_with_options_async(
        self,
        request: ccc20200701_models.TakeBreakRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.TakeBreakResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Code'] = request.code
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TakeBreak',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.TakeBreakResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def take_break(
        self,
        request: ccc20200701_models.TakeBreakRequest,
    ) -> ccc20200701_models.TakeBreakResponse:
        runtime = util_models.RuntimeOptions()
        return self.take_break_with_options(request, runtime)

    async def take_break_async(
        self,
        request: ccc20200701_models.TakeBreakRequest,
    ) -> ccc20200701_models.TakeBreakResponse:
        runtime = util_models.RuntimeOptions()
        return await self.take_break_with_options_async(request, runtime)

    def unmute_call_with_options(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnmuteCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnmuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UnmuteCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def unmute_call_with_options_async(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnmuteCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ChannelId'] = request.channel_id
        query['DeviceId'] = request.device_id
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnmuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UnmuteCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unmute_call(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
    ) -> ccc20200701_models.UnmuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.unmute_call_with_options(request, runtime)

    async def unmute_call_async(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
    ) -> ccc20200701_models.UnmuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unmute_call_with_options_async(request, runtime)

    def update_config_items_with_options(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigItems'] = request.config_items
        query['InstanceId'] = request.instance_id
        query['ObjectId'] = request.object_id
        query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateConfigItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_items_with_options_async(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigItems'] = request.config_items
        query['InstanceId'] = request.instance_id
        query['ObjectId'] = request.object_id
        query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateConfigItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_items(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_config_items_with_options(request, runtime)

    async def update_config_items_async(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_config_items_with_options_async(request, runtime)
