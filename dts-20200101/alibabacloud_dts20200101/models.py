# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ConfigureDtsJobRequest(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        db_list: str = None,
        delay_notice: bool = None,
        delay_phone: str = None,
        delay_rule_time: int = None,
        destination_endpoint_data_base_name: str = None,
        destination_endpoint_engine_name: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_port: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_user_name: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        error_notice: bool = None,
        error_phone: str = None,
        job_type: str = None,
        owner_id: str = None,
        region_id: str = None,
        reserve: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_owner_id: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_role: str = None,
        source_endpoint_user_name: str = None,
        structure_initialization: bool = None,
        synchronization_direction: str = None,
    ):
        self.checkpoint = checkpoint
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.db_list = db_list
        self.delay_notice = delay_notice
        self.delay_phone = delay_phone
        self.delay_rule_time = delay_rule_time
        self.destination_endpoint_data_base_name = destination_endpoint_data_base_name
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        self.destination_endpoint_ip = destination_endpoint_ip
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        self.destination_endpoint_password = destination_endpoint_password
        self.destination_endpoint_port = destination_endpoint_port
        self.destination_endpoint_region = destination_endpoint_region
        self.destination_endpoint_user_name = destination_endpoint_user_name
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.error_notice = error_notice
        self.error_phone = error_phone
        self.job_type = job_type
        self.owner_id = owner_id
        self.region_id = region_id
        self.reserve = reserve
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.source_endpoint_owner_id = source_endpoint_owner_id
        self.source_endpoint_password = source_endpoint_password
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_role = source_endpoint_role
        self.source_endpoint_user_name = source_endpoint_user_name
        self.structure_initialization = structure_initialization
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.delay_notice is not None:
            result['DelayNotice'] = self.delay_notice
        if self.delay_phone is not None:
            result['DelayPhone'] = self.delay_phone
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.destination_endpoint_data_base_name is not None:
            result['DestinationEndpointDataBaseName'] = self.destination_endpoint_data_base_name
        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name
        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password
        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.error_notice is not None:
            result['ErrorNotice'] = self.error_notice
        if self.error_phone is not None:
            result['ErrorPhone'] = self.error_phone
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserve is not None:
            result['Reserve'] = self.reserve
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.source_endpoint_owner_id is not None:
            result['SourceEndpointOwnerID'] = self.source_endpoint_owner_id
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_role is not None:
            result['SourceEndpointRole'] = self.source_endpoint_role
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('DelayNotice') is not None:
            self.delay_notice = m.get('DelayNotice')
        if m.get('DelayPhone') is not None:
            self.delay_phone = m.get('DelayPhone')
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('DestinationEndpointDataBaseName') is not None:
            self.destination_endpoint_data_base_name = m.get('DestinationEndpointDataBaseName')
        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')
        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')
        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('ErrorNotice') is not None:
            self.error_notice = m.get('ErrorNotice')
        if m.get('ErrorPhone') is not None:
            self.error_phone = m.get('ErrorPhone')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reserve') is not None:
            self.reserve = m.get('Reserve')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('SourceEndpointOwnerID') is not None:
            self.source_endpoint_owner_id = m.get('SourceEndpointOwnerID')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointRole') is not None:
            self.source_endpoint_role = m.get('SourceEndpointRole')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class ConfigureDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureDtsJobResponseBody = None,
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
            temp_model = ConfigureDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureMigrationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        data_base_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        user_name: str = None,
    ):
        self.data_base_name = data_base_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.password = password
        self.port = port
        self.region = region
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureMigrationJobRequestMigrationMode(TeaModel):
    def __init__(
        self,
        data_intialization: bool = None,
        data_synchronization: bool = None,
        structure_intialization: bool = None,
    ):
        self.data_intialization = data_intialization
        self.data_synchronization = data_synchronization
        self.structure_intialization = structure_intialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_intialization is not None:
            result['DataIntialization'] = self.data_intialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_intialization is not None:
            result['StructureIntialization'] = self.structure_intialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIntialization') is not None:
            self.data_intialization = m.get('DataIntialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureIntialization') is not None:
            self.structure_intialization = m.get('StructureIntialization')
        return self


class ConfigureMigrationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        role: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.owner_id = owner_id
        self.password = password
        self.port = port
        self.region = region
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureMigrationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: ConfigureMigrationJobRequestDestinationEndpoint = None,
        migration_mode: ConfigureMigrationJobRequestMigrationMode = None,
        source_endpoint: ConfigureMigrationJobRequestSourceEndpoint = None,
        account_id: str = None,
        checkpoint: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_object: str = None,
        migration_reserved: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.source_endpoint = source_endpoint
        self.account_id = account_id
        self.checkpoint = checkpoint
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_object = migration_object
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigureMigrationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = ConfigureMigrationJobRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureMigrationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigureMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureMigrationJobResponseBody = None,
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
            temp_model = ConfigureMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureMigrationJobAlertRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.delay_alert_phone = delay_alert_phone
        self.delay_alert_status = delay_alert_status
        self.delay_over_seconds = delay_over_seconds
        self.error_alert_phone = error_alert_phone
        self.error_alert_status = error_alert_status
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigureMigrationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureMigrationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureMigrationJobAlertResponseBody = None,
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
            temp_model = ConfigureMigrationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSubscriptionRequest(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        db_list: str = None,
        delay_notice: bool = None,
        delay_phone: str = None,
        delay_rule_time: int = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        error_notice: bool = None,
        error_phone: str = None,
        region_id: str = None,
        reserve: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_owner_id: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_role: str = None,
        source_endpoint_user_name: str = None,
        subscription_data_type_ddl: bool = None,
        subscription_data_type_dml: bool = None,
        subscription_instance_network_type: str = None,
        subscription_instance_vpcid: str = None,
        subscription_instance_vswitch_id: str = None,
    ):
        self.checkpoint = checkpoint
        self.db_list = db_list
        self.delay_notice = delay_notice
        self.delay_phone = delay_phone
        self.delay_rule_time = delay_rule_time
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.error_notice = error_notice
        self.error_phone = error_phone
        self.region_id = region_id
        self.reserve = reserve
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.source_endpoint_owner_id = source_endpoint_owner_id
        self.source_endpoint_password = source_endpoint_password
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_role = source_endpoint_role
        self.source_endpoint_user_name = source_endpoint_user_name
        self.subscription_data_type_ddl = subscription_data_type_ddl
        self.subscription_data_type_dml = subscription_data_type_dml
        self.subscription_instance_network_type = subscription_instance_network_type
        self.subscription_instance_vpcid = subscription_instance_vpcid
        self.subscription_instance_vswitch_id = subscription_instance_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.delay_notice is not None:
            result['DelayNotice'] = self.delay_notice
        if self.delay_phone is not None:
            result['DelayPhone'] = self.delay_phone
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.error_notice is not None:
            result['ErrorNotice'] = self.error_notice
        if self.error_phone is not None:
            result['ErrorPhone'] = self.error_phone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserve is not None:
            result['Reserve'] = self.reserve
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.source_endpoint_owner_id is not None:
            result['SourceEndpointOwnerID'] = self.source_endpoint_owner_id
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_role is not None:
            result['SourceEndpointRole'] = self.source_endpoint_role
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.subscription_data_type_ddl is not None:
            result['SubscriptionDataTypeDDL'] = self.subscription_data_type_ddl
        if self.subscription_data_type_dml is not None:
            result['SubscriptionDataTypeDML'] = self.subscription_data_type_dml
        if self.subscription_instance_network_type is not None:
            result['SubscriptionInstanceNetworkType'] = self.subscription_instance_network_type
        if self.subscription_instance_vpcid is not None:
            result['SubscriptionInstanceVPCId'] = self.subscription_instance_vpcid
        if self.subscription_instance_vswitch_id is not None:
            result['SubscriptionInstanceVSwitchId'] = self.subscription_instance_vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('DelayNotice') is not None:
            self.delay_notice = m.get('DelayNotice')
        if m.get('DelayPhone') is not None:
            self.delay_phone = m.get('DelayPhone')
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('ErrorNotice') is not None:
            self.error_notice = m.get('ErrorNotice')
        if m.get('ErrorPhone') is not None:
            self.error_phone = m.get('ErrorPhone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reserve') is not None:
            self.reserve = m.get('Reserve')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('SourceEndpointOwnerID') is not None:
            self.source_endpoint_owner_id = m.get('SourceEndpointOwnerID')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointRole') is not None:
            self.source_endpoint_role = m.get('SourceEndpointRole')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('SubscriptionDataTypeDDL') is not None:
            self.subscription_data_type_ddl = m.get('SubscriptionDataTypeDDL')
        if m.get('SubscriptionDataTypeDML') is not None:
            self.subscription_data_type_dml = m.get('SubscriptionDataTypeDML')
        if m.get('SubscriptionInstanceNetworkType') is not None:
            self.subscription_instance_network_type = m.get('SubscriptionInstanceNetworkType')
        if m.get('SubscriptionInstanceVPCId') is not None:
            self.subscription_instance_vpcid = m.get('SubscriptionInstanceVPCId')
        if m.get('SubscriptionInstanceVSwitchId') is not None:
            self.subscription_instance_vswitch_id = m.get('SubscriptionInstanceVSwitchId')
        return self


class ConfigureSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSubscriptionResponseBody = None,
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
            temp_model = ConfigureSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSubscriptionInstanceRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        role: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.owner_id = owner_id
        self.password = password
        self.port = port
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureSubscriptionInstanceRequestSubscriptionDataType(TeaModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        self.ddl = ddl
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['DDL'] = self.ddl
        if self.dml is not None:
            result['DML'] = self.dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        return self


class ConfigureSubscriptionInstanceRequestSubscriptionInstance(TeaModel):
    def __init__(
        self,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ConfigureSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: ConfigureSubscriptionInstanceRequestSourceEndpoint = None,
        subscription_data_type: ConfigureSubscriptionInstanceRequestSubscriptionDataType = None,
        subscription_instance: ConfigureSubscriptionInstanceRequestSubscriptionInstance = None,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_instance_network_type: str = None,
        subscription_object: str = None,
    ):
        self.source_endpoint = source_endpoint
        self.subscription_data_type = subscription_data_type
        self.subscription_instance = subscription_instance
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.subscription_instance_network_type = subscription_instance_network_type
        self.subscription_object = subscription_object

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_instance:
            self.subscription_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_instance is not None:
            result['SubscriptionInstance'] = self.subscription_instance.to_map()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_instance_network_type is not None:
            result['SubscriptionInstanceNetworkType'] = self.subscription_instance_network_type
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('SubscriptionDataType') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionInstance') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSubscriptionInstance()
            self.subscription_instance = temp_model.from_map(m['SubscriptionInstance'])
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionInstanceNetworkType') is not None:
            self.subscription_instance_network_type = m.get('SubscriptionInstanceNetworkType')
        if m.get('SubscriptionObject') is not None:
            self.subscription_object = m.get('SubscriptionObject')
        return self


class ConfigureSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSubscriptionInstanceResponseBody = None,
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
            temp_model = ConfigureSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSubscriptionInstanceAlertRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.delay_alert_phone = delay_alert_phone
        self.delay_alert_status = delay_alert_status
        self.delay_over_seconds = delay_over_seconds
        self.error_alert_phone = error_alert_phone
        self.error_alert_status = error_alert_status
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class ConfigureSubscriptionInstanceAlertResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSubscriptionInstanceAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSubscriptionInstanceAlertResponseBody = None,
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
            temp_model = ConfigureSubscriptionInstanceAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        data_base_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        password: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.data_base_name = data_base_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.password = password
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureSynchronizationJobRequestPartitionKey(TeaModel):
    def __init__(
        self,
        modify_time_day: bool = None,
        modify_time_hour: bool = None,
        modify_time_minute: bool = None,
        modify_time_month: bool = None,
        modify_time_year: bool = None,
    ):
        self.modify_time_day = modify_time_day
        self.modify_time_hour = modify_time_hour
        self.modify_time_minute = modify_time_minute
        self.modify_time_month = modify_time_month
        self.modify_time_year = modify_time_year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time_day is not None:
            result['ModifyTime_Day'] = self.modify_time_day
        if self.modify_time_hour is not None:
            result['ModifyTime_Hour'] = self.modify_time_hour
        if self.modify_time_minute is not None:
            result['ModifyTime_Minute'] = self.modify_time_minute
        if self.modify_time_month is not None:
            result['ModifyTime_Month'] = self.modify_time_month
        if self.modify_time_year is not None:
            result['ModifyTime_Year'] = self.modify_time_year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime_Day') is not None:
            self.modify_time_day = m.get('ModifyTime_Day')
        if m.get('ModifyTime_Hour') is not None:
            self.modify_time_hour = m.get('ModifyTime_Hour')
        if m.get('ModifyTime_Minute') is not None:
            self.modify_time_minute = m.get('ModifyTime_Minute')
        if m.get('ModifyTime_Month') is not None:
            self.modify_time_month = m.get('ModifyTime_Month')
        if m.get('ModifyTime_Year') is not None:
            self.modify_time_year = m.get('ModifyTime_Year')
        return self


class ConfigureSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        role: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.password = password
        self.port = port
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: ConfigureSynchronizationJobRequestDestinationEndpoint = None,
        partition_key: ConfigureSynchronizationJobRequestPartitionKey = None,
        source_endpoint: ConfigureSynchronizationJobRequestSourceEndpoint = None,
        account_id: str = None,
        checkpoint: str = None,
        data_initialization: bool = None,
        migration_reserved: str = None,
        owner_id: str = None,
        region_id: str = None,
        structure_initialization: bool = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.partition_key = partition_key
        self.source_endpoint = source_endpoint
        self.account_id = account_id
        self.checkpoint = checkpoint
        self.data_initialization = data_initialization
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        self.region_id = region_id
        self.structure_initialization = structure_initialization
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_objects = synchronization_objects

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.partition_key:
            self.partition_key.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('PartitionKey') is not None:
            temp_model = ConfigureSynchronizationJobRequestPartitionKey()
            self.partition_key = temp_model.from_map(m['PartitionKey'])
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        return self


class ConfigureSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSynchronizationJobResponseBody = None,
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
            temp_model = ConfigureSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobAlertRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.delay_alert_phone = delay_alert_phone
        self.delay_alert_status = delay_alert_status
        self.delay_over_seconds = delay_over_seconds
        self.error_alert_phone = error_alert_phone
        self.error_alert_status = error_alert_status
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class ConfigureSynchronizationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSynchronizationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSynchronizationJobAlertResponseBody = None,
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
            temp_model = ConfigureSynchronizationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobReplicatorCompareRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
        synchronization_replicator_compare_enable: bool = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_replicator_compare_enable = synchronization_replicator_compare_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_replicator_compare_enable is not None:
            result['SynchronizationReplicatorCompareEnable'] = self.synchronization_replicator_compare_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationReplicatorCompareEnable') is not None:
            self.synchronization_replicator_compare_enable = m.get('SynchronizationReplicatorCompareEnable')
        return self


class ConfigureSynchronizationJobReplicatorCompareResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSynchronizationJobReplicatorCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSynchronizationJobReplicatorCompareResponseBody = None,
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
            temp_model = ConfigureSynchronizationJobReplicatorCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountJobByConditionRequest(TeaModel):
    def __init__(
        self,
        dest_db_type: str = None,
        group_id: str = None,
        job_type: str = None,
        params: str = None,
        region: str = None,
        region_id: str = None,
        src_db_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # 目标端数据库类型
        self.dest_db_type = dest_db_type
        # 父任务id
        self.group_id = group_id
        self.job_type = job_type
        # 查询的值，与Type对应
        self.params = params
        self.region = region
        self.region_id = region_id
        # 源端数据库类型
        self.src_db_type = src_db_type
        self.status = status
        # 查询类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_db_type is not None:
            result['DestDbType'] = self.dest_db_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.params is not None:
            result['Params'] = self.params
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.src_db_type is not None:
            result['SrcDbType'] = self.src_db_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestDbType') is not None:
            self.dest_db_type = m.get('DestDbType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SrcDbType') is not None:
            self.src_db_type = m.get('SrcDbType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CountJobByConditionResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total_record_count: int = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class CountJobByConditionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CountJobByConditionResponseBody = None,
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
            temp_model = CountJobByConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        consumer_group_name: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
    ):
        self.consumer_group_name = consumer_group_name
        self.consumer_group_password = consumer_group_password
        self.consumer_group_user_name = consumer_group_user_name
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConsumerChannelResponseBody = None,
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
            temp_model = CreateConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        consumer_group_name: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_password = consumer_group_password
        self.consumer_group_user_name = consumer_group_user_name
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class CreateConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConsumerGroupResponseBody = None,
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
            temp_model = CreateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDtsInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_start: bool = None,
        compute_unit: int = None,
        database_count: int = None,
        destination_endpoint_engine_name: str = None,
        destination_region: str = None,
        fee_type: str = None,
        instance_class: str = None,
        job_id: str = None,
        pay_type: str = None,
        period: str = None,
        quantity: int = None,
        region_id: str = None,
        source_endpoint_engine_name: str = None,
        source_region: str = None,
        sync_architecture: str = None,
        type: str = None,
        used_time: int = None,
    ):
        self.auto_pay = auto_pay
        self.auto_start = auto_start
        self.compute_unit = compute_unit
        self.database_count = database_count
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        self.destination_region = destination_region
        self.fee_type = fee_type
        self.instance_class = instance_class
        self.job_id = job_id
        self.pay_type = pay_type
        self.period = period
        self.quantity = quantity
        self.region_id = region_id
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.source_region = source_region
        self.sync_architecture = sync_architecture
        self.type = type
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.compute_unit is not None:
            result['ComputeUnit'] = self.compute_unit
        if self.database_count is not None:
            result['DatabaseCount'] = self.database_count
        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name
        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region
        if self.fee_type is not None:
            result['FeeType'] = self.fee_type
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.sync_architecture is not None:
            result['SyncArchitecture'] = self.sync_architecture
        if self.type is not None:
            result['Type'] = self.type
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ComputeUnit') is not None:
            self.compute_unit = m.get('ComputeUnit')
        if m.get('DatabaseCount') is not None:
            self.database_count = m.get('DatabaseCount')
        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')
        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')
        if m.get('FeeType') is not None:
            self.fee_type = m.get('FeeType')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('SyncArchitecture') is not None:
            self.sync_architecture = m.get('SyncArchitecture')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class CreateDtsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        instance_id: str = None,
        job_id: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.instance_id = instance_id
        self.job_id = job_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDtsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDtsInstanceResponseBody = None,
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
            temp_model = CreateDtsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        delay_rule_time: int = None,
        dts_job_id: str = None,
        phone: str = None,
        region_id: str = None,
        state: str = None,
        type: str = None,
    ):
        self.delay_rule_time = delay_rule_time
        self.dts_job_id = dts_job_id
        self.phone = phone
        self.region_id = region_id
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateJobMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dts_job_id = dts_job_id
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateJobMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobMonitorRuleResponseBody = None,
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
            temp_model = CreateJobMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMigrationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        migration_job_class: str = None,
        owner_id: str = None,
        region: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.migration_job_class = migration_job_class
        self.owner_id = owner_id
        self.region = region
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        migration_job_id: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.migration_job_id = migration_job_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMigrationJobResponseBody = None,
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
            temp_model = CreateMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubscriptionInstanceRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: CreateSubscriptionInstanceRequestSourceEndpoint = None,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        region: str = None,
        region_id: str = None,
        used_time: int = None,
    ):
        self.source_endpoint = source_endpoint
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.pay_type = pay_type
        self.period = period
        self.region = region
        self.region_id = region_id
        self.used_time = used_time

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = CreateSubscriptionInstanceRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class CreateSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        subscription_instance_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.subscription_instance_id = subscription_instance_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSubscriptionInstanceResponseBody = None,
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
            temp_model = CreateSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: CreateSynchronizationJobRequestDestinationEndpoint = None,
        source_endpoint: CreateSynchronizationJobRequestSourceEndpoint = None,
        account_id: str = None,
        client_token: str = None,
        dbinstance_count: int = None,
        dest_region: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        source_region: str = None,
        synchronization_job_class: str = None,
        topology: str = None,
        used_time: int = None,
        network_type: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.source_endpoint = source_endpoint
        self.account_id = account_id
        self.client_token = client_token
        self.dbinstance_count = dbinstance_count
        self.dest_region = dest_region
        self.owner_id = owner_id
        self.pay_type = pay_type
        self.period = period
        self.region_id = region_id
        self.source_region = source_region
        self.synchronization_job_class = synchronization_job_class
        self.topology = topology
        self.used_time = used_time
        self.network_type = network_type

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_count is not None:
            result['DBInstanceCount'] = self.dbinstance_count
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.topology is not None:
            result['Topology'] = self.topology
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.network_type is not None:
            result['networkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('SourceEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceCount') is not None:
            self.dbinstance_count = m.get('DBInstanceCount')
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('Topology') is not None:
            self.topology = m.get('Topology')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        return self


class CreateSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        synchronization_job_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class CreateSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSynchronizationJobResponseBody = None,
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
            temp_model = CreateSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConsumerChannelResponseBody = None,
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
            temp_model = DeleteConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        consumer_group_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.consumer_group_id = consumer_group_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConsumerGroupResponseBody = None,
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
            temp_model = DeleteConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class DeleteDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDtsJobResponseBody = None,
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
            temp_model = DeleteDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMigrationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMigrationJobResponseBody = None,
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
            temp_model = DeleteMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DeleteSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSubscriptionInstanceResponseBody = None,
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
            temp_model = DeleteSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DeleteSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSynchronizationJobResponseBody = None,
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
            temp_model = DeleteSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectionStatusRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint_architecture: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_engine_name: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_port: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_user_name: str = None,
        region_id: str = None,
        source_endpoint_architecture: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
    ):
        self.destination_endpoint_architecture = destination_endpoint_architecture
        self.destination_endpoint_database_name = destination_endpoint_database_name
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        self.destination_endpoint_ip = destination_endpoint_ip
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        self.destination_endpoint_password = destination_endpoint_password
        self.destination_endpoint_port = destination_endpoint_port
        self.destination_endpoint_region = destination_endpoint_region
        self.destination_endpoint_user_name = destination_endpoint_user_name
        self.region_id = region_id
        self.source_endpoint_architecture = source_endpoint_architecture
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.source_endpoint_password = source_endpoint_password
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_user_name = source_endpoint_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint_architecture is not None:
            result['DestinationEndpointArchitecture'] = self.destination_endpoint_architecture
        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name
        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name
        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password
        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_endpoint_architecture is not None:
            result['SourceEndpointArchitecture'] = self.source_endpoint_architecture
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpointArchitecture') is not None:
            self.destination_endpoint_architecture = m.get('DestinationEndpointArchitecture')
        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')
        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')
        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')
        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceEndpointArchitecture') is not None:
            self.source_endpoint_architecture = m.get('SourceEndpointArchitecture')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        return self


