# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class Alert(TeaModel):
    def __init__(
        self,
        body: str = None,
        subtitle: str = None,
        title: str = None,
    ):
        self.body = body
        self.subtitle = subtitle
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.subtitle is not None:
            result['subtitle'] = self.subtitle
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('subtitle') is not None:
            self.subtitle = m.get('subtitle')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class Body(TeaModel):
    def __init__(
        self,
        activity: str = None,
        after_open: str = None,
        badge: int = None,
        builder_id: int = None,
        custom: str = None,
        expand_image: str = None,
        icon: str = None,
        img: str = None,
        large_icon: str = None,
        play_lights: bool = None,
        play_sound: bool = None,
        play_vibrate: bool = None,
        sound: str = None,
        text: str = None,
        title: str = None,
        url: str = None,
    ):
        self.activity = activity
        self.after_open = after_open
        self.badge = badge
        self.builder_id = builder_id
        self.custom = custom
        self.expand_image = expand_image
        self.icon = icon
        self.img = img
        self.large_icon = large_icon
        self.play_lights = play_lights
        self.play_sound = play_sound
        self.play_vibrate = play_vibrate
        self.sound = sound
        self.text = text
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity is not None:
            result['activity'] = self.activity
        if self.after_open is not None:
            result['afterOpen'] = self.after_open
        if self.badge is not None:
            result['badge'] = self.badge
        if self.builder_id is not None:
            result['builderId'] = self.builder_id
        if self.custom is not None:
            result['custom'] = self.custom
        if self.expand_image is not None:
            result['expandImage'] = self.expand_image
        if self.icon is not None:
            result['icon'] = self.icon
        if self.img is not None:
            result['img'] = self.img
        if self.large_icon is not None:
            result['largeIcon'] = self.large_icon
        if self.play_lights is not None:
            result['playLights'] = self.play_lights
        if self.play_sound is not None:
            result['playSound'] = self.play_sound
        if self.play_vibrate is not None:
            result['playVibrate'] = self.play_vibrate
        if self.sound is not None:
            result['sound'] = self.sound
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activity') is not None:
            self.activity = m.get('activity')
        if m.get('afterOpen') is not None:
            self.after_open = m.get('afterOpen')
        if m.get('badge') is not None:
            self.badge = m.get('badge')
        if m.get('builderId') is not None:
            self.builder_id = m.get('builderId')
        if m.get('custom') is not None:
            self.custom = m.get('custom')
        if m.get('expandImage') is not None:
            self.expand_image = m.get('expandImage')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('img') is not None:
            self.img = m.get('img')
        if m.get('largeIcon') is not None:
            self.large_icon = m.get('largeIcon')
        if m.get('playLights') is not None:
            self.play_lights = m.get('playLights')
        if m.get('playSound') is not None:
            self.play_sound = m.get('playSound')
        if m.get('playVibrate') is not None:
            self.play_vibrate = m.get('playVibrate')
        if m.get('sound') is not None:
            self.sound = m.get('sound')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class AndroidPayload(TeaModel):
    def __init__(
        self,
        body: Body = None,
        display_type: str = None,
        extra: Dict[str, Any] = None,
    ):
        self.body = body
        self.display_type = display_type
        self.extra = extra

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.display_type is not None:
            result['displayType'] = self.display_type
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Body()
            self.body = temp_model.from_map(m['body'])
        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        return self


