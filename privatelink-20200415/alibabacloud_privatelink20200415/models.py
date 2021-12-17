# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddUserToVpcEndpointServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        service_id: str = None,
        user_id: int = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.service_id = service_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUserToVpcEndpointServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserToVpcEndpointServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUserToVpcEndpointServiceResponseBody = None,
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
            temp_model = AddUserToVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddZoneToVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        ip: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class AddZoneToVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddZoneToVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddZoneToVpcEndpointResponseBody = None,
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
            temp_model = AddZoneToVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachResourceToVpcEndpointServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class AttachResourceToVpcEndpointServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachResourceToVpcEndpointServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachResourceToVpcEndpointServiceResponseBody = None,
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
            temp_model = AttachResourceToVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachSecurityGroupToVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        security_group_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class AttachSecurityGroupToVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachSecurityGroupToVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachSecurityGroupToVpcEndpointResponseBody = None,
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
            temp_model = AttachSecurityGroupToVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckProductOpenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckProductOpenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckProductOpenResponseBody = None,
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
            temp_model = CheckProductOpenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcEndpointRequestZone(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
        ip: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class CreateVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_description: str = None,
        endpoint_name: str = None,
        endpoint_type: str = None,
        protected_enabled: bool = None,
        region_id: str = None,
        security_group_id: List[str] = None,
        service_id: str = None,
        service_name: str = None,
        vpc_id: str = None,
        zone: List[CreateVpcEndpointRequestZone] = None,
        zone_private_ip_address_count: int = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_description = endpoint_description
        self.endpoint_name = endpoint_name
        self.endpoint_type = endpoint_type
        self.protected_enabled = protected_enabled
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.service_id = service_id
        self.service_name = service_name
        self.vpc_id = vpc_id
        self.zone = zone
        self.zone_private_ip_address_count = zone_private_ip_address_count

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.protected_enabled is not None:
            result['ProtectedEnabled'] = self.protected_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        if self.zone_private_ip_address_count is not None:
            result['ZonePrivateIpAddressCount'] = self.zone_private_ip_address_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('ProtectedEnabled') is not None:
            self.protected_enabled = m.get('ProtectedEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = CreateVpcEndpointRequestZone()
                self.zone.append(temp_model.from_map(k))
        if m.get('ZonePrivateIpAddressCount') is not None:
            self.zone_private_ip_address_count = m.get('ZonePrivateIpAddressCount')
        return self


class CreateVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        connection_status: str = None,
        create_time: str = None,
        endpoint_business_status: str = None,
        endpoint_description: str = None,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        request_id: str = None,
        service_id: str = None,
        service_name: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.connection_status = connection_status
        self.create_time = create_time
        self.endpoint_business_status = endpoint_business_status
        self.endpoint_description = endpoint_description
        self.endpoint_domain = endpoint_domain
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.endpoint_status = endpoint_status
        self.request_id = request_id
        self.service_id = service_id
        self.service_name = service_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint_business_status is not None:
            result['EndpointBusinessStatus'] = self.endpoint_business_status
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_domain is not None:
            result['EndpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('EndpointBusinessStatus')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointDomain') is not None:
            self.endpoint_domain = m.get('EndpointDomain')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVpcEndpointResponseBody = None,
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
            temp_model = CreateVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcEndpointServiceRequestResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateVpcEndpointServiceRequest(TeaModel):
    def __init__(
        self,
        auto_accept_enabled: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        payer: str = None,
        region_id: str = None,
        resource: List[CreateVpcEndpointServiceRequestResource] = None,
        service_description: str = None,
        service_resource_type: str = None,
        zone_affinity_enabled: bool = None,
    ):
        self.auto_accept_enabled = auto_accept_enabled
        self.client_token = client_token
        self.dry_run = dry_run
        self.payer = payer
        self.region_id = region_id
        self.resource = resource
        self.service_description = service_description
        self.service_resource_type = service_resource_type
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = CreateVpcEndpointServiceRequestResource()
                self.resource.append(temp_model.from_map(k))
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class CreateVpcEndpointServiceResponseBody(TeaModel):
    def __init__(
        self,
        auto_accept_enabled: bool = None,
        create_time: str = None,
        request_id: str = None,
        service_business_status: str = None,
        service_description: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        service_status: str = None,
        zone_affinity_enabled: bool = None,
    ):
        self.auto_accept_enabled = auto_accept_enabled
        self.create_time = create_time
        self.request_id = request_id
        self.service_business_status = service_business_status
        self.service_description = service_description
        self.service_domain = service_domain
        self.service_id = service_id
        self.service_name = service_name
        self.service_status = service_status
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class CreateVpcEndpointServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVpcEndpointServiceResponseBody = None,
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
            temp_model = CreateVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVpcEndpointResponseBody = None,
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
            temp_model = DeleteVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcEndpointServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteVpcEndpointServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpcEndpointServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVpcEndpointServiceResponseBody = None,
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
            temp_model = DeleteVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
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
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
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
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZonesResponseBody = None,
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachResourceFromVpcEndpointServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DetachResourceFromVpcEndpointServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachResourceFromVpcEndpointServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachResourceFromVpcEndpointServiceResponseBody = None,
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
            temp_model = DetachResourceFromVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachSecurityGroupFromVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        security_group_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DetachSecurityGroupFromVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachSecurityGroupFromVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachSecurityGroupFromVpcEndpointResponseBody = None,
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
            temp_model = DetachSecurityGroupFromVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVpcEndpointConnectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DisableVpcEndpointConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableVpcEndpointConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableVpcEndpointConnectionResponseBody = None,
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
            temp_model = DisableVpcEndpointConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableVpcEndpointConnectionRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class EnableVpcEndpointConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableVpcEndpointConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableVpcEndpointConnectionResponseBody = None,
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
            temp_model = EnableVpcEndpointConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpcEndpointAttributeRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        region_id: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetVpcEndpointAttributeResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        connection_status: str = None,
        create_time: str = None,
        endpoint_business_status: str = None,
        endpoint_description: str = None,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        endpoint_type: str = None,
        payer: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_owner: bool = None,
        service_id: str = None,
        service_name: str = None,
        vpc_id: str = None,
        zone_affinity_enabled: bool = None,
        zone_private_ip_address_count: int = None,
    ):
        self.bandwidth = bandwidth
        self.connection_status = connection_status
        self.create_time = create_time
        self.endpoint_business_status = endpoint_business_status
        self.endpoint_description = endpoint_description
        self.endpoint_domain = endpoint_domain
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.endpoint_status = endpoint_status
        self.endpoint_type = endpoint_type
        self.payer = payer
        self.region_id = region_id
        self.request_id = request_id
        self.resource_owner = resource_owner
        self.service_id = service_id
        self.service_name = service_name
        self.vpc_id = vpc_id
        self.zone_affinity_enabled = zone_affinity_enabled
        self.zone_private_ip_address_count = zone_private_ip_address_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint_business_status is not None:
            result['EndpointBusinessStatus'] = self.endpoint_business_status
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_domain is not None:
            result['EndpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        if self.zone_private_ip_address_count is not None:
            result['ZonePrivateIpAddressCount'] = self.zone_private_ip_address_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('EndpointBusinessStatus')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointDomain') is not None:
            self.endpoint_domain = m.get('EndpointDomain')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        if m.get('ZonePrivateIpAddressCount') is not None:
            self.zone_private_ip_address_count = m.get('ZonePrivateIpAddressCount')
        return self


class GetVpcEndpointAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVpcEndpointAttributeResponseBody = None,
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
            temp_model = GetVpcEndpointAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpcEndpointServiceAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
    ):
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetVpcEndpointServiceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        auto_accept_enabled: bool = None,
        connect_bandwidth: int = None,
        create_time: str = None,
        max_bandwidth: int = None,
        min_bandwidth: int = None,
        payer: str = None,
        region_id: str = None,
        request_id: str = None,
        service_business_status: str = None,
        service_description: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        service_resource_type: str = None,
        service_status: str = None,
        service_type: str = None,
        zone_affinity_enabled: bool = None,
        zones: List[str] = None,
    ):
        self.auto_accept_enabled = auto_accept_enabled
        self.connect_bandwidth = connect_bandwidth
        self.create_time = create_time
        self.max_bandwidth = max_bandwidth
        self.min_bandwidth = min_bandwidth
        self.payer = payer
        self.region_id = region_id
        self.request_id = request_id
        self.service_business_status = service_business_status
        self.service_description = service_description
        self.service_domain = service_domain
        self.service_id = service_id
        self.service_name = service_name
        self.service_resource_type = service_resource_type
        self.service_status = service_status
        self.service_type = service_type
        self.zone_affinity_enabled = zone_affinity_enabled
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth
        if self.min_bandwidth is not None:
            result['MinBandwidth'] = self.min_bandwidth
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')
        if m.get('MinBandwidth') is not None:
            self.min_bandwidth = m.get('MinBandwidth')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class GetVpcEndpointServiceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVpcEndpointServiceAttributeResponseBody = None,
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
            temp_model = GetVpcEndpointServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointConnectionsRequest(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        endpoint_id: str = None,
        endpoint_owner_id: int = None,
        eni_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.connection_status = connection_status
        self.endpoint_id = endpoint_id
        self.endpoint_owner_id = endpoint_owner_id
        self.eni_id = eni_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_owner_id is not None:
            result['EndpointOwnerId'] = self.endpoint_owner_id
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointOwnerId') is not None:
            self.endpoint_owner_id = m.get('EndpointOwnerId')
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ListVpcEndpointConnectionsResponseBodyConnectionsZones(TeaModel):
    def __init__(
        self,
        eni_id: str = None,
        resource_id: str = None,
        v_switch_id: str = None,
        zone_domain: str = None,
        zone_id: str = None,
    ):
        self.eni_id = eni_id
        self.resource_id = resource_id
        self.v_switch_id = v_switch_id
        self.zone_domain = zone_domain
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_domain is not None:
            result['ZoneDomain'] = self.zone_domain
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneDomain') is not None:
            self.zone_domain = m.get('ZoneDomain')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVpcEndpointConnectionsResponseBodyConnections(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        connection_status: str = None,
        endpoint_id: str = None,
        endpoint_owner_id: int = None,
        endpoint_vpc_id: str = None,
        modified_time: str = None,
        resource_owner: bool = None,
        service_id: str = None,
        zones: List[ListVpcEndpointConnectionsResponseBodyConnectionsZones] = None,
    ):
        self.bandwidth = bandwidth
        self.connection_status = connection_status
        self.endpoint_id = endpoint_id
        self.endpoint_owner_id = endpoint_owner_id
        self.endpoint_vpc_id = endpoint_vpc_id
        self.modified_time = modified_time
        self.resource_owner = resource_owner
        self.service_id = service_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_owner_id is not None:
            result['EndpointOwnerId'] = self.endpoint_owner_id
        if self.endpoint_vpc_id is not None:
            result['EndpointVpcId'] = self.endpoint_vpc_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointOwnerId') is not None:
            self.endpoint_owner_id = m.get('EndpointOwnerId')
        if m.get('EndpointVpcId') is not None:
            self.endpoint_vpc_id = m.get('EndpointVpcId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = ListVpcEndpointConnectionsResponseBodyConnectionsZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListVpcEndpointConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        connections: List[ListVpcEndpointConnectionsResponseBodyConnections] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.connections = connections
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = ListVpcEndpointConnectionsResponseBodyConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpcEndpointConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointConnectionsResponseBody = None,
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
            temp_model = ListVpcEndpointConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpcEndpointSecurityGroupsResponseBodySecurityGroups(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class ListVpcEndpointSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        security_groups: List[ListVpcEndpointSecurityGroupsResponseBodySecurityGroups] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.security_groups = security_groups

    def validate(self):
        if self.security_groups:
            for k in self.security_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k in self.security_groups:
                result['SecurityGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k in m.get('SecurityGroups'):
                temp_model = ListVpcEndpointSecurityGroupsResponseBodySecurityGroups()
                self.security_groups.append(temp_model.from_map(k))
        return self


class ListVpcEndpointSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointSecurityGroupsResponseBody = None,
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
            temp_model = ListVpcEndpointSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServiceResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ListVpcEndpointServiceResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        ip: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.ip = ip
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVpcEndpointServiceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[ListVpcEndpointServiceResourcesResponseBodyResources] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListVpcEndpointServiceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListVpcEndpointServiceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointServiceResourcesResponseBody = None,
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
            temp_model = ListVpcEndpointServiceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServiceUsersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_id: str = None,
        user_id: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_id = service_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListVpcEndpointServiceUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_id: int = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListVpcEndpointServiceUsersResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        users: List[ListVpcEndpointServiceUsersResponseBodyUsers] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListVpcEndpointServiceUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListVpcEndpointServiceUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointServiceUsersResponseBody = None,
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
            temp_model = ListVpcEndpointServiceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServicesRequest(TeaModel):
    def __init__(
        self,
        auto_accept_enabled: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_business_status: str = None,
        service_id: str = None,
        service_name: str = None,
        service_resource_type: str = None,
        service_status: str = None,
        zone_affinity_enabled: bool = None,
    ):
        self.auto_accept_enabled = auto_accept_enabled
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_business_status = service_business_status
        self.service_id = service_id
        self.service_name = service_name
        self.service_resource_type = service_resource_type
        self.service_status = service_status
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class ListVpcEndpointServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        auto_accept_enabled: bool = None,
        connect_bandwidth: int = None,
        create_time: str = None,
        max_bandwidth: int = None,
        min_bandwidth: int = None,
        payer: str = None,
        region_id: str = None,
        service_business_status: str = None,
        service_description: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        service_resource_type: str = None,
        service_status: str = None,
        service_type: str = None,
        zone_affinity_enabled: bool = None,
    ):
        self.auto_accept_enabled = auto_accept_enabled
        self.connect_bandwidth = connect_bandwidth
        self.create_time = create_time
        self.max_bandwidth = max_bandwidth
        self.min_bandwidth = min_bandwidth
        self.payer = payer
        self.region_id = region_id
        self.service_business_status = service_business_status
        self.service_description = service_description
        self.service_domain = service_domain
        self.service_id = service_id
        self.service_name = service_name
        self.service_resource_type = service_resource_type
        self.service_status = service_status
        self.service_type = service_type
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth
        if self.min_bandwidth is not None:
            result['MinBandwidth'] = self.min_bandwidth
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')
        if m.get('MinBandwidth') is not None:
            self.min_bandwidth = m.get('MinBandwidth')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class ListVpcEndpointServicesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        services: List[ListVpcEndpointServicesResponseBodyServices] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListVpcEndpointServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListVpcEndpointServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointServicesResponseBody = None,
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
            temp_model = ListVpcEndpointServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServicesByEndUserRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_id: str = None,
        service_name: str = None,
        service_type: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_id = service_id
        self.service_name = service_name
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListVpcEndpointServicesByEndUserResponseBodyServices(TeaModel):
    def __init__(
        self,
        payer: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        service_type: str = None,
        zones: List[str] = None,
    ):
        self.payer = payer
        self.service_domain = service_domain
        self.service_id = service_id
        self.service_name = service_name
        self.service_type = service_type
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class ListVpcEndpointServicesByEndUserResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        services: List[ListVpcEndpointServicesByEndUserResponseBodyServices] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListVpcEndpointServicesByEndUserResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListVpcEndpointServicesByEndUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointServicesByEndUserResponseBody = None,
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
            temp_model = ListVpcEndpointServicesByEndUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointZonesRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpcEndpointZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_ip: str = None,
        region_id: str = None,
        service_status: str = None,
        v_switch_id: str = None,
        zone_domain: str = None,
        zone_id: str = None,
        zone_status: str = None,
    ):
        self.eni_id = eni_id
        self.eni_ip = eni_ip
        self.region_id = region_id
        self.service_status = service_status
        self.v_switch_id = v_switch_id
        self.zone_domain = zone_domain
        self.zone_id = zone_id
        self.zone_status = zone_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_ip is not None:
            result['EniIp'] = self.eni_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_domain is not None:
            result['ZoneDomain'] = self.zone_domain
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_status is not None:
            result['ZoneStatus'] = self.zone_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniIp') is not None:
            self.eni_ip = m.get('EniIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneDomain') is not None:
            self.zone_domain = m.get('ZoneDomain')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneStatus') is not None:
            self.zone_status = m.get('ZoneStatus')
        return self


class ListVpcEndpointZonesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        zones: List[ListVpcEndpointZonesResponseBodyZones] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = ListVpcEndpointZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListVpcEndpointZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointZonesResponseBody = None,
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
            temp_model = ListVpcEndpointZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointsRequest(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        endpoint_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_name: str = None,
        vpc_id: str = None,
    ):
        self.connection_status = connection_status
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.endpoint_status = endpoint_status
        self.endpoint_type = endpoint_type
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_name = service_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcEndpointsResponseBodyEndpoints(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        connection_status: str = None,
        create_time: str = None,
        endpoint_business_status: str = None,
        endpoint_description: str = None,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        endpoint_type: str = None,
        region_id: str = None,
        resource_owner: bool = None,
        service_id: str = None,
        service_name: str = None,
        vpc_id: str = None,
        zone_affinity_enabled: bool = None,
    ):
        self.bandwidth = bandwidth
        self.connection_status = connection_status
        self.create_time = create_time
        self.endpoint_business_status = endpoint_business_status
        self.endpoint_description = endpoint_description
        self.endpoint_domain = endpoint_domain
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.endpoint_status = endpoint_status
        self.endpoint_type = endpoint_type
        self.region_id = region_id
        self.resource_owner = resource_owner
        self.service_id = service_id
        self.service_name = service_name
        self.vpc_id = vpc_id
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint_business_status is not None:
            result['EndpointBusinessStatus'] = self.endpoint_business_status
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_domain is not None:
            result['EndpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('EndpointBusinessStatus')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointDomain') is not None:
            self.endpoint_domain = m.get('EndpointDomain')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class ListVpcEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        endpoints: List[ListVpcEndpointsResponseBodyEndpoints] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.endpoints = endpoints
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListVpcEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpcEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointsResponseBody = None,
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
            temp_model = ListVpcEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenPrivateLinkServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class OpenPrivateLinkServiceResponseBody(TeaModel):
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


class OpenPrivateLinkServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenPrivateLinkServiceResponseBody = None,
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
            temp_model = OpenPrivateLinkServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromVpcEndpointServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        service_id: str = None,
        user_id: int = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.service_id = service_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RemoveUserFromVpcEndpointServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUserFromVpcEndpointServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUserFromVpcEndpointServiceResponseBody = None,
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
            temp_model = RemoveUserFromVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveZoneFromVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class RemoveZoneFromVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveZoneFromVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveZoneFromVpcEndpointResponseBody = None,
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
            temp_model = RemoveZoneFromVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpcEndpointAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_description: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_description = endpoint_description
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateVpcEndpointAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVpcEndpointAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateVpcEndpointAttributeResponseBody = None,
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
            temp_model = UpdateVpcEndpointAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpcEndpointConnectionAttributeRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_id = endpoint_id
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateVpcEndpointConnectionAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVpcEndpointConnectionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateVpcEndpointConnectionAttributeResponseBody = None,
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
            temp_model = UpdateVpcEndpointConnectionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpcEndpointServiceAttributeRequest(TeaModel):
    def __init__(
        self,
        auto_accept_enabled: bool = None,
        client_token: str = None,
        connect_bandwidth: int = None,
        dry_run: bool = None,
        region_id: str = None,
        service_description: str = None,
        service_id: str = None,
        zone_affinity_enabled: bool = None,
    ):
        self.auto_accept_enabled = auto_accept_enabled
        self.client_token = client_token
        self.connect_bandwidth = connect_bandwidth
        self.dry_run = dry_run
        self.region_id = region_id
        self.service_description = service_description
        self.service_id = service_id
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class UpdateVpcEndpointServiceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVpcEndpointServiceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateVpcEndpointServiceAttributeResponseBody = None,
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
            temp_model = UpdateVpcEndpointServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