class DescribeConnectionStatusResponseBody(TeaModel):
    def __init__(
        self,
        destination_connection_status: Dict[str, Any] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        source_connection_status: Dict[str, Any] = None,
        success: str = None,
    ):
        self.destination_connection_status = destination_connection_status
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.source_connection_status = source_connection_status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_connection_status is not None:
            result['DestinationConnectionStatus'] = self.destination_connection_status
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_connection_status is not None:
            result['SourceConnectionStatus'] = self.source_connection_status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationConnectionStatus') is not None:
            self.destination_connection_status = m.get('DestinationConnectionStatus')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceConnectionStatus') is not None:
            self.source_connection_status = m.get('SourceConnectionStatus')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeConnectionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConnectionStatusResponseBody = None,
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
            temp_model = DescribeConnectionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_channel_id: str = None,
        region_id: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.page_number = page_number
        self.page_size = page_size
        self.parent_channel_id = parent_channel_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_channel_id is not None:
            result['ParentChannelId'] = self.parent_channel_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentChannelId') is not None:
            self.parent_channel_id = m.get('ParentChannelId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeConsumerChannelResponseBodyConsumerChannels(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_user_name: str = None,
        consumption_checkpoint: str = None,
        message_delay: int = None,
        unconsumed_data: int = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_user_name = consumer_group_user_name
        self.consumption_checkpoint = consumption_checkpoint
        self.message_delay = message_delay
        self.unconsumed_data = unconsumed_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.message_delay is not None:
            result['MessageDelay'] = self.message_delay
        if self.unconsumed_data is not None:
            result['UnconsumedData'] = self.unconsumed_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('MessageDelay') is not None:
            self.message_delay = m.get('MessageDelay')
        if m.get('UnconsumedData') is not None:
            self.unconsumed_data = m.get('UnconsumedData')
        return self


class DescribeConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        consumer_channels: List[DescribeConsumerChannelResponseBodyConsumerChannels] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.consumer_channels = consumer_channels
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        if self.consumer_channels:
            for k in self.consumer_channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConsumerChannels'] = []
        if self.consumer_channels is not None:
            for k in self.consumer_channels:
                result['ConsumerChannels'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_channels = []
        if m.get('ConsumerChannels') is not None:
            for k in m.get('ConsumerChannels'):
                temp_model = DescribeConsumerChannelResponseBodyConsumerChannels()
                self.consumer_channels.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConsumerChannelResponseBody = None,
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
            temp_model = DescribeConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_user_name: str = None,
        consumption_checkpoint: str = None,
        message_delay: int = None,
        unconsumed_data: int = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_user_name = consumer_group_user_name
        self.consumption_checkpoint = consumption_checkpoint
        self.message_delay = message_delay
        self.unconsumed_data = unconsumed_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.message_delay is not None:
            result['MessageDelay'] = self.message_delay
        if self.unconsumed_data is not None:
            result['UnconsumedData'] = self.unconsumed_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('MessageDelay') is not None:
            self.message_delay = m.get('MessageDelay')
        if m.get('UnconsumedData') is not None:
            self.unconsumed_data = m.get('UnconsumedData')
        return self


class DescribeConsumerGroupResponseBodyConsumerChannels(TeaModel):
    def __init__(
        self,
        describe_consumer_channel: List[DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel] = None,
    ):
        self.describe_consumer_channel = describe_consumer_channel

    def validate(self):
        if self.describe_consumer_channel:
            for k in self.describe_consumer_channel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DescribeConsumerChannel'] = []
        if self.describe_consumer_channel is not None:
            for k in self.describe_consumer_channel:
                result['DescribeConsumerChannel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_consumer_channel = []
        if m.get('DescribeConsumerChannel') is not None:
            for k in m.get('DescribeConsumerChannel'):
                temp_model = DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel()
                self.describe_consumer_channel.append(temp_model.from_map(k))
        return self


class DescribeConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        consumer_channels: DescribeConsumerGroupResponseBodyConsumerChannels = None,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.consumer_channels = consumer_channels
        self.err_code = err_code
        self.err_message = err_message
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        if self.consumer_channels:
            self.consumer_channels.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_channels is not None:
            result['ConsumerChannels'] = self.consumer_channels.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerChannels') is not None:
            temp_model = DescribeConsumerGroupResponseBodyConsumerChannels()
            self.consumer_channels = temp_model.from_map(m['ConsumerChannels'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConsumerGroupResponseBody = None,
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
            temp_model = DescribeConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDTSIPRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint_region: str = None,
        region_id: str = None,
        source_endpoint_region: str = None,
    ):
        self.destination_endpoint_region = destination_endpoint_region
        self.region_id = region_id
        self.source_endpoint_region = source_endpoint_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        return self


class DescribeDTSIPResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDTSIPResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDTSIPResponseBody = None,
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
            temp_model = DescribeDTSIPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDtsJobDetailRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class DescribeDtsJobDetailResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobDetailResponseBodyMigrationMode(TeaModel):
    def __init__(
        self,
        data_extract_transform_load: bool = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_extract_transform_load = data_extract_transform_load
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_extract_transform_load is not None:
            result['DataExtractTransformLoad'] = self.data_extract_transform_load
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataExtractTransformLoad') is not None:
            self.data_extract_transform_load = m.get('DataExtractTransformLoad')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeDtsJobDetailResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        role_name: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.role_name = role_name
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobDetailResponseBodySubscriptionDataType(TeaModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        self.ddl = ddl
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['Ddl'] = self.ddl
        if self.dml is not None:
            result['Dml'] = self.dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ddl') is not None:
            self.ddl = m.get('Ddl')
        if m.get('Dml') is not None:
            self.dml = m.get('Dml')
        return self


class DescribeDtsJobDetailResponseBodySubscriptionHost(TeaModel):
    def __init__(
        self,
        private_host: str = None,
        public_host: str = None,
        vpc_host: str = None,
    ):
        self.private_host = private_host
        self.public_host = public_host
        self.vpc_host = vpc_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        if self.vpc_host is not None:
            result['VpcHost'] = self.vpc_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        if m.get('VpcHost') is not None:
            self.vpc_host = m.get('VpcHost')
        return self


class DescribeDtsJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        begin_timestamp: str = None,
        checkpoint: int = None,
        code: int = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        create_time: str = None,
        database_count: int = None,
        db_object: str = None,
        delay: int = None,
        demo_job: bool = None,
        dest_net_type: str = None,
        destination_endpoint: DescribeDtsJobDetailResponseBodyDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        dynamic_message: str = None,
        end_timestamp: str = None,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        etl_calculator: str = None,
        expire_time: str = None,
        finish_time: str = None,
        group_id: str = None,
        http_status_code: int = None,
        migration_mode: DescribeDtsJobDetailResponseBodyMigrationMode = None,
        pay_type: str = None,
        request_id: str = None,
        reserved: str = None,
        source_endpoint: DescribeDtsJobDetailResponseBodySourceEndpoint = None,
        status: str = None,
        subscribe_topic: str = None,
        subscription_data_type: DescribeDtsJobDetailResponseBodySubscriptionDataType = None,
        subscription_host: DescribeDtsJobDetailResponseBodySubscriptionHost = None,
        success: bool = None,
        synchronization_direction: str = None,
    ):
        self.app_name = app_name
        self.begin_timestamp = begin_timestamp
        self.checkpoint = checkpoint
        self.code = code
        self.consumption_checkpoint = consumption_checkpoint
        self.consumption_client = consumption_client
        self.create_time = create_time
        self.database_count = database_count
        self.db_object = db_object
        self.delay = delay
        self.demo_job = demo_job
        self.dest_net_type = dest_net_type
        self.destination_endpoint = destination_endpoint
        self.dts_instance_id = dts_instance_id
        self.dts_job_class = dts_job_class
        self.dts_job_direction = dts_job_direction
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.dynamic_message = dynamic_message
        self.end_timestamp = end_timestamp
        self.err_code = err_code
        self.err_message = err_message
        self.error_message = error_message
        self.etl_calculator = etl_calculator
        self.expire_time = expire_time
        self.finish_time = finish_time
        self.group_id = group_id
        self.http_status_code = http_status_code
        self.migration_mode = migration_mode
        self.pay_type = pay_type
        self.request_id = request_id
        self.reserved = reserved
        self.source_endpoint = source_endpoint
        self.status = status
        self.subscribe_topic = subscribe_topic
        self.subscription_data_type = subscription_data_type
        self.subscription_host = subscription_host
        self.success = success
        self.synchronization_direction = synchronization_direction

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_host:
            self.subscription_host.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.code is not None:
            result['Code'] = self.code
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_count is not None:
            result['DatabaseCount'] = self.database_count
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.demo_job is not None:
            result['DemoJob'] = self.demo_job
        if self.dest_net_type is not None:
            result['DestNetType'] = self.dest_net_type
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.etl_calculator is not None:
            result['EtlCalculator'] = self.etl_calculator
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_host is not None:
            result['SubscriptionHost'] = self.subscription_host.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseCount') is not None:
            self.database_count = m.get('DatabaseCount')
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DemoJob') is not None:
            self.demo_job = m.get('DemoJob')
        if m.get('DestNetType') is not None:
            self.dest_net_type = m.get('DestNetType')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobDetailResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EtlCalculator') is not None:
            self.etl_calculator = m.get('EtlCalculator')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobDetailResponseBodyMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobDetailResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeDtsJobDetailResponseBodySubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionHost') is not None:
            temp_model = DescribeDtsJobDetailResponseBodySubscriptionHost()
            self.subscription_host = temp_model.from_map(m['SubscriptionHost'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class DescribeDtsJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDtsJobDetailResponseBody = None,
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
            temp_model = DescribeDtsJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDtsJobsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_type: str = None,
        order_column: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        params: str = None,
        region: str = None,
        region_id: str = None,
        status: str = None,
        tags: str = None,
        type: str = None,
    ):
        self.group_id = group_id
        self.job_type = job_type
        self.order_column = order_column
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.params = params
        self.region = region
        self.region_id = region_id
        self.status = status
        self.tags = tags
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.order_column is not None:
            result['OrderColumn'] = self.order_column
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.params is not None:
            result['Params'] = self.params
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.need_upgrade = need_upgrade
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeDtsJobsResponseBodyDtsJobListPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.rps is not None:
            result['Rps'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        return self


class DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        self.check_item = check_item
        self.check_item_description = check_item_description
        self.check_result = check_result
        self.failed_reason = failed_reason
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('CheckItemDescription') is not None:
            self.check_item_description = m.get('CheckItemDescription')
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListRetryState(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        max_retry_time: int = None,
        retry_count: int = None,
        retry_target: str = None,
        retry_time: int = None,
    ):
        self.err_message = err_message
        self.max_retry_time = max_retry_time
        self.retry_count = retry_count
        self.retry_target = retry_target
        self.retry_time = retry_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.max_retry_time is not None:
            result['MaxRetryTime'] = self.max_retry_time
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.retry_target is not None:
            result['RetryTarget'] = self.retry_target
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('MaxRetryTime') is not None:
            self.max_retry_time = m.get('MaxRetryTime')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('RetryTarget') is not None:
            self.retry_target = m.get('RetryTarget')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.need_upgrade = need_upgrade
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.rps is not None:
            result['Rps'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        self.check_item = check_item
        self.check_item_description = check_item_description
        self.check_result = check_result
        self.failed_reason = failed_reason
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('CheckItemDescription') is not None:
            self.check_item_description = m.get('CheckItemDescription')
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJob(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        create_time: str = None,
        data_initialization_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus = None,
        data_synchronization_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus = None,
        db_object: str = None,
        delay: int = None,
        destination_endpoint: DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        error_message: str = None,
        expire_time: str = None,
        migration_mode: DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode = None,
        pay_type: str = None,
        performance: DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance = None,
        precheck_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus = None,
        reserved: str = None,
        source_endpoint: DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus = None,
    ):
        self.checkpoint = checkpoint
        self.create_time = create_time
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.db_object = db_object
        self.delay = delay
        self.destination_endpoint = destination_endpoint
        self.dts_instance_id = dts_instance_id
        self.dts_job_class = dts_job_class
        self.dts_job_direction = dts_job_direction
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.error_message = error_message
        self.expire_time = expire_time
        self.migration_mode = migration_mode
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.reserved = reserved
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization_status = structure_initialization_status

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyDtsJobListTagList(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDtsJobsResponseBodyDtsJobList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        begin_timestamp: str = None,
        checkpoint: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        create_time: str = None,
        data_etl_status: DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus = None,
        data_initialization_status: DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus = None,
        data_synchronization_status: DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus = None,
        db_object: str = None,
        delay: int = None,
        destination_endpoint: DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        end_timestamp: str = None,
        error_message: str = None,
        expire_time: str = None,
        migration_mode: DescribeDtsJobsResponseBodyDtsJobListMigrationMode = None,
        origin_type: str = None,
        pay_type: str = None,
        performance: DescribeDtsJobsResponseBodyDtsJobListPerformance = None,
        precheck_status: DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus = None,
        reserved: str = None,
        retry_state: DescribeDtsJobsResponseBodyDtsJobListRetryState = None,
        reverse_job: DescribeDtsJobsResponseBodyDtsJobListReverseJob = None,
        source_endpoint: DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus = None,
        tag_list: List[DescribeDtsJobsResponseBodyDtsJobListTagList] = None,
    ):
        self.app_name = app_name
        self.begin_timestamp = begin_timestamp
        self.checkpoint = checkpoint
        self.consumption_checkpoint = consumption_checkpoint
        self.consumption_client = consumption_client
        self.create_time = create_time
        self.data_etl_status = data_etl_status
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.db_object = db_object
        self.delay = delay
        self.destination_endpoint = destination_endpoint
        self.dts_instance_id = dts_instance_id
        self.dts_job_class = dts_job_class
        self.dts_job_direction = dts_job_direction
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.end_timestamp = end_timestamp
        self.error_message = error_message
        self.expire_time = expire_time
        self.migration_mode = migration_mode
        self.origin_type = origin_type
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.reserved = reserved
        self.retry_state = retry_state
        self.reverse_job = reverse_job
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization_status = structure_initialization_status
        self.tag_list = tag_list

    def validate(self):
        if self.data_etl_status:
            self.data_etl_status.validate()
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.retry_state:
            self.retry_state.validate()
        if self.reverse_job:
            self.reverse_job.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_etl_status is not None:
            result['DataEtlStatus'] = self.data_etl_status.to_map()
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.origin_type is not None:
            result['OriginType'] = self.origin_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.retry_state is not None:
            result['RetryState'] = self.retry_state.to_map()
        if self.reverse_job is not None:
            result['ReverseJob'] = self.reverse_job.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataEtlStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus()
            self.data_etl_status = temp_model.from_map(m['DataEtlStatus'])
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('OriginType') is not None:
            self.origin_type = m.get('OriginType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('RetryState') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListRetryState()
            self.retry_state = temp_model.from_map(m['RetryState'])
        if m.get('ReverseJob') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJob()
            self.reverse_job = temp_model.from_map(m['ReverseJob'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobListTagList()
                self.tag_list.append(temp_model.from_map(k))
        return self


class DescribeDtsJobsResponseBodyEtlDemoListDataEtlStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.need_upgrade = need_upgrade
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.rps is not None:
            result['Rps'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        self.check_item = check_item
        self.check_item_description = check_item_description
        self.check_result = check_result
        self.failed_reason = failed_reason
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('CheckItemDescription') is not None:
            self.check_item_description = m.get('CheckItemDescription')
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListRetryState(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        max_retry_time: int = None,
        retry_count: int = None,
        retry_target: str = None,
        retry_time: int = None,
    ):
        self.err_message = err_message
        self.max_retry_time = max_retry_time
        self.retry_count = retry_count
        self.retry_target = retry_target
        self.retry_time = retry_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.max_retry_time is not None:
            result['MaxRetryTime'] = self.max_retry_time
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.retry_target is not None:
            result['RetryTarget'] = self.retry_target
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('MaxRetryTime') is not None:
            self.max_retry_time = m.get('MaxRetryTime')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('RetryTarget') is not None:
            self.retry_target = m.get('RetryTarget')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.need_upgrade = need_upgrade
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.rps is not None:
            result['Rps'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        self.check_item = check_item
        self.check_item_description = check_item_description
        self.check_result = check_result
        self.failed_reason = failed_reason
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('CheckItemDescription') is not None:
            self.check_item_description = m.get('CheckItemDescription')
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJobStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListReverseJob(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        create_time: str = None,
        data_initialization_status: DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataInitializationStatus = None,
        data_synchronization_status: DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataSynchronizationStatus = None,
        db_object: str = None,
        delay: int = None,
        destination_endpoint: DescribeDtsJobsResponseBodyEtlDemoListReverseJobDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        error_message: str = None,
        expire_time: str = None,
        migration_mode: DescribeDtsJobsResponseBodyEtlDemoListReverseJobMigrationMode = None,
        pay_type: str = None,
        performance: DescribeDtsJobsResponseBodyEtlDemoListReverseJobPerformance = None,
        precheck_status: DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatus = None,
        reserved: str = None,
        source_endpoint: DescribeDtsJobsResponseBodyEtlDemoListReverseJobSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: DescribeDtsJobsResponseBodyEtlDemoListReverseJobStructureInitializationStatus = None,
    ):
        self.checkpoint = checkpoint
        self.create_time = create_time
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.db_object = db_object
        self.delay = delay
        self.destination_endpoint = destination_endpoint
        self.dts_instance_id = dts_instance_id
        self.dts_job_class = dts_job_class
        self.dts_job_direction = dts_job_direction
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.error_message = error_message
        self.expire_time = expire_time
        self.migration_mode = migration_mode
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.reserved = reserved
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization_status = structure_initialization_status

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJobStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeDtsJobsResponseBodyEtlDemoListSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.oracle_sid = oracle_sid
        self.port = port
        self.region = region
        self.ssl_solution_enum = ssl_solution_enum
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDtsJobsResponseBodyEtlDemoListTagList(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDtsJobsResponseBodyEtlDemoList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        begin_timestamp: str = None,
        checkpoint: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        create_time: str = None,
        data_etl_status: DescribeDtsJobsResponseBodyEtlDemoListDataEtlStatus = None,
        data_initialization_status: DescribeDtsJobsResponseBodyEtlDemoListDataInitializationStatus = None,
        data_synchronization_status: DescribeDtsJobsResponseBodyEtlDemoListDataSynchronizationStatus = None,
        db_object: str = None,
        delay: int = None,
        destination_endpoint: DescribeDtsJobsResponseBodyEtlDemoListDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        end_timestamp: str = None,
        error_message: str = None,
        expire_time: str = None,
        migration_mode: DescribeDtsJobsResponseBodyEtlDemoListMigrationMode = None,
        origin_type: str = None,
        pay_type: str = None,
        performance: DescribeDtsJobsResponseBodyEtlDemoListPerformance = None,
        precheck_status: DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatus = None,
        reserved: str = None,
        retry_state: DescribeDtsJobsResponseBodyEtlDemoListRetryState = None,
        reverse_job: DescribeDtsJobsResponseBodyEtlDemoListReverseJob = None,
        source_endpoint: DescribeDtsJobsResponseBodyEtlDemoListSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: DescribeDtsJobsResponseBodyEtlDemoListStructureInitializationStatus = None,
        tag_list: List[DescribeDtsJobsResponseBodyEtlDemoListTagList] = None,
    ):
        self.app_name = app_name
        self.begin_timestamp = begin_timestamp
        self.checkpoint = checkpoint
        self.consumption_checkpoint = consumption_checkpoint
        self.consumption_client = consumption_client
        self.create_time = create_time
        self.data_etl_status = data_etl_status
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.db_object = db_object
        self.delay = delay
        self.destination_endpoint = destination_endpoint
        self.dts_instance_id = dts_instance_id
        self.dts_job_class = dts_job_class
        self.dts_job_direction = dts_job_direction
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.end_timestamp = end_timestamp
        self.error_message = error_message
        self.expire_time = expire_time
        self.migration_mode = migration_mode
        self.origin_type = origin_type
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.reserved = reserved
        self.retry_state = retry_state
        self.reverse_job = reverse_job
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization_status = structure_initialization_status
        self.tag_list = tag_list

    def validate(self):
        if self.data_etl_status:
            self.data_etl_status.validate()
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.retry_state:
            self.retry_state.validate()
        if self.reverse_job:
            self.reverse_job.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_etl_status is not None:
            result['DataEtlStatus'] = self.data_etl_status.to_map()
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.origin_type is not None:
            result['OriginType'] = self.origin_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.retry_state is not None:
            result['RetryState'] = self.retry_state.to_map()
        if self.reverse_job is not None:
            result['ReverseJob'] = self.reverse_job.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataEtlStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListDataEtlStatus()
            self.data_etl_status = temp_model.from_map(m['DataEtlStatus'])
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('OriginType') is not None:
            self.origin_type = m.get('OriginType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('RetryState') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListRetryState()
            self.retry_state = temp_model.from_map(m['RetryState'])
        if m.get('ReverseJob') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListReverseJob()
            self.reverse_job = temp_model.from_map(m['ReverseJob'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyEtlDemoListStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeDtsJobsResponseBodyEtlDemoListTagList()
                self.tag_list.append(temp_model.from_map(k))
        return self


class DescribeDtsJobsResponseBody(TeaModel):
    def __init__(
        self,
        dts_job_list: List[DescribeDtsJobsResponseBodyDtsJobList] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        etl_demo_list: List[DescribeDtsJobsResponseBodyEtlDemoList] = None,
        http_status_code: int = None,
        job_type: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: bool = None,
        total_record_count: int = None,
    ):
        self.dts_job_list = dts_job_list
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.etl_demo_list = etl_demo_list
        self.http_status_code = http_status_code
        self.job_type = job_type
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        if self.dts_job_list:
            for k in self.dts_job_list:
                if k:
                    k.validate()
        if self.etl_demo_list:
            for k in self.etl_demo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DtsJobList'] = []
        if self.dts_job_list is not None:
            for k in self.dts_job_list:
                result['DtsJobList'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        result['EtlDemoList'] = []
        if self.etl_demo_list is not None:
            for k in self.etl_demo_list:
                result['EtlDemoList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dts_job_list = []
        if m.get('DtsJobList') is not None:
            for k in m.get('DtsJobList'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobList()
                self.dts_job_list.append(temp_model.from_map(k))
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        self.etl_demo_list = []
        if m.get('EtlDemoList') is not None:
            for k in m.get('EtlDemoList'):
                temp_model = DescribeDtsJobsResponseBodyEtlDemoList()
                self.etl_demo_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDtsJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDtsJobsResponseBody = None,
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
            temp_model = DescribeDtsJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointSwitchStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeEndpointSwitchStatusResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        request_id: str = None,
        status: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.error_message = error_message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEndpointSwitchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEndpointSwitchStatusResponseBody = None,
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
            temp_model = DescribeEndpointSwitchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInitializationStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeInitializationStatusResponseBodyDataInitializationDetails(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
        total_row_num: str = None,
        used_time: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.finish_row_num = finish_row_num
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name
        self.total_row_num = total_row_num
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_row_num is not None:
            result['FinishRowNum'] = self.finish_row_num
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TotalRowNum') is not None:
            self.total_row_num = m.get('TotalRowNum')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class DescribeInitializationStatusResponseBodyDataSynchronizationDetails(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInitializationStatusResponseBodyStructureInitializationDetails(TeaModel):
    def __init__(
        self,
        constraints: List[DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints] = None,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.constraints = constraints
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        if self.constraints:
            for k in self.constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Constraints'] = []
        if self.constraints is not None:
            for k in self.constraints:
                result['Constraints'].append(k.to_map() if k else None)
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constraints = []
        if m.get('Constraints') is not None:
            for k in m.get('Constraints'):
                temp_model = DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints()
                self.constraints.append(temp_model.from_map(k))
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInitializationStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_details: List[DescribeInitializationStatusResponseBodyDataInitializationDetails] = None,
        data_synchronization_details: List[DescribeInitializationStatusResponseBodyDataSynchronizationDetails] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        structure_initialization_details: List[DescribeInitializationStatusResponseBodyStructureInitializationDetails] = None,
        success: str = None,
    ):
        self.data_initialization_details = data_initialization_details
        self.data_synchronization_details = data_synchronization_details
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.structure_initialization_details = structure_initialization_details
        self.success = success

    def validate(self):
        if self.data_initialization_details:
            for k in self.data_initialization_details:
                if k:
                    k.validate()
        if self.data_synchronization_details:
            for k in self.data_synchronization_details:
                if k:
                    k.validate()
        if self.structure_initialization_details:
            for k in self.structure_initialization_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataInitializationDetails'] = []
        if self.data_initialization_details is not None:
            for k in self.data_initialization_details:
                result['DataInitializationDetails'].append(k.to_map() if k else None)
        result['DataSynchronizationDetails'] = []
        if self.data_synchronization_details is not None:
            for k in self.data_synchronization_details:
                result['DataSynchronizationDetails'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StructureInitializationDetails'] = []
        if self.structure_initialization_details is not None:
            for k in self.structure_initialization_details:
                result['StructureInitializationDetails'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_initialization_details = []
        if m.get('DataInitializationDetails') is not None:
            for k in m.get('DataInitializationDetails'):
                temp_model = DescribeInitializationStatusResponseBodyDataInitializationDetails()
                self.data_initialization_details.append(temp_model.from_map(k))
        self.data_synchronization_details = []
        if m.get('DataSynchronizationDetails') is not None:
            for k in m.get('DataSynchronizationDetails'):
                temp_model = DescribeInitializationStatusResponseBodyDataSynchronizationDetails()
                self.data_synchronization_details.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.structure_initialization_details = []
        if m.get('StructureInitializationDetails') is not None:
            for k in m.get('StructureInitializationDetails'):
                temp_model = DescribeInitializationStatusResponseBodyStructureInitializationDetails()
                self.structure_initialization_details.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeInitializationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInitializationStatusResponseBody = None,
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
            temp_model = DescribeInitializationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeJobMonitorRuleResponseBodyMonitorRules(TeaModel):
    def __init__(
        self,
        delay_rule_time: int = None,
        phone: str = None,
        state: str = None,
        type: str = None,
    ):
        self.delay_rule_time = delay_rule_time
        self.phone = phone
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeJobMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        monitor_rules: List[DescribeJobMonitorRuleResponseBodyMonitorRules] = None,
        request_id: str = None,
        success: bool = None,
        topics: List[str] = None,
    ):
        self.code = code
        self.dts_job_id = dts_job_id
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.monitor_rules = monitor_rules
        self.request_id = request_id
        self.success = success
        self.topics = topics

    def validate(self):
        if self.monitor_rules:
            for k in self.monitor_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['MonitorRules'] = []
        if self.monitor_rules is not None:
            for k in self.monitor_rules:
                result['MonitorRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topics is not None:
            result['Topics'] = self.topics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.monitor_rules = []
        if m.get('MonitorRules') is not None:
            for k in m.get('MonitorRules'):
                temp_model = DescribeJobMonitorRuleResponseBodyMonitorRules()
                self.monitor_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Topics') is not None:
            self.topics = m.get('Topics')
        return self


class DescribeJobMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJobMonitorRuleResponseBody = None,
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
            temp_model = DescribeJobMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobAlertRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMigrationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        err_code: str = None,
        err_message: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.delay_alert_phone = delay_alert_phone
        self.delay_alert_status = delay_alert_status
        self.delay_over_seconds = delay_over_seconds
        self.err_code = err_code
        self.err_message = err_message
        self.error_alert_phone = error_alert_phone
        self.error_alert_status = error_alert_status
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMigrationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationJobAlertResponseBody = None,
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
            temp_model = DescribeMigrationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobDetailRequestMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeMigrationJobDetailRequest(TeaModel):
    def __init__(
        self,
        migration_mode: DescribeMigrationJobDetailRequestMigrationMode = None,
        account_id: str = None,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.migration_mode = migration_mode
        self.account_id = account_id
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        if self.migration_mode:
            self.migration_mode.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobDetailRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        migration_time: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
        total_row_num: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.finish_row_num = finish_row_num
        self.migration_time = migration_time
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name
        self.total_row_num = total_row_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_row_num is not None:
            result['FinishRowNum'] = self.finish_row_num
        if self.migration_time is not None:
            result['MigrationTime'] = self.migration_time
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')
        if m.get('MigrationTime') is not None:
            self.migration_time = m.get('MigrationTime')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TotalRowNum') is not None:
            self.total_row_num = m.get('TotalRowNum')
        return self


class DescribeMigrationJobDetailResponseBodyDataInitializationDetailList(TeaModel):
    def __init__(
        self,
        data_initialization_detail: List[DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail] = None,
    ):
        self.data_initialization_detail = data_initialization_detail

    def validate(self):
        if self.data_initialization_detail:
            for k in self.data_initialization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataInitializationDetail'] = []
        if self.data_initialization_detail is not None:
            for k in self.data_initialization_detail:
                result['DataInitializationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_initialization_detail = []
        if m.get('DataInitializationDetail') is not None:
            for k in m.get('DataInitializationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail()
                self.data_initialization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList(TeaModel):
    def __init__(
        self,
        data_synchronization_detail: List[DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail] = None,
    ):
        self.data_synchronization_detail = data_synchronization_detail

    def validate(self):
        if self.data_synchronization_detail:
            for k in self.data_synchronization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSynchronizationDetail'] = []
        if self.data_synchronization_detail is not None:
            for k in self.data_synchronization_detail:
                result['DataSynchronizationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_synchronization_detail = []
        if m.get('DataSynchronizationDetail') is not None:
            for k in m.get('DataSynchronizationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail()
                self.data_synchronization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList(TeaModel):
    def __init__(
        self,
        structure_initialization_detail: List[DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail] = None,
    ):
        self.structure_initialization_detail = structure_initialization_detail

    def validate(self):
        if self.structure_initialization_detail:
            for k in self.structure_initialization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StructureInitializationDetail'] = []
        if self.structure_initialization_detail is not None:
            for k in self.structure_initialization_detail:
                result['StructureInitializationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.structure_initialization_detail = []
        if m.get('StructureInitializationDetail') is not None:
            for k in m.get('StructureInitializationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail()
                self.structure_initialization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail(TeaModel):
    def __init__(
        self,
        constraint_list: DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList = None,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.constraint_list = constraint_list
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        if self.constraint_list:
            self.constraint_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_list is not None:
            result['ConstraintList'] = self.constraint_list.to_map()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList()
            self.constraint_list = temp_model.from_map(m['ConstraintList'])
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList(TeaModel):
    def __init__(
        self,
        structure_initialization_detail: List[DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail] = None,
    ):
        self.structure_initialization_detail = structure_initialization_detail

    def validate(self):
        if self.structure_initialization_detail:
            for k in self.structure_initialization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StructureInitializationDetail'] = []
        if self.structure_initialization_detail is not None:
            for k in self.structure_initialization_detail:
                result['StructureInitializationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.structure_initialization_detail = []
        if m.get('StructureInitializationDetail') is not None:
            for k in m.get('StructureInitializationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail()
                self.structure_initialization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_detail_list: DescribeMigrationJobDetailResponseBodyDataInitializationDetailList = None,
        data_synchronization_detail_list: DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList = None,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        structure_initialization_detail_list: DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.data_initialization_detail_list = data_initialization_detail_list
        self.data_synchronization_detail_list = data_synchronization_detail_list
        self.err_code = err_code
        self.err_message = err_message
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.structure_initialization_detail_list = structure_initialization_detail_list
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        if self.data_initialization_detail_list:
            self.data_initialization_detail_list.validate()
        if self.data_synchronization_detail_list:
            self.data_synchronization_detail_list.validate()
        if self.structure_initialization_detail_list:
            self.structure_initialization_detail_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization_detail_list is not None:
            result['DataInitializationDetailList'] = self.data_initialization_detail_list.to_map()
        if self.data_synchronization_detail_list is not None:
            result['DataSynchronizationDetailList'] = self.data_synchronization_detail_list.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.structure_initialization_detail_list is not None:
            result['StructureInitializationDetailList'] = self.structure_initialization_detail_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyDataInitializationDetailList()
            self.data_initialization_detail_list = temp_model.from_map(m['DataInitializationDetailList'])
        if m.get('DataSynchronizationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList()
            self.data_synchronization_detail_list = temp_model.from_map(m['DataSynchronizationDetailList'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StructureInitializationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList()
            self.structure_initialization_detail_list = temp_model.from_map(m['StructureInitializationDetailList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeMigrationJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationJobDetailResponseBody = None,
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
            temp_model = DescribeMigrationJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMigrationJobStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.checkpoint = checkpoint
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        oracle_sid: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.oracle_sid = oracle_sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.oracle_sid is not None:
            result['oracleSID'] = self.oracle_sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('oracleSID') is not None:
            self.oracle_sid = m.get('oracleSID')
        return self


class DescribeMigrationJobStatusResponseBodyMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['dataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['dataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['structureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataInitialization') is not None:
            self.data_initialization = m.get('dataInitialization')
        if m.get('dataSynchronization') is not None:
            self.data_synchronization = m.get('dataSynchronization')
        if m.get('structureInitialization') is not None:
            self.structure_initialization = m.get('structureInitialization')
        return self


class DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_item: List[DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem] = None,
    ):
        self.check_item = check_item

    def validate(self):
        if self.check_item:
            for k in self.check_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItem'] = []
        if self.check_item is not None:
            for k in self.check_item:
                result['CheckItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_item = []
        if m.get('CheckItem') is not None:
            for k in m.get('CheckItem'):
                temp_model = DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem()
                self.check_item.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        oracle_sid: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.oracle_sid = oracle_sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.oracle_sid is not None:
            result['oracleSID'] = self.oracle_sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('oracleSID') is not None:
            self.oracle_sid = m.get('oracleSID')
        return self


class DescribeMigrationJobStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_status: DescribeMigrationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus = None,
        destination_endpoint: DescribeMigrationJobStatusResponseBodyDestinationEndpoint = None,
        err_code: str = None,
        err_message: str = None,
        migration_job_class: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        migration_mode: DescribeMigrationJobStatusResponseBodyMigrationMode = None,
        migration_object: str = None,
        pay_type: str = None,
        precheck_status: DescribeMigrationJobStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        source_endpoint: DescribeMigrationJobStatusResponseBodySourceEndpoint = None,
        structure_initialization_status: DescribeMigrationJobStatusResponseBodyStructureInitializationStatus = None,
        success: str = None,
        task_id: str = None,
    ):
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.destination_endpoint = destination_endpoint
        self.err_code = err_code
        self.err_message = err_message
        self.migration_job_class = migration_job_class
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_job_status = migration_job_status
        self.migration_mode = migration_mode
        self.migration_object = migration_object
        self.pay_type = pay_type
        self.precheck_status = precheck_status
        self.request_id = request_id
        self.source_endpoint = source_endpoint
        self.structure_initialization_status = structure_initialization_status
        self.success = success
        self.task_id = task_id

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_job_status is not None:
            result['MigrationJobStatus'] = self.migration_job_status
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeMigrationJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationJobStatusResponseBody = None,
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
            temp_model = DescribeMigrationJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobsRequestTag(TeaModel):
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


class DescribeMigrationJobsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        migration_job_name: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        tag: List[DescribeMigrationJobsRequestTag] = None,
    ):
        self.account_id = account_id
        self.migration_job_name = migration_job_name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeMigrationJobsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization(TeaModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        self.database_name = database_name
        self.table_list = table_list
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableList') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for k in self.synchronous_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k in self.synchronous_object:
                result['SynchronousObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k in m.get('SynchronousObject'):
                temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck(TeaModel):
    def __init__(
        self,
        percent: str = None,
        status: str = None,
    ):
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag(TeaModel):
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


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag] = None,
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
                temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob(TeaModel):
    def __init__(
        self,
        data_initialization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization = None,
        data_synchronization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization = None,
        destination_endpoint: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint = None,
        instance_create_time: str = None,
        job_create_time: str = None,
        migration_job_class: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        migration_mode: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode = None,
        migration_object: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject = None,
        pay_type: str = None,
        precheck: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck = None,
        source_endpoint: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint = None,
        structure_initialization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization = None,
        tags: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.destination_endpoint = destination_endpoint
        self.instance_create_time = instance_create_time
        self.job_create_time = job_create_time
        self.migration_job_class = migration_job_class
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_job_status = migration_job_status
        self.migration_mode = migration_mode
        self.migration_object = migration_object
        self.pay_type = pay_type
        self.precheck = precheck
        self.source_endpoint = source_endpoint
        self.structure_initialization = structure_initialization
        self.tags = tags

    def validate(self):
        if self.data_initialization:
            self.data_initialization.validate()
        if self.data_synchronization:
            self.data_synchronization.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.migration_object:
            self.migration_object.validate()
        if self.precheck:
            self.precheck.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization:
            self.structure_initialization.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization.to_map()
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time
        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.migration_job_id is not None:
            result['MigrationJobID'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_job_status is not None:
            result['MigrationJobStatus'] = self.migration_job_status
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object.to_map()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.precheck is not None:
            result['Precheck'] = self.precheck.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization()
            self.data_initialization = temp_model.from_map(m['DataInitialization'])
        if m.get('DataSynchronization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization()
            self.data_synchronization = temp_model.from_map(m['DataSynchronization'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')
        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('MigrationJobID') is not None:
            self.migration_job_id = m.get('MigrationJobID')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('MigrationObject') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject()
            self.migration_object = temp_model.from_map(m['MigrationObject'])
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Precheck') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck()
            self.precheck = temp_model.from_map(m['Precheck'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitialization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization()
            self.structure_initialization = temp_model.from_map(m['StructureInitialization'])
        if m.get('Tags') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeMigrationJobsResponseBodyMigrationJobs(TeaModel):
    def __init__(
        self,
        migration_job: List[DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob] = None,
    ):
        self.migration_job = migration_job

    def validate(self):
        if self.migration_job:
            for k in self.migration_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MigrationJob'] = []
        if self.migration_job is not None:
            for k in self.migration_job:
                result['MigrationJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migration_job = []
        if m.get('MigrationJob') is not None:
            for k in m.get('MigrationJob'):
                temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob()
                self.migration_job.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobsResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        migration_jobs: DescribeMigrationJobsResponseBodyMigrationJobs = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.migration_jobs = migration_jobs
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        if self.migration_jobs:
            self.migration_jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.migration_jobs is not None:
            result['MigrationJobs'] = self.migration_jobs.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('MigrationJobs') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobs()
            self.migration_jobs = temp_model.from_map(m['MigrationJobs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeMigrationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationJobsResponseBody = None,
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
            temp_model = DescribeMigrationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePreCheckStatusRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_code: str = None,
        name: str = None,
        page_no: str = None,
        page_size: str = None,
        region_id: str = None,
        struct_phase: str = None,
        struct_type: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.job_code = job_code
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.region_id = region_id
        self.struct_phase = struct_phase
        self.struct_type = struct_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.job_code is not None:
            result['JobCode'] = self.job_code
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.struct_phase is not None:
            result['StructPhase'] = self.struct_phase
        if self.struct_type is not None:
            result['StructType'] = self.struct_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('JobCode') is not None:
            self.job_code = m.get('JobCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StructPhase') is not None:
            self.struct_phase = m.get('StructPhase')
        if m.get('StructType') is not None:
            self.struct_type = m.get('StructType')
        return self


class DescribePreCheckStatusResponseBodyJobProgressLogs(TeaModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        err_type: str = None,
        log_level: str = None,
    ):
        self.err_data = err_data
        self.err_msg = err_msg
        self.err_type = err_type
        self.log_level = log_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_data is not None:
            result['ErrData'] = self.err_data
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.err_type is not None:
            result['ErrType'] = self.err_type
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        return self


class DescribePreCheckStatusResponseBodyJobProgress(TeaModel):
    def __init__(
        self,
        boot_time: str = None,
        can_skip: bool = None,
        ddl_sql: str = None,
        delay_seconds: int = None,
        dest_schema: str = None,
        diff_row: int = None,
        err_detail: str = None,
        err_msg: str = None,
        finish_time: str = None,
        id: str = None,
        ignore_flag: str = None,
        item: str = None,
        job_id: str = None,
        logs: List[DescribePreCheckStatusResponseBodyJobProgressLogs] = None,
        names: str = None,
        order_num: int = None,
        parent_obj: str = None,
        repair_method: str = None,
        skip: bool = None,
        source_schema: str = None,
        state: str = None,
        sub: str = None,
        target_names: str = None,
        total: int = None,
    ):
        self.boot_time = boot_time
        self.can_skip = can_skip
        self.ddl_sql = ddl_sql
        self.delay_seconds = delay_seconds
        self.dest_schema = dest_schema
        self.diff_row = diff_row
        self.err_detail = err_detail
        self.err_msg = err_msg
        self.finish_time = finish_time
        self.id = id
        self.ignore_flag = ignore_flag
        self.item = item
        self.job_id = job_id
        self.logs = logs
        self.names = names
        self.order_num = order_num
        self.parent_obj = parent_obj
        self.repair_method = repair_method
        self.skip = skip
        self.source_schema = source_schema
        self.state = state
        self.sub = sub
        self.target_names = target_names
        self.total = total

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time
        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip
        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema
        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row
        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.id is not None:
            result['Id'] = self.id
        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag
        if self.item is not None:
            result['Item'] = self.item
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.names is not None:
            result['Names'] = self.names
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema
        if self.state is not None:
            result['State'] = self.state
        if self.sub is not None:
            result['Sub'] = self.sub
        if self.target_names is not None:
            result['TargetNames'] = self.target_names
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')
        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')
        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')
        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')
        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribePreCheckStatusResponseBodyJobProgressLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Sub') is not None:
            self.sub = m.get('Sub')
        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs(TeaModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        err_type: str = None,
        log_level: str = None,
    ):
        self.err_data = err_data
        self.err_msg = err_msg
        self.err_type = err_type
        self.log_level = log_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_data is not None:
            result['ErrData'] = self.err_data
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.err_type is not None:
            result['ErrType'] = self.err_type
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        return self


class DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress(TeaModel):
    def __init__(
        self,
        boot_time: str = None,
        can_skip: bool = None,
        ddl_sql: str = None,
        delay_seconds: int = None,
        dest_schema: str = None,
        diff_row: int = None,
        err_detail: str = None,
        err_msg: str = None,
        finish_time: str = None,
        id: str = None,
        ignore_flag: str = None,
        item: str = None,
        job_id: str = None,
        logs: List[DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs] = None,
        names: str = None,
        order_num: int = None,
        parent_obj: str = None,
        repair_method: str = None,
        skip: bool = None,
        source_schema: str = None,
        state: str = None,
        sub: str = None,
        target_names: str = None,
        total: int = None,
    ):
        self.boot_time = boot_time
        self.can_skip = can_skip
        self.ddl_sql = ddl_sql
        self.delay_seconds = delay_seconds
        self.dest_schema = dest_schema
        self.diff_row = diff_row
        self.err_detail = err_detail
        self.err_msg = err_msg
        self.finish_time = finish_time
        self.id = id
        self.ignore_flag = ignore_flag
        self.item = item
        self.job_id = job_id
        self.logs = logs
        self.names = names
        self.order_num = order_num
        self.parent_obj = parent_obj
        self.repair_method = repair_method
        self.skip = skip
        self.source_schema = source_schema
        self.state = state
        self.sub = sub
        self.target_names = target_names
        self.total = total

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time
        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip
        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema
        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row
        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.id is not None:
            result['Id'] = self.id
        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag
        if self.item is not None:
            result['Item'] = self.item
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.names is not None:
            result['Names'] = self.names
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema
        if self.state is not None:
            result['State'] = self.state
        if self.sub is not None:
            result['Sub'] = self.sub
        if self.target_names is not None:
            result['TargetNames'] = self.target_names
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')
        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')
        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')
        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')
        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Sub') is not None:
            self.sub = m.get('Sub')
        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribePreCheckStatusResponseBodySubDistributedJobStatus(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_item: int = None,
        job_id: str = None,
        job_name: str = None,
        job_progress: List[DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress] = None,
        state: str = None,
        total: int = None,
    ):
        self.code = code
        self.error_item = error_item
        self.job_id = job_id
        self.job_name = job_name
        self.job_progress = job_progress
        self.state = state
        self.total = total

    def validate(self):
        if self.job_progress:
            for k in self.job_progress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_item is not None:
            result['ErrorItem'] = self.error_item
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        result['JobProgress'] = []
        if self.job_progress is not None:
            for k in self.job_progress:
                result['JobProgress'].append(k.to_map() if k else None)
        if self.state is not None:
            result['State'] = self.state
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorItem') is not None:
            self.error_item = m.get('ErrorItem')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        self.job_progress = []
        if m.get('JobProgress') is not None:
            for k in m.get('JobProgress'):
                temp_model = DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress()
                self.job_progress.append(temp_model.from_map(k))
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribePreCheckStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_item: int = None,
        http_status_code: int = None,
        job_id: str = None,
        job_name: str = None,
        job_progress: List[DescribePreCheckStatusResponseBodyJobProgress] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        state: str = None,
        sub_distributed_job_status: List[DescribePreCheckStatusResponseBodySubDistributedJobStatus] = None,
        success: bool = None,
        total: int = None,
        total_record_count: int = None,
    ):
        self.code = code
        self.error_item = error_item
        self.http_status_code = http_status_code
        self.job_id = job_id
        self.job_name = job_name
        self.job_progress = job_progress
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.state = state
        self.sub_distributed_job_status = sub_distributed_job_status
        self.success = success
        self.total = total
        self.total_record_count = total_record_count

    def validate(self):
        if self.job_progress:
            for k in self.job_progress:
                if k:
                    k.validate()
        if self.sub_distributed_job_status:
            for k in self.sub_distributed_job_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_item is not None:
            result['ErrorItem'] = self.error_item
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        result['JobProgress'] = []
        if self.job_progress is not None:
            for k in self.job_progress:
                result['JobProgress'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        result['SubDistributedJobStatus'] = []
        if self.sub_distributed_job_status is not None:
            for k in self.sub_distributed_job_status:
                result['SubDistributedJobStatus'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorItem') is not None:
            self.error_item = m.get('ErrorItem')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        self.job_progress = []
        if m.get('JobProgress') is not None:
            for k in m.get('JobProgress'):
                temp_model = DescribePreCheckStatusResponseBodyJobProgress()
                self.job_progress.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.sub_distributed_job_status = []
        if m.get('SubDistributedJobStatus') is not None:
            for k in m.get('SubDistributedJobStatus'):
                temp_model = DescribePreCheckStatusResponseBodySubDistributedJobStatus()
                self.sub_distributed_job_status.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribePreCheckStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePreCheckStatusResponseBody = None,
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
            temp_model = DescribePreCheckStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstanceAlertRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DescribeSubscriptionInstanceAlertResponseBody(TeaModel):
    def __init__(
        self,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        err_code: str = None,
        err_message: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        request_id: str = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        success: str = None,
    ):
        self.delay_alert_phone = delay_alert_phone
        self.delay_alert_status = delay_alert_status
        self.delay_over_seconds = delay_over_seconds
        self.err_code = err_code
        self.err_message = err_message
        self.error_alert_phone = error_alert_phone
        self.error_alert_status = error_alert_status
        self.request_id = request_id
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSubscriptionInstanceAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionInstanceAlertResponseBody = None,
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
            temp_model = DescribeSubscriptionInstanceAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType(TeaModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        self.ddl = ddl
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['DDL'] = self.ddl
        if self.dml is not None:
            result['DML'] = self.dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionHost(TeaModel):
    def __init__(
        self,
        private_host: str = None,
        public_host: str = None,
        vpchost: str = None,
    ):
        self.private_host = private_host
        self.public_host = public_host
        self.vpchost = vpchost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        if self.vpchost is not None:
            result['VPCHost'] = self.vpchost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        if m.get('VPCHost') is not None:
            self.vpchost = m.get('VPCHost')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        self.database_name = database_name
        self.table_list = table_list
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableList') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for k in self.synchronous_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k in self.synchronous_object:
                result['SynchronousObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k in m.get('SynchronousObject'):
                temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        begin_timestamp: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        end_timestamp: str = None,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        pay_type: str = None,
        request_id: str = None,
        source_endpoint: DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint = None,
        status: str = None,
        subscribe_topic: str = None,
        subscription_data_type: DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType = None,
        subscription_host: DescribeSubscriptionInstanceStatusResponseBodySubscriptionHost = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_object: DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject = None,
        success: str = None,
        task_id: str = None,
    ):
        self.begin_timestamp = begin_timestamp
        self.consumption_checkpoint = consumption_checkpoint
        self.consumption_client = consumption_client
        self.end_timestamp = end_timestamp
        self.err_code = err_code
        self.err_message = err_message
        self.error_message = error_message
        self.pay_type = pay_type
        self.request_id = request_id
        self.source_endpoint = source_endpoint
        self.status = status
        self.subscribe_topic = subscribe_topic
        self.subscription_data_type = subscription_data_type
        self.subscription_host = subscription_host
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.subscription_object = subscription_object
        self.success = success
        self.task_id = task_id

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_host:
            self.subscription_host.validate()
        if self.subscription_object:
            self.subscription_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_host is not None:
            result['SubscriptionHost'] = self.subscription_host.to_map()
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionHost') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionHost()
            self.subscription_host = temp_model.from_map(m['SubscriptionHost'])
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionObject') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject()
            self.subscription_object = temp_model.from_map(m['SubscriptionObject'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeSubscriptionInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionInstanceStatusResponseBody = None,
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
            temp_model = DescribeSubscriptionInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstancesRequestTag(TeaModel):
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


class DescribeSubscriptionInstancesRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        subscription_instance_name: str = None,
        tag: List[DescribeSubscriptionInstancesRequestTag] = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.subscription_instance_name = subscription_instance_name
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSubscriptionInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType(TeaModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        self.ddl = ddl
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['DDL'] = self.ddl
        if self.dml is not None:
            result['DML'] = self.dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost(TeaModel):
    def __init__(
        self,
        private_host: str = None,
        public_host: str = None,
        vpchost: str = None,
    ):
        self.private_host = private_host
        self.public_host = public_host
        self.vpchost = vpchost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        if self.vpchost is not None:
            result['VPCHost'] = self.vpchost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        if m.get('VPCHost') is not None:
            self.vpchost = m.get('VPCHost')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        self.database_name = database_name
        self.table_list = table_list
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableList') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for k in self.synchronous_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k in self.synchronous_object:
                result['SynchronousObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k in m.get('SynchronousObject'):
                temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag(TeaModel):
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


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag] = None,
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
                temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance(TeaModel):
    def __init__(
        self,
        begin_timestamp: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        end_timestamp: str = None,
        error_message: str = None,
        instance_create_time: str = None,
        job_create_time: str = None,
        pay_type: str = None,
        source_endpoint: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint = None,
        status: str = None,
        subscribe_topic: str = None,
        subscription_data_type: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType = None,
        subscription_host: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_object: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject = None,
        tags: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags = None,
    ):
        self.begin_timestamp = begin_timestamp
        self.consumption_checkpoint = consumption_checkpoint
        self.consumption_client = consumption_client
        self.end_timestamp = end_timestamp
        self.error_message = error_message
        self.instance_create_time = instance_create_time
        self.job_create_time = job_create_time
        self.pay_type = pay_type
        self.source_endpoint = source_endpoint
        self.status = status
        self.subscribe_topic = subscribe_topic
        self.subscription_data_type = subscription_data_type
        self.subscription_host = subscription_host
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.subscription_object = subscription_object
        self.tags = tags

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_host:
            self.subscription_host.validate()
        if self.subscription_object:
            self.subscription_object.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time
        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_host is not None:
            result['SubscriptionHost'] = self.subscription_host.to_map()
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')
        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionHost') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost()
            self.subscription_host = temp_model.from_map(m['SubscriptionHost'])
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionObject') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject()
            self.subscription_object = temp_model.from_map(m['SubscriptionObject'])
        if m.get('Tags') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstances(TeaModel):
    def __init__(
        self,
        subscription_instance: List[DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance] = None,
    ):
        self.subscription_instance = subscription_instance

    def validate(self):
        if self.subscription_instance:
            for k in self.subscription_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubscriptionInstance'] = []
        if self.subscription_instance is not None:
            for k in self.subscription_instance:
                result['SubscriptionInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_instance = []
        if m.get('SubscriptionInstance') is not None:
            for k in m.get('SubscriptionInstance'):
                temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance()
                self.subscription_instance.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstancesResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        subscription_instances: DescribeSubscriptionInstancesResponseBodySubscriptionInstances = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.subscription_instances = subscription_instances
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        if self.subscription_instances:
            self.subscription_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_instances is not None:
            result['SubscriptionInstances'] = self.subscription_instances.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionInstances') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstances()
            self.subscription_instances = temp_model.from_map(m['SubscriptionInstances'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSubscriptionInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionInstancesResponseBody = None,
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
            temp_model = DescribeSubscriptionInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionMetaRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        region_id: str = None,
        sid: str = None,
        sub_migration_job_ids: Dict[str, Any] = None,
        topics: Dict[str, Any] = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.region_id = region_id
        self.sid = sid
        self.sub_migration_job_ids = sub_migration_job_ids
        self.topics = topics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.sub_migration_job_ids is not None:
            result['SubMigrationJobIds'] = self.sub_migration_job_ids
        if self.topics is not None:
            result['Topics'] = self.topics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('SubMigrationJobIds') is not None:
            self.sub_migration_job_ids = m.get('SubMigrationJobIds')
        if m.get('Topics') is not None:
            self.topics = m.get('Topics')
        return self


class DescribeSubscriptionMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        region_id: str = None,
        sid: str = None,
        sub_migration_job_ids_shrink: str = None,
        topics_shrink: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.region_id = region_id
        self.sid = sid
        self.sub_migration_job_ids_shrink = sub_migration_job_ids_shrink
        self.topics_shrink = topics_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.sub_migration_job_ids_shrink is not None:
            result['SubMigrationJobIds'] = self.sub_migration_job_ids_shrink
        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('SubMigrationJobIds') is not None:
            self.sub_migration_job_ids_shrink = m.get('SubMigrationJobIds')
        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')
        return self


class DescribeSubscriptionMetaResponseBodySubscriptionMetaList(TeaModel):
    def __init__(
        self,
        checkpoint: int = None,
        dblist: str = None,
        dproxy_url: str = None,
        sid: str = None,
        topic: str = None,
    ):
        self.checkpoint = checkpoint
        self.dblist = dblist
        self.dproxy_url = dproxy_url
        self.sid = sid
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.dblist is not None:
            result['DBList'] = self.dblist
        if self.dproxy_url is not None:
            result['DProxyUrl'] = self.dproxy_url
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DBList') is not None:
            self.dblist = m.get('DBList')
        if m.get('DProxyUrl') is not None:
            self.dproxy_url = m.get('DProxyUrl')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DescribeSubscriptionMetaResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        subscription_meta_list: List[DescribeSubscriptionMetaResponseBodySubscriptionMetaList] = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.subscription_meta_list = subscription_meta_list
        self.success = success

    def validate(self):
        if self.subscription_meta_list:
            for k in self.subscription_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubscriptionMetaList'] = []
        if self.subscription_meta_list is not None:
            for k in self.subscription_meta_list:
                result['SubscriptionMetaList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.subscription_meta_list = []
        if m.get('SubscriptionMetaList') is not None:
            for k in m.get('SubscriptionMetaList'):
                temp_model = DescribeSubscriptionMetaResponseBodySubscriptionMetaList()
                self.subscription_meta_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSubscriptionMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionMetaResponseBody = None,
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
            temp_model = DescribeSubscriptionMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobAlertRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeSynchronizationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        err_code: str = None,
        err_message: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        request_id: str = None,
        success: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
    ):
        self.delay_alert_phone = delay_alert_phone
        self.delay_alert_status = delay_alert_status
        self.delay_over_seconds = delay_over_seconds
        self.err_code = err_code
        self.err_message = err_message
        self.error_alert_phone = error_alert_phone
        self.error_alert_status = error_alert_status
        self.request_id = request_id
        self.success = success
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        return self


class DescribeSynchronizationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobAlertResponseBody = None,
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
            temp_model = DescribeSynchronizationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobReplicatorCompareRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeSynchronizationJobReplicatorCompareResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        synchronization_replicator_compare_enable: bool = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.synchronization_replicator_compare_enable = synchronization_replicator_compare_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_replicator_compare_enable is not None:
            result['SynchronizationReplicatorCompareEnable'] = self.synchronization_replicator_compare_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationReplicatorCompareEnable') is not None:
            self.synchronization_replicator_compare_enable = m.get('SynchronizationReplicatorCompareEnable')
        return self


class DescribeSynchronizationJobReplicatorCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobReplicatorCompareResponseBody = None,
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
            temp_model = DescribeSynchronizationJobReplicatorCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        delay: str = None,
        delay_millis: int = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.checkpoint = checkpoint
        self.delay = delay
        self.delay_millis = delay_millis
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.delay_millis is not None:
            result['DelayMillis'] = self.delay_millis
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DelayMillis') is not None:
            self.delay_millis = m.get('DelayMillis')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobStatusResponseBodyPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['FLOW'] = self.flow
        if self.rps is not None:
            result['RPS'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        return self


class DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationJobStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjects(TeaModel):
    def __init__(
        self,
        new_schema_name: str = None,
        schema_name: str = None,
        table_excludes: List[DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes] = None,
        table_includes: List[DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes] = None,
    ):
        self.new_schema_name = new_schema_name
        self.schema_name = schema_name
        self.table_excludes = table_excludes
        self.table_includes = table_includes

    def validate(self):
        if self.table_excludes:
            for k in self.table_excludes:
                if k:
                    k.validate()
        if self.table_includes:
            for k in self.table_includes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        result['TableExcludes'] = []
        if self.table_excludes is not None:
            for k in self.table_excludes:
                result['TableExcludes'].append(k.to_map() if k else None)
        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k in self.table_includes:
                result['TableIncludes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        self.table_excludes = []
        if m.get('TableExcludes') is not None:
            for k in m.get('TableExcludes'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k))
        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k in m.get('TableIncludes'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        data_initialization: str = None,
        data_initialization_status: DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus = None,
        delay: str = None,
        delay_millis: int = None,
        destination_endpoint: DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint = None,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        expire_time: str = None,
        pay_type: str = None,
        performance: DescribeSynchronizationJobStatusResponseBodyPerformance = None,
        precheck_status: DescribeSynchronizationJobStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        source_endpoint: DescribeSynchronizationJobStatusResponseBodySourceEndpoint = None,
        status: str = None,
        structure_initialization: str = None,
        structure_initialization_status: DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus = None,
        success: str = None,
        synchronization_direction: str = None,
        synchronization_job_class: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: List[DescribeSynchronizationJobStatusResponseBodySynchronizationObjects] = None,
        task_id: str = None,
    ):
        self.checkpoint = checkpoint
        self.data_initialization = data_initialization
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.delay = delay
        self.delay_millis = delay_millis
        self.destination_endpoint = destination_endpoint
        self.err_code = err_code
        self.err_message = err_message
        self.error_message = error_message
        self.expire_time = expire_time
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.request_id = request_id
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization = structure_initialization
        self.structure_initialization_status = structure_initialization_status
        self.success = success
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_class = synchronization_job_class
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_objects = synchronization_objects
        self.task_id = task_id

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.synchronization_objects:
            for k in self.synchronization_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.delay_millis is not None:
            result['DelayMillis'] = self.delay_millis
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DelayMillis') is not None:
            self.delay_millis = m.get('DelayMillis')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k in m.get('SynchronizationObjects'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeSynchronizationJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobStatusResponseBody = None,
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
            temp_model = DescribeSynchronizationJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobStatusListRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_job_id_list_json_str: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_job_id_list_json_str = synchronization_job_id_list_json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id_list_json_str is not None:
            result['SynchronizationJobIdListJsonStr'] = self.synchronization_job_id_list_json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobIdListJsonStr') is not None:
            self.synchronization_job_id_list_json_str = m.get('SynchronizationJobIdListJsonStr')
        return self


class DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        status: str = None,
        synchronization_direction: str = None,
    ):
        self.checkpoint = checkpoint
        self.status = status
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.status is not None:
            result['Status'] = self.status
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList(TeaModel):
    def __init__(
        self,
        synchronization_direction_info_list: List[DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList] = None,
        synchronization_job_id: str = None,
    ):
        self.synchronization_direction_info_list = synchronization_direction_info_list
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        if self.synchronization_direction_info_list:
            for k in self.synchronization_direction_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronizationDirectionInfoList'] = []
        if self.synchronization_direction_info_list is not None:
            for k in self.synchronization_direction_info_list:
                result['SynchronizationDirectionInfoList'].append(k.to_map() if k else None)
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronization_direction_info_list = []
        if m.get('SynchronizationDirectionInfoList') is not None:
            for k in m.get('SynchronizationDirectionInfoList'):
                temp_model = DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList()
                self.synchronization_direction_info_list.append(temp_model.from_map(k))
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeSynchronizationJobStatusListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        synchronization_job_list_status_list: List[DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList] = None,
        total_record_count: int = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.success = success
        self.synchronization_job_list_status_list = synchronization_job_list_status_list
        self.total_record_count = total_record_count

    def validate(self):
        if self.synchronization_job_list_status_list:
            for k in self.synchronization_job_list_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['SynchronizationJobListStatusList'] = []
        if self.synchronization_job_list_status_list is not None:
            for k in self.synchronization_job_list_status_list:
                result['SynchronizationJobListStatusList'].append(k.to_map() if k else None)
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.synchronization_job_list_status_list = []
        if m.get('SynchronizationJobListStatusList') is not None:
            for k in m.get('SynchronizationJobListStatusList'):
                temp_model = DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList()
                self.synchronization_job_list_status_list.append(temp_model.from_map(k))
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSynchronizationJobStatusListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobStatusListResponseBody = None,
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
            temp_model = DescribeSynchronizationJobStatusListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobsRequestTag(TeaModel):
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


class DescribeSynchronizationJobsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        synchronization_job_name: str = None,
        tag: List[DescribeSynchronizationJobsRequestTag] = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id
        self.synchronization_job_name = synchronization_job_name
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSynchronizationJobsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint(TeaModel):
    def __init__(
        self,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['FLOW'] = self.flow
        if self.rps is not None:
            result['RPS'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint(TeaModel):
    def __init__(
        self,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects(TeaModel):
    def __init__(
        self,
        new_schema_name: str = None,
        schema_name: str = None,
        table_excludes: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes] = None,
        table_includes: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes] = None,
    ):
        self.new_schema_name = new_schema_name
        self.schema_name = schema_name
        self.table_excludes = table_excludes
        self.table_includes = table_includes

    def validate(self):
        if self.table_excludes:
            for k in self.table_excludes:
                if k:
                    k.validate()
        if self.table_includes:
            for k in self.table_includes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        result['TableExcludes'] = []
        if self.table_excludes is not None:
            for k in self.table_excludes:
                result['TableExcludes'].append(k.to_map() if k else None)
        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k in self.table_includes:
                result['TableIncludes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        self.table_excludes = []
        if m.get('TableExcludes') is not None:
            for k in m.get('TableExcludes'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k))
        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k in m.get('TableIncludes'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags(TeaModel):
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


class DescribeSynchronizationJobsResponseBodySynchronizationInstances(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_initialization: str = None,
        data_initialization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus = None,
        delay: str = None,
        destination_endpoint: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint = None,
        error_message: str = None,
        expire_time: str = None,
        instance_create_time: str = None,
        job_create_time: str = None,
        pay_type: str = None,
        performance: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance = None,
        precheck_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus = None,
        source_endpoint: DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint = None,
        status: str = None,
        structure_initialization: str = None,
        structure_initialization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus = None,
        synchronization_direction: str = None,
        synchronization_job_class: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects] = None,
        tags: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags] = None,
    ):
        self.create_time = create_time
        self.data_initialization = data_initialization
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.delay = delay
        self.destination_endpoint = destination_endpoint
        self.error_message = error_message
        self.expire_time = expire_time
        self.instance_create_time = instance_create_time
        self.job_create_time = job_create_time
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization = structure_initialization
        self.structure_initialization_status = structure_initialization_status
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_class = synchronization_job_class
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_objects = synchronization_objects
        self.tags = tags

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.synchronization_objects:
            for k in self.synchronization_objects:
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time
        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')
        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k in m.get('SynchronizationObjects'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        synchronization_instances: List[DescribeSynchronizationJobsResponseBodySynchronizationInstances] = None,
        total_record_count: int = None,
    ):
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.synchronization_instances = synchronization_instances
        self.total_record_count = total_record_count

    def validate(self):
        if self.synchronization_instances:
            for k in self.synchronization_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SynchronizationInstances'] = []
        if self.synchronization_instances is not None:
            for k in self.synchronization_instances:
                result['SynchronizationInstances'].append(k.to_map() if k else None)
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.synchronization_instances = []
        if m.get('SynchronizationInstances') is not None:
            for k in m.get('SynchronizationInstances'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstances()
                self.synchronization_instances.append(temp_model.from_map(k))
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSynchronizationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobsResponseBody = None,
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
            temp_model = DescribeSynchronizationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationObjectModifyStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_status: DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus = None,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        precheck_status: DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        status: str = None,
        structure_initialization_status: DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus = None,
        success: str = None,
    ):
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.err_code = err_code
        self.err_message = err_message
        self.error_message = error_message
        self.precheck_status = precheck_status
        self.request_id = request_id
        self.status = status
        self.structure_initialization_status = structure_initialization_status
        self.success = success

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSynchronizationObjectModifyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationObjectModifyStatusResponseBody = None,
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
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitDtsRdsInstanceRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        endpoint_cen_id: str = None,
        endpoint_instance_id: str = None,
        endpoint_instance_type: str = None,
        endpoint_region: str = None,
        region_id: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.endpoint_cen_id = endpoint_cen_id
        self.endpoint_instance_id = endpoint_instance_id
        self.endpoint_instance_type = endpoint_instance_type
        self.endpoint_region = endpoint_region
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.endpoint_cen_id is not None:
            result['EndpointCenId'] = self.endpoint_cen_id
        if self.endpoint_instance_id is not None:
            result['EndpointInstanceId'] = self.endpoint_instance_id
        if self.endpoint_instance_type is not None:
            result['EndpointInstanceType'] = self.endpoint_instance_type
        if self.endpoint_region is not None:
            result['EndpointRegion'] = self.endpoint_region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('EndpointCenId') is not None:
            self.endpoint_cen_id = m.get('EndpointCenId')
        if m.get('EndpointInstanceId') is not None:
            self.endpoint_instance_id = m.get('EndpointInstanceId')
        if m.get('EndpointInstanceType') is not None:
            self.endpoint_instance_type = m.get('EndpointInstanceType')
        if m.get('EndpointRegion') is not None:
            self.endpoint_region = m.get('EndpointRegion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InitDtsRdsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        admin_account: str = None,
        admin_password: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.admin_account = admin_account
        self.admin_password = admin_password
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_account is not None:
            result['AdminAccount'] = self.admin_account
        if self.admin_password is not None:
            result['AdminPassword'] = self.admin_password
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminAccount') is not None:
            self.admin_account = m.get('AdminAccount')
        if m.get('AdminPassword') is not None:
            self.admin_password = m.get('AdminPassword')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InitDtsRdsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitDtsRdsInstanceResponseBody = None,
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
            temp_model = InitDtsRdsInstanceResponseBody()
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
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
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
        err_code: str = None,
        err_message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class ModifyConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_password = consumer_group_password
        self.consumer_group_user_name = consumer_group_user_name
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyConsumerChannelResponseBody = None,
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
            temp_model = ModifyConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyConsumerGroupPasswordRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
        consumer_group_new_password: str = None,
    ):
        self.account_id = account_id
        self.consumer_group_id = consumer_group_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_password = consumer_group_password
        self.consumer_group_user_name = consumer_group_user_name
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.consumer_group_new_password = consumer_group_new_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.consumer_group_new_password is not None:
            result['consumerGroupNewPassword'] = self.consumer_group_new_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('consumerGroupNewPassword') is not None:
            self.consumer_group_new_password = m.get('consumerGroupNewPassword')
        return self


class ModifyConsumerGroupPasswordResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyConsumerGroupPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyConsumerGroupPasswordResponseBody = None,
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
            temp_model = ModifyConsumerGroupPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyConsumptionTimestampRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        consumption_timestamp: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.consumption_timestamp = consumption_timestamp
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.consumption_timestamp is not None:
            result['ConsumptionTimestamp'] = self.consumption_timestamp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConsumptionTimestamp') is not None:
            self.consumption_timestamp = m.get('ConsumptionTimestamp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class ModifyConsumptionTimestampResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyConsumptionTimestampResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyConsumptionTimestampResponseBody = None,
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
            temp_model = ModifyConsumptionTimestampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDtsJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        db_list: Dict[str, Any] = None,
        dts_instance_id: str = None,
        etl_operator_column_reference: str = None,
        modify_type_enum: str = None,
        region_id: str = None,
        reserved: str = None,
        synchronization_direction: str = None,
    ):
        self.client_token = client_token
        self.db_list = db_list
        self.dts_instance_id = dts_instance_id
        self.etl_operator_column_reference = etl_operator_column_reference
        # 修改任务的方式，当为UPDATE_RESERVED时为修改reserve字段，不传默认修改dbList
        self.modify_type_enum = modify_type_enum
        self.region_id = region_id
        # 新增的reserved字段，新增而不是覆盖
        self.reserved = reserved
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.etl_operator_column_reference is not None:
            result['EtlOperatorColumnReference'] = self.etl_operator_column_reference
        if self.modify_type_enum is not None:
            result['ModifyTypeEnum'] = self.modify_type_enum
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('EtlOperatorColumnReference') is not None:
            self.etl_operator_column_reference = m.get('EtlOperatorColumnReference')
        if m.get('ModifyTypeEnum') is not None:
            self.modify_type_enum = m.get('ModifyTypeEnum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class ModifyDtsJobShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        db_list_shrink: str = None,
        dts_instance_id: str = None,
        etl_operator_column_reference: str = None,
        modify_type_enum: str = None,
        region_id: str = None,
        reserved: str = None,
        synchronization_direction: str = None,
    ):
        self.client_token = client_token
        self.db_list_shrink = db_list_shrink
        self.dts_instance_id = dts_instance_id
        self.etl_operator_column_reference = etl_operator_column_reference
        # 修改任务的方式，当为UPDATE_RESERVED时为修改reserve字段，不传默认修改dbList
        self.modify_type_enum = modify_type_enum
        self.region_id = region_id
        # 新增的reserved字段，新增而不是覆盖
        self.reserved = reserved
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.db_list_shrink is not None:
            result['DbList'] = self.db_list_shrink
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.etl_operator_column_reference is not None:
            result['EtlOperatorColumnReference'] = self.etl_operator_column_reference
        if self.modify_type_enum is not None:
            result['ModifyTypeEnum'] = self.modify_type_enum
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbList') is not None:
            self.db_list_shrink = m.get('DbList')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('EtlOperatorColumnReference') is not None:
            self.etl_operator_column_reference = m.get('EtlOperatorColumnReference')
        if m.get('ModifyTypeEnum') is not None:
            self.modify_type_enum = m.get('ModifyTypeEnum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class ModifyDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        err_code: str = None,
        err_message: bool = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDtsJobResponseBody = None,
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
            temp_model = ModifyDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDtsJobNameRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_job_name: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDtsJobNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDtsJobNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDtsJobNameResponseBody = None,
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
            temp_model = ModifyDtsJobNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDtsJobPasswordRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        endpoint: str = None,
        password: str = None,
        region_id: str = None,
        user_name: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.endpoint = endpoint
        self.password = password
        self.region_id = region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyDtsJobPasswordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDtsJobPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDtsJobPasswordResponseBody = None,
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
            temp_model = ModifyDtsJobPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubscriptionRequest(TeaModel):
    def __init__(
        self,
        db_list: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        subscription_data_type_ddl: bool = None,
        subscription_data_type_dml: bool = None,
    ):
        self.db_list = db_list
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id
        self.subscription_data_type_ddl = subscription_data_type_ddl
        self.subscription_data_type_dml = subscription_data_type_dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_data_type_ddl is not None:
            result['SubscriptionDataTypeDDL'] = self.subscription_data_type_ddl
        if self.subscription_data_type_dml is not None:
            result['SubscriptionDataTypeDML'] = self.subscription_data_type_dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionDataTypeDDL') is not None:
            self.subscription_data_type_ddl = m.get('SubscriptionDataTypeDDL')
        if m.get('SubscriptionDataTypeDML') is not None:
            self.subscription_data_type_dml = m.get('SubscriptionDataTypeDML')
        return self


class ModifySubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySubscriptionResponseBody = None,
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
            temp_model = ModifySubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubscriptionObjectRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
        subscription_object: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.subscription_object = subscription_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('SubscriptionObject') is not None:
            self.subscription_object = m.get('SubscriptionObject')
        return self


class ModifySubscriptionObjectResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySubscriptionObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySubscriptionObjectResponseBody = None,
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
            temp_model = ModifySubscriptionObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySynchronizationObjectRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
        synchronization_objects: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_objects = synchronization_objects

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        return self


class ModifySynchronizationObjectResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifySynchronizationObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySynchronizationObjectResponseBody = None,
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
            temp_model = ModifySynchronizationObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        buy_count: str = None,
        charge_type: str = None,
        dts_job_id: str = None,
        period: str = None,
        region_id: str = None,
    ):
        self.buy_count = buy_count
        self.charge_type = charge_type
        self.dts_job_id = dts_job_id
        self.period = period
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        code: str = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        end_time: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.charge_type = charge_type
        self.code = code
        self.dts_job_id = dts_job_id
        self.dynamic_message = dynamic_message
        self.end_time = end_time
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.code is not None:
            result['Code'] = self.code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class ResetDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetDtsJobResponseBody = None,
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
            temp_model = ResetDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class ResetSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetSynchronizationJobResponseBody = None,
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
            temp_model = ResetSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShieldPrecheckRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        precheck_items: str = None,
        region_id: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.precheck_items = precheck_items
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.precheck_items is not None:
            result['PrecheckItems'] = self.precheck_items
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('PrecheckItems') is not None:
            self.precheck_items = m.get('PrecheckItems')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ShieldPrecheckResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ShieldPrecheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ShieldPrecheckResponseBody = None,
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
            temp_model = ShieldPrecheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipPreCheckRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_id: str = None,
        region_id: str = None,
        skip: bool = None,
        skip_pre_check_items: str = None,
        skip_pre_check_names: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.job_id = job_id
        self.region_id = region_id
        self.skip = skip
        self.skip_pre_check_items = skip_pre_check_items
        self.skip_pre_check_names = skip_pre_check_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.skip_pre_check_items is not None:
            result['SkipPreCheckItems'] = self.skip_pre_check_items
        if self.skip_pre_check_names is not None:
            result['SkipPreCheckNames'] = self.skip_pre_check_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('SkipPreCheckItems') is not None:
            self.skip_pre_check_items = m.get('SkipPreCheckItems')
        if m.get('SkipPreCheckNames') is not None:
            self.skip_pre_check_names = m.get('SkipPreCheckNames')
        return self


class SkipPreCheckResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        migration_job_id: str = None,
        request_id: str = None,
        schedule_job_id: str = None,
        skip_items: str = None,
        skip_names: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.migration_job_id = migration_job_id
        self.request_id = request_id
        self.schedule_job_id = schedule_job_id
        self.skip_items = skip_items
        self.skip_names = skip_names
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_job_id is not None:
            result['ScheduleJobId'] = self.schedule_job_id
        if self.skip_items is not None:
            result['SkipItems'] = self.skip_items
        if self.skip_names is not None:
            result['SkipNames'] = self.skip_names
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleJobId') is not None:
            self.schedule_job_id = m.get('ScheduleJobId')
        if m.get('SkipItems') is not None:
            self.skip_items = m.get('SkipItems')
        if m.get('SkipNames') is not None:
            self.skip_names = m.get('SkipNames')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SkipPreCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SkipPreCheckResponseBody = None,
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
            temp_model = SkipPreCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class StartDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDtsJobResponseBody = None,
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
            temp_model = StartDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMigrationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartMigrationJobResponseBody = None,
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
            temp_model = StartMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class StartSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartSubscriptionInstanceResponseBody = None,
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
            temp_model = StartSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class StartSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartSynchronizationJobResponseBody = None,
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
            temp_model = StartSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class StopDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDtsJobResponseBody = None,
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
            temp_model = StopDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMigrationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopMigrationJobResponseBody = None,
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
            temp_model = StopMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class SuspendDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendDtsJobResponseBody = None,
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
            temp_model = SuspendDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendMigrationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SuspendMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendMigrationJobResponseBody = None,
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
            temp_model = SuspendMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class SuspendSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendSynchronizationJobResponseBody = None,
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
            temp_model = SuspendSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSynchronizationEndpointRequestEndpoint(TeaModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        type: str = None,
    ):
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SwitchSynchronizationEndpointRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        role: str = None,
    ):
        self.owner_id = owner_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class SwitchSynchronizationEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint: SwitchSynchronizationEndpointRequestEndpoint = None,
        source_endpoint: SwitchSynchronizationEndpointRequestSourceEndpoint = None,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.endpoint = endpoint
        self.source_endpoint = source_endpoint
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        if self.endpoint:
            self.endpoint.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            temp_model = SwitchSynchronizationEndpointRequestEndpoint()
            self.endpoint = temp_model.from_map(m['Endpoint'])
        if m.get('SourceEndpoint') is not None:
            temp_model = SwitchSynchronizationEndpointRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class SwitchSynchronizationEndpointResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SwitchSynchronizationEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SwitchSynchronizationEndpointResponseBody = None,
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
            temp_model = SwitchSynchronizationEndpointResponseBody()
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
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class TransferInstanceClassRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        instance_class: str = None,
        order_type: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.instance_class = instance_class
        self.order_type = order_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class TransferInstanceClassResponseBody(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        code: str = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        end_time: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.charge_type = charge_type
        self.code = code
        self.dts_job_id = dts_job_id
        self.dynamic_message = dynamic_message
        self.end_time = end_time
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.code is not None:
            result['Code'] = self.code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferInstanceClassResponseBody = None,
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
            temp_model = TransferInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferPayTypeRequest(TeaModel):
    def __init__(
        self,
        buy_count: str = None,
        charge_type: str = None,
        dts_job_id: str = None,
        period: str = None,
        region_id: str = None,
    ):
        self.buy_count = buy_count
        self.charge_type = charge_type
        self.dts_job_id = dts_job_id
        self.period = period
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class TransferPayTypeResponseBody(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        code: str = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        end_time: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.charge_type = charge_type
        self.code = code
        self.dts_job_id = dts_job_id
        self.dynamic_message = dynamic_message
        self.end_time = end_time
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.code is not None:
            result['Code'] = self.code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferPayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferPayTypeResponseBody = None,
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
            temp_model = TransferPayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class UpgradeTwoWayRequest(TeaModel):
    def __init__(
        self,
        instance_class: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpgradeTwoWayResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeTwoWayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeTwoWayResponseBody = None,
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
            temp_model = UpgradeTwoWayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WhiteIpListRequest(TeaModel):
    def __init__(
        self,
        destination_region: str = None,
        region: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.destination_region = destination_region
        self.region = region
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class WhiteIpListResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        ip_list: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.ip_list = ip_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WhiteIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WhiteIpListResponseBody = None,
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
            temp_model = WhiteIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


