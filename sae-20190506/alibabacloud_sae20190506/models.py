# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AbortAndRollbackChangeOrderRequest(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortAndRollbackChangeOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortAndRollbackChangeOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AbortAndRollbackChangeOrderResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AbortAndRollbackChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class AbortAndRollbackChangeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbortAndRollbackChangeOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AbortAndRollbackChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbortChangeOrderRequest(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortChangeOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortChangeOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AbortChangeOrderResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AbortChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class AbortChangeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbortChangeOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AbortChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_ids: str = None,
        namespace_id: str = None,
    ):
        self.app_ids = app_ids
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class BatchStartApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BatchStartApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchStartApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BatchStartApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BatchStartApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStartApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchStartApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_ids: str = None,
        namespace_id: str = None,
    ):
        self.app_ids = app_ids
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class BatchStopApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BatchStopApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchStopApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BatchStopApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BatchStopApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStopApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchStopApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindSlbRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        internet: str = None,
        internet_slb_id: str = None,
        intranet: str = None,
        intranet_slb_id: str = None,
    ):
        self.app_id = app_id
        self.internet = internet
        self.internet_slb_id = internet_slb_id
        self.intranet = intranet
        self.intranet_slb_id = intranet_slb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.internet is not None:
            result['Internet'] = self.internet
        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id
        if self.intranet is not None:
            result['Intranet'] = self.intranet
        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Internet') is not None:
            self.internet = m.get('Internet')
        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')
        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')
        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')
        return self


class BindSlbResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BindSlbResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BindSlbResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BindSlbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BindSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindSlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmPipelineBatchRequest(TeaModel):
    def __init__(
        self,
        confirm: bool = None,
        pipeline_id: str = None,
    ):
        self.confirm = confirm
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm is not None:
            result['Confirm'] = self.confirm
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confirm') is not None:
            self.confirm = m.get('Confirm')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ConfirmPipelineBatchResponseBodyData(TeaModel):
    def __init__(
        self,
        pipeline_id: str = None,
    ):
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ConfirmPipelineBatchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ConfirmPipelineBatchResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ConfirmPipelineBatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ConfirmPipelineBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmPipelineBatchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfirmPipelineBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        app_description: str = None,
        app_name: str = None,
        associate_eip: bool = None,
        auto_config: bool = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        custom_host_alias: str = None,
        deploy: bool = None,
        edas_container_version: str = None,
        envs: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        liveness: str = None,
        memory: int = None,
        mount_desc: str = None,
        mount_host: str = None,
        namespace_id: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        readiness: str = None,
        replicas: int = None,
        security_group_id: str = None,
        sls_configs: str = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.app_description = app_description
        self.app_name = app_name
        # 是否绑定EIP
        self.associate_eip = associate_eip
        self.auto_config = auto_config
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.cpu = cpu
        self.custom_host_alias = custom_host_alias
        self.deploy = deploy
        self.edas_container_version = edas_container_version
        self.envs = envs
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.liveness = liveness
        self.memory = memory
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.namespace_id = namespace_id
        self.nas_id = nas_id
        # OSS使用的AKID
        self.oss_ak_id = oss_ak_id
        # OSS AKID对应的secret
        self.oss_ak_secret = oss_ak_secret
        # OSS挂载描述信息
        self.oss_mount_descs = oss_mount_descs
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.php_arms_config_location = php_arms_config_location
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.readiness = readiness
        self.replicas = replicas
        self.security_group_id = security_group_id
        self.sls_configs = sls_configs
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.deploy is not None:
            result['Deploy'] = self.deploy
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class CreateApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        change_order_id: str = None,
    ):
        self.app_id = app_id
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_enable: bool = None,
        scaling_rule_name: str = None,
        scaling_rule_timer: str = None,
        scaling_rule_type: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_enable = scaling_rule_enable
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_timer = scaling_rule_timer
        self.scaling_rule_type = scaling_rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_enable is not None:
            result['ScalingRuleEnable'] = self.scaling_rule_enable
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleEnable') is not None:
            self.scaling_rule_enable = m.get('ScalingRuleEnable')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        return self


class CreateApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(
        self,
        at_time: str = None,
        target_replicas: int = None,
    ):
        self.at_time = at_time
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class CreateApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[CreateApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.period = period
        self.schedules = schedules

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = CreateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class CreateApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: CreateApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.scale_rule_enabled = scale_rule_enabled
        self.scale_rule_name = scale_rule_name
        self.scale_rule_type = scale_rule_type
        self.timer = timer
        self.update_time = update_time

    def validate(self):
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateApplicationScalingRuleResponseBodyData = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigMapRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
    ):
        self.data = data
        self.description = description
        self.name = name
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class CreateConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class CreateConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        dubbo_rules: str = None,
        name: str = None,
        sc_rules: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 规则名称
        self.description = description
        # Dubbo规则
        self.dubbo_rules = dubbo_rules
        # 规则名称
        self.name = name
        # SpringCloud规则
        self.sc_rules = sc_rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules
        if self.name is not None:
            result['Name'] = self.name
        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')
        return self


class CreateGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class CreateGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIngressRequest(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        default_rule: str = None,
        description: str = None,
        listener_port: int = None,
        namespace_id: str = None,
        rules: str = None,
        slb_id: str = None,
    ):
        self.cert_id = cert_id
        self.default_rule = default_rule
        self.description = description
        self.listener_port = listener_port
        self.namespace_id = namespace_id
        self.rules = rules
        self.slb_id = slb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        return self


class CreateIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class CreateIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIngressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class CreateNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DeleteApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigMapRequest(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DeleteConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DeleteConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        # 规则ID
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DeleteGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DeleteGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIngressRequest(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DeleteIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DeleteIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIngressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationRequest(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_id: str = None,
        associate_eip: bool = None,
        auto_enable_application_scaling_rule: bool = None,
        batch_wait_time: int = None,
        change_order_desc: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        enable_ahas: str = None,
        enable_grey_tag_route: bool = None,
        envs: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        liveness: str = None,
        min_ready_instances: int = None,
        mount_desc: str = None,
        mount_host: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_url: str = None,
        package_version: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        readiness: str = None,
        sls_configs: str = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        update_strategy: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        # ACR 企业版实例 ID
        self.acr_instance_id = acr_instance_id
        self.app_id = app_id
        # 是否绑定EIP
        self.associate_eip = associate_eip
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        self.batch_wait_time = batch_wait_time
        self.change_order_desc = change_order_desc
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.custom_host_alias = custom_host_alias
        self.edas_container_version = edas_container_version
        self.enable_ahas = enable_ahas
        # 是否开启发布流量灰度规则
        self.enable_grey_tag_route = enable_grey_tag_route
        self.envs = envs
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.liveness = liveness
        self.min_ready_instances = min_ready_instances
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.nas_id = nas_id
        # OSS使用的AKID
        self.oss_ak_id = oss_ak_id
        # OSS AKID对应的secret
        self.oss_ak_secret = oss_ak_secret
        # OSS挂载描述信息
        self.oss_mount_descs = oss_mount_descs
        self.package_url = package_url
        self.package_version = package_version
        self.php_arms_config_location = php_arms_config_location
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.readiness = readiness
        self.sls_configs = sls_configs
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.update_strategy = update_strategy
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.change_order_desc is not None:
            result['ChangeOrderDesc'] = self.change_order_desc
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas
        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('ChangeOrderDesc') is not None:
            self.change_order_desc = m.get('ChangeOrderDesc')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')
        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DeployApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        change_order_id: str = None,
        is_need_approval: bool = None,
    ):
        self.app_id = app_id
        self.change_order_id = change_order_id
        self.is_need_approval = is_need_approval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')
        return self


class DeployApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeployApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeployApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeployApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppServiceDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        service_group: str = None,
        service_name: str = None,
        service_type: str = None,
        service_version: str = None,
    ):
        # mse 的 appId
        self.app_id = app_id
        self.service_group = service_group
        self.service_name = service_name
        self.service_type = service_type
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAppServiceDetailResponseBodyDataMethods(TeaModel):
    def __init__(
        self,
        method_controller: str = None,
        name: str = None,
        name_detail: str = None,
        parameter_definitions: List[DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions] = None,
        parameter_details: List[str] = None,
        parameter_types: List[str] = None,
        paths: List[str] = None,
        request_methods: List[str] = None,
        return_details: str = None,
        return_type: str = None,
    ):
        self.method_controller = method_controller
        self.name = name
        self.name_detail = name_detail
        self.parameter_definitions = parameter_definitions
        self.parameter_details = parameter_details
        self.parameter_types = parameter_types
        self.paths = paths
        self.request_methods = request_methods
        self.return_details = return_details
        self.return_type = return_type

    def validate(self):
        if self.parameter_definitions:
            for k in self.parameter_definitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_controller is not None:
            result['MethodController'] = self.method_controller
        if self.name is not None:
            result['Name'] = self.name
        if self.name_detail is not None:
            result['NameDetail'] = self.name_detail
        result['ParameterDefinitions'] = []
        if self.parameter_definitions is not None:
            for k in self.parameter_definitions:
                result['ParameterDefinitions'].append(k.to_map() if k else None)
        if self.parameter_details is not None:
            result['ParameterDetails'] = self.parameter_details
        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods
        if self.return_details is not None:
            result['ReturnDetails'] = self.return_details
        if self.return_type is not None:
            result['ReturnType'] = self.return_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MethodController') is not None:
            self.method_controller = m.get('MethodController')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameDetail') is not None:
            self.name_detail = m.get('NameDetail')
        self.parameter_definitions = []
        if m.get('ParameterDefinitions') is not None:
            for k in m.get('ParameterDefinitions'):
                temp_model = DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions()
                self.parameter_definitions.append(temp_model.from_map(k))
        if m.get('ParameterDetails') is not None:
            self.parameter_details = m.get('ParameterDetails')
        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')
        if m.get('ReturnDetails') is not None:
            self.return_details = m.get('ReturnDetails')
        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')
        return self


class DescribeAppServiceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        dubbo_application_name: str = None,
        edas_app_name: str = None,
        group: str = None,
        metadata: Dict[str, Any] = None,
        methods: List[DescribeAppServiceDetailResponseBodyDataMethods] = None,
        service_name: str = None,
        service_type: str = None,
        spring_application_name: str = None,
        version: str = None,
    ):
        self.dubbo_application_name = dubbo_application_name
        self.edas_app_name = edas_app_name
        self.group = group
        self.metadata = metadata
        self.methods = methods
        self.service_name = service_name
        self.service_type = service_type
        self.spring_application_name = spring_application_name
        self.version = version

    def validate(self):
        if self.methods:
            for k in self.methods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_application_name is not None:
            result['DubboApplicationName'] = self.dubbo_application_name
        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name
        if self.group is not None:
            result['Group'] = self.group
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        result['Methods'] = []
        if self.methods is not None:
            for k in self.methods:
                result['Methods'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.spring_application_name is not None:
            result['SpringApplicationName'] = self.spring_application_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DubboApplicationName') is not None:
            self.dubbo_application_name = m.get('DubboApplicationName')
        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        self.methods = []
        if m.get('Methods') is not None:
            for k in m.get('Methods'):
                temp_model = DescribeAppServiceDetailResponseBodyDataMethods()
                self.methods.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SpringApplicationName') is not None:
            self.spring_application_name = m.get('SpringApplicationName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppServiceDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAppServiceDetailResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAppServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeAppServiceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppServiceDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        version_id: str = None,
    ):
        self.app_id = app_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeApplicationConfigResponseBodyDataConfigMapMountDesc(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        config_map_name: str = None,
        key: str = None,
        mount_path: str = None,
    ):
        self.config_map_id = config_map_id
        self.config_map_name = config_map_name
        self.key = key
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name
        if self.key is not None:
            result['Key'] = self.key
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class DescribeApplicationConfigResponseBodyDataMountDesc(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        nas_path: str = None,
    ):
        self.mount_path = mount_path
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.nas_path is not None:
            result['NasPath'] = self.nas_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')
        return self


class DescribeApplicationConfigResponseBodyDataOssMountDescs(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        # Bucket名称
        self.bucket_name = bucket_name
        # Bucket中Oss Key名称
        self.bucket_path = bucket_path
        # 挂载到容器的路径
        self.mount_path = mount_path
        # 是否只读
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class DescribeApplicationConfigResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApplicationConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        associate_eip: bool = None,
        batch_wait_time: int = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: List[DescribeApplicationConfigResponseBodyDataConfigMapMountDesc] = None,
        cpu: int = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        enable_ahas: str = None,
        enable_grey_tag_route: bool = None,
        envs: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        liveness: str = None,
        memory: int = None,
        min_ready_instances: int = None,
        mount_desc: List[DescribeApplicationConfigResponseBodyDataMountDesc] = None,
        mount_host: str = None,
        mse_application_id: str = None,
        namespace_id: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: List[DescribeApplicationConfigResponseBodyDataOssMountDescs] = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        readiness: str = None,
        region_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        sls_configs: str = None,
        tags: List[DescribeApplicationConfigResponseBodyDataTags] = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        update_strategy: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.app_description = app_description
        self.app_id = app_id
        self.app_name = app_name
        # 是否绑定EIP
        self.associate_eip = associate_eip
        self.batch_wait_time = batch_wait_time
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.cpu = cpu
        self.custom_host_alias = custom_host_alias
        self.edas_container_version = edas_container_version
        self.enable_ahas = enable_ahas
        # 开启流量灰度
        self.enable_grey_tag_route = enable_grey_tag_route
        self.envs = envs
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.liveness = liveness
        self.memory = memory
        self.min_ready_instances = min_ready_instances
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        # 对应MSE产品侧应用ID
        self.mse_application_id = mse_application_id
        self.namespace_id = namespace_id
        self.nas_id = nas_id
        # OSS读写的AK
        self.oss_ak_id = oss_ak_id
        # OSS读写的secret
        self.oss_ak_secret = oss_ak_secret
        # OSS挂载描述信息
        self.oss_mount_descs = oss_mount_descs
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.php_arms_config_location = php_arms_config_location
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.readiness = readiness
        self.region_id = region_id
        self.replicas = replicas
        self.security_group_id = security_group_id
        self.sls_configs = sls_configs
        self.tags = tags
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.update_strategy = update_strategy
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        if self.config_map_mount_desc:
            for k in self.config_map_mount_desc:
                if k:
                    k.validate()
        if self.mount_desc:
            for k in self.mount_desc:
                if k:
                    k.validate()
        if self.oss_mount_descs:
            for k in self.oss_mount_descs:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas
        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        result['MountDesc'] = []
        if self.mount_desc is not None:
            for k in self.mount_desc:
                result['MountDesc'].append(k.to_map() if k else None)
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.mse_application_id is not None:
            result['MseApplicationId'] = self.mse_application_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        result['OssMountDescs'] = []
        if self.oss_mount_descs is not None:
            for k in self.oss_mount_descs:
                result['OssMountDescs'].append(k.to_map() if k else None)
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k in m.get('ConfigMapMountDesc'):
                temp_model = DescribeApplicationConfigResponseBodyDataConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')
        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        self.mount_desc = []
        if m.get('MountDesc') is not None:
            for k in m.get('MountDesc'):
                temp_model = DescribeApplicationConfigResponseBodyDataMountDesc()
                self.mount_desc.append(temp_model.from_map(k))
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('MseApplicationId') is not None:
            self.mse_application_id = m.get('MseApplicationId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        self.oss_mount_descs = []
        if m.get('OssMountDescs') is not None:
            for k in m.get('OssMountDescs'):
                temp_model = DescribeApplicationConfigResponseBodyDataOssMountDescs()
                self.oss_mount_descs.append(temp_model.from_map(k))
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeApplicationConfigResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DescribeApplicationConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationConfigResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationGroupsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeApplicationGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        edas_container_version: str = None,
        group_id: str = None,
        group_name: str = None,
        group_type: int = None,
        image_url: str = None,
        jdk: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        replicas: int = None,
        running_instances: int = None,
        web_container: str = None,
    ):
        self.edas_container_version = edas_container_version
        self.group_id = group_id
        self.group_name = group_name
        self.group_type = group_type
        self.image_url = image_url
        self.jdk = jdk
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.replicas = replicas
        self.running_instances = running_instances
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DescribeApplicationGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeApplicationGroupsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeApplicationGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationImageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image_url: str = None,
    ):
        self.app_id = app_id
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class DescribeApplicationImageResponseBodyData(TeaModel):
    def __init__(
        self,
        cr_url: str = None,
        logo: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_origin_type: str = None,
        repo_tag: str = None,
        repo_type: str = None,
    ):
        self.cr_url = cr_url
        self.logo = logo
        self.region_id = region_id
        self.repo_name = repo_name
        self.repo_namespace = repo_namespace
        self.repo_origin_type = repo_origin_type
        self.repo_tag = repo_tag
        self.repo_type = repo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cr_url is not None:
            result['CrUrl'] = self.cr_url
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.repo_origin_type is not None:
            result['RepoOriginType'] = self.repo_origin_type
        if self.repo_tag is not None:
            result['RepoTag'] = self.repo_tag
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrUrl') is not None:
            self.cr_url = m.get('CrUrl')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('RepoOriginType') is not None:
            self.repo_origin_type = m.get('RepoOriginType')
        if m.get('RepoTag') is not None:
            self.repo_tag = m.get('RepoTag')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        return self


class DescribeApplicationImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationImageResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationInstancesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        group_id: str = None,
        page_size: int = None,
        reverse: bool = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.group_id = group_id
        self.page_size = page_size
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class DescribeApplicationInstancesResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        create_time_stamp: int = None,
        eip: str = None,
        group_id: str = None,
        image_url: str = None,
        instance_container_ip: str = None,
        instance_container_restarts: int = None,
        instance_container_status: str = None,
        instance_health_status: str = None,
        instance_id: str = None,
        package_version: str = None,
        v_switch_id: str = None,
    ):
        self.create_time_stamp = create_time_stamp
        self.eip = eip
        self.group_id = group_id
        self.image_url = image_url
        self.instance_container_ip = instance_container_ip
        self.instance_container_restarts = instance_container_restarts
        self.instance_container_status = instance_container_status
        self.instance_health_status = instance_health_status
        self.instance_id = instance_id
        self.package_version = package_version
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_container_ip is not None:
            result['InstanceContainerIp'] = self.instance_container_ip
        if self.instance_container_restarts is not None:
            result['InstanceContainerRestarts'] = self.instance_container_restarts
        if self.instance_container_status is not None:
            result['InstanceContainerStatus'] = self.instance_container_status
        if self.instance_health_status is not None:
            result['InstanceHealthStatus'] = self.instance_health_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceContainerIp') is not None:
            self.instance_container_ip = m.get('InstanceContainerIp')
        if m.get('InstanceContainerRestarts') is not None:
            self.instance_container_restarts = m.get('InstanceContainerRestarts')
        if m.get('InstanceContainerStatus') is not None:
            self.instance_container_status = m.get('InstanceContainerStatus')
        if m.get('InstanceHealthStatus') is not None:
            self.instance_health_status = m.get('InstanceHealthStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeApplicationInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instances: List[DescribeApplicationInstancesResponseBodyDataInstances] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.instances = instances
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeApplicationInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeApplicationInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationInstancesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationScalingRulesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules(TeaModel):
    def __init__(
        self,
        at_time: str = None,
        max_replicas: int = None,
        min_replicas: int = None,
        target_replicas: int = None,
    ):
        self.at_time = at_time
        self.max_replicas = max_replicas
        self.min_replicas = min_replicas
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.period = period
        self.schedules = schedules

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.scale_rule_enabled = scale_rule_enabled
        self.scale_rule_name = scale_rule_name
        self.scale_rule_type = scale_rule_type
        self.timer = timer
        self.update_time = update_time

    def validate(self):
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeApplicationScalingRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        application_scaling_rules: List[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.application_scaling_rules = application_scaling_rules
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.application_scaling_rules:
            for k in self.application_scaling_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationScalingRules'] = []
        if self.application_scaling_rules is not None:
            for k in self.application_scaling_rules:
                result['ApplicationScalingRules'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_scaling_rules = []
        if m.get('ApplicationScalingRules') is not None:
            for k in m.get('ApplicationScalingRules'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules()
                self.application_scaling_rules.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeApplicationScalingRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeApplicationScalingRulesResponseBodyData = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationScalingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationScalingRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationSlbsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationSlbsResponseBodyDataInternet(TeaModel):
    def __init__(
        self,
        https_cert_id: str = None,
        port: int = None,
        protocol: str = None,
        target_port: int = None,
    ):
        self.https_cert_id = https_cert_id
        self.port = port
        self.protocol = protocol
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeApplicationSlbsResponseBodyDataIntranet(TeaModel):
    def __init__(
        self,
        https_cert_id: str = None,
        port: int = None,
        protocol: str = None,
        target_port: int = None,
    ):
        self.https_cert_id = https_cert_id
        self.port = port
        self.protocol = protocol
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeApplicationSlbsResponseBodyData(TeaModel):
    def __init__(
        self,
        internet: List[DescribeApplicationSlbsResponseBodyDataInternet] = None,
        internet_ip: str = None,
        internet_slb_id: str = None,
        intranet: List[DescribeApplicationSlbsResponseBodyDataIntranet] = None,
        intranet_ip: str = None,
        intranet_slb_id: str = None,
    ):
        self.internet = internet
        self.internet_ip = internet_ip
        self.internet_slb_id = internet_slb_id
        self.intranet = intranet
        self.intranet_ip = intranet_ip
        self.intranet_slb_id = intranet_slb_id

    def validate(self):
        if self.internet:
            for k in self.internet:
                if k:
                    k.validate()
        if self.intranet:
            for k in self.intranet:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Internet'] = []
        if self.internet is not None:
            for k in self.internet:
                result['Internet'].append(k.to_map() if k else None)
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id
        result['Intranet'] = []
        if self.intranet is not None:
            for k in self.intranet:
                result['Intranet'].append(k.to_map() if k else None)
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.internet = []
        if m.get('Internet') is not None:
            for k in m.get('Internet'):
                temp_model = DescribeApplicationSlbsResponseBodyDataInternet()
                self.internet.append(temp_model.from_map(k))
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')
        self.intranet = []
        if m.get('Intranet') is not None:
            for k in m.get('Intranet'):
                temp_model = DescribeApplicationSlbsResponseBodyDataIntranet()
                self.intranet.append(temp_model.from_map(k))
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')
        return self


class DescribeApplicationSlbsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationSlbsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationSlbsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationSlbsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationSlbsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationSlbsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        arms_advanced_enabled: str = None,
        arms_apm_info: str = None,
        create_time: str = None,
        current_status: str = None,
        enable_agent: bool = None,
        last_change_order_id: str = None,
        last_change_order_running: bool = None,
        last_change_order_status: str = None,
        running_instances: int = None,
        sub_status: str = None,
    ):
        self.app_id = app_id
        self.arms_advanced_enabled = arms_advanced_enabled
        self.arms_apm_info = arms_apm_info
        self.create_time = create_time
        self.current_status = current_status
        self.enable_agent = enable_agent
        self.last_change_order_id = last_change_order_id
        self.last_change_order_running = last_change_order_running
        self.last_change_order_status = last_change_order_status
        self.running_instances = running_instances
        self.sub_status = sub_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.arms_advanced_enabled is not None:
            result['ArmsAdvancedEnabled'] = self.arms_advanced_enabled
        if self.arms_apm_info is not None:
            result['ArmsApmInfo'] = self.arms_apm_info
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.enable_agent is not None:
            result['EnableAgent'] = self.enable_agent
        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id
        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running
        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArmsAdvancedEnabled') is not None:
            self.arms_advanced_enabled = m.get('ArmsAdvancedEnabled')
        if m.get('ArmsApmInfo') is not None:
            self.arms_apm_info = m.get('ArmsApmInfo')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('EnableAgent') is not None:
            self.enable_agent = m.get('EnableAgent')
        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')
        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')
        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        return self


class DescribeApplicationStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationStatusResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChangeOrderRequest(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class DescribeChangeOrderResponseBodyDataPipelines(TeaModel):
    def __init__(
        self,
        batch_type: int = None,
        parallel_count: int = None,
        pipeline_id: str = None,
        pipeline_name: str = None,
        start_time: int = None,
        status: int = None,
        update_time: int = None,
    ):
        self.batch_type = batch_type
        self.parallel_count = parallel_count
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.start_time = start_time
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.parallel_count is not None:
            result['ParallelCount'] = self.parallel_count
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ParallelCount') is not None:
            self.parallel_count = m.get('ParallelCount')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeChangeOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        approval_id: str = None,
        auto: bool = None,
        batch_count: int = None,
        batch_type: str = None,
        batch_wait_time: int = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        current_pipeline_id: str = None,
        description: str = None,
        error_message: str = None,
        pipelines: List[DescribeChangeOrderResponseBodyDataPipelines] = None,
        status: int = None,
        sub_status: int = None,
        support_rollback: bool = None,
    ):
        self.app_name = app_name
        self.approval_id = approval_id
        self.auto = auto
        self.batch_count = batch_count
        self.batch_type = batch_type
        self.batch_wait_time = batch_wait_time
        self.change_order_id = change_order_id
        self.co_type = co_type
        self.co_type_code = co_type_code
        self.create_time = create_time
        self.current_pipeline_id = current_pipeline_id
        self.description = description
        self.error_message = error_message
        self.pipelines = pipelines
        self.status = status
        self.sub_status = sub_status
        self.support_rollback = support_rollback

    def validate(self):
        if self.pipelines:
            for k in self.pipelines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_pipeline_id is not None:
            result['CurrentPipelineId'] = self.current_pipeline_id
        if self.description is not None:
            result['Description'] = self.description
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Pipelines'] = []
        if self.pipelines is not None:
            for k in self.pipelines:
                result['Pipelines'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.support_rollback is not None:
            result['SupportRollback'] = self.support_rollback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPipelineId') is not None:
            self.current_pipeline_id = m.get('CurrentPipelineId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.pipelines = []
        if m.get('Pipelines') is not None:
            for k in m.get('Pipelines'):
                temp_model = DescribeChangeOrderResponseBodyDataPipelines()
                self.pipelines.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('SupportRollback') is not None:
            self.support_rollback = m.get('SupportRollback')
        return self


class DescribeChangeOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeChangeOrderResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeChangeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChangeOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeComponentsResponseBodyData(TeaModel):
    def __init__(
        self,
        component_description: str = None,
        component_key: str = None,
        expired: bool = None,
        type: str = None,
    ):
        self.component_description = component_description
        self.component_key = component_key
        self.expired = expired
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_description is not None:
            result['ComponentDescription'] = self.component_description
        if self.component_key is not None:
            result['ComponentKey'] = self.component_key
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentDescription') is not None:
            self.component_description = m.get('ComponentDescription')
        if m.get('ComponentKey') is not None:
            self.component_key = m.get('ComponentKey')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeComponentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeComponentsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeComponentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeComponentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigMapRequest(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DescribeConfigMapResponseBodyDataRelateApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class DescribeConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        create_time: int = None,
        data: Dict[str, Any] = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        relate_apps: List[DescribeConfigMapResponseBodyDataRelateApps] = None,
        update_time: int = None,
    ):
        self.config_map_id = config_map_id
        self.create_time = create_time
        self.data = data
        self.description = description
        self.name = name
        self.namespace_id = namespace_id
        self.relate_apps = relate_apps
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = DescribeConfigMapResponseBodyDataRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdasContainersResponseBodyData(TeaModel):
    def __init__(
        self,
        disabled: bool = None,
        edas_container_version: str = None,
    ):
        self.disabled = disabled
        self.edas_container_version = edas_container_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        return self


class DescribeEdasContainersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeEdasContainersResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeEdasContainersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeEdasContainersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEdasContainersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEdasContainersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        # 规则ID
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DescribeGreyTagRouteResponseBodyDataDubboRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        # abandon
        self.name = name
        self.operator = operator
        # abandon
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeGreyTagRouteResponseBodyDataDubboRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        group: str = None,
        items: List[DescribeGreyTagRouteResponseBodyDataDubboRulesItems] = None,
        method_name: str = None,
        service_name: str = None,
        version: str = None,
    ):
        self.condition = condition
        self.group = group
        self.items = items
        self.method_name = method_name
        self.service_name = service_name
        self.version = version

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.group is not None:
            result['group'] = self.group
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('group') is not None:
            self.group = m.get('group')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeGreyTagRouteResponseBodyDataDubboRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeGreyTagRouteResponseBodyDataScRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        # abandon
        self.expr = expr
        # abandon
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeGreyTagRouteResponseBodyDataScRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        items: List[DescribeGreyTagRouteResponseBodyDataScRulesItems] = None,
        path: str = None,
    ):
        self.condition = condition
        self.items = items
        self.path = path

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeGreyTagRouteResponseBodyDataScRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class DescribeGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        dubbo_rules: List[DescribeGreyTagRouteResponseBodyDataDubboRules] = None,
        grey_tag_route_id: int = None,
        name: str = None,
        sc_rules: List[DescribeGreyTagRouteResponseBodyDataScRules] = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.dubbo_rules = dubbo_rules
        self.grey_tag_route_id = grey_tag_route_id
        self.name = name
        self.sc_rules = sc_rules
        self.update_time = update_time

    def validate(self):
        if self.dubbo_rules:
            for k in self.dubbo_rules:
                if k:
                    k.validate()
        if self.sc_rules:
            for k in self.sc_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['DubboRules'] = []
        if self.dubbo_rules is not None:
            for k in self.dubbo_rules:
                result['DubboRules'].append(k.to_map() if k else None)
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.name is not None:
            result['Name'] = self.name
        result['ScRules'] = []
        if self.sc_rules is not None:
            for k in self.sc_rules:
                result['ScRules'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k in m.get('DubboRules'):
                temp_model = DescribeGreyTagRouteResponseBodyDataDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k))
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k in m.get('ScRules'):
                temp_model = DescribeGreyTagRouteResponseBodyDataScRules()
                self.sc_rules.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIngressRequest(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DescribeIngressResponseBodyDataDefaultRule(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        container_port: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.container_port = container_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.container_port is not None:
            result['ContainerPort'] = self.container_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')
        return self


class DescribeIngressResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        container_port: int = None,
        domain: str = None,
        path: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.container_port = container_port
        self.domain = domain
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.container_port is not None:
            result['ContainerPort'] = self.container_port
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        default_rule: DescribeIngressResponseBodyDataDefaultRule = None,
        description: str = None,
        id: int = None,
        listener_port: int = None,
        name: str = None,
        namespace_id: str = None,
        rules: List[DescribeIngressResponseBodyDataRules] = None,
        slb_id: str = None,
        slb_type: str = None,
    ):
        self.cert_id = cert_id
        self.default_rule = default_rule
        self.description = description
        self.id = id
        self.listener_port = listener_port
        self.name = name
        self.namespace_id = namespace_id
        self.rules = rules
        self.slb_id = slb_id
        self.slb_type = slb_type

    def validate(self):
        if self.default_rule:
            self.default_rule.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('DefaultRule') is not None:
            temp_model = DescribeIngressResponseBodyDataDefaultRule()
            self.default_rule = temp_model.from_map(m['DefaultRule'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeIngressResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class DescribeIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIngressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceLogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeInstanceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecificationsResponseBodyData(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        enable: bool = None,
        id: int = None,
        memory: int = None,
        spec_info: str = None,
        version: int = None,
    ):
        self.cpu = cpu
        self.enable = enable
        self.id = id
        self.memory = memory
        self.spec_info = spec_info
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.spec_info is not None:
            result['SpecInfo'] = self.spec_info
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SpecInfo') is not None:
            self.spec_info = m.get('SpecInfo')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceSpecificationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeInstanceSpecificationsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeInstanceSpecificationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeInstanceSpecificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceSpecificationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSpecificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceListRequest(TeaModel):
    def __init__(
        self,
        contain_custom: bool = None,
        hybrid_cloud_exclude: bool = None,
    ):
        self.contain_custom = contain_custom
        self.hybrid_cloud_exclude = hybrid_cloud_exclude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_custom is not None:
            result['ContainCustom'] = self.contain_custom
        if self.hybrid_cloud_exclude is not None:
            result['HybridCloudExclude'] = self.hybrid_cloud_exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainCustom') is not None:
            self.contain_custom = m.get('ContainCustom')
        if m.get('HybridCloudExclude') is not None:
            self.hybrid_cloud_exclude = m.get('HybridCloudExclude')
        return self


class DescribeNamespaceListResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_install: str = None,
        current: bool = None,
        custom: bool = None,
        hybrid_cloud_enable: bool = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.agent_install = agent_install
        self.current = current
        self.custom = custom
        self.hybrid_cloud_enable = hybrid_cloud_enable
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_install is not None:
            result['AgentInstall'] = self.agent_install
        if self.current is not None:
            result['Current'] = self.current
        if self.custom is not None:
            result['Custom'] = self.custom
        if self.hybrid_cloud_enable is not None:
            result['HybridCloudEnable'] = self.hybrid_cloud_enable
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstall') is not None:
            self.agent_install = m.get('AgentInstall')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Custom') is not None:
            self.custom = m.get('Custom')
        if m.get('HybridCloudEnable') is not None:
            self.hybrid_cloud_enable = m.get('HybridCloudEnable')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeNamespaceListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeNamespaceListResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeNamespaceListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespaceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespaceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceResourcesRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeNamespaceResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_count: int = None,
        belong_region: str = None,
        description: str = None,
        last_change_order_id: str = None,
        last_change_order_running: bool = None,
        last_change_order_status: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        notification_expired: bool = None,
        security_group_id: str = None,
        tenant_id: str = None,
        user_id: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.app_count = app_count
        self.belong_region = belong_region
        self.description = description
        self.last_change_order_id = last_change_order_id
        self.last_change_order_running = last_change_order_running
        self.last_change_order_status = last_change_order_status
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.notification_expired = notification_expired
        self.security_group_id = security_group_id
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_count is not None:
            result['AppCount'] = self.app_count
        if self.belong_region is not None:
            result['BelongRegion'] = self.belong_region
        if self.description is not None:
            result['Description'] = self.description
        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id
        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running
        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.notification_expired is not None:
            result['NotificationExpired'] = self.notification_expired
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')
        if m.get('BelongRegion') is not None:
            self.belong_region = m.get('BelongRegion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')
        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')
        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NotificationExpired') is not None:
            self.notification_expired = m.get('NotificationExpired')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeNamespaceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeNamespaceResourcesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespaceResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespaceResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespaceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespacesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeNamespacesResponseBodyDataNamespaces(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
        secret_key: str = None,
        tenant_id: str = None,
    ):
        self.access_key = access_key
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id
        self.secret_key = secret_key
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeNamespacesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        namespaces: List[DescribeNamespacesResponseBodyDataNamespaces] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.namespaces = namespaces
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = DescribeNamespacesResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeNamespacesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePipelineRequest(TeaModel):
    def __init__(
        self,
        pipeline_id: str = None,
    ):
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class DescribePipelineResponseBodyDataStageListTaskList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_ignore: int = None,
        error_message: str = None,
        message: str = None,
        show_manual_ignore: bool = None,
        stage_id: str = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.error_code = error_code
        self.error_ignore = error_ignore
        self.error_message = error_message
        self.message = message
        self.show_manual_ignore = show_manual_ignore
        self.stage_id = stage_id
        self.status = status
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_ignore is not None:
            result['ErrorIgnore'] = self.error_ignore
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.show_manual_ignore is not None:
            result['ShowManualIgnore'] = self.show_manual_ignore
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorIgnore') is not None:
            self.error_ignore = m.get('ErrorIgnore')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ShowManualIgnore') is not None:
            self.show_manual_ignore = m.get('ShowManualIgnore')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribePipelineResponseBodyDataStageList(TeaModel):
    def __init__(
        self,
        executor_type: int = None,
        stage_id: str = None,
        stage_name: str = None,
        status: int = None,
        task_list: List[DescribePipelineResponseBodyDataStageListTaskList] = None,
    ):
        self.executor_type = executor_type
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.status = status
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_type is not None:
            result['ExecutorType'] = self.executor_type
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.status is not None:
            result['Status'] = self.status
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorType') is not None:
            self.executor_type = m.get('ExecutorType')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = DescribePipelineResponseBodyDataStageListTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class DescribePipelineResponseBodyData(TeaModel):
    def __init__(
        self,
        co_status: str = None,
        current_stage_id: str = None,
        next_pipeline_id: str = None,
        pipeline_id: str = None,
        pipeline_name: str = None,
        pipeline_status: int = None,
        show_batch: bool = None,
        stage_list: List[DescribePipelineResponseBodyDataStageList] = None,
    ):
        self.co_status = co_status
        self.current_stage_id = current_stage_id
        self.next_pipeline_id = next_pipeline_id
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.pipeline_status = pipeline_status
        self.show_batch = show_batch
        self.stage_list = stage_list

    def validate(self):
        if self.stage_list:
            for k in self.stage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.current_stage_id is not None:
            result['CurrentStageId'] = self.current_stage_id
        if self.next_pipeline_id is not None:
            result['NextPipelineId'] = self.next_pipeline_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.pipeline_status is not None:
            result['PipelineStatus'] = self.pipeline_status
        if self.show_batch is not None:
            result['ShowBatch'] = self.show_batch
        result['StageList'] = []
        if self.stage_list is not None:
            for k in self.stage_list:
                result['StageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CurrentStageId') is not None:
            self.current_stage_id = m.get('CurrentStageId')
        if m.get('NextPipelineId') is not None:
            self.next_pipeline_id = m.get('NextPipelineId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('PipelineStatus') is not None:
            self.pipeline_status = m.get('PipelineStatus')
        if m.get('ShowBatch') is not None:
            self.show_batch = m.get('ShowBatch')
        self.stage_list = []
        if m.get('StageList') is not None:
            for k in m.get('StageList'):
                temp_model = DescribePipelineResponseBodyDataStageList()
                self.stage_list.append(temp_model.from_map(k))
        return self


class DescribePipelineResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePipelineResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribePipelineResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePipelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegionRecommendZones(TeaModel):
    def __init__(
        self,
        recommend_zone: List[str] = None,
    ):
        self.recommend_zone = recommend_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_zone is not None:
            result['RecommendZone'] = self.recommend_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendZone') is not None:
            self.recommend_zone = m.get('RecommendZone')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        recommend_zones: DescribeRegionsResponseBodyRegionsRegionRecommendZones = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.recommend_zones = recommend_zones
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        if self.recommend_zones:
            self.recommend_zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.recommend_zones is not None:
            result['RecommendZones'] = self.recommend_zones.to_map()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RecommendZones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionRecommendZones()
            self.recommend_zones = temp_model.from_map(m['RecommendZones'])
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DisableApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DisableApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadFilesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        instance_id: str = None,
        localpath: str = None,
    ):
        self.app_id = app_id
        self.instance_id = instance_id
        self.localpath = localpath

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.localpath is not None:
            result['Localpath'] = self.localpath
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Localpath') is not None:
            self.localpath = m.get('Localpath')
        return self


class DownloadFilesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DownloadFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DownloadFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class EnableApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class EnableApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppEventsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        event_type: str = None,
        namespace: str = None,
        object_kind: str = None,
        object_name: str = None,
        page_size: int = None,
        reason: str = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.event_type = event_type
        self.namespace = namespace
        self.object_kind = object_kind
        self.object_name = object_name
        self.page_size = page_size
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListAppEventsResponseBodyDataAppEventEntity(TeaModel):
    def __init__(
        self,
        event_type: str = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        object_kind: str = None,
        object_name: str = None,
        reason: str = None,
    ):
        self.event_type = event_type
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp
        self.message = message
        self.object_kind = object_kind
        self.object_name = object_name
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListAppEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_event_entity: List[ListAppEventsResponseBodyDataAppEventEntity] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.app_event_entity = app_event_entity
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.app_event_entity:
            for k in self.app_event_entity:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppEventEntity'] = []
        if self.app_event_entity is not None:
            for k in self.app_event_entity:
                result['AppEventEntity'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_event_entity = []
        if m.get('AppEventEntity') is not None:
            for k in m.get('AppEventEntity'):
                temp_model = ListAppEventsResponseBodyDataAppEventEntity()
                self.app_event_entity.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAppEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAppEventsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = ListAppEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppServicesPageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        service_type: str = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListAppServicesPageResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        edas_app_id: str = None,
        edas_app_name: str = None,
        gmt_modify_time: str = None,
        group: str = None,
        instance_num: int = None,
        service_name: str = None,
        version: str = None,
    ):
        self.cluster_name = cluster_name
        self.edas_app_id = edas_app_id
        self.edas_app_name = edas_app_name
        self.gmt_modify_time = gmt_modify_time
        self.group = group
        self.instance_num = instance_num
        self.service_name = service_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.edas_app_id is not None:
            result['EdasAppId'] = self.edas_app_id
        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('EdasAppId') is not None:
            self.edas_app_id = m.get('EdasAppId')
        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAppServicesPageResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        page_number: str = None,
        page_size: str = None,
        result: List[ListAppServicesPageResponseBodyDataResult] = None,
        total_size: str = None,
    ):
        self.current_page = current_page
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAppServicesPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAppServicesPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAppServicesPageResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppServicesPageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListAppServicesPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppServicesPageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppServicesPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppVersionsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListAppVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        build_package_url: str = None,
        create_time: str = None,
        id: str = None,
        type: str = None,
        war_url: str = None,
    ):
        self.build_package_url = build_package_url
        self.create_time = create_time
        self.id = id
        self.type = type
        self.war_url = war_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_package_url is not None:
            result['BuildPackageUrl'] = self.build_package_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        if self.war_url is not None:
            result['WarUrl'] = self.war_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildPackageUrl') is not None:
            self.build_package_url = m.get('BuildPackageUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WarUrl') is not None:
            self.war_url = m.get('WarUrl')
        return self


class ListAppVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAppVersionsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        current_page: int = None,
        field_type: str = None,
        field_value: str = None,
        namespace_id: str = None,
        order_by: str = None,
        page_size: int = None,
        reverse: bool = None,
        tags: str = None,
    ):
        self.app_name = app_name
        self.current_page = current_page
        self.field_type = field_type
        self.field_value = field_value
        self.namespace_id = namespace_id
        self.order_by = order_by
        self.page_size = page_size
        self.reverse = reverse
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListApplicationsResponseBodyDataApplicationsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListApplicationsResponseBodyDataApplications(TeaModel):
    def __init__(
        self,
        app_deleting_status: bool = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        instances: int = None,
        namespace_id: str = None,
        region_id: str = None,
        running_instances: int = None,
        tags: List[ListApplicationsResponseBodyDataApplicationsTags] = None,
    ):
        self.app_deleting_status = app_deleting_status
        self.app_description = app_description
        self.app_id = app_id
        self.app_name = app_name
        self.instances = instances
        self.namespace_id = namespace_id
        self.region_id = region_id
        self.running_instances = running_instances
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_deleting_status is not None:
            result['AppDeletingStatus'] = self.app_deleting_status
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDeletingStatus') is not None:
            self.app_deleting_status = m.get('AppDeletingStatus')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListApplicationsResponseBodyDataApplicationsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        applications: List[ListApplicationsResponseBodyDataApplications] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.applications = applications
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsResponseBodyDataApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: ListApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.data = data
        self.error_code = error_code
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = ListApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChangeOrdersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        co_status: str = None,
        co_type: str = None,
        current_page: int = None,
        key: str = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.co_status = co_status
        self.co_type = co_type
        self.current_page = current_page
        self.key = key
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key is not None:
            result['Key'] = self.key
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChangeOrdersResponseBodyDataChangeOrderList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        batch_count: int = None,
        batch_type: str = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        create_user_id: str = None,
        description: str = None,
        finish_time: str = None,
        group_id: str = None,
        source: str = None,
        status: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.batch_count = batch_count
        self.batch_type = batch_type
        self.change_order_id = change_order_id
        self.co_type = co_type
        self.co_type_code = co_type_code
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.description = description
        self.finish_time = finish_time
        self.group_id = group_id
        self.source = source
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.description is not None:
            result['Description'] = self.description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListChangeOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_list: List[ListChangeOrdersResponseBodyDataChangeOrderList] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.change_order_list = change_order_list
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.change_order_list:
            for k in self.change_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeOrderList'] = []
        if self.change_order_list is not None:
            for k in self.change_order_list:
                result['ChangeOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_order_list = []
        if m.get('ChangeOrderList') is not None:
            for k in m.get('ChangeOrderList'):
                temp_model = ListChangeOrdersResponseBodyDataChangeOrderList()
                self.change_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListChangeOrdersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListChangeOrdersResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListChangeOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListChangeOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListChangeOrdersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListChangeOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumedServicesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListConsumedServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        group_2ip: str = None,
        groups: List[str] = None,
        ips: List[str] = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.group_2ip = group_2ip
        self.groups = groups
        self.ips = ips
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListConsumedServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListConsumedServicesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListConsumedServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListConsumedServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConsumedServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConsumedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListGreyTagRouteResponseBodyDataResultDubboRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        # abandon
        self.name = name
        self.operator = operator
        # abandon
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGreyTagRouteResponseBodyDataResultDubboRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        group: str = None,
        items: List[ListGreyTagRouteResponseBodyDataResultDubboRulesItems] = None,
        method_name: str = None,
        service_name: str = None,
        version: str = None,
    ):
        self.condition = condition
        self.group = group
        self.items = items
        self.method_name = method_name
        self.service_name = service_name
        self.version = version

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.group is not None:
            result['group'] = self.group
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('group') is not None:
            self.group = m.get('group')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListGreyTagRouteResponseBodyDataResultDubboRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListGreyTagRouteResponseBodyDataResultScRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        # abandon
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGreyTagRouteResponseBodyDataResultScRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        items: List[ListGreyTagRouteResponseBodyDataResultScRulesItems] = None,
        path: str = None,
    ):
        self.condition = condition
        self.items = items
        self.path = path

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListGreyTagRouteResponseBodyDataResultScRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ListGreyTagRouteResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        dubbo_rules: List[ListGreyTagRouteResponseBodyDataResultDubboRules] = None,
        grey_tag_route_id: int = None,
        name: str = None,
        sc_rules: List[ListGreyTagRouteResponseBodyDataResultScRules] = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.dubbo_rules = dubbo_rules
        self.grey_tag_route_id = grey_tag_route_id
        self.name = name
        self.sc_rules = sc_rules
        self.update_time = update_time

    def validate(self):
        if self.dubbo_rules:
            for k in self.dubbo_rules:
                if k:
                    k.validate()
        if self.sc_rules:
            for k in self.sc_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['DubboRules'] = []
        if self.dubbo_rules is not None:
            for k in self.dubbo_rules:
                result['DubboRules'].append(k.to_map() if k else None)
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.name is not None:
            result['Name'] = self.name
        result['ScRules'] = []
        if self.sc_rules is not None:
            for k in self.sc_rules:
                result['ScRules'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k in m.get('DubboRules'):
                temp_model = ListGreyTagRouteResponseBodyDataResultDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k))
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k in m.get('ScRules'):
                temp_model = ListGreyTagRouteResponseBodyDataResultScRules()
                self.sc_rules.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        result: List[ListGreyTagRouteResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGreyTagRouteResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIngressesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        namespace_id: str = None,
    ):
        self.app_id = app_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListIngressesResponseBodyDataIngressList(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        description: str = None,
        id: int = None,
        listener_port: str = None,
        name: str = None,
        namespace_id: str = None,
        slb_id: str = None,
        slb_type: str = None,
    ):
        self.cert_id = cert_id
        self.description = description
        self.id = id
        self.listener_port = listener_port
        self.name = name
        self.namespace_id = namespace_id
        self.slb_id = slb_id
        self.slb_type = slb_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class ListIngressesResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_list: List[ListIngressesResponseBodyDataIngressList] = None,
    ):
        self.ingress_list = ingress_list

    def validate(self):
        if self.ingress_list:
            for k in self.ingress_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IngressList'] = []
        if self.ingress_list is not None:
            for k in self.ingress_list:
                result['IngressList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ingress_list = []
        if m.get('IngressList') is not None:
            for k in m.get('IngressList'):
                temp_model = ListIngressesResponseBodyDataIngressList()
                self.ingress_list.append(temp_model.from_map(k))
        return self


class ListIngressesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListIngressesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListIngressesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListIngressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIngressesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIngressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogConfigsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLogConfigsResponseBodyDataLogConfigs(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        create_time: str = None,
        log_dir: str = None,
        log_type: str = None,
        region_id: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
        store_type: str = None,
    ):
        self.config_name = config_name
        self.create_time = create_time
        self.log_dir = log_dir
        self.log_type = log_type
        self.region_id = region_id
        self.sls_log_store = sls_log_store
        self.sls_project = sls_project
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log_dir is not None:
            result['LogDir'] = self.log_dir
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.store_type is not None:
            result['StoreType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LogDir') is not None:
            self.log_dir = m.get('LogDir')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')
        return self


class ListLogConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        log_configs: List[ListLogConfigsResponseBodyDataLogConfigs] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.log_configs = log_configs
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.log_configs:
            for k in self.log_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['LogConfigs'] = []
        if self.log_configs is not None:
            for k in self.log_configs:
                result['LogConfigs'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.log_configs = []
        if m.get('LogConfigs') is not None:
            for k in m.get('LogConfigs'):
                temp_model = ListLogConfigsResponseBodyDataLogConfigs()
                self.log_configs.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListLogConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListLogConfigsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListLogConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListLogConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListLogConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespaceChangeOrdersRequest(TeaModel):
    def __init__(
        self,
        co_status: str = None,
        co_type: str = None,
        current_page: int = None,
        key: str = None,
        namespace_id: str = None,
        page_size: int = None,
    ):
        self.co_status = co_status
        self.co_type = co_type
        self.current_page = current_page
        self.key = key
        self.namespace_id = namespace_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNamespaceChangeOrdersResponseBodyDataChangeOrderList(TeaModel):
    def __init__(
        self,
        batch_count: int = None,
        batch_type: str = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        create_user_id: str = None,
        description: str = None,
        finish_time: str = None,
        group_id: str = None,
        namespace_id: str = None,
        pipelines: str = None,
        source: str = None,
        status: int = None,
        user_id: str = None,
    ):
        self.batch_count = batch_count
        self.batch_type = batch_type
        self.change_order_id = change_order_id
        self.co_type = co_type
        self.co_type_code = co_type_code
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.description = description
        self.finish_time = finish_time
        self.group_id = group_id
        self.namespace_id = namespace_id
        self.pipelines = pipelines
        self.source = source
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.description is not None:
            result['Description'] = self.description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.pipelines is not None:
            result['Pipelines'] = self.pipelines
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Pipelines') is not None:
            self.pipelines = m.get('Pipelines')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListNamespaceChangeOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_list: List[ListNamespaceChangeOrdersResponseBodyDataChangeOrderList] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.change_order_list = change_order_list
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.change_order_list:
            for k in self.change_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeOrderList'] = []
        if self.change_order_list is not None:
            for k in self.change_order_list:
                result['ChangeOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_order_list = []
        if m.get('ChangeOrderList') is not None:
            for k in m.get('ChangeOrderList'):
                temp_model = ListNamespaceChangeOrdersResponseBodyDataChangeOrderList()
                self.change_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListNamespaceChangeOrdersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListNamespaceChangeOrdersResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListNamespaceChangeOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListNamespaceChangeOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNamespaceChangeOrdersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNamespaceChangeOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacedConfigMapsRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ListNamespacedConfigMapsResponseBodyDataConfigMaps(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        create_time: int = None,
        data: Dict[str, Any] = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        relate_apps: List[ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps] = None,
        update_time: int = None,
    ):
        self.config_map_id = config_map_id
        self.create_time = create_time
        self.data = data
        self.description = description
        self.name = name
        self.namespace_id = namespace_id
        self.relate_apps = relate_apps
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListNamespacedConfigMapsResponseBodyData(TeaModel):
    def __init__(
        self,
        config_maps: List[ListNamespacedConfigMapsResponseBodyDataConfigMaps] = None,
    ):
        self.config_maps = config_maps

    def validate(self):
        if self.config_maps:
            for k in self.config_maps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigMaps'] = []
        if self.config_maps is not None:
            for k in self.config_maps:
                result['ConfigMaps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_maps = []
        if m.get('ConfigMaps') is not None:
            for k in m.get('ConfigMaps'):
                temp_model = ListNamespacedConfigMapsResponseBodyDataConfigMaps()
                self.config_maps.append(temp_model.from_map(k))
        return self


class ListNamespacedConfigMapsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListNamespacedConfigMapsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListNamespacedConfigMapsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListNamespacedConfigMapsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNamespacedConfigMapsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNamespacedConfigMapsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedServicesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListPublishedServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        group_2ip: str = None,
        groups: List[str] = None,
        ips: List[str] = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.group_2ip = group_2ip
        self.groups = groups
        self.ips = ips
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListPublishedServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListPublishedServicesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPublishedServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListPublishedServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPublishedServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPublishedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesResponseBodyDataTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        tag_resources: List[ListTagResourcesResponseBodyDataTagResources] = None,
    ):
        self.next_token = next_token
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyDataTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTagResourcesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTagResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenSaeServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenSaeServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenSaeServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenSaeServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResourceStaticsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class QueryResourceStaticsResponseBodyDataRealTimeRes(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        memory: float = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class QueryResourceStaticsResponseBodyDataSummary(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        memory: float = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class QueryResourceStaticsResponseBodyData(TeaModel):
    def __init__(
        self,
        real_time_res: QueryResourceStaticsResponseBodyDataRealTimeRes = None,
        summary: QueryResourceStaticsResponseBodyDataSummary = None,
    ):
        self.real_time_res = real_time_res
        self.summary = summary

    def validate(self):
        if self.real_time_res:
            self.real_time_res.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_time_res is not None:
            result['RealTimeRes'] = self.real_time_res.to_map()
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealTimeRes') is not None:
            temp_model = QueryResourceStaticsResponseBodyDataRealTimeRes()
            self.real_time_res = temp_model.from_map(m['RealTimeRes'])
        if m.get('Summary') is not None:
            temp_model = QueryResourceStaticsResponseBodyDataSummary()
            self.summary = temp_model.from_map(m['Summary'])
        return self


class QueryResourceStaticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryResourceStaticsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryResourceStaticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class QueryResourceStaticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryResourceStaticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryResourceStaticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReduceApplicationCapacityByInstanceIdsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        instance_ids: str = None,
    ):
        self.app_id = app_id
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ReduceApplicationCapacityByInstanceIdsResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class ReduceApplicationCapacityByInstanceIdsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReduceApplicationCapacityByInstanceIdsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReduceApplicationCapacityByInstanceIdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ReduceApplicationCapacityByInstanceIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReduceApplicationCapacityByInstanceIdsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReduceApplicationCapacityByInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        auto_enable_application_scaling_rule: bool = None,
        min_ready_instances: int = None,
        replicas: int = None,
    ):
        self.app_id = app_id
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        self.min_ready_instances = min_ready_instances
        self.replicas = replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class RescaleApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RescaleApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RescaleApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = RescaleApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RescaleApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RescaleApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RescaleApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationVerticallyRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cpu: str = None,
        memory: str = None,
    ):
        self.app_id = app_id
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class RescaleApplicationVerticallyResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RescaleApplicationVerticallyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RescaleApplicationVerticallyResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RescaleApplicationVerticallyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RescaleApplicationVerticallyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RescaleApplicationVerticallyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RescaleApplicationVerticallyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        min_ready_instances: int = None,
    ):
        self.app_id = app_id
        self.min_ready_instances = min_ready_instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        return self


class RestartApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RestartApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RestartApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RestartApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RestartApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstancesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        instance_ids: str = None,
    ):
        self.app_id = app_id
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class RestartInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RestartInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RestartInstancesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RestartInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RestartInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        auto_enable_application_scaling_rule: str = None,
        batch_wait_time: int = None,
        min_ready_instances: int = None,
        update_strategy: str = None,
        version_id: str = None,
    ):
        self.app_id = app_id
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        self.batch_wait_time = batch_wait_time
        self.min_ready_instances = min_ready_instances
        self.update_strategy = update_strategy
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RollbackApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
        is_need_approval: bool = None,
    ):
        self.change_order_id = change_order_id
        self.is_need_approval = is_need_approval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')
        return self


class RollbackApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RollbackApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RollbackApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RollbackApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StartApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class StartApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StartApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StartApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StopApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class StopApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StopApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StopApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StopApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindSlbRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        internet: bool = None,
        intranet: bool = None,
    ):
        self.app_id = app_id
        self.internet = internet
        self.intranet = intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.internet is not None:
            result['Internet'] = self.internet
        if self.intranet is not None:
            result['Intranet'] = self.intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Internet') is not None:
            self.internet = m.get('Internet')
        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')
        return self


class UnbindSlbResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class UnbindSlbResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UnbindSlbResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UnbindSlbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UnbindSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindSlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        delete_all: bool = None,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tag_keys: str = None,
    ):
        self.delete_all = delete_all
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_all is not None:
            result['DeleteAll'] = self.delete_all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAll') is not None:
            self.delete_all = m.get('DeleteAll')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        security_group_id: str = None,
    ):
        self.app_id = app_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class UpdateAppSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateAppSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAppSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
        scaling_rule_timer: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_timer = scaling_rule_timer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')
        return self


class UpdateApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(
        self,
        at_time: str = None,
        target_replicas: int = None,
    ):
        self.at_time = at_time
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class UpdateApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[UpdateApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.period = period
        self.schedules = schedules

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = UpdateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class UpdateApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: UpdateApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.scale_rule_enabled = scale_rule_enabled
        self.scale_rule_name = scale_rule_name
        self.scale_rule_type = scale_rule_type
        self.timer = timer
        self.update_time = update_time

    def validate(self):
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateApplicationScalingRuleResponseBodyData = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigMapRequest(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        data: str = None,
        description: str = None,
    ):
        self.config_map_id = config_map_id
        self.data = data
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: str = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class UpdateConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        dubbo_rules: str = None,
        grey_tag_route_id: int = None,
        sc_rules: str = None,
    ):
        # 规则名称
        self.description = description
        # Dubbo规则
        self.dubbo_rules = dubbo_rules
        # 规则ID
        self.grey_tag_route_id = grey_tag_route_id
        # SpringCloud规则
        self.sc_rules = sc_rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')
        return self


class UpdateGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class UpdateGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIngressRequest(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        default_rule: str = None,
        description: str = None,
        ingress_id: int = None,
        listener_port: str = None,
        rules: str = None,
    ):
        self.cert_id = cert_id
        self.default_rule = default_rule
        self.description = description
        self.ingress_id = ingress_id
        self.listener_port = listener_port
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.description is not None:
            result['Description'] = self.description
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class UpdateIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class UpdateIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIngressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class UpdateNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceVpcRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        vpc_id: str = None,
    ):
        self.namespace_id = namespace_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateNamespaceVpcResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateNamespaceVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNamespaceVpcResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNamespaceVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadFilesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cloud_url: str = None,
        instance_id: str = None,
        localpath: str = None,
    ):
        self.app_id = app_id
        self.cloud_url = cloud_url
        self.instance_id = instance_id
        self.localpath = localpath

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cloud_url is not None:
            result['CloudUrl'] = self.cloud_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.localpath is not None:
            result['Localpath'] = self.localpath
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CloudUrl') is not None:
            self.cloud_url = m.get('CloudUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Localpath') is not None:
            self.localpath = m.get('Localpath')
        return self


class UploadFilesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UploadFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UploadFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self

