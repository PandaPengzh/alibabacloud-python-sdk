# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # rg-aek2ajbjoloa23q
        self.new_resource_group_id = new_resource_group_id
        # P7RMVSVM9LOVYQOM
        self.resource_id = resource_id
        # APPLICATION
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequestInstances(TeaModel):
    def __init__(
        self,
        id: str = None,
        node_name: str = None,
        node_type: str = None,
    ):
        # The ID of the instance.
        self.id = id
        # The name of the instance.
        self.node_name = node_name
        # The type of the instance.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        configuration: Dict[str, str] = None,
        instances: List[CreateApplicationRequestInstances] = None,
        name: str = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables: Dict[str, str] = None,
    ):
        # The ID of the region.
        self.area_id = area_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The parameters that are used to configure the application you want to create. For example, enableMonitor specifies whether to automatically create a CloudMonitor task for the application, and enableReport specifies whether to generate reports.
        self.configuration = configuration
        # The instances in which you want to create the application. You can create applications in an existing virtual private cloud (VPC).
        self.instances = instances
        # The name of the application that you want to create.
        self.name = name
        # The ID of the resource group to which the application you want to create belongs.
        self.resource_group_id = resource_group_id
        # The ID of the template.
        self.template_id = template_id
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables = variables

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
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = CreateApplicationRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class CreateApplicationShrinkRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        configuration_shrink: str = None,
        instances_shrink: str = None,
        name: str = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables_shrink: str = None,
    ):
        # The ID of the region.
        self.area_id = area_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The parameters that are used to configure the application you want to create. For example, enableMonitor specifies whether to automatically create a CloudMonitor task for the application, and enableReport specifies whether to generate reports.
        self.configuration_shrink = configuration_shrink
        # The instances in which you want to create the application. You can create applications in an existing virtual private cloud (VPC).
        self.instances_shrink = instances_shrink
        # The name of the application that you want to create.
        self.name = name
        # The ID of the resource group to which the application you want to create belongs.
        self.resource_group_id = resource_group_id
        # The ID of the template.
        self.template_id = template_id
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables_shrink = variables_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_shrink is not None:
            result['Configuration'] = self.configuration_shrink
        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables_shrink is not None:
            result['Variables'] = self.variables_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configuration') is not None:
            self.configuration_shrink = m.get('Configuration')
        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables_shrink = m.get('Variables')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The ID of the application.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationResponseBody = None,
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApplicationResponseBody = None,
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeployApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data of the application.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeployApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployApplicationResponseBody = None,
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
            temp_model = DeployApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteOperationASyncRequest(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        operation: str = None,
        resource_group_id: str = None,
        service_type: str = None,
    ):
        self.attributes = attributes
        self.operation = operation
        self.resource_group_id = resource_group_id
        # The HTTP status code. A value of 200 indicates that the request is successful, and other values indicate that the request fails.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncShrinkRequest(TeaModel):
    def __init__(
        self,
        attributes_shrink: str = None,
        operation: str = None,
        resource_group_id: str = None,
        service_type: str = None,
    ):
        self.attributes_shrink = attributes_shrink
        self.operation = operation
        self.resource_group_id = resource_group_id
        # The HTTP status code. A value of 200 indicates that the request is successful, and other values indicate that the request fails.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteOperationASyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteOperationASyncResponseBody = None,
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
            temp_model = ExecuteOperationASyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the request.
        self.application_id = application_id
        # Queries the basic information, verification results, billing results, and deployment results of an application.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetApplicationResponseBodyDataChecklist(TeaModel):
    def __init__(
        self,
        lifecycle: str = None,
        region: str = None,
        remark: str = None,
        resource_code: str = None,
        resource_name: str = None,
        result: str = None,
        specification: str = None,
    ):
        # The message returned for verification.
        self.lifecycle = lifecycle
        # The verification results returned.
        self.region = region
        # The name of the instance.
        self.remark = remark
        # The error message that is returned when a price query fails.
        self.resource_code = resource_code
        # ECS instance sold out
        self.resource_name = resource_name
        # The service code.
        self.result = result
        # The verification result.
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.result is not None:
            result['Result'] = self.result
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class GetApplicationResponseBodyDataPriceList(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        count: int = None,
        instance_name: str = None,
        lifecycle: str = None,
        one_price: float = None,
        original_price: float = None,
        period: float = None,
        price: float = None,
        price_unit: str = None,
        region: str = None,
        remark: str = None,
        resource_code: str = None,
        specification: str = None,
    ):
        # The price unit.
        self.charge_type = charge_type
        # The original price.
        self.count = count
        # The ID of the resource group to which the application belongs.
        self.instance_name = instance_name
        # The ID of the region.
        self.lifecycle = lifecycle
        # The service code.
        self.one_price = one_price
        # The billing results.
        self.original_price = original_price
        # The name of the instance.
        self.period = period
        # The quantity.
        self.price = price
        # The unit price.
        self.price_unit = price_unit
        # USD/Hour
        self.region = region
        # The instance type.
        self.remark = remark
        # The time when the application was created.
        self.resource_code = resource_code
        # The total price.
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.one_price is not None:
            result['OnePrice'] = self.one_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.period is not None:
            result['Period'] = self.period
        if self.price is not None:
            result['Price'] = self.price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('OnePrice') is not None:
            self.one_price = m.get('OnePrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class GetApplicationResponseBodyDataResourceList(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        lifecycle: str = None,
        remark: str = None,
        resource_code: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        # The service code.
        self.charge_type = charge_type
        # The billing method.
        self.lifecycle = lifecycle
        # The ID of the instance.
        self.remark = remark
        # The status of the application.
        self.resource_code = resource_code
        # The resource deployment result.
        self.resource_id = resource_id
        # The resources.
        self.resource_name = resource_name
        # The name of the instance.
        self.resource_type = resource_type
        # The resource tag.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        checklist: List[GetApplicationResponseBodyDataChecklist] = None,
        create_time: str = None,
        description: str = None,
        error: str = None,
        image_url: str = None,
        name: str = None,
        price_list: List[GetApplicationResponseBodyDataPriceList] = None,
        resource_group_id: str = None,
        resource_list: List[GetApplicationResponseBodyDataResourceList] = None,
        status: str = None,
        template_id: str = None,
    ):
        # The description of the application.
        self.application_id = application_id
        # The resource tag.
        self.checklist = checklist
        # The URL of the application topology image.
        self.create_time = create_time
        # The message returned for the request.
        self.description = description
        # The resource type.
        self.error = error
        # The ID of the request.
        self.image_url = image_url
        # The URL of the image in the database.
        self.name = name
        # The ID of the template associated with the application.
        self.price_list = price_list
        # 1411182597819805/topo-MCEXDI5EL2OM10NY.json
        self.resource_group_id = resource_group_id
        # The resource specification.
        self.resource_list = resource_list
        # Verification passed
        self.status = status
        # CADT application
        self.template_id = template_id

    def validate(self):
        if self.checklist:
            for k in self.checklist:
                if k:
                    k.validate()
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['Checklist'] = []
        if self.checklist is not None:
            for k in self.checklist:
                result['Checklist'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.error is not None:
            result['Error'] = self.error
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.checklist = []
        if m.get('Checklist') is not None:
            for k in m.get('Checklist'):
                temp_model = GetApplicationResponseBodyDataChecklist()
                self.checklist.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = GetApplicationResponseBodyDataPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = GetApplicationResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetApplicationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The deployment result.
        self.code = code
        # The ID of the resource group.
        self.data = data
        # Possible application states:
        # 
        # *   Creating: The application is being created.
        # *   Modified: The application has been modified.
        # *   Verifying: The application is being verified.
        # *   Verified_Failure: The application failed to pass the verification.
        # *   Verified_Success: The application has passed the verification.
        # *   Valuating: Fees are being calculated for the application.
        # *   Valuating_Failure: Fees failed to be calculated for the application.
        # *   Valuating_Success: Fees are calculated for the application.
        # *   Deploying: The application is being deployed.
        # *   Deployed_Failure: The application failed to be deployed.
        # *   Partially_Deployed_Success: Some resources of the application are deployed.
        # *   Deployed_Success: The application is deployed.
        # *   Destroying: The application is being released.
        # *   Delayed_Destroy: The application release is delayed.
        # *   Destroyed_Failure: The application failed to be released.
        # *   Partially_Destroyed_Success: Some resources of the application are released.
        # *   Destroyed_Success: The application is released.
        # *   Revised: The application architecture is adjusted.
        # *   Verifying_In_Revision: The application resources are being verified during architecture adjustment.
        # *   Verified_Failure_In_Revision: The application resources failed to pass the verification during architecture adjustment.
        # *   Verified_Success_In_Revision: The application resources are verified during architecture adjustment.
        # *   Valuating_In_Revision: Fees are being calculated for the application during architecture adjustment.
        # *   Valuating_Failure_In_Revision: Fees failed to be calculated for the application during architecture adjustment.
        # *   Valuating_Success_In_Revision: Fees are calculated for the application during architecture adjustment.
        self.message = message
        # The ID of the application.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationResponseBody = None,
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
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecuteOperationResultRequest(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the operation.
        self.operation_id = operation_id
        # The ID of the resource group. This parameter is specified to verify the permissions on the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetExecuteOperationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        arguments: str = None,
        message: str = None,
        operation_id: str = None,
        status: str = None,
    ):
        # The output of the operation.
        self.arguments = arguments
        # The returned message.
        self.message = message
        # The ID of the operation.
        self.operation_id = operation_id
        # The status of the operation.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.message is not None:
            result['Message'] = self.message
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExecuteOperationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetExecuteOperationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. A value of 200 indicates that the request is successful.
        self.code = code
        # The details of the operation.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetExecuteOperationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExecuteOperationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExecuteOperationResultResponseBody = None,
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
            temp_model = GetExecuteOperationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_group_id: str = None,
        template_id: str = None,
    ):
        self.region = region
        self.resource_group_id = resource_group_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBodyDataVariables(TeaModel):
    def __init__(
        self,
        attribute: str = None,
        data_type: str = None,
        default_value: str = None,
        variable: str = None,
    ):
        # 变量名
        self.attribute = attribute
        # 变量类型
        self.data_type = data_type
        # 默认值
        self.default_value = default_value
        # 变量值
        self.variable = variable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['Attribute'] = self.attribute
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.variable is not None:
            result['Variable'] = self.variable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Variable') is not None:
            self.variable = m.get('Variable')
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        image_url: str = None,
        name: str = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables: List[GetTemplateResponseBodyDataVariables] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.image_url = image_url
        self.name = name
        self.resource_group_id = resource_group_id
        self.template_id = template_id
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
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
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = GetTemplateResponseBodyDataVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateResponseBody = None,
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        security_token: str = None,
        snapshot_bucket: str = None,
    ):
        # The AccessKey ID that is used to access OSS.
        self.access_key_id = access_key_id
        # The AccessKey secret that is used to access OSS.
        self.access_key_secret = access_key_secret
        # The OSS bucket that is used to store the architecture image.
        self.bucket = bucket
        # The OSS endpoint.
        self.endpoint = endpoint
        # The token that is used to access the Object Storage Service (OSS) bucket that stores the architecture image.
        self.security_token = security_token
        # The OSS bucket that is used to save data snapshots.
        self.snapshot_bucket = snapshot_bucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.snapshot_bucket is not None:
            result['SnapshotBucket'] = self.snapshot_bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SnapshotBucket') is not None:
            self.snapshot_bucket = m.get('SnapshotBucket')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The information about the token.
        self.data = data
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTokenResponseBody = None,
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: int = None,
        order_type: int = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        self.keyword = keyword
        # The HTTP status code.
        self.max_results = max_results
        # The ID of the resource group to which the application belongs.
        self.next_token = next_token
        self.order_type = order_type
        self.resource_group_id = resource_group_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        create_time: str = None,
        image_url: str = None,
        name: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        self.application_id = application_id
        self.create_time = create_time
        self.image_url = image_url
        self.name = name
        self.resource_group_id = resource_group_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListApplicationResponseBodyData] = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

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
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListApplicationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationResponseBody = None,
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
            temp_model = ListApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The resource IDs. You can specify a maximum number of 50 IDs.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The tags. A maximum of 20 tags are supported.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type. Valid values: application and template.
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The HTTP status code. A value of 200 indicates that the request is successful.
        self.code = code
        # The error message returned if the request failed.
        self.message = message
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the NextToken parameter is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags that are added to the resources.
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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplateRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: int = None,
        order_type: int = None,
        resource_group_id: str = None,
        tag_list: int = None,
        type: str = None,
    ):
        # The keyword that is used to search for templates.
        self.keyword = keyword
        # The number of entries to return on each page.
        self.max_results = max_results
        # The number of the page to return.
        self.next_token = next_token
        # The criterion by which the templates are sorted. Valid values:
        # 
        # *   1: modification time
        # *   2: creation time
        self.order_type = order_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tag of the template.
        self.tag_list = tag_list
        # The type of the template.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        image_url: str = None,
        name: str = None,
        resource_group_id: str = None,
        tag_id: int = None,
        tag_name: str = None,
        template_id: str = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        # The URL of the architecture image.
        self.image_url = image_url
        # The name of the template.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the tag that is added to the template.
        self.tag_id = tag_id
        # The name of the tag that is added to the template.
        self.tag_name = tag_name
        # The ID of the template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListTemplateResponseBodyData] = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The HTTP status code.
        self.code = code
        # The details about templates.
        self.data = data
        # The returned message.
        self.message = message
        # The page number of the returned page.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

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
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTemplateResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplateResponseBody = None,
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
            temp_model = ListTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The ID of the resource.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ReleaseApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The return value.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseApplicationResponseBody = None,
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
            temp_model = ReleaseApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ValidateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data of the application.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateApplicationResponseBody = None,
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
            temp_model = ValidateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValuateApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ValuateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data of the application.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValuateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValuateApplicationResponseBody = None,
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
            temp_model = ValuateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValuateTemplateRequestInstances(TeaModel):
    def __init__(
        self,
        id: str = None,
        node_name: str = None,
        node_type: str = None,
    ):
        self.id = id
        self.node_name = node_name
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class ValuateTemplateRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        instances: List[ValuateTemplateRequestInstances] = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables: Dict[str, str] = None,
    ):
        self.area_id = area_id
        self.client_token = client_token
        self.instances = instances
        self.resource_group_id = resource_group_id
        self.template_id = template_id
        self.variables = variables

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
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ValuateTemplateRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class ValuateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        instances_shrink: str = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables_shrink: str = None,
    ):
        self.area_id = area_id
        self.client_token = client_token
        self.instances_shrink = instances_shrink
        self.resource_group_id = resource_group_id
        self.template_id = template_id
        self.variables_shrink = variables_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables_shrink is not None:
            result['Variables'] = self.variables_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables_shrink = m.get('Variables')
        return self


