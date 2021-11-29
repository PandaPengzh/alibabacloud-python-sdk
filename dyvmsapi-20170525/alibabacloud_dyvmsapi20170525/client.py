# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyvmsapi20170525 import models as dyvmsapi_20170525_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dyvmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_rtc_account_with_options(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRtcAccount',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddRtcAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_rtc_account_with_options_async(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRtcAccount',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddRtcAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rtc_account(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_rtc_account_with_options(request, runtime)

    async def add_rtc_account_async(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_rtc_account_with_options_async(request, runtime)

    def add_virtual_number_relation_with_options(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CorpNameList'] = request.corp_name_list
        query['NumberList'] = request.number_list
        query['OwnerId'] = request.owner_id
        query['PhoneNum'] = request.phone_num
        query['ProdCode'] = request.prod_code
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RouteType'] = request.route_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddVirtualNumberRelation',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddVirtualNumberRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_virtual_number_relation_with_options_async(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CorpNameList'] = request.corp_name_list
        query['NumberList'] = request.number_list
        query['OwnerId'] = request.owner_id
        query['PhoneNum'] = request.phone_num
        query['ProdCode'] = request.prod_code
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RouteType'] = request.route_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddVirtualNumberRelation',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddVirtualNumberRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_virtual_number_relation(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_virtual_number_relation_with_options(request, runtime)

    async def add_virtual_number_relation_async(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_virtual_number_relation_with_options_async(request, runtime)

    def batch_robot_smart_call_with_options(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['CorpName'] = request.corp_name
        query['DialogId'] = request.dialog_id
        query['EarlyMediaAsr'] = request.early_media_asr
        query['IsSelfLine'] = request.is_self_line
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ScheduleCall'] = request.schedule_call
        query['ScheduleTime'] = request.schedule_time
        query['TaskName'] = request.task_name
        query['TtsParam'] = request.tts_param
        query['TtsParamHead'] = request.tts_param_head
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchRobotSmartCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BatchRobotSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_robot_smart_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['CorpName'] = request.corp_name
        query['DialogId'] = request.dialog_id
        query['EarlyMediaAsr'] = request.early_media_asr
        query['IsSelfLine'] = request.is_self_line
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ScheduleCall'] = request.schedule_call
        query['ScheduleTime'] = request.schedule_time
        query['TaskName'] = request.task_name
        query['TtsParam'] = request.tts_param
        query['TtsParamHead'] = request.tts_param_head
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchRobotSmartCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BatchRobotSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_robot_smart_call(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_robot_smart_call_with_options(request, runtime)

    async def batch_robot_smart_call_async(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_robot_smart_call_with_options_async(request, runtime)

    def cancel_call_with_options(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_call(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_call_with_options(request, runtime)

    async def cancel_call_async(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_call_with_options_async(request, runtime)

    def cancel_order_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelOrderRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelOrderRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelOrderRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelOrderRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order_robot_task(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_robot_task_with_options(request, runtime)

    async def cancel_order_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_robot_task_with_options_async(request, runtime)

    def cancel_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_robot_task(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_robot_task_with_options(request, runtime)

    async def cancel_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_robot_task_with_options_async(request, runtime)

    def click_to_dial_with_options(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AsrFlag'] = request.asr_flag
        query['AsrModelId'] = request.asr_model_id
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['CallerNumber'] = request.caller_number
        query['CallerShowNumber'] = request.caller_show_number
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['RecordFlag'] = request.record_flag
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SessionTimeout'] = request.session_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClickToDial',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ClickToDialResponse(),
            self.call_api(params, req, runtime)
        )

    async def click_to_dial_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AsrFlag'] = request.asr_flag
        query['AsrModelId'] = request.asr_model_id
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['CallerNumber'] = request.caller_number
        query['CallerShowNumber'] = request.caller_show_number
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['RecordFlag'] = request.record_flag
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SessionTimeout'] = request.session_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClickToDial',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ClickToDialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def click_to_dial(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        runtime = util_models.RuntimeOptions()
        return self.click_to_dial_with_options(request, runtime)

    async def click_to_dial_async(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.click_to_dial_with_options_async(request, runtime)

    def create_call_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['Data'] = request.data
        query['DataType'] = request.data_type
        query['FireTime'] = request.fire_time
        query['OwnerId'] = request.owner_id
        query['Resource'] = request.resource
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
        query['ScheduleType'] = request.schedule_type
        query['StopTime'] = request.stop_time
        query['TaskName'] = request.task_name
        query['TemplateCode'] = request.template_code
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_call_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['Data'] = request.data
        query['DataType'] = request.data_type
        query['FireTime'] = request.fire_time
        query['OwnerId'] = request.owner_id
        query['Resource'] = request.resource
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
        query['ScheduleType'] = request.schedule_type
        query['StopTime'] = request.stop_time
        query['TaskName'] = request.task_name
        query['TemplateCode'] = request.template_code
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_call_task(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_call_task_with_options(request, runtime)

    async def create_call_task_async(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_call_task_with_options_async(request, runtime)

    def create_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Caller'] = request.caller
        query['CorpName'] = request.corp_name
        query['DialogId'] = request.dialog_id
        query['IsSelfLine'] = request.is_self_line
        query['NumberStatusIdent'] = request.number_status_ident
        query['OwnerId'] = request.owner_id
        query['RecallInterval'] = request.recall_interval
        query['RecallStateCodes'] = request.recall_state_codes
        query['RecallTimes'] = request.recall_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RetryType'] = request.retry_type
        query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Caller'] = request.caller
        query['CorpName'] = request.corp_name
        query['DialogId'] = request.dialog_id
        query['IsSelfLine'] = request.is_self_line
        query['NumberStatusIdent'] = request.number_status_ident
        query['OwnerId'] = request.owner_id
        query['RecallInterval'] = request.recall_interval
        query['RecallStateCodes'] = request.recall_state_codes
        query['RecallTimes'] = request.recall_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RetryType'] = request.retry_type
        query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_robot_task(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_robot_task_with_options(request, runtime)

    async def create_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_robot_task_with_options_async(request, runtime)

    def delete_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DeleteRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DeleteRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_robot_task(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_robot_task_with_options(request, runtime)

    async def delete_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_robot_task_with_options_async(request, runtime)

    def execute_call_task_with_options(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FireTime'] = request.fire_time
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ExecuteCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_call_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FireTime'] = request.fire_time
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ExecuteCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_call_task(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_call_task_with_options(request, runtime)

    async def execute_call_task_async(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_call_task_with_options_async(request, runtime)

    def get_call_info_with_options(
        self,
        request: dyvmsapi_20170525_models.GetCallInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetCallInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RtcId'] = request.rtc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetCallInfo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetCallInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_info_with_options_async(
        self,
        request: dyvmsapi_20170525_models.GetCallInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetCallInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RtcId'] = request.rtc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetCallInfo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetCallInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_info(
        self,
        request: dyvmsapi_20170525_models.GetCallInfoRequest,
    ) -> dyvmsapi_20170525_models.GetCallInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_call_info_with_options(request, runtime)

    async def get_call_info_async(
        self,
        request: dyvmsapi_20170525_models.GetCallInfoRequest,
    ) -> dyvmsapi_20170525_models.GetCallInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_call_info_with_options_async(request, runtime)

    def get_hotline_qualification_by_order_with_options(
        self,
        request: dyvmsapi_20170525_models.GetHotlineQualificationByOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OrderId'] = request.order_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHotlineQualificationByOrder',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_qualification_by_order_with_options_async(
        self,
        request: dyvmsapi_20170525_models.GetHotlineQualificationByOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OrderId'] = request.order_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHotlineQualificationByOrder',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_qualification_by_order(
        self,
        request: dyvmsapi_20170525_models.GetHotlineQualificationByOrderRequest,
    ) -> dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_qualification_by_order_with_options(request, runtime)

    async def get_hotline_qualification_by_order_async(
        self,
        request: dyvmsapi_20170525_models.GetHotlineQualificationByOrderRequest,
    ) -> dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_qualification_by_order_with_options_async(request, runtime)

    def get_mqtt_token_with_options(
        self,
        request: dyvmsapi_20170525_models.GetMqttTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetMqttTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMqttToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetMqttTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mqtt_token_with_options_async(
        self,
        request: dyvmsapi_20170525_models.GetMqttTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetMqttTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMqttToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetMqttTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mqtt_token(
        self,
        request: dyvmsapi_20170525_models.GetMqttTokenRequest,
    ) -> dyvmsapi_20170525_models.GetMqttTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mqtt_token_with_options(request, runtime)

    async def get_mqtt_token_async(
        self,
        request: dyvmsapi_20170525_models.GetMqttTokenRequest,
    ) -> dyvmsapi_20170525_models.GetMqttTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mqtt_token_with_options_async(request, runtime)

    def get_rtc_token_with_options(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['IsCustomAccount'] = request.is_custom_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRtcToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetRtcTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rtc_token_with_options_async(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['IsCustomAccount'] = request.is_custom_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRtcToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetRtcTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rtc_token(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rtc_token_with_options(request, runtime)

    async def get_rtc_token_async(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rtc_token_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TokenType'] = request.token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TokenType'] = request.token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def ivr_call_with_options(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ByeCode'] = request.bye_code
        query['ByeTtsParams'] = request.bye_tts_params
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['MenuKeyMap'] = request.menu_key_map
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PlayTimes'] = request.play_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartCode'] = request.start_code
        query['StartTtsParams'] = request.start_tts_params
        query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IvrCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.IvrCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def ivr_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ByeCode'] = request.bye_code
        query['ByeTtsParams'] = request.bye_tts_params
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['MenuKeyMap'] = request.menu_key_map
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PlayTimes'] = request.play_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartCode'] = request.start_code
        query['StartTtsParams'] = request.start_tts_params
        query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IvrCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.IvrCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ivr_call(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.ivr_call_with_options(request, runtime)

    async def ivr_call_async(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ivr_call_with_options_async(request, runtime)

    def list_call_task_with_options(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        query['TaskName'] = request.task_name
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        query['TaskName'] = request.task_name
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_task(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_with_options(request, runtime)

    async def list_call_task_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_task_with_options_async(request, runtime)

    def list_call_task_detail_with_options(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNum'] = request.called_num
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCallTaskDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_task_detail_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNum'] = request.called_num
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCallTaskDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_task_detail(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_detail_with_options(request, runtime)

    async def list_call_task_detail_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_task_detail_with_options_async(request, runtime)

    def list_hotline_transfer_number_with_options(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['HotlineNumber'] = request.hotline_number
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListHotlineTransferNumber',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotline_transfer_number_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['HotlineNumber'] = request.hotline_number
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListHotlineTransferNumber',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotline_transfer_number(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferNumberRequest,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_transfer_number_with_options(request, runtime)

    async def list_hotline_transfer_number_async(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferNumberRequest,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hotline_transfer_number_with_options_async(request, runtime)

    def list_hotline_transfer_register_file_with_options(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferRegisterFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['HotlineNumber'] = request.hotline_number
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListHotlineTransferRegisterFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotline_transfer_register_file_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferRegisterFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['HotlineNumber'] = request.hotline_number
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListHotlineTransferRegisterFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotline_transfer_register_file(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferRegisterFileRequest,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_transfer_register_file_with_options(request, runtime)

    async def list_hotline_transfer_register_file_async(
        self,
        request: dyvmsapi_20170525_models.ListHotlineTransferRegisterFileRequest,
    ) -> dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hotline_transfer_register_file_with_options_async(request, runtime)

    def query_call_detail_by_call_id_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['OwnerId'] = request.owner_id
        query['ProdId'] = request.prod_id
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallDetailByCallId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_detail_by_call_id_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['OwnerId'] = request.owner_id
        query['ProdId'] = request.prod_id
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallDetailByCallId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_detail_by_call_id(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_call_id_with_options(request, runtime)

    async def query_call_detail_by_call_id_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_detail_by_call_id_with_options_async(request, runtime)

    def query_call_detail_by_task_id_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['OwnerId'] = request.owner_id
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallDetailByTaskId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_detail_by_task_id_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['OwnerId'] = request.owner_id
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallDetailByTaskId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_detail_by_task_id(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_task_id_with_options(request, runtime)

    async def query_call_detail_by_task_id_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_detail_by_task_id_with_options_async(request, runtime)

    def query_call_in_pool_transfer_config_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryCallInPoolTransferConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PhoneNumber'] = request.phone_number
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallInPoolTransferConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_in_pool_transfer_config_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallInPoolTransferConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PhoneNumber'] = request.phone_number
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallInPoolTransferConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_in_pool_transfer_config(
        self,
        request: dyvmsapi_20170525_models.QueryCallInPoolTransferConfigRequest,
    ) -> dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_in_pool_transfer_config_with_options(request, runtime)

    async def query_call_in_pool_transfer_config_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallInPoolTransferConfigRequest,
    ) -> dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_in_pool_transfer_config_with_options_async(request, runtime)

    def query_call_in_transfer_record_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryCallInTransferRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallInTransferRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallInCaller'] = request.call_in_caller
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['PhoneNumber'] = request.phone_number
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallInTransferRecord',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_in_transfer_record_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallInTransferRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallInTransferRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallInCaller'] = request.call_in_caller
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['PhoneNumber'] = request.phone_number
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCallInTransferRecord',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInTransferRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_in_transfer_record(
        self,
        request: dyvmsapi_20170525_models.QueryCallInTransferRecordRequest,
    ) -> dyvmsapi_20170525_models.QueryCallInTransferRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_in_transfer_record_with_options(request, runtime)

    async def query_call_in_transfer_record_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallInTransferRecordRequest,
    ) -> dyvmsapi_20170525_models.QueryCallInTransferRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_in_transfer_record_with_options_async(request, runtime)

    def query_robot_info_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuditStatus'] = request.audit_status
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotInfoList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_info_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuditStatus'] = request.audit_status
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotInfoList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_info_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_info_list_with_options(request, runtime)

    async def query_robot_info_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_info_list_with_options_async(request, runtime)

    def query_robot_task_call_detail_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['OwnerId'] = request.owner_id
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskCallDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_call_detail_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Callee'] = request.callee
        query['OwnerId'] = request.owner_id
        query['QueryDate'] = request.query_date
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskCallDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_call_detail(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_detail_with_options(request, runtime)

    async def query_robot_task_call_detail_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_call_detail_with_options_async(request, runtime)

    def query_robot_task_call_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallResult'] = request.call_result
        query['Called'] = request.called
        query['DialogCountFrom'] = request.dialog_count_from
        query['DialogCountTo'] = request.dialog_count_to
        query['DurationFrom'] = request.duration_from
        query['DurationTo'] = request.duration_to
        query['HangupDirection'] = request.hangup_direction
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskCallList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_call_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallResult'] = request.call_result
        query['Called'] = request.called
        query['DialogCountFrom'] = request.dialog_count_from
        query['DialogCountTo'] = request.dialog_count_to
        query['DurationFrom'] = request.duration_from
        query['DurationTo'] = request.duration_to
        query['HangupDirection'] = request.hangup_direction
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskCallList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_call_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_list_with_options(request, runtime)

    async def query_robot_task_call_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_call_list_with_options_async(request, runtime)

    def query_robot_task_detail_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_detail_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_detail(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_detail_with_options(request, runtime)

    async def query_robot_task_detail_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_detail_with_options_async(request, runtime)

    def query_robot_task_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskName'] = request.task_name
        query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['TaskName'] = request.task_name
        query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_list_with_options(request, runtime)

    async def query_robot_task_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_list_with_options_async(request, runtime)

    def query_robotv_2all_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotv2AllList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotv2AllListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robotv_2all_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRobotv2AllList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotv2AllListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robotv_2all_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robotv_2all_list_with_options(request, runtime)

    async def query_robotv_2all_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robotv_2all_list_with_options_async(request, runtime)

    def query_virtual_number_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProdCode'] = request.prod_code
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RouteType'] = request.route_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVirtualNumber',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_virtual_number_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProdCode'] = request.prod_code
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RouteType'] = request.route_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVirtualNumber',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_virtual_number(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_with_options(request, runtime)

    async def query_virtual_number_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_virtual_number_with_options_async(request, runtime)

    def query_virtual_number_relation_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['PhoneNum'] = request.phone_num
        query['ProdCode'] = request.prod_code
        query['QualificationId'] = request.qualification_id
        query['RegionNameCity'] = request.region_name_city
        query['RelatedNum'] = request.related_num
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RouteType'] = request.route_type
        query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVirtualNumberRelation',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_virtual_number_relation_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['PhoneNum'] = request.phone_num
        query['ProdCode'] = request.prod_code
        query['QualificationId'] = request.qualification_id
        query['RegionNameCity'] = request.region_name_city
        query['RelatedNum'] = request.related_num
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RouteType'] = request.route_type
        query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVirtualNumberRelation',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_virtual_number_relation(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_relation_with_options(request, runtime)

    async def query_virtual_number_relation_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_virtual_number_relation_with_options_async(request, runtime)

    def refresh_mqtt_token_with_options(
        self,
        request: dyvmsapi_20170525_models.RefreshMqttTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.RefreshMqttTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientId'] = request.client_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshMqttToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.RefreshMqttTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_mqtt_token_with_options_async(
        self,
        request: dyvmsapi_20170525_models.RefreshMqttTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.RefreshMqttTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientId'] = request.client_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshMqttToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.RefreshMqttTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_mqtt_token(
        self,
        request: dyvmsapi_20170525_models.RefreshMqttTokenRequest,
    ) -> dyvmsapi_20170525_models.RefreshMqttTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_mqtt_token_with_options(request, runtime)

    async def refresh_mqtt_token_async(
        self,
        request: dyvmsapi_20170525_models.RefreshMqttTokenRequest,
    ) -> dyvmsapi_20170525_models.RefreshMqttTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_mqtt_token_with_options_async(request, runtime)

    def send_verification_with_options(
        self,
        request: dyvmsapi_20170525_models.SendVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SendVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Target'] = request.target
        query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SendVerification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SendVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SendVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SendVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Target'] = request.target
        query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SendVerification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SendVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification(
        self,
        request: dyvmsapi_20170525_models.SendVerificationRequest,
    ) -> dyvmsapi_20170525_models.SendVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verification_with_options(request, runtime)

    async def send_verification_async(
        self,
        request: dyvmsapi_20170525_models.SendVerificationRequest,
    ) -> dyvmsapi_20170525_models.SendVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_with_options_async(request, runtime)

    def set_transfer_callee_pool_config_with_options(
        self,
        request: dyvmsapi_20170525_models.SetTransferCalleePoolConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledRouteMode'] = request.called_route_mode
        query['Details'] = request.details
        query['OwnerId'] = request.owner_id
        query['PhoneNumber'] = request.phone_number
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetTransferCalleePoolConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_transfer_callee_pool_config_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SetTransferCalleePoolConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledRouteMode'] = request.called_route_mode
        query['Details'] = request.details
        query['OwnerId'] = request.owner_id
        query['PhoneNumber'] = request.phone_number
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetTransferCalleePoolConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_transfer_callee_pool_config(
        self,
        request: dyvmsapi_20170525_models.SetTransferCalleePoolConfigRequest,
    ) -> dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_transfer_callee_pool_config_with_options(request, runtime)

    async def set_transfer_callee_pool_config_async(
        self,
        request: dyvmsapi_20170525_models.SetTransferCalleePoolConfigRequest,
    ) -> dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_transfer_callee_pool_config_with_options_async(request, runtime)

    def single_call_by_tts_with_options(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PlayTimes'] = request.play_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Speed'] = request.speed
        query['TtsCode'] = request.tts_code
        query['TtsParam'] = request.tts_param
        query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SingleCallByTts',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByTtsResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_call_by_tts_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PlayTimes'] = request.play_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Speed'] = request.speed
        query['TtsCode'] = request.tts_code
        query['TtsParam'] = request.tts_param
        query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SingleCallByTts',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByTtsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_call_by_tts(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_tts_with_options(request, runtime)

    async def single_call_by_tts_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.single_call_by_tts_with_options_async(request, runtime)

    def single_call_by_voice_with_options(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PlayTimes'] = request.play_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Speed'] = request.speed
        query['VoiceCode'] = request.voice_code
        query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SingleCallByVoice',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_call_by_voice_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PlayTimes'] = request.play_times
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Speed'] = request.speed
        query['VoiceCode'] = request.voice_code
        query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SingleCallByVoice',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_call_by_voice(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_voice_with_options(request, runtime)

    async def single_call_by_voice_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.single_call_by_voice_with_options_async(request, runtime)

    def smart_call_with_options(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionCodeBreak'] = request.action_code_break
        query['ActionCodeTimeBreak'] = request.action_code_time_break
        query['AsrBaseId'] = request.asr_base_id
        query['AsrModelId'] = request.asr_model_id
        query['BackgroundFileCode'] = request.background_file_code
        query['BackgroundSpeed'] = request.background_speed
        query['BackgroundVolume'] = request.background_volume
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['DynamicId'] = request.dynamic_id
        query['EarlyMediaAsr'] = request.early_media_asr
        query['EnableITN'] = request.enable_itn
        query['MuteTime'] = request.mute_time
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PauseTime'] = request.pause_time
        query['RecordFlag'] = request.record_flag
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SessionTimeout'] = request.session_timeout
        query['Speed'] = request.speed
        query['StreamAsr'] = request.stream_asr
        query['TtsConf'] = request.tts_conf
        query['TtsSpeed'] = request.tts_speed
        query['TtsStyle'] = request.tts_style
        query['TtsVolume'] = request.tts_volume
        query['VoiceCode'] = request.voice_code
        query['VoiceCodeParam'] = request.voice_code_param
        query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SmartCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def smart_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionCodeBreak'] = request.action_code_break
        query['ActionCodeTimeBreak'] = request.action_code_time_break
        query['AsrBaseId'] = request.asr_base_id
        query['AsrModelId'] = request.asr_model_id
        query['BackgroundFileCode'] = request.background_file_code
        query['BackgroundSpeed'] = request.background_speed
        query['BackgroundVolume'] = request.background_volume
        query['CalledNumber'] = request.called_number
        query['CalledShowNumber'] = request.called_show_number
        query['DynamicId'] = request.dynamic_id
        query['EarlyMediaAsr'] = request.early_media_asr
        query['EnableITN'] = request.enable_itn
        query['MuteTime'] = request.mute_time
        query['OutId'] = request.out_id
        query['OwnerId'] = request.owner_id
        query['PauseTime'] = request.pause_time
        query['RecordFlag'] = request.record_flag
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SessionTimeout'] = request.session_timeout
        query['Speed'] = request.speed
        query['StreamAsr'] = request.stream_asr
        query['TtsConf'] = request.tts_conf
        query['TtsSpeed'] = request.tts_speed
        query['TtsStyle'] = request.tts_style
        query['TtsVolume'] = request.tts_volume
        query['VoiceCode'] = request.voice_code
        query['VoiceCodeParam'] = request.voice_code_param
        query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SmartCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def smart_call(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.smart_call_with_options(request, runtime)

    async def smart_call_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.smart_call_with_options_async(request, runtime)

    def smart_call_operate_with_options(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['Command'] = request.command
        query['OwnerId'] = request.owner_id
        query['Param'] = request.param
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SmartCallOperate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def smart_call_operate_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallId'] = request.call_id
        query['Command'] = request.command
        query['OwnerId'] = request.owner_id
        query['Param'] = request.param
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SmartCallOperate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def smart_call_operate(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        runtime = util_models.RuntimeOptions()
        return self.smart_call_operate_with_options(request, runtime)

    async def smart_call_operate_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.smart_call_operate_with_options_async(request, runtime)

    def start_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ScheduleTime'] = request.schedule_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ScheduleTime'] = request.schedule_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_robot_task(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_robot_task_with_options(request, runtime)

    async def start_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_robot_task_with_options_async(request, runtime)

    def stop_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StopRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StopRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_robot_task(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_robot_task_with_options(request, runtime)

    async def stop_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_robot_task_with_options_async(request, runtime)

    def submit_hotline_transfer_register_with_options(
        self,
        request: dyvmsapi_20170525_models.SubmitHotlineTransferRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Agreement'] = request.agreement
        query['HotlineNumber'] = request.hotline_number
        query['OperatorIdentityCard'] = request.operator_identity_card
        query['OperatorMail'] = request.operator_mail
        query['OperatorMailVerifyCode'] = request.operator_mail_verify_code
        query['OperatorMobile'] = request.operator_mobile
        query['OperatorMobileVerifyCode'] = request.operator_mobile_verify_code
        query['OperatorName'] = request.operator_name
        query['OwnerId'] = request.owner_id
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TransferPhoneNumberInfos'] = request.transfer_phone_number_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitHotlineTransferRegister',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_hotline_transfer_register_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SubmitHotlineTransferRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Agreement'] = request.agreement
        query['HotlineNumber'] = request.hotline_number
        query['OperatorIdentityCard'] = request.operator_identity_card
        query['OperatorMail'] = request.operator_mail
        query['OperatorMailVerifyCode'] = request.operator_mail_verify_code
        query['OperatorMobile'] = request.operator_mobile
        query['OperatorMobileVerifyCode'] = request.operator_mobile_verify_code
        query['OperatorName'] = request.operator_name
        query['OwnerId'] = request.owner_id
        query['QualificationId'] = request.qualification_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TransferPhoneNumberInfos'] = request.transfer_phone_number_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitHotlineTransferRegister',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_hotline_transfer_register(
        self,
        request: dyvmsapi_20170525_models.SubmitHotlineTransferRegisterRequest,
    ) -> dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_hotline_transfer_register_with_options(request, runtime)

    async def submit_hotline_transfer_register_async(
        self,
        request: dyvmsapi_20170525_models.SubmitHotlineTransferRegisterRequest,
    ) -> dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_hotline_transfer_register_with_options_async(request, runtime)

    def upload_robot_task_called_file_with_options(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['Id'] = request.id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TtsParam'] = request.tts_param
        query['TtsParamHead'] = request.tts_param_head
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UploadRobotTaskCalledFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_robot_task_called_file_with_options_async(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CalledNumber'] = request.called_number
        query['Id'] = request.id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TtsParam'] = request.tts_param
        query['TtsParamHead'] = request.tts_param_head
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UploadRobotTaskCalledFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_robot_task_called_file(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_robot_task_called_file_with_options(request, runtime)

    async def upload_robot_task_called_file_async(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_robot_task_called_file_with_options_async(request, runtime)
