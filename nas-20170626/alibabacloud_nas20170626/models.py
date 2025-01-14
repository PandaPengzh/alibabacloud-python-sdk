# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddClientToBlackListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        file_system_id: str = None,
        client_ip: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.file_system_id = file_system_id
        self.client_ip = client_ip
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddClientToBlackListResponseBody(TeaModel):
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


class AddClientToBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddClientToBlackListResponseBody = None,
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
            temp_model = AddClientToBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTagsRequestTag(TeaModel):
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


class AddTagsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        tag: List[AddTagsRequestTag] = None,
    ):
        self.file_system_id = file_system_id
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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = AddTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class AddTagsResponseBody(TeaModel):
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


class AddTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddTagsResponseBody = None,
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
            temp_model = AddTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        file_system_ids: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.file_system_ids = file_system_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        return self


class ApplyAutoSnapshotPolicyResponseBody(TeaModel):
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


class ApplyAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyAutoSnapshotPolicyResponseBody = None,
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
            temp_model = ApplyAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_ids: str = None,
    ):
        self.file_system_ids = file_system_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        return self


class CancelAutoSnapshotPolicyResponseBody(TeaModel):
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


class CancelAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelAutoSnapshotPolicyResponseBody = None,
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
            temp_model = CancelAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDirQuotaRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
        user_type: str = None,
        user_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.path = path
        self.user_type = user_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CancelDirQuotaResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelDirQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelDirQuotaResponseBody = None,
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
            temp_model = CancelDirQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelLifecycleRetrieveJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CancelLifecycleRetrieveJobResponseBody(TeaModel):
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


class CancelLifecycleRetrieveJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelLifecycleRetrieveJobResponseBody = None,
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
            temp_model = CancelLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRecycleBinJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CancelRecycleBinJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class CancelRecycleBinJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelRecycleBinJobResponseBody = None,
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
            temp_model = CancelRecycleBinJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_group_type: str = None,
        description: str = None,
        file_system_type: str = None,
    ):
        self.access_group_name = access_group_name
        self.access_group_type = access_group_type
        self.description = description
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class CreateAccessGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        request_id: str = None,
    ):
        self.access_group_name = access_group_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccessGroupResponseBody = None,
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
            temp_model = CreateAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        source_cidr_ip: str = None,
        rwaccess_type: str = None,
        user_access_type: str = None,
        priority: int = None,
        file_system_type: str = None,
        ipv_6source_cidr_ip: str = None,
    ):
        self.access_group_name = access_group_name
        self.source_cidr_ip = source_cidr_ip
        self.rwaccess_type = rwaccess_type
        self.user_access_type = user_access_type
        self.priority = priority
        self.file_system_type = file_system_type
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.user_access_type is not None:
            result['UserAccessType'] = self.user_access_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('UserAccessType') is not None:
            self.user_access_type = m.get('UserAccessType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        return self


class CreateAccessRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_rule_id: str = None,
        request_id: str = None,
    ):
        self.access_rule_id = access_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccessRuleResponseBody = None,
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
            temp_model = CreateAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        repeat_weekdays: str = None,
        time_points: str = None,
        retention_days: int = None,
        auto_snapshot_policy_name: str = None,
        file_system_type: str = None,
    ):
        self.repeat_weekdays = repeat_weekdays
        self.time_points = time_points
        self.retention_days = retention_days
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class CreateAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        request_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAutoSnapshotPolicyResponseBody = None,
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
            temp_model = CreateAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_type: str = None,
        charge_type: str = None,
        duration: int = None,
        capacity: int = None,
        bandwidth: int = None,
        storage_type: str = None,
        zone_id: str = None,
        protocol_type: str = None,
        encrypt_type: int = None,
        snapshot_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        description: str = None,
        client_token: str = None,
        kms_key_id: str = None,
        dry_run: bool = None,
    ):
        self.file_system_type = file_system_type
        self.charge_type = charge_type
        self.duration = duration
        self.capacity = capacity
        self.bandwidth = bandwidth
        self.storage_type = storage_type
        self.zone_id = zone_id
        self.protocol_type = protocol_type
        self.encrypt_type = encrypt_type
        self.snapshot_id = snapshot_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.description = description
        self.client_token = client_token
        self.kms_key_id = kms_key_id
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.description is not None:
            result['Description'] = self.description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class CreateFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        file_system_id: str = None,
    ):
        self.request_id = request_id
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class CreateFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFileSystemResponseBody = None,
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
            temp_model = CreateFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLDAPConfigRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        uri: str = None,
        bind_dn: str = None,
        search_base: str = None,
    ):
        self.file_system_id = file_system_id
        self.uri = uri
        self.bind_dn = bind_dn
        self.search_base = search_base

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.uri is not None:
            result['URI'] = self.uri
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        return self


class CreateLDAPConfigResponseBody(TeaModel):
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


class CreateLDAPConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLDAPConfigResponseBody = None,
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
            temp_model = CreateLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecyclePolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
        path: str = None,
        lifecycle_rule_name: str = None,
        storage_type: str = None,
        paths: List[str] = None,
    ):
        self.file_system_id = file_system_id
        self.lifecycle_policy_name = lifecycle_policy_name
        self.path = path
        self.lifecycle_rule_name = lifecycle_rule_name
        self.storage_type = storage_type
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.path is not None:
            result['Path'] = self.path
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.paths is not None:
            result['Paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        return self


class CreateLifecyclePolicyResponseBody(TeaModel):
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


class CreateLifecyclePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLifecyclePolicyResponseBody = None,
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
            temp_model = CreateLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecycleRetrieveJobRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        paths: List[str] = None,
    ):
        self.file_system_id = file_system_id
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.paths is not None:
            result['Paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        return self


class CreateLifecycleRetrieveJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
    ):
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateLifecycleRetrieveJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLifecycleRetrieveJobResponseBody = None,
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
            temp_model = CreateLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMountTargetRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        access_group_name: str = None,
        network_type: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        security_group_id: str = None,
        enable_ipv_6: bool = None,
        dry_run: bool = None,
    ):
        self.file_system_id = file_system_id
        self.access_group_name = access_group_name
        self.network_type = network_type
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.security_group_id = security_group_id
        self.enable_ipv_6 = enable_ipv_6
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class CreateMountTargetResponseBodyMountTargetExtra(TeaModel):
    def __init__(
        self,
        dual_stack_mount_target_domain: str = None,
    ):
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        return self


class CreateMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mount_target_domain: str = None,
        mount_target_extra: CreateMountTargetResponseBodyMountTargetExtra = None,
    ):
        self.request_id = request_id
        self.mount_target_domain = mount_target_domain
        self.mount_target_extra = mount_target_extra

    def validate(self):
        if self.mount_target_extra:
            self.mount_target_extra.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.mount_target_extra is not None:
            result['MountTargetExtra'] = self.mount_target_extra.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('MountTargetExtra') is not None:
            temp_model = CreateMountTargetResponseBodyMountTargetExtra()
            self.mount_target_extra = temp_model.from_map(m['MountTargetExtra'])
        return self


class CreateMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMountTargetResponseBody = None,
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
            temp_model = CreateMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecycleBinDeleteJobRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_id: str = None,
        client_token: str = None,
    ):
        self.file_system_id = file_system_id
        self.file_id = file_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRecycleBinDeleteJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateRecycleBinDeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRecycleBinDeleteJobResponseBody = None,
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
            temp_model = CreateRecycleBinDeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecycleBinRestoreJobRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_id: str = None,
        target_file_id: str = None,
        client_token: str = None,
    ):
        self.file_system_id = file_system_id
        self.file_id = file_id
        self.target_file_id = target_file_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.target_file_id is not None:
            result['TargetFileId'] = self.target_file_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('TargetFileId') is not None:
            self.target_file_id = m.get('TargetFileId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRecycleBinRestoreJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateRecycleBinRestoreJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRecycleBinRestoreJobResponseBody = None,
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
            temp_model = CreateRecycleBinRestoreJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        snapshot_name: str = None,
        description: str = None,
        retention_days: int = None,
    ):
        self.file_system_id = file_system_id
        self.snapshot_name = snapshot_name
        self.description = description
        self.retention_days = retention_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
        request_id: str = None,
    ):
        self.snapshot_id = snapshot_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSnapshotResponseBody = None,
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
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        file_system_type: str = None,
    ):
        self.access_group_name = access_group_name
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DeleteAccessGroupResponseBody(TeaModel):
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


class DeleteAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccessGroupResponseBody = None,
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
            temp_model = DeleteAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        file_system_type: str = None,
    ):
        self.access_group_name = access_group_name
        self.access_rule_id = access_rule_id
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DeleteAccessRuleResponseBody(TeaModel):
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


class DeleteAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccessRuleResponseBody = None,
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
            temp_model = DeleteAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        return self


class DeleteAutoSnapshotPolicyResponseBody(TeaModel):
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


class DeleteAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAutoSnapshotPolicyResponseBody = None,
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
            temp_model = DeleteAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteFileSystemResponseBody(TeaModel):
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


class DeleteFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileSystemResponseBody = None,
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
            temp_model = DeleteFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLDAPConfigRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteLDAPConfigResponseBody(TeaModel):
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


class DeleteLDAPConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLDAPConfigResponseBody = None,
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
            temp_model = DeleteLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLifecyclePolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
    ):
        self.file_system_id = file_system_id
        self.lifecycle_policy_name = lifecycle_policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        return self


class DeleteLifecyclePolicyResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLifecyclePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLifecyclePolicyResponseBody = None,
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
            temp_model = DeleteLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMountTargetRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_target_domain: str = None,
    ):
        self.file_system_id = file_system_id
        self.mount_target_domain = mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        return self


class DeleteMountTargetResponseBody(TeaModel):
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


class DeleteMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMountTargetResponseBody = None,
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
            temp_model = DeleteMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
    ):
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
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


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSnapshotResponseBody = None,
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
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessGroupsRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        page_size: int = None,
        page_number: int = None,
        use_utcdate_time: bool = None,
        file_system_type: str = None,
    ):
        self.access_group_name = access_group_name
        self.page_size = page_size
        self.page_number = page_number
        self.use_utcdate_time = use_utcdate_time
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.use_utcdate_time is not None:
            result['UseUTCDateTime'] = self.use_utcdate_time
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UseUTCDateTime') is not None:
            self.use_utcdate_time = m.get('UseUTCDateTime')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        description: str = None,
        access_group_type: str = None,
        rule_count: int = None,
        mount_target_count: int = None,
    ):
        self.access_group_name = access_group_name
        self.description = description
        self.access_group_type = access_group_type
        self.rule_count = rule_count
        self.mount_target_count = mount_target_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        if self.mount_target_count is not None:
            result['MountTargetCount'] = self.mount_target_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        if m.get('MountTargetCount') is not None:
            self.mount_target_count = m.get('MountTargetCount')
        return self