class ValuateTemplateResponseBodyDataResourceListPriceList(TeaModel):
    def __init__(
        self,
        discount_amount: float = None,
        error: str = None,
        node_type: str = None,
        original_price: float = None,
        price_unit: str = None,
        promotion_name: str = None,
        resource_id: str = None,
        trade_price: float = None,
        type: str = None,
    ):
        self.discount_amount = discount_amount
        self.error = error
        self.node_type = node_type
        self.original_price = original_price
        self.price_unit = price_unit
        self.promotion_name = promotion_name
        self.resource_id = resource_id
        self.trade_price = trade_price
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.error is not None:
            result['Error'] = self.error
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ValuateTemplateResponseBodyDataResourceList(TeaModel):
    def __init__(
        self,
        discount_amount: float = None,
        error: str = None,
        node_type: str = None,
        original_price: float = None,
        price_list: List[ValuateTemplateResponseBodyDataResourceListPriceList] = None,
        price_unit: str = None,
        promotion_name: str = None,
        trade_price: float = None,
    ):
        self.discount_amount = discount_amount
        self.error = error
        self.node_type = node_type
        self.original_price = original_price
        self.price_list = price_list
        self.price_unit = price_unit
        self.promotion_name = promotion_name
        self.trade_price = trade_price

    def validate(self):
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.error is not None:
            result['Error'] = self.error
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = ValuateTemplateResponseBodyDataResourceListPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class ValuateTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        resource_list: List[ValuateTemplateResponseBodyDataResourceList] = None,
    ):
        self.resource_list = resource_list

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = ValuateTemplateResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k))
        return self


class ValuateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ValuateTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ValuateTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValuateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValuateTemplateResponseBody = None,
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
            temp_model = ValuateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