class Aps(TeaModel):
    def __init__(
        self,
        alert: Alert = None,
        badge: int = None,
        category: str = None,
        content_available: int = None,
        interruption_level: str = None,
        sound: str = None,
    ):
        self.alert = alert
        self.badge = badge
        self.category = category
        self.content_available = content_available
        self.interruption_level = interruption_level
        self.sound = sound

    def validate(self):
        if self.alert:
            self.alert.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert is not None:
            result['alert'] = self.alert.to_map()
        if self.badge is not None:
            result['badge'] = self.badge
        if self.category is not None:
            result['category'] = self.category
        if self.content_available is not None:
            result['contentAvailable'] = self.content_available
        if self.interruption_level is not None:
            result['interruptionLevel'] = self.interruption_level
        if self.sound is not None:
            result['sound'] = self.sound
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alert') is not None:
            temp_model = Alert()
            self.alert = temp_model.from_map(m['alert'])
        if m.get('badge') is not None:
            self.badge = m.get('badge')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('contentAvailable') is not None:
            self.content_available = m.get('contentAvailable')
        if m.get('interruptionLevel') is not None:
            self.interruption_level = m.get('interruptionLevel')
        if m.get('sound') is not None:
            self.sound = m.get('sound')
        return self


class ChannelProperties(TeaModel):
    def __init__(
        self,
        channel_activity: str = None,
        main_activity: str = None,
        oppo_channel_id: str = None,
        vivo_classification: str = None,
        xiaomi_channel_id: str = None,
    ):
        self.channel_activity = channel_activity
        self.main_activity = main_activity
        self.oppo_channel_id = oppo_channel_id
        self.vivo_classification = vivo_classification
        self.xiaomi_channel_id = xiaomi_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_activity is not None:
            result['channelActivity'] = self.channel_activity
        if self.main_activity is not None:
            result['mainActivity'] = self.main_activity
        if self.oppo_channel_id is not None:
            result['oppoChannelId'] = self.oppo_channel_id
        if self.vivo_classification is not None:
            result['vivoClassification'] = self.vivo_classification
        if self.xiaomi_channel_id is not None:
            result['xiaomiChannelId'] = self.xiaomi_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelActivity') is not None:
            self.channel_activity = m.get('channelActivity')
        if m.get('mainActivity') is not None:
            self.main_activity = m.get('mainActivity')
        if m.get('oppoChannelId') is not None:
            self.oppo_channel_id = m.get('oppoChannelId')
        if m.get('vivoClassification') is not None:
            self.vivo_classification = m.get('vivoClassification')
        if m.get('xiaomiChannelId') is not None:
            self.xiaomi_channel_id = m.get('xiaomiChannelId')
        return self


class IosPayload(TeaModel):
    def __init__(
        self,
        aps: Aps = None,
        extra: Dict[str, Any] = None,
    ):
        self.aps = aps
        self.extra = extra

    def validate(self):
        if self.aps:
            self.aps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aps is not None:
            result['aps'] = self.aps.to_map()
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aps') is not None:
            temp_model = Aps()
            self.aps = temp_model.from_map(m['aps'])
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        return self


class Policy(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        outer_biz_no: str = None,
        speed: int = None,
        start_time: str = None,
    ):
        self.expire_time = expire_time
        self.outer_biz_no = outer_biz_no
        self.speed = speed
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.outer_biz_no is not None:
            result['outerBizNo'] = self.outer_biz_no
        if self.speed is not None:
            result['speed'] = self.speed
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('outerBizNo') is not None:
            self.outer_biz_no = m.get('outerBizNo')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class SendByAppRequest(TeaModel):
    def __init__(
        self,
        android_payload: AndroidPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
    ):
        self.android_payload = android_payload
        self.channel_properties = channel_properties
        self.description = description
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByAppShrinkRequest(TeaModel):
    def __init__(
        self,
        android_payload_shrink: str = None,
        channel_properties_shrink: str = None,
        description: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
    ):
        self.android_payload_shrink = android_payload_shrink
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByAppResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByAppResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByDeviceRequest(TeaModel):
    def __init__(
        self,
        android_payload: AndroidPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        device_tokens: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
    ):
        self.android_payload = android_payload
        self.channel_properties = channel_properties
        self.description = description
        self.device_tokens = device_tokens
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        android_payload_shrink: str = None,
        channel_properties_shrink: str = None,
        description: str = None,
        device_tokens: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
    ):
        self.android_payload_shrink = android_payload_shrink
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        self.device_tokens = device_tokens
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByDeviceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self