class DescribeAccessGroupsResponseBodyAccessGroups(TeaModel):
    def __init__(
        self,
        access_group: List[DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup] = None,
    ):
        self.access_group = access_group

    def validate(self):
        if self.access_group:
            for k in self.access_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessGroup'] = []
        if self.access_group is not None:
            for k in self.access_group:
                result['AccessGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_group = []
        if m.get('AccessGroup') is not None:
            for k in m.get('AccessGroup'):
                temp_model = DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup()
                self.access_group.append(temp_model.from_map(k))
        return self


class DescribeAccessGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        access_groups: DescribeAccessGroupsResponseBodyAccessGroups = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.access_groups = access_groups

    def validate(self):
        if self.access_groups:
            self.access_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.access_groups is not None:
            result['AccessGroups'] = self.access_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('AccessGroups') is not None:
            temp_model = DescribeAccessGroupsResponseBodyAccessGroups()
            self.access_groups = temp_model.from_map(m['AccessGroups'])
        return self


class DescribeAccessGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccessGroupsResponseBody = None,
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
            temp_model = DescribeAccessGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessRulesRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        page_size: int = None,
        page_number: int = None,
        file_system_type: str = None,
    ):
        self.access_group_name = access_group_name
        self.access_rule_id = access_rule_id
        self.page_size = page_size
        self.page_number = page_number
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DescribeAccessRulesResponseBodyAccessRulesAccessRule(TeaModel):
    def __init__(
        self,
        access_rule_id: str = None,
        source_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        rwaccess: str = None,
        user_access: str = None,
        priority: int = None,
    ):
        self.access_rule_id = access_rule_id
        self.source_cidr_ip = source_cidr_ip
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        self.rwaccess = rwaccess
        self.user_access = user_access
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.rwaccess is not None:
            result['RWAccess'] = self.rwaccess
        if self.user_access is not None:
            result['UserAccess'] = self.user_access
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('RWAccess') is not None:
            self.rwaccess = m.get('RWAccess')
        if m.get('UserAccess') is not None:
            self.user_access = m.get('UserAccess')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class DescribeAccessRulesResponseBodyAccessRules(TeaModel):
    def __init__(
        self,
        access_rule: List[DescribeAccessRulesResponseBodyAccessRulesAccessRule] = None,
    ):
        self.access_rule = access_rule

    def validate(self):
        if self.access_rule:
            for k in self.access_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessRule'] = []
        if self.access_rule is not None:
            for k in self.access_rule:
                result['AccessRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_rule = []
        if m.get('AccessRule') is not None:
            for k in m.get('AccessRule'):
                temp_model = DescribeAccessRulesResponseBodyAccessRulesAccessRule()
                self.access_rule.append(temp_model.from_map(k))
        return self


class DescribeAccessRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        access_rules: DescribeAccessRulesResponseBodyAccessRules = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.access_rules = access_rules

    def validate(self):
        if self.access_rules:
            self.access_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.access_rules is not None:
            result['AccessRules'] = self.access_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('AccessRules') is not None:
            temp_model = DescribeAccessRulesResponseBodyAccessRules()
            self.access_rules = temp_model.from_map(m['AccessRules'])
        return self


class DescribeAccessRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccessRulesResponseBody = None,
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
            temp_model = DescribeAccessRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoSnapshotPoliciesRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        page_size: int = None,
        page_number: int = None,
        file_system_type: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.page_size = page_size
        self.page_number = page_number
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy(TeaModel):
    def __init__(
        self,
        time_points: str = None,
        status: str = None,
        repeat_weekdays: str = None,
        auto_snapshot_policy_name: str = None,
        create_time: str = None,
        auto_snapshot_policy_id: str = None,
        retention_days: int = None,
        file_system_nums: int = None,
        region_id: str = None,
    ):
        self.time_points = time_points
        self.status = status
        self.repeat_weekdays = repeat_weekdays
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        self.create_time = create_time
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.retention_days = retention_days
        self.file_system_nums = file_system_nums
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        if self.status is not None:
            result['Status'] = self.status
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.file_system_nums is not None:
            result['FileSystemNums'] = self.file_system_nums
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('FileSystemNums') is not None:
            self.file_system_nums = m.get('FileSystemNums')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy: List[DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy] = None,
    ):
        self.auto_snapshot_policy = auto_snapshot_policy

    def validate(self):
        if self.auto_snapshot_policy:
            for k in self.auto_snapshot_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoSnapshotPolicy'] = []
        if self.auto_snapshot_policy is not None:
            for k in self.auto_snapshot_policy:
                result['AutoSnapshotPolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_policy = []
        if m.get('AutoSnapshotPolicy') is not None:
            for k in m.get('AutoSnapshotPolicy'):
                temp_model = DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy()
                self.auto_snapshot_policy.append(temp_model.from_map(k))
        return self


class DescribeAutoSnapshotPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        auto_snapshot_policies: DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.auto_snapshot_policies = auto_snapshot_policies

    def validate(self):
        if self.auto_snapshot_policies:
            self.auto_snapshot_policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.auto_snapshot_policies is not None:
            result['AutoSnapshotPolicies'] = self.auto_snapshot_policies.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('AutoSnapshotPolicies') is not None:
            temp_model = DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies()
            self.auto_snapshot_policies = temp_model.from_map(m['AutoSnapshotPolicies'])
        return self


class DescribeAutoSnapshotPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutoSnapshotPoliciesResponseBody = None,
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
            temp_model = DescribeAutoSnapshotPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoSnapshotTasksRequest(TeaModel):
    def __init__(
        self,
        file_system_ids: str = None,
        auto_snapshot_policy_ids: str = None,
        file_system_type: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.file_system_ids = file_system_ids
        self.auto_snapshot_policy_ids = auto_snapshot_policy_ids
        self.file_system_type = file_system_type
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        if self.auto_snapshot_policy_ids is not None:
            result['AutoSnapshotPolicyIds'] = self.auto_snapshot_policy_ids
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        if m.get('AutoSnapshotPolicyIds') is not None:
            self.auto_snapshot_policy_ids = m.get('AutoSnapshotPolicyIds')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        source_file_system_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.source_file_system_id = source_file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')
        return self


class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks(TeaModel):
    def __init__(
        self,
        auto_snapshot_task: List[DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask] = None,
    ):
        self.auto_snapshot_task = auto_snapshot_task

    def validate(self):
        if self.auto_snapshot_task:
            for k in self.auto_snapshot_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoSnapshotTask'] = []
        if self.auto_snapshot_task is not None:
            for k in self.auto_snapshot_task:
                result['AutoSnapshotTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_task = []
        if m.get('AutoSnapshotTask') is not None:
            for k in m.get('AutoSnapshotTask'):
                temp_model = DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask()
                self.auto_snapshot_task.append(temp_model.from_map(k))
        return self


class DescribeAutoSnapshotTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        auto_snapshot_tasks: DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.auto_snapshot_tasks = auto_snapshot_tasks

    def validate(self):
        if self.auto_snapshot_tasks:
            self.auto_snapshot_tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.auto_snapshot_tasks is not None:
            result['AutoSnapshotTasks'] = self.auto_snapshot_tasks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('AutoSnapshotTasks') is not None:
            temp_model = DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks()
            self.auto_snapshot_tasks = temp_model.from_map(m['AutoSnapshotTasks'])
        return self


class DescribeAutoSnapshotTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutoSnapshotTasksResponseBody = None,
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
            temp_model = DescribeAutoSnapshotTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackListClientsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        file_system_id: str = None,
        client_ip: str = None,
    ):
        self.region_id = region_id
        self.file_system_id = file_system_id
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        return self


class DescribeBlackListClientsResponseBody(TeaModel):
    def __init__(
        self,
        clients: str = None,
        request_id: str = None,
    ):
        self.clients = clients
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clients is not None:
            result['Clients'] = self.clients
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clients') is not None:
            self.clients = m.get('Clients')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBlackListClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBlackListClientsResponseBody = None,
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
            temp_model = DescribeBlackListClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirQuotasRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.file_system_id = file_system_id
        self.path = path
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos(TeaModel):
    def __init__(
        self,
        file_count_real: int = None,
        user_type: str = None,
        file_count_limit: int = None,
        user_id: str = None,
        size_limit: int = None,
        quota_type: str = None,
        size_real: int = None,
    ):
        self.file_count_real = file_count_real
        self.user_type = user_type
        self.file_count_limit = file_count_limit
        self.user_id = user_id
        self.size_limit = size_limit
        self.quota_type = quota_type
        self.size_real = size_real

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count_real is not None:
            result['FileCountReal'] = self.file_count_real
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.size_real is not None:
            result['SizeReal'] = self.size_real
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountReal') is not None:
            self.file_count_real = m.get('FileCountReal')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('SizeReal') is not None:
            self.size_real = m.get('SizeReal')
        return self


class DescribeDirQuotasResponseBodyDirQuotaInfos(TeaModel):
    def __init__(
        self,
        path: str = None,
        status: str = None,
        dir_inode: str = None,
        user_quota_infos: List[DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos] = None,
    ):
        self.path = path
        self.status = status
        self.dir_inode = dir_inode
        self.user_quota_infos = user_quota_infos

    def validate(self):
        if self.user_quota_infos:
            for k in self.user_quota_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        if self.dir_inode is not None:
            result['DirInode'] = self.dir_inode
        result['UserQuotaInfos'] = []
        if self.user_quota_infos is not None:
            for k in self.user_quota_infos:
                result['UserQuotaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DirInode') is not None:
            self.dir_inode = m.get('DirInode')
        self.user_quota_infos = []
        if m.get('UserQuotaInfos') is not None:
            for k in m.get('UserQuotaInfos'):
                temp_model = DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos()
                self.user_quota_infos.append(temp_model.from_map(k))
        return self


class DescribeDirQuotasResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        dir_quota_infos: List[DescribeDirQuotasResponseBodyDirQuotaInfos] = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.dir_quota_infos = dir_quota_infos

    def validate(self):
        if self.dir_quota_infos:
            for k in self.dir_quota_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['DirQuotaInfos'] = []
        if self.dir_quota_infos is not None:
            for k in self.dir_quota_infos:
                result['DirQuotaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.dir_quota_infos = []
        if m.get('DirQuotaInfos') is not None:
            for k in m.get('DirQuotaInfos'):
                temp_model = DescribeDirQuotasResponseBodyDirQuotaInfos()
                self.dir_quota_infos.append(temp_model.from_map(k))
        return self


class DescribeDirQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDirQuotasResponseBody = None,
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
            temp_model = DescribeDirQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileSystemsRequestTag(TeaModel):
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


class DescribeFileSystemsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_type: str = None,
        vpc_id: str = None,
        page_size: int = None,
        page_number: int = None,
        tag: List[DescribeFileSystemsRequestTag] = None,
    ):
        self.file_system_id = file_system_id
        self.file_system_type = file_system_type
        self.vpc_id = vpc_id
        self.page_size = page_size
        self.page_number = page_number
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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFileSystemsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode(TeaModel):
    def __init__(
        self,
        ecs_ip: str = None,
        ecs_id: str = None,
        default_passwd: str = None,
    ):
        self.ecs_ip = ecs_ip
        self.ecs_id = ecs_id
        self.default_passwd = default_passwd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes(TeaModel):
    def __init__(
        self,
        client_master_node: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode] = None,
    ):
        self.client_master_node = client_master_node

    def validate(self):
        if self.client_master_node:
            for k in self.client_master_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k in self.client_master_node:
                result['ClientMasterNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k in m.get('ClientMasterNode'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag(TeaModel):
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


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        mount_target_domain: str = None,
        access_group_name: str = None,
        dual_stack_mount_target_domain: str = None,
        vsw_id: str = None,
        network_type: str = None,
        client_master_nodes: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes = None,
        tags: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.mount_target_domain = mount_target_domain
        self.access_group_name = access_group_name
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        self.vsw_id = vsw_id
        self.network_type = network_type
        self.client_master_nodes = client_master_nodes
        self.tags = tags

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ClientMasterNodes') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m['ClientMasterNodes'])
        if m.get('Tags') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets(TeaModel):
    def __init__(
        self,
        mount_target: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget] = None,
    ):
        self.mount_target = mount_target

    def validate(self):
        if self.mount_target:
            for k in self.mount_target:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k in self.mount_target:
                result['MountTarget'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k in m.get('MountTarget'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        package_id: str = None,
        expired_time: str = None,
        size: int = None,
        package_type: str = None,
    ):
        self.start_time = start_time
        self.package_id = package_id
        self.expired_time = expired_time
        self.size = size
        self.package_type = package_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.size is not None:
            result['Size'] = self.size
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages(TeaModel):
    def __init__(
        self,
        package: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag(TeaModel):
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


class DescribeFileSystemsResponseBodyFileSystemsFileSystemTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures(TeaModel):
    def __init__(
        self,
        supported_feature: List[str] = None,
    ):
        self.supported_feature = supported_feature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_feature is not None:
            result['SupportedFeature'] = self.supported_feature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedFeature') is not None:
            self.supported_feature = m.get('SupportedFeature')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap(TeaModel):
    def __init__(
        self,
        search_base: str = None,
        uri: str = None,
        bind_dn: str = None,
    ):
        self.search_base = search_base
        self.uri = uri
        self.bind_dn = bind_dn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystem(TeaModel):
    def __init__(
        self,
        status: str = None,
        capacity: int = None,
        metered_iasize: int = None,
        create_time: str = None,
        charge_type: str = None,
        storage_type: str = None,
        region_id: str = None,
        file_system_type: str = None,
        file_system_id: str = None,
        metered_size: int = None,
        encrypt_type: int = None,
        bandwidth: int = None,
        description: str = None,
        version: str = None,
        expired_time: str = None,
        zone_id: str = None,
        protocol_type: str = None,
        kmskey_id: str = None,
        mount_targets: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets = None,
        packages: DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages = None,
        tags: DescribeFileSystemsResponseBodyFileSystemsFileSystemTags = None,
        supported_features: DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures = None,
        ldap: DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap = None,
    ):
        self.status = status
        self.capacity = capacity
        self.metered_iasize = metered_iasize
        self.create_time = create_time
        self.charge_type = charge_type
        self.storage_type = storage_type
        self.region_id = region_id
        self.file_system_type = file_system_type
        self.file_system_id = file_system_id
        self.metered_size = metered_size
        self.encrypt_type = encrypt_type
        self.bandwidth = bandwidth
        self.description = description
        self.version = version
        self.expired_time = expired_time
        self.zone_id = zone_id
        self.protocol_type = protocol_type
        self.kmskey_id = kmskey_id
        self.mount_targets = mount_targets
        self.packages = packages
        self.tags = tags
        self.supported_features = supported_features
        self.ldap = ldap

    def validate(self):
        if self.mount_targets:
            self.mount_targets.validate()
        if self.packages:
            self.packages.validate()
        if self.tags:
            self.tags.validate()
        if self.supported_features:
            self.supported_features.validate()
        if self.ldap:
            self.ldap.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.version is not None:
            result['Version'] = self.version
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.supported_features is not None:
            result['SupportedFeatures'] = self.supported_features.to_map()
        if self.ldap is not None:
            result['Ldap'] = self.ldap.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('MountTargets') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets()
            self.mount_targets = temp_model.from_map(m['MountTargets'])
        if m.get('Packages') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m['Packages'])
        if m.get('Tags') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('SupportedFeatures') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures()
            self.supported_features = temp_model.from_map(m['SupportedFeatures'])
        if m.get('Ldap') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap()
            self.ldap = temp_model.from_map(m['Ldap'])
        return self


class DescribeFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(
        self,
        file_system: List[DescribeFileSystemsResponseBodyFileSystemsFileSystem] = None,
    ):
        self.file_system = file_system

    def validate(self):
        if self.file_system:
            for k in self.file_system:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystem'] = []
        if self.file_system is not None:
            for k in self.file_system:
                result['FileSystem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k in m.get('FileSystem'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        file_systems: DescribeFileSystemsResponseBodyFileSystems = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.file_systems = file_systems

    def validate(self):
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('FileSystems') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m['FileSystems'])
        return self


class DescribeFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFileSystemsResponseBody = None,
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
            temp_model = DescribeFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileSystemStatisticsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic(TeaModel):
    def __init__(
        self,
        expiring_count: int = None,
        file_system_type: str = None,
        metered_size: int = None,
        total_count: int = None,
        expired_count: int = None,
    ):
        self.expiring_count = expiring_count
        self.file_system_type = file_system_type
        self.metered_size = metered_size
        self.total_count = total_count
        self.expired_count = expired_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiring_count is not None:
            result['ExpiringCount'] = self.expiring_count
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiringCount') is not None:
            self.expiring_count = m.get('ExpiringCount')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemStatistics(TeaModel):
    def __init__(
        self,
        file_system_statistic: List[DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic] = None,
    ):
        self.file_system_statistic = file_system_statistic

    def validate(self):
        if self.file_system_statistic:
            for k in self.file_system_statistic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystemStatistic'] = []
        if self.file_system_statistic is not None:
            for k in self.file_system_statistic:
                result['FileSystemStatistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system_statistic = []
        if m.get('FileSystemStatistic') is not None:
            for k in m.get('FileSystemStatistic'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic()
                self.file_system_statistic.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        package_id: str = None,
        expired_time: str = None,
        size: int = None,
    ):
        self.start_time = start_time
        self.package_id = package_id
        self.expired_time = expired_time
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages(TeaModel):
    def __init__(
        self,
        package: List[DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem(TeaModel):
    def __init__(
        self,
        status: str = None,
        metered_iasize: int = None,
        capacity: int = None,
        create_time: str = None,
        charge_type: str = None,
        storage_type: str = None,
        region_id: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        metered_size: int = None,
        description: str = None,
        expired_time: str = None,
        zone_id: str = None,
        protocol_type: str = None,
        packages: DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages = None,
    ):
        self.status = status
        self.metered_iasize = metered_iasize
        self.capacity = capacity
        self.create_time = create_time
        self.charge_type = charge_type
        self.storage_type = storage_type
        self.region_id = region_id
        self.file_system_id = file_system_id
        self.file_system_type = file_system_type
        self.metered_size = metered_size
        self.description = description
        self.expired_time = expired_time
        self.zone_id = zone_id
        self.protocol_type = protocol_type
        self.packages = packages

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Packages') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m['Packages'])
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystems(TeaModel):
    def __init__(
        self,
        file_system: List[DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem] = None,
    ):
        self.file_system = file_system

    def validate(self):
        if self.file_system:
            for k in self.file_system:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystem'] = []
        if self.file_system is not None:
            for k in self.file_system:
                result['FileSystem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k in m.get('FileSystem'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        file_system_statistics: DescribeFileSystemStatisticsResponseBodyFileSystemStatistics = None,
        file_systems: DescribeFileSystemStatisticsResponseBodyFileSystems = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.file_system_statistics = file_system_statistics
        self.file_systems = file_systems

    def validate(self):
        if self.file_system_statistics:
            self.file_system_statistics.validate()
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.file_system_statistics is not None:
            result['FileSystemStatistics'] = self.file_system_statistics.to_map()
        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('FileSystemStatistics') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemStatistics()
            self.file_system_statistics = temp_model.from_map(m['FileSystemStatistics'])
        if m.get('FileSystems') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m['FileSystems'])
        return self


class DescribeFileSystemStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFileSystemStatisticsResponseBody = None,
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
            temp_model = DescribeFileSystemStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLDAPConfigRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeLDAPConfigResponseBodyLdap(TeaModel):
    def __init__(
        self,
        search_base: str = None,
        uri: str = None,
        bind_dn: str = None,
    ):
        self.search_base = search_base
        self.uri = uri
        self.bind_dn = bind_dn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        return self


class DescribeLDAPConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ldap: DescribeLDAPConfigResponseBodyLdap = None,
    ):
        self.request_id = request_id
        self.ldap = ldap

    def validate(self):
        if self.ldap:
            self.ldap.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ldap is not None:
            result['Ldap'] = self.ldap.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ldap') is not None:
            temp_model = DescribeLDAPConfigResponseBodyLdap()
            self.ldap = temp_model.from_map(m['Ldap'])
        return self


class DescribeLDAPConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLDAPConfigResponseBody = None,
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
            temp_model = DescribeLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLifecyclePoliciesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.file_system_id = file_system_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeLifecyclePoliciesResponseBodyLifecyclePolicies(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_rule_name: str = None,
        create_time: str = None,
        path: str = None,
        storage_type: str = None,
        lifecycle_policy_name: str = None,
        paths: List[str] = None,
    ):
        self.file_system_id = file_system_id
        self.lifecycle_rule_name = lifecycle_rule_name
        self.create_time = create_time
        self.path = path
        self.storage_type = storage_type
        self.lifecycle_policy_name = lifecycle_policy_name
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.path is not None:
            result['Path'] = self.path
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.paths is not None:
            result['Paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        return self


class DescribeLifecyclePoliciesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        lifecycle_policies: List[DescribeLifecyclePoliciesResponseBodyLifecyclePolicies] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.lifecycle_policies = lifecycle_policies

    def validate(self):
        if self.lifecycle_policies:
            for k in self.lifecycle_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['LifecyclePolicies'] = []
        if self.lifecycle_policies is not None:
            for k in self.lifecycle_policies:
                result['LifecyclePolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.lifecycle_policies = []
        if m.get('LifecyclePolicies') is not None:
            for k in m.get('LifecyclePolicies'):
                temp_model = DescribeLifecyclePoliciesResponseBodyLifecyclePolicies()
                self.lifecycle_policies.append(temp_model.from_map(k))
        return self


class DescribeLifecyclePoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLifecyclePoliciesResponseBody = None,
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
            temp_model = DescribeLifecyclePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogAnalysisRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        role_arn: str = None,
        project: str = None,
        region: str = None,
    ):
        self.logstore = logstore
        self.role_arn = role_arn
        self.project = project
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeLogAnalysisResponseBodyAnalysesAnalysis(TeaModel):
    def __init__(
        self,
        meta_key: str = None,
        meta_value: DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue = None,
    ):
        self.meta_key = meta_key
        self.meta_value = meta_value

    def validate(self):
        if self.meta_value:
            self.meta_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_key is not None:
            result['MetaKey'] = self.meta_key
        if self.meta_value is not None:
            result['MetaValue'] = self.meta_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaKey') is not None:
            self.meta_key = m.get('MetaKey')
        if m.get('MetaValue') is not None:
            temp_model = DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue()
            self.meta_value = temp_model.from_map(m['MetaValue'])
        return self


class DescribeLogAnalysisResponseBodyAnalyses(TeaModel):
    def __init__(
        self,
        analysis: List[DescribeLogAnalysisResponseBodyAnalysesAnalysis] = None,
    ):
        self.analysis = analysis

    def validate(self):
        if self.analysis:
            for k in self.analysis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Analysis'] = []
        if self.analysis is not None:
            for k in self.analysis:
                result['Analysis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis = []
        if m.get('Analysis') is not None:
            for k in m.get('Analysis'):
                temp_model = DescribeLogAnalysisResponseBodyAnalysesAnalysis()
                self.analysis.append(temp_model.from_map(k))
        return self


class DescribeLogAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        analyses: DescribeLogAnalysisResponseBodyAnalyses = None,
    ):
        self.code = code
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.analyses = analyses

    def validate(self):
        if self.analyses:
            self.analyses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.analyses is not None:
            result['Analyses'] = self.analyses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Analyses') is not None:
            temp_model = DescribeLogAnalysisResponseBodyAnalyses()
            self.analyses = temp_model.from_map(m['Analyses'])
        return self


class DescribeLogAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLogAnalysisResponseBody = None,
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
            temp_model = DescribeLogAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMountedClientsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        file_system_id: str = None,
        client_ip: str = None,
        mount_target_domain: str = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.file_system_id = file_system_id
        self.client_ip = client_ip
        self.mount_target_domain = mount_target_domain
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeMountedClientsResponseBodyClientsClient(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
    ):
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        return self


class DescribeMountedClientsResponseBodyClients(TeaModel):
    def __init__(
        self,
        client: List[DescribeMountedClientsResponseBodyClientsClient] = None,
    ):
        self.client = client

    def validate(self):
        if self.client:
            for k in self.client:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Client'] = []
        if self.client is not None:
            for k in self.client:
                result['Client'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client = []
        if m.get('Client') is not None:
            for k in m.get('Client'):
                temp_model = DescribeMountedClientsResponseBodyClientsClient()
                self.client.append(temp_model.from_map(k))
        return self


class DescribeMountedClientsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        clients: DescribeMountedClientsResponseBodyClients = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.clients = clients

    def validate(self):
        if self.clients:
            self.clients.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.clients is not None:
            result['Clients'] = self.clients.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Clients') is not None:
            temp_model = DescribeMountedClientsResponseBodyClients()
            self.clients = temp_model.from_map(m['Clients'])
        return self


class DescribeMountedClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMountedClientsResponseBody = None,
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
            temp_model = DescribeMountedClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMountTargetsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_target_domain: str = None,
        page_size: int = None,
        page_number: int = None,
        dual_stack_mount_target_domain: str = None,
    ):
        self.file_system_id = file_system_id
        self.mount_target_domain = mount_target_domain
        self.page_size = page_size
        self.page_number = page_number
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode(TeaModel):
    def __init__(
        self,
        ecs_ip: str = None,
        ecs_id: str = None,
        default_passwd: str = None,
    ):
        self.ecs_ip = ecs_ip
        self.ecs_id = ecs_id
        self.default_passwd = default_passwd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes(TeaModel):
    def __init__(
        self,
        client_master_node: List[DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode] = None,
    ):
        self.client_master_node = client_master_node

    def validate(self):
        if self.client_master_node:
            for k in self.client_master_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k in self.client_master_node:
                result['ClientMasterNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k in m.get('ClientMasterNode'):
                temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k))
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTarget(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        mount_target_domain: str = None,
        access_group: str = None,
        dual_stack_mount_target_domain: str = None,
        vsw_id: str = None,
        network_type: str = None,
        client_master_nodes: DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.mount_target_domain = mount_target_domain
        self.access_group = access_group
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        self.vsw_id = vsw_id
        self.network_type = network_type
        self.client_master_nodes = client_master_nodes

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ClientMasterNodes') is not None:
            temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m['ClientMasterNodes'])
        return self


class DescribeMountTargetsResponseBodyMountTargets(TeaModel):
    def __init__(
        self,
        mount_target: List[DescribeMountTargetsResponseBodyMountTargetsMountTarget] = None,
    ):
        self.mount_target = mount_target

    def validate(self):
        if self.mount_target:
            for k in self.mount_target:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k in self.mount_target:
                result['MountTarget'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k in m.get('MountTarget'):
                temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k))
        return self


class DescribeMountTargetsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        mount_targets: DescribeMountTargetsResponseBodyMountTargets = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.mount_targets = mount_targets

    def validate(self):
        if self.mount_targets:
            self.mount_targets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MountTargets') is not None:
            temp_model = DescribeMountTargetsResponseBodyMountTargets()
            self.mount_targets = temp_model.from_map(m['MountTargets'])
        return self


class DescribeMountTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMountTargetsResponseBody = None,
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
            temp_model = DescribeMountTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        file_system_type: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        self.region_endpoint = region_endpoint
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
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
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
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


class DescribeSnapshotsRequest(TeaModel):
    def __init__(
        self,
        file_system_type: str = None,
        file_system_id: str = None,
        snapshot_ids: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        status: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.file_system_type = file_system_type
        self.file_system_id = file_system_id
        self.snapshot_ids = snapshot_ids
        self.snapshot_name = snapshot_name
        self.snapshot_type = snapshot_type
        self.status = status
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeSnapshotsResponseBodySnapshotsSnapshot(TeaModel):
    def __init__(
        self,
        status: str = None,
        progress: str = None,
        create_time: str = None,
        source_file_system_id: str = None,
        remain_time: int = None,
        retention_days: int = None,
        source_file_system_size: int = None,
        snapshot_name: str = None,
        source_file_system_version: str = None,
        encrypt_type: int = None,
        description: str = None,
        snapshot_id: str = None,
    ):
        self.status = status
        self.progress = progress
        self.create_time = create_time
        self.source_file_system_id = source_file_system_id
        self.remain_time = remain_time
        self.retention_days = retention_days
        self.source_file_system_size = source_file_system_size
        self.snapshot_name = snapshot_name
        self.source_file_system_version = source_file_system_version
        self.encrypt_type = encrypt_type
        self.description = description
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.source_file_system_size is not None:
            result['SourceFileSystemSize'] = self.source_file_system_size
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.source_file_system_version is not None:
            result['SourceFileSystemVersion'] = self.source_file_system_version
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SourceFileSystemSize') is not None:
            self.source_file_system_size = m.get('SourceFileSystemSize')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SourceFileSystemVersion') is not None:
            self.source_file_system_version = m.get('SourceFileSystemVersion')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        snapshot: List[DescribeSnapshotsResponseBodySnapshotsSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for k in self.snapshot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k in self.snapshot:
                result['Snapshot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k in m.get('Snapshot'):
                temp_model = DescribeSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        snapshots: DescribeSnapshotsResponseBodySnapshots = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.snapshots = snapshots

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Snapshots') is not None:
            temp_model = DescribeSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSnapshotsResponseBody = None,
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
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoragePackagesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        use_utcdate_time: bool = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.use_utcdate_time = use_utcdate_time
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.use_utcdate_time is not None:
            result['UseUTCDateTime'] = self.use_utcdate_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UseUTCDateTime') is not None:
            self.use_utcdate_time = m.get('UseUTCDateTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeStoragePackagesResponseBodyPackagesPackage(TeaModel):
    def __init__(
        self,
        status: str = None,
        file_system_id: str = None,
        start_time: str = None,
        expired_time: str = None,
        size: int = None,
        storage_type: str = None,
        package_id: str = None,
    ):
        self.status = status
        self.file_system_id = file_system_id
        self.start_time = start_time
        self.expired_time = expired_time
        self.size = size
        self.storage_type = storage_type
        self.package_id = package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        return self


class DescribeStoragePackagesResponseBodyPackages(TeaModel):
    def __init__(
        self,
        package: List[DescribeStoragePackagesResponseBodyPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeStoragePackagesResponseBodyPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeStoragePackagesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        packages: DescribeStoragePackagesResponseBodyPackages = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.packages = packages

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Packages') is not None:
            temp_model = DescribeStoragePackagesResponseBodyPackages()
            self.packages = temp_model.from_map(m['Packages'])
        return self


class DescribeStoragePackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStoragePackagesResponseBody = None,
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
            temp_model = DescribeStoragePackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequestTag(TeaModel):
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


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        page_size: int = None,
        page_number: int = None,
        tag: List[DescribeTagsRequestTag] = None,
    ):
        self.file_system_id = file_system_id
        self.page_size = page_size
        self.page_number = page_number
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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagsResponseBodyTagsTagFileSystemIds(TeaModel):
    def __init__(
        self,
        file_system_id: List[str] = None,
    ):
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeTagsResponseBodyTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        file_system_ids: DescribeTagsResponseBodyTagsTagFileSystemIds = None,
    ):
        self.key = key
        self.value = value
        self.file_system_ids = file_system_ids

    def validate(self):
        if self.file_system_ids:
            self.file_system_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('FileSystemIds') is not None:
            temp_model = DescribeTagsResponseBodyTagsTagFileSystemIds()
            self.file_system_ids = temp_model.from_map(m['FileSystemIds'])
        return self


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeTagsResponseBodyTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        tags: DescribeTagsResponseBodyTags = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tags') is not None:
            temp_model = DescribeTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagsResponseBody = None,
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
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        file_system_type: str = None,
    ):
        self.region_id = region_id
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DescribeZonesResponseBodyZonesZonePerformance(TeaModel):
    def __init__(
        self,
        protocol: List[str] = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeZonesResponseBodyZonesZoneCapacity(TeaModel):
    def __init__(
        self,
        protocol: List[str] = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType(TeaModel):
    def __init__(
        self,
        storage_type: str = None,
        protocol_type: str = None,
    ):
        self.storage_type = storage_type
        self.protocol_type = protocol_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        return self


class DescribeZonesResponseBodyZonesZoneInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type: List[DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for k in self.instance_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k in self.instance_type:
                result['InstanceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k in m.get('InstanceType'):
                temp_model = DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        performance: DescribeZonesResponseBodyZonesZonePerformance = None,
        capacity: DescribeZonesResponseBodyZonesZoneCapacity = None,
        zone_id: str = None,
        instance_types: DescribeZonesResponseBodyZonesZoneInstanceTypes = None,
    ):
        self.performance = performance
        self.capacity = capacity
        self.zone_id = zone_id
        self.instance_types = instance_types

    def validate(self):
        if self.performance:
            self.performance.validate()
        if self.capacity:
            self.capacity.validate()
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.capacity is not None:
            result['Capacity'] = self.capacity.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Performance') is not None:
            temp_model = DescribeZonesResponseBodyZonesZonePerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('Capacity') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneCapacity()
            self.capacity = temp_model.from_map(m['Capacity'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
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


class DisableAndCleanRecycleBinRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DisableAndCleanRecycleBinResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DisableAndCleanRecycleBinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableAndCleanRecycleBinResponseBody = None,
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
            temp_model = DisableAndCleanRecycleBinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRecycleBinRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        reserved_days: int = None,
    ):
        self.file_system_id = file_system_id
        self.reserved_days = reserved_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        return self


class EnableRecycleBinResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class EnableRecycleBinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableRecycleBinResponseBody = None,
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
            temp_model = EnableRecycleBinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectoryOrFilePropertiesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
    ):
        self.file_system_id = file_system_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetDirectoryOrFilePropertiesResponseBodyEntry(TeaModel):
    def __init__(
        self,
        type: str = None,
        has_infrequent_access_file: bool = None,
        mtime: str = None,
        atime: str = None,
        size: int = None,
        ctime: str = None,
        storage_type: str = None,
        name: str = None,
        retrieve_time: str = None,
        inode: str = None,
    ):
        self.type = type
        self.has_infrequent_access_file = has_infrequent_access_file
        self.mtime = mtime
        self.atime = atime
        self.size = size
        self.ctime = ctime
        self.storage_type = storage_type
        self.name = name
        self.retrieve_time = retrieve_time
        self.inode = inode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file
        if self.mtime is not None:
            result['MTime'] = self.mtime
        if self.atime is not None:
            result['ATime'] = self.atime
        if self.size is not None:
            result['Size'] = self.size
        if self.ctime is not None:
            result['CTime'] = self.ctime
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.name is not None:
            result['Name'] = self.name
        if self.retrieve_time is not None:
            result['RetrieveTime'] = self.retrieve_time
        if self.inode is not None:
            result['Inode'] = self.inode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')
        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        return self


class GetDirectoryOrFilePropertiesResponseBody(TeaModel):
    def __init__(
        self,
        entry: GetDirectoryOrFilePropertiesResponseBodyEntry = None,
        request_id: str = None,
    ):
        self.entry = entry
        self.request_id = request_id

    def validate(self):
        if self.entry:
            self.entry.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            temp_model = GetDirectoryOrFilePropertiesResponseBodyEntry()
            self.entry = temp_model.from_map(m['Entry'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDirectoryOrFilePropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDirectoryOrFilePropertiesResponseBody = None,
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
            temp_model = GetDirectoryOrFilePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecycleBinAttributeRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class GetRecycleBinAttributeResponseBodyRecycleBinAttribute(TeaModel):
    def __init__(
        self,
        size: int = None,
        status: str = None,
        reserved_days: int = None,
        enable_time: str = None,
    ):
        self.size = size
        self.status = status
        self.reserved_days = reserved_days
        self.enable_time = enable_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        return self


class GetRecycleBinAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        recycle_bin_attribute: GetRecycleBinAttributeResponseBodyRecycleBinAttribute = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.recycle_bin_attribute = recycle_bin_attribute

    def validate(self):
        if self.recycle_bin_attribute:
            self.recycle_bin_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.recycle_bin_attribute is not None:
            result['RecycleBinAttribute'] = self.recycle_bin_attribute.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecycleBinAttribute') is not None:
            temp_model = GetRecycleBinAttributeResponseBodyRecycleBinAttribute()
            self.recycle_bin_attribute = temp_model.from_map(m['RecycleBinAttribute'])
        return self


class GetRecycleBinAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRecycleBinAttributeResponseBody = None,
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
            temp_model = GetRecycleBinAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoriesAndFilesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
        next_token: str = None,
        storage_type: str = None,
        directory_only: bool = None,
        max_results: int = None,
    ):
        self.file_system_id = file_system_id
        self.path = path
        self.next_token = next_token
        self.storage_type = storage_type
        self.directory_only = directory_only
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.directory_only is not None:
            result['DirectoryOnly'] = self.directory_only
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('DirectoryOnly') is not None:
            self.directory_only = m.get('DirectoryOnly')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDirectoriesAndFilesResponseBodyEntries(TeaModel):
    def __init__(
        self,
        type: str = None,
        has_infrequent_access_file: bool = None,
        ctime: str = None,
        mtime: str = None,
        size: int = None,
        storage_type: str = None,
        atime: str = None,
        name: str = None,
        retrieve_time: str = None,
        inode: str = None,
        file_id: str = None,
    ):
        self.type = type
        self.has_infrequent_access_file = has_infrequent_access_file
        self.ctime = ctime
        self.mtime = mtime
        self.size = size
        self.storage_type = storage_type
        self.atime = atime
        self.name = name
        self.retrieve_time = retrieve_time
        self.inode = inode
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.atime is not None:
            result['Atime'] = self.atime
        if self.name is not None:
            result['Name'] = self.name
        if self.retrieve_time is not None:
            result['RetrieveTime'] = self.retrieve_time
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Atime') is not None:
            self.atime = m.get('Atime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class ListDirectoriesAndFilesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        entries: List[ListDirectoriesAndFilesResponseBodyEntries] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.entries = entries

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        return self


class ListDirectoriesAndFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDirectoriesAndFilesResponseBody = None,
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
            temp_model = ListDirectoriesAndFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLifecycleRetrieveJobsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        file_system_id: str = None,
        status: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.file_system_id = file_system_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        status: str = None,
        discovered_file_count: int = None,
        update_time: str = None,
        paths: List[str] = None,
        retrieved_file_count: int = None,
        job_id: str = None,
        create_time: str = None,
    ):
        self.file_system_id = file_system_id
        self.status = status
        self.discovered_file_count = discovered_file_count
        self.update_time = update_time
        self.paths = paths
        self.retrieved_file_count = retrieved_file_count
        self.job_id = job_id
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.status is not None:
            result['Status'] = self.status
        if self.discovered_file_count is not None:
            result['DiscoveredFileCount'] = self.discovered_file_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.retrieved_file_count is not None:
            result['RetrievedFileCount'] = self.retrieved_file_count
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DiscoveredFileCount') is not None:
            self.discovered_file_count = m.get('DiscoveredFileCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('RetrievedFileCount') is not None:
            self.retrieved_file_count = m.get('RetrievedFileCount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListLifecycleRetrieveJobsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        lifecycle_retrieve_jobs: List[ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.lifecycle_retrieve_jobs = lifecycle_retrieve_jobs

    def validate(self):
        if self.lifecycle_retrieve_jobs:
            for k in self.lifecycle_retrieve_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['LifecycleRetrieveJobs'] = []
        if self.lifecycle_retrieve_jobs is not None:
            for k in self.lifecycle_retrieve_jobs:
                result['LifecycleRetrieveJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.lifecycle_retrieve_jobs = []
        if m.get('LifecycleRetrieveJobs') is not None:
            for k in m.get('LifecycleRetrieveJobs'):
                temp_model = ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs()
                self.lifecycle_retrieve_jobs.append(temp_model.from_map(k))
        return self


class ListLifecycleRetrieveJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLifecycleRetrieveJobsResponseBody = None,
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
            temp_model = ListLifecycleRetrieveJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecentlyRecycledDirectoriesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.file_system_id = file_system_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListRecentlyRecycledDirectoriesResponseBodyEntries(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        path: str = None,
        name: str = None,
        last_delete_time: str = None,
    ):
        self.file_id = file_id
        self.path = path
        self.name = name
        self.last_delete_time = last_delete_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.path is not None:
            result['Path'] = self.path
        if self.name is not None:
            result['Name'] = self.name
        if self.last_delete_time is not None:
            result['LastDeleteTime'] = self.last_delete_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LastDeleteTime') is not None:
            self.last_delete_time = m.get('LastDeleteTime')
        return self


class ListRecentlyRecycledDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        entries: List[ListRecentlyRecycledDirectoriesResponseBodyEntries] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # Id of the request
        self.next_token = next_token
        self.entries = entries

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListRecentlyRecycledDirectoriesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        return self


class ListRecentlyRecycledDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRecentlyRecycledDirectoriesResponseBody = None,
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
            temp_model = ListRecentlyRecycledDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecycleBinJobsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        job_id: str = None,
        page_size: int = None,
        page_number: int = None,
        status: str = None,
    ):
        self.file_system_id = file_system_id
        self.job_id = job_id
        self.page_size = page_size
        self.page_number = page_number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRecycleBinJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
        file_id: str = None,
        status: str = None,
        error_code: str = None,
        progress: str = None,
        create_time: str = None,
        file_name: str = None,
        error_message: str = None,
    ):
        self.id = id
        self.type = type
        self.file_id = file_id
        self.status = status
        self.error_code = error_code
        self.progress = progress
        self.create_time = create_time
        self.file_name = file_name
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.status is not None:
            result['Status'] = self.status
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class ListRecycleBinJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        jobs: List[ListRecycleBinJobsResponseBodyJobs] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.jobs = jobs

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListRecycleBinJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        return self


class ListRecycleBinJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRecycleBinJobsResponseBody = None,
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
            temp_model = ListRecycleBinJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecycledDirectoriesAndFilesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_id: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.file_system_id = file_system_id
        self.file_id = file_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListRecycledDirectoriesAndFilesResponseBodyEntries(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        type: str = None,
        name: str = None,
        delete_time: str = None,
        inode: str = None,
        atime: str = None,
        mtime: str = None,
        ctime: str = None,
        size: int = None,
    ):
        self.file_id = file_id
        self.type = type
        self.name = name
        self.delete_time = delete_time
        self.inode = inode
        self.atime = atime
        self.mtime = mtime
        self.ctime = ctime
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.atime is not None:
            result['ATime'] = self.atime
        if self.mtime is not None:
            result['MTime'] = self.mtime
        if self.ctime is not None:
            result['CTime'] = self.ctime
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')
        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')
        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListRecycledDirectoriesAndFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        entries: List[ListRecycledDirectoriesAndFilesResponseBodyEntries] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # Id of the request
        self.next_token = next_token
        self.entries = entries

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListRecycledDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        return self


class ListRecycledDirectoriesAndFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRecycledDirectoriesAndFilesResponseBody = None,
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
            temp_model = ListRecycledDirectoriesAndFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
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


class ModifyAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        description: str = None,
        file_system_type: str = None,
    ):
        self.access_group_name = access_group_name
        self.description = description
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class ModifyAccessGroupResponseBody(TeaModel):
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


class ModifyAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccessGroupResponseBody = None,
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
            temp_model = ModifyAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        source_cidr_ip: str = None,
        rwaccess_type: str = None,
        user_access_type: str = None,
        priority: int = None,
        file_system_type: str = None,
        ipv_6source_cidr_ip: str = None,
    ):
        self.access_group_name = access_group_name
        self.access_rule_id = access_rule_id
        self.source_cidr_ip = source_cidr_ip
        self.rwaccess_type = rwaccess_type
        self.user_access_type = user_access_type
        self.priority = priority
        self.file_system_type = file_system_type
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.user_access_type is not None:
            result['UserAccessType'] = self.user_access_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('UserAccessType') is not None:
            self.user_access_type = m.get('UserAccessType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        return self


class ModifyAccessRuleResponseBody(TeaModel):
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


class ModifyAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccessRuleResponseBody = None,
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
            temp_model = ModifyAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        self.repeat_weekdays = repeat_weekdays
        self.retention_days = retention_days
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class ModifyAutoSnapshotPolicyResponseBody(TeaModel):
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


class ModifyAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAutoSnapshotPolicyResponseBody = None,
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
            temp_model = ModifyAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        description: str = None,
    ):
        self.file_system_id = file_system_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyFileSystemResponseBody(TeaModel):
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


class ModifyFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFileSystemResponseBody = None,
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
            temp_model = ModifyFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLDAPConfigRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        uri: str = None,
        bind_dn: str = None,
        search_base: str = None,
    ):
        self.file_system_id = file_system_id
        self.uri = uri
        self.bind_dn = bind_dn
        self.search_base = search_base

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.uri is not None:
            result['URI'] = self.uri
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        return self


class ModifyLDAPConfigResponseBody(TeaModel):
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


class ModifyLDAPConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLDAPConfigResponseBody = None,
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
            temp_model = ModifyLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLifecyclePolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
        path: str = None,
        lifecycle_rule_name: str = None,
        storage_type: str = None,
    ):
        self.file_system_id = file_system_id
        self.lifecycle_policy_name = lifecycle_policy_name
        self.path = path
        self.lifecycle_rule_name = lifecycle_rule_name
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.path is not None:
            result['Path'] = self.path
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class ModifyLifecyclePolicyResponseBody(TeaModel):
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


class ModifyLifecyclePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLifecyclePolicyResponseBody = None,
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
            temp_model = ModifyLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMountTargetRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_target_domain: str = None,
        access_group_name: str = None,
        status: str = None,
        dual_stack_mount_target_domain: str = None,
    ):
        self.file_system_id = file_system_id
        self.mount_target_domain = mount_target_domain
        self.access_group_name = access_group_name
        self.status = status
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.status is not None:
            result['Status'] = self.status
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        return self


class ModifyMountTargetResponseBody(TeaModel):
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


class ModifyMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyMountTargetResponseBody = None,
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
            temp_model = ModifyMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenNASServiceResponseBody(TeaModel):
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


class OpenNASServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenNASServiceResponseBody = None,
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
            temp_model = OpenNASServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClientFromBlackListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        file_system_id: str = None,
        client_ip: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.file_system_id = file_system_id
        self.client_ip = client_ip
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RemoveClientFromBlackListResponseBody(TeaModel):
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


class RemoveClientFromBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveClientFromBlackListResponseBody = None,
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
            temp_model = RemoveClientFromBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTagsRequestTag(TeaModel):
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


class RemoveTagsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        tag: List[RemoveTagsRequestTag] = None,
    ):
        self.file_system_id = file_system_id
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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = RemoveTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class RemoveTagsResponseBody(TeaModel):
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


class RemoveTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveTagsResponseBody = None,
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
            temp_model = RemoveTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        snapshot_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetFileSystemResponseBody(TeaModel):
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


class ResetFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetFileSystemResponseBody = None,
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
            temp_model = ResetFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryLifecycleRetrieveJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class RetryLifecycleRetrieveJobResponseBody(TeaModel):
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


class RetryLifecycleRetrieveJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryLifecycleRetrieveJobResponseBody = None,
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
            temp_model = RetryLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDirQuotaRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
        quota_type: str = None,
        user_type: str = None,
        user_id: str = None,
        size_limit: int = None,
        file_count_limit: int = None,
    ):
        self.file_system_id = file_system_id
        self.path = path
        self.quota_type = quota_type
        self.user_type = user_type
        self.user_id = user_id
        self.size_limit = size_limit
        self.file_count_limit = file_count_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        return self


class SetDirQuotaResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDirQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDirQuotaResponseBody = None,
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
            temp_model = SetDirQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UpdateRecycleBinAttributeRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        reserved_days: int = None,
    ):
        self.file_system_id = file_system_id
        self.reserved_days = reserved_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        return self


class UpdateRecycleBinAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateRecycleBinAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRecycleBinAttributeResponseBody = None,
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
            temp_model = UpdateRecycleBinAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        capacity: int = None,
        dry_run: bool = None,
        client_token: str = None,
    ):
        self.file_system_id = file_system_id
        self.capacity = capacity
        self.dry_run = dry_run
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpgradeFileSystemResponseBody(TeaModel):
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


class UpgradeFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeFileSystemResponseBody = None,
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
            temp_model = UpgradeFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


