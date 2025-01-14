# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ColDetailModel(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        create_time: str = None,
        description: str = None,
        distribute_key: bool = None,
        nullable: bool = None,
        partition_key: bool = None,
        primary_key: bool = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.column_name = column_name
        self.create_time = create_time
        self.description = description
        self.distribute_key = distribute_key
        self.nullable = nullable
        self.partition_key = partition_key
        self.primary_key = primary_key
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.distribute_key is not None:
            result['DistributeKey'] = self.distribute_key
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributeKey') is not None:
            self.distribute_key = m.get('DistributeKey')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('PartitionKey') is not None:
            self.partition_key = m.get('PartitionKey')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class FieldSchemaModel(TeaModel):
    def __init__(
        self,
        auto_increment: bool = None,
        column_raw_name: str = None,
        comment: str = None,
        compress_float_use_short: bool = None,
        compression: str = None,
        create_time: str = None,
        data_type: str = None,
        database_name: str = None,
        default_value: str = None,
        delimiter: str = None,
        encode: str = None,
        is_partition_key: bool = None,
        mapped_name: str = None,
        name: str = None,
        nullable: bool = None,
        on_update: str = None,
        ordinal_position: int = None,
        physical_column_name: str = None,
        pk_position: int = None,
        precision: int = None,
        primarykey: bool = None,
        scale: int = None,
        table_name: str = None,
        tokenizer: str = None,
        type: str = None,
        update_time: str = None,
        value_type: str = None,
    ):
        self.auto_increment = auto_increment
        self.column_raw_name = column_raw_name
        self.comment = comment
        self.compress_float_use_short = compress_float_use_short
        self.compression = compression
        self.create_time = create_time
        self.data_type = data_type
        self.database_name = database_name
        self.default_value = default_value
        self.delimiter = delimiter
        self.encode = encode
        self.is_partition_key = is_partition_key
        self.mapped_name = mapped_name
        self.name = name
        self.nullable = nullable
        self.on_update = on_update
        self.ordinal_position = ordinal_position
        self.physical_column_name = physical_column_name
        self.pk_position = pk_position
        self.precision = precision
        self.primarykey = primarykey
        self.scale = scale
        self.table_name = table_name
        self.tokenizer = tokenizer
        self.type = type
        self.update_time = update_time
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment
        if self.column_raw_name is not None:
            result['ColumnRawName'] = self.column_raw_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.compress_float_use_short is not None:
            result['CompressFloatUseShort'] = self.compress_float_use_short
        if self.compression is not None:
            result['Compression'] = self.compression
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encode is not None:
            result['Encode'] = self.encode
        if self.is_partition_key is not None:
            result['IsPartitionKey'] = self.is_partition_key
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        if self.name is not None:
            result['Name'] = self.name
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.on_update is not None:
            result['OnUpdate'] = self.on_update
        if self.ordinal_position is not None:
            result['OrdinalPosition'] = self.ordinal_position
        if self.physical_column_name is not None:
            result['PhysicalColumnName'] = self.physical_column_name
        if self.pk_position is not None:
            result['PkPosition'] = self.pk_position
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.primarykey is not None:
            result['Primarykey'] = self.primarykey
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tokenizer is not None:
            result['Tokenizer'] = self.tokenizer
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')
        if m.get('ColumnRawName') is not None:
            self.column_raw_name = m.get('ColumnRawName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CompressFloatUseShort') is not None:
            self.compress_float_use_short = m.get('CompressFloatUseShort')
        if m.get('Compression') is not None:
            self.compression = m.get('Compression')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('Encode') is not None:
            self.encode = m.get('Encode')
        if m.get('IsPartitionKey') is not None:
            self.is_partition_key = m.get('IsPartitionKey')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('OnUpdate') is not None:
            self.on_update = m.get('OnUpdate')
        if m.get('OrdinalPosition') is not None:
            self.ordinal_position = m.get('OrdinalPosition')
        if m.get('PhysicalColumnName') is not None:
            self.physical_column_name = m.get('PhysicalColumnName')
        if m.get('PkPosition') is not None:
            self.pk_position = m.get('PkPosition')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Primarykey') is not None:
            self.primarykey = m.get('Primarykey')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tokenizer') is not None:
            self.tokenizer = m.get('Tokenizer')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class CstoreIndexModel(TeaModel):
    def __init__(
        self,
        column_ords: List[str] = None,
        create_time: str = None,
        database_name: str = None,
        index_columns: List[FieldSchemaModel] = None,
        index_name: str = None,
        index_type: str = None,
        options: Dict[str, str] = None,
        physical_table_name: str = None,
        update_time: str = None,
    ):
        self.column_ords = column_ords
        self.create_time = create_time
        self.database_name = database_name
        self.index_columns = index_columns
        self.index_name = index_name
        self.index_type = index_type
        self.options = options
        self.physical_table_name = physical_table_name
        self.update_time = update_time

    def validate(self):
        if self.index_columns:
            for k in self.index_columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_ords is not None:
            result['ColumnOrds'] = self.column_ords
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        result['IndexColumns'] = []
        if self.index_columns is not None:
            for k in self.index_columns:
                result['IndexColumns'].append(k.to_map() if k else None)
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.index_type is not None:
            result['IndexType'] = self.index_type
        if self.options is not None:
            result['Options'] = self.options
        if self.physical_table_name is not None:
            result['PhysicalTableName'] = self.physical_table_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnOrds') is not None:
            self.column_ords = m.get('ColumnOrds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        self.index_columns = []
        if m.get('IndexColumns') is not None:
            for k in m.get('IndexColumns'):
                temp_model = FieldSchemaModel()
                self.index_columns.append(temp_model.from_map(k))
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('PhysicalTableName') is not None:
            self.physical_table_name = m.get('PhysicalTableName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DatabaseSummaryModel(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        owner: str = None,
        schema_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.owner = owner
        self.schema_name = schema_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Detail(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        data: str = None,
        duration_in_millis: int = None,
        estimate_execution_cpu_time_in_seconds: int = None,
        last_attempt_id: str = None,
        last_updated_time_in_millis: int = None,
        log_root_path: str = None,
        resource_group_name: str = None,
        started_time_in_millis: int = None,
        submitted_time_in_millis: int = None,
        terminated_time_in_millis: int = None,
        web_ui_address: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.data = data
        self.duration_in_millis = duration_in_millis
        self.estimate_execution_cpu_time_in_seconds = estimate_execution_cpu_time_in_seconds
        self.last_attempt_id = last_attempt_id
        self.last_updated_time_in_millis = last_updated_time_in_millis
        self.log_root_path = log_root_path
        self.resource_group_name = resource_group_name
        self.started_time_in_millis = started_time_in_millis
        self.submitted_time_in_millis = submitted_time_in_millis
        self.terminated_time_in_millis = terminated_time_in_millis
        self.web_ui_address = web_ui_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.data is not None:
            result['Data'] = self.data
        if self.duration_in_millis is not None:
            result['DurationInMillis'] = self.duration_in_millis
        if self.estimate_execution_cpu_time_in_seconds is not None:
            result['EstimateExecutionCpuTimeInSeconds'] = self.estimate_execution_cpu_time_in_seconds
        if self.last_attempt_id is not None:
            result['LastAttemptId'] = self.last_attempt_id
        if self.last_updated_time_in_millis is not None:
            result['LastUpdatedTimeInMillis'] = self.last_updated_time_in_millis
        if self.log_root_path is not None:
            result['LogRootPath'] = self.log_root_path
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.started_time_in_millis is not None:
            result['StartedTimeInMillis'] = self.started_time_in_millis
        if self.submitted_time_in_millis is not None:
            result['SubmittedTimeInMillis'] = self.submitted_time_in_millis
        if self.terminated_time_in_millis is not None:
            result['TerminatedTimeInMillis'] = self.terminated_time_in_millis
        if self.web_ui_address is not None:
            result['WebUiAddress'] = self.web_ui_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DurationInMillis') is not None:
            self.duration_in_millis = m.get('DurationInMillis')
        if m.get('EstimateExecutionCpuTimeInSeconds') is not None:
            self.estimate_execution_cpu_time_in_seconds = m.get('EstimateExecutionCpuTimeInSeconds')
        if m.get('LastAttemptId') is not None:
            self.last_attempt_id = m.get('LastAttemptId')
        if m.get('LastUpdatedTimeInMillis') is not None:
            self.last_updated_time_in_millis = m.get('LastUpdatedTimeInMillis')
        if m.get('LogRootPath') is not None:
            self.log_root_path = m.get('LogRootPath')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('StartedTimeInMillis') is not None:
            self.started_time_in_millis = m.get('StartedTimeInMillis')
        if m.get('SubmittedTimeInMillis') is not None:
            self.submitted_time_in_millis = m.get('SubmittedTimeInMillis')
        if m.get('TerminatedTimeInMillis') is not None:
            self.terminated_time_in_millis = m.get('TerminatedTimeInMillis')
        if m.get('WebUiAddress') is not None:
            self.web_ui_address = m.get('WebUiAddress')
        return self


class FiltersExecutionTimeRange(TeaModel):
    def __init__(
        self,
        max_time_in_seconds: int = None,
        min_time_in_seconds: int = None,
    ):
        self.max_time_in_seconds = max_time_in_seconds
        self.min_time_in_seconds = min_time_in_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_time_in_seconds is not None:
            result['MaxTimeInSeconds'] = self.max_time_in_seconds
        if self.min_time_in_seconds is not None:
            result['MinTimeInSeconds'] = self.min_time_in_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTimeInSeconds') is not None:
            self.max_time_in_seconds = m.get('MaxTimeInSeconds')
        if m.get('MinTimeInSeconds') is not None:
            self.min_time_in_seconds = m.get('MinTimeInSeconds')
        return self


class FiltersSubmitTimeRange(TeaModel):
    def __init__(
        self,
        max_time_in_mills: int = None,
        min_time_in_mills: int = None,
    ):
        self.max_time_in_mills = max_time_in_mills
        self.min_time_in_mills = min_time_in_mills

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_time_in_mills is not None:
            result['MaxTimeInMills'] = self.max_time_in_mills
        if self.min_time_in_mills is not None:
            result['MinTimeInMills'] = self.min_time_in_mills
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTimeInMills') is not None:
            self.max_time_in_mills = m.get('MaxTimeInMills')
        if m.get('MinTimeInMills') is not None:
            self.min_time_in_mills = m.get('MinTimeInMills')
        return self


class FiltersTermiatedTimeRange(TeaModel):
    def __init__(
        self,
        max_time_in_mills: int = None,
        min_time_in_mills: int = None,
    ):
        self.max_time_in_mills = max_time_in_mills
        self.min_time_in_mills = min_time_in_mills

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_time_in_mills is not None:
            result['MaxTimeInMills'] = self.max_time_in_mills
        if self.min_time_in_mills is not None:
            result['MinTimeInMills'] = self.min_time_in_mills
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTimeInMills') is not None:
            self.max_time_in_mills = m.get('MaxTimeInMills')
        if m.get('MinTimeInMills') is not None:
            self.min_time_in_mills = m.get('MinTimeInMills')
        return self


class Filters(TeaModel):
    def __init__(
        self,
        app_id_regex: str = None,
        app_name_regex: str = None,
        app_state: str = None,
        app_type: str = None,
        execution_time_range: FiltersExecutionTimeRange = None,
        submit_time_range: FiltersSubmitTimeRange = None,
        termiated_time_range: FiltersTermiatedTimeRange = None,
    ):
        self.app_id_regex = app_id_regex
        self.app_name_regex = app_name_regex
        self.app_state = app_state
        self.app_type = app_type
        self.execution_time_range = execution_time_range
        self.submit_time_range = submit_time_range
        self.termiated_time_range = termiated_time_range

    def validate(self):
        if self.execution_time_range:
            self.execution_time_range.validate()
        if self.submit_time_range:
            self.submit_time_range.validate()
        if self.termiated_time_range:
            self.termiated_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_regex is not None:
            result['AppIdRegex'] = self.app_id_regex
        if self.app_name_regex is not None:
            result['AppNameRegex'] = self.app_name_regex
        if self.app_state is not None:
            result['AppState'] = self.app_state
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.execution_time_range is not None:
            result['ExecutionTimeRange'] = self.execution_time_range.to_map()
        if self.submit_time_range is not None:
            result['SubmitTimeRange'] = self.submit_time_range.to_map()
        if self.termiated_time_range is not None:
            result['TermiatedTimeRange'] = self.termiated_time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdRegex') is not None:
            self.app_id_regex = m.get('AppIdRegex')
        if m.get('AppNameRegex') is not None:
            self.app_name_regex = m.get('AppNameRegex')
        if m.get('AppState') is not None:
            self.app_state = m.get('AppState')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ExecutionTimeRange') is not None:
            temp_model = FiltersExecutionTimeRange()
            self.execution_time_range = temp_model.from_map(m['ExecutionTimeRange'])
        if m.get('SubmitTimeRange') is not None:
            temp_model = FiltersSubmitTimeRange()
            self.submit_time_range = temp_model.from_map(m['SubmitTimeRange'])
        if m.get('TermiatedTimeRange') is not None:
            temp_model = FiltersTermiatedTimeRange()
            self.termiated_time_range = temp_model.from_map(m['TermiatedTimeRange'])
        return self


class LogAnalyzeResult(TeaModel):
    def __init__(
        self,
        app_error_advice: str = None,
        app_error_code: str = None,
        app_error_log: str = None,
    ):
        self.app_error_advice = app_error_advice
        self.app_error_code = app_error_code
        self.app_error_log = app_error_log

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_error_advice is not None:
            result['AppErrorAdvice'] = self.app_error_advice
        if self.app_error_code is not None:
            result['AppErrorCode'] = self.app_error_code
        if self.app_error_log is not None:
            result['AppErrorLog'] = self.app_error_log
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppErrorAdvice') is not None:
            self.app_error_advice = m.get('AppErrorAdvice')
        if m.get('AppErrorCode') is not None:
            self.app_error_code = m.get('AppErrorCode')
        if m.get('AppErrorLog') is not None:
            self.app_error_log = m.get('AppErrorLog')
        return self


class SerDeInfoModel(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        ser_de_id: int = None,
        serialization_lib: str = None,
    ):
        self.name = name
        self.parameters = parameters
        self.ser_de_id = ser_de_id
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_id is not None:
            result['SerDeId'] = self.ser_de_id
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeId') is not None:
            self.ser_de_id = m.get('SerDeId')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class SparkAnalyzeLogTask(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        result: LogAnalyzeResult = None,
        rule_matched: bool = None,
        started_time_in_millis: int = None,
        submitted_time_in_millis: int = None,
        task_err_msg: str = None,
        task_id: int = None,
        task_state: str = None,
        terminated_time_in_millis: int = None,
        user_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.result = result
        self.rule_matched = rule_matched
        self.started_time_in_millis = started_time_in_millis
        self.submitted_time_in_millis = submitted_time_in_millis
        self.task_err_msg = task_err_msg
        self.task_id = task_id
        self.task_state = task_state
        self.terminated_time_in_millis = terminated_time_in_millis
        self.user_id = user_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.rule_matched is not None:
            result['RuleMatched'] = self.rule_matched
        if self.started_time_in_millis is not None:
            result['StartedTimeInMillis'] = self.started_time_in_millis
        if self.submitted_time_in_millis is not None:
            result['SubmittedTimeInMillis'] = self.submitted_time_in_millis
        if self.task_err_msg is not None:
            result['TaskErrMsg'] = self.task_err_msg
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.terminated_time_in_millis is not None:
            result['TerminatedTimeInMillis'] = self.terminated_time_in_millis
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Result') is not None:
            temp_model = LogAnalyzeResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('RuleMatched') is not None:
            self.rule_matched = m.get('RuleMatched')
        if m.get('StartedTimeInMillis') is not None:
            self.started_time_in_millis = m.get('StartedTimeInMillis')
        if m.get('SubmittedTimeInMillis') is not None:
            self.submitted_time_in_millis = m.get('SubmittedTimeInMillis')
        if m.get('TaskErrMsg') is not None:
            self.task_err_msg = m.get('TaskErrMsg')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('TerminatedTimeInMillis') is not None:
            self.terminated_time_in_millis = m.get('TerminatedTimeInMillis')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SparkAppInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        dbcluster_id: str = None,
        detail: Detail = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.dbcluster_id = dbcluster_id
        self.detail = detail
        self.message = message
        self.state = state

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Detail') is not None:
            temp_model = Detail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SparkAttemptInfo(TeaModel):
    def __init__(
        self,
        attempt_id: str = None,
        detail: Detail = None,
        message: str = None,
        state: str = None,
    ):
        self.attempt_id = attempt_id
        self.detail = detail
        self.message = message
        self.state = state

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('Detail') is not None:
            temp_model = Detail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SparkSession(TeaModel):
    def __init__(
        self,
        active: str = None,
        aliyun_uid: int = None,
        session_id: int = None,
        state: str = None,
    ):
        self.active = active
        self.aliyun_uid = aliyun_uid
        self.session_id = session_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class Statement(TeaModel):
    def __init__(
        self,
        aliyun_uid: int = None,
        code: str = None,
        code_state: str = None,
        code_type: str = None,
        end_time: int = None,
        error: str = None,
        have_rows: bool = None,
        output: str = None,
        resource_group: str = None,
        session_id: int = None,
        start_time: int = None,
        statement_id: int = None,
        total_count: int = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.code = code
        self.code_state = code_state
        self.code_type = code_type
        self.end_time = end_time
        self.error = error
        self.have_rows = have_rows
        self.output = output
        self.resource_group = resource_group
        self.session_id = session_id
        self.start_time = start_time
        self.statement_id = statement_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.code is not None:
            result['Code'] = self.code
        if self.code_state is not None:
            result['CodeState'] = self.code_state
        if self.code_type is not None:
            result['CodeType'] = self.code_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error is not None:
            result['Error'] = self.error
        if self.have_rows is not None:
            result['HaveRows'] = self.have_rows
        if self.output is not None:
            result['Output'] = self.output
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statement_id is not None:
            result['StatementId'] = self.statement_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeState') is not None:
            self.code_state = m.get('CodeState')
        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('HaveRows') is not None:
            self.have_rows = m.get('HaveRows')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class StatementInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed_time_in_mills: int = None,
        output: str = None,
        process: float = None,
        started_time_in_mills: int = None,
        state: str = None,
        statement_id: str = None,
    ):
        self.code = code
        self.completed_time_in_mills = completed_time_in_mills
        self.output = output
        self.process = process
        self.started_time_in_mills = started_time_in_mills
        self.state = state
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed_time_in_mills is not None:
            result['CompletedTimeInMills'] = self.completed_time_in_mills
        if self.output is not None:
            result['Output'] = self.output
        if self.process is not None:
            result['Process'] = self.process
        if self.started_time_in_mills is not None:
            result['StartedTimeInMills'] = self.started_time_in_mills
        if self.state is not None:
            result['State'] = self.state
        if self.statement_id is not None:
            result['StatementId'] = self.statement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompletedTimeInMills') is not None:
            self.completed_time_in_mills = m.get('CompletedTimeInMills')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('StartedTimeInMills') is not None:
            self.started_time_in_mills = m.get('StartedTimeInMills')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')
        return self


class StorageDescriptorModel(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        input_format: str = None,
        location: str = None,
        num_buckets: int = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        sd_id: int = None,
        ser_de_info: SerDeInfoModel = None,
        stored_as_sub_directories: bool = None,
    ):
        self.compressed = compressed
        self.input_format = input_format
        self.location = location
        self.num_buckets = num_buckets
        self.output_format = output_format
        self.parameters = parameters
        self.sd_id = sd_id
        self.ser_de_info = ser_de_info
        self.stored_as_sub_directories = stored_as_sub_directories

    def validate(self):
        if self.ser_de_info:
            self.ser_de_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.num_buckets is not None:
            result['NumBuckets'] = self.num_buckets
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.sd_id is not None:
            result['SdId'] = self.sd_id
        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()
        if self.stored_as_sub_directories is not None:
            result['StoredAsSubDirectories'] = self.stored_as_sub_directories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NumBuckets') is not None:
            self.num_buckets = m.get('NumBuckets')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SdId') is not None:
            self.sd_id = m.get('SdId')
        if m.get('SerDeInfo') is not None:
            temp_model = SerDeInfoModel()
            self.ser_de_info = temp_model.from_map(m['SerDeInfo'])
        if m.get('StoredAsSubDirectories') is not None:
            self.stored_as_sub_directories = m.get('StoredAsSubDirectories')
        return self


class TableDetailModel(TeaModel):
    def __init__(
        self,
        catalog: str = None,
        columns: List[ColDetailModel] = None,
        create_time: str = None,
        description: str = None,
        owner: str = None,
        schema_name: str = None,
        table_name: str = None,
        table_type: str = None,
        update_time: str = None,
    ):
        self.catalog = catalog
        self.columns = columns
        self.create_time = create_time
        self.description = description
        self.owner = owner
        self.schema_name = schema_name
        self.table_name = table_name
        self.table_type = table_type
        self.update_time = update_time

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog is not None:
            result['Catalog'] = self.catalog
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = ColDetailModel()
                self.columns.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class TableModel(TeaModel):
    def __init__(
        self,
        archive_type: str = None,
        block_size: int = None,
        bucket: int = None,
        bucket_count: int = None,
        cols: List[FieldSchemaModel] = None,
        comment: str = None,
        compression: str = None,
        create_time: str = None,
        current_version: int = None,
        db_name: str = None,
        dict_encode: bool = None,
        distribute_columns: List[FieldSchemaModel] = None,
        distribute_type: str = None,
        enable_dfs: bool = None,
        hot_partition_count: int = None,
        indexes: List[CstoreIndexModel] = None,
        is_all_index: bool = None,
        is_fulltext_dict: bool = None,
        max_column_id: int = None,
        parameters: Dict[str, str] = None,
        partition_column: str = None,
        partition_count: int = None,
        partition_keys: List[FieldSchemaModel] = None,
        partition_type: str = None,
        physical_database_name: str = None,
        physical_table_name: str = None,
        previous_version: int = None,
        raw_table_name: str = None,
        route_columns: List[FieldSchemaModel] = None,
        route_effective_column: FieldSchemaModel = None,
        route_type: str = None,
        rt_engine_type: str = None,
        rt_index_all: bool = None,
        rt_mode_type: str = None,
        sd: StorageDescriptorModel = None,
        storage_policy: str = None,
        subpartition_column: str = None,
        subpartition_count: int = None,
        subpartition_type: str = None,
        table_engine_name: str = None,
        table_name: str = None,
        table_type: str = None,
        tbl_id: int = None,
        temporary: bool = None,
        update_time: str = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
        view_security_mode: str = None,
    ):
        self.archive_type = archive_type
        self.block_size = block_size
        self.bucket = bucket
        self.bucket_count = bucket_count
        self.cols = cols
        self.comment = comment
        self.compression = compression
        self.create_time = create_time
        self.current_version = current_version
        self.db_name = db_name
        self.dict_encode = dict_encode
        self.distribute_columns = distribute_columns
        self.distribute_type = distribute_type
        self.enable_dfs = enable_dfs
        self.hot_partition_count = hot_partition_count
        self.indexes = indexes
        self.is_all_index = is_all_index
        self.is_fulltext_dict = is_fulltext_dict
        self.max_column_id = max_column_id
        self.parameters = parameters
        self.partition_column = partition_column
        self.partition_count = partition_count
        self.partition_keys = partition_keys
        self.partition_type = partition_type
        self.physical_database_name = physical_database_name
        self.physical_table_name = physical_table_name
        self.previous_version = previous_version
        self.raw_table_name = raw_table_name
        self.route_columns = route_columns
        self.route_effective_column = route_effective_column
        self.route_type = route_type
        self.rt_engine_type = rt_engine_type
        self.rt_index_all = rt_index_all
        self.rt_mode_type = rt_mode_type
        self.sd = sd
        self.storage_policy = storage_policy
        self.subpartition_column = subpartition_column
        self.subpartition_count = subpartition_count
        self.subpartition_type = subpartition_type
        self.table_engine_name = table_engine_name
        self.table_name = table_name
        self.table_type = table_type
        self.tbl_id = tbl_id
        self.temporary = temporary
        self.update_time = update_time
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text
        self.view_security_mode = view_security_mode

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()
        if self.distribute_columns:
            for k in self.distribute_columns:
                if k:
                    k.validate()
        if self.indexes:
            for k in self.indexes:
                if k:
                    k.validate()
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.route_columns:
            for k in self.route_columns:
                if k:
                    k.validate()
        if self.route_effective_column:
            self.route_effective_column.validate()
        if self.sd:
            self.sd.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_type is not None:
            result['ArchiveType'] = self.archive_type
        if self.block_size is not None:
            result['BlockSize'] = self.block_size
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.compression is not None:
            result['Compression'] = self.compression
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.dict_encode is not None:
            result['DictEncode'] = self.dict_encode
        result['DistributeColumns'] = []
        if self.distribute_columns is not None:
            for k in self.distribute_columns:
                result['DistributeColumns'].append(k.to_map() if k else None)
        if self.distribute_type is not None:
            result['DistributeType'] = self.distribute_type
        if self.enable_dfs is not None:
            result['EnableDfs'] = self.enable_dfs
        if self.hot_partition_count is not None:
            result['HotPartitionCount'] = self.hot_partition_count
        result['Indexes'] = []
        if self.indexes is not None:
            for k in self.indexes:
                result['Indexes'].append(k.to_map() if k else None)
        if self.is_all_index is not None:
            result['IsAllIndex'] = self.is_all_index
        if self.is_fulltext_dict is not None:
            result['IsFulltextDict'] = self.is_fulltext_dict
        if self.max_column_id is not None:
            result['MaxColumnId'] = self.max_column_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.partition_column is not None:
            result['PartitionColumn'] = self.partition_column
        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type
        if self.physical_database_name is not None:
            result['PhysicalDatabaseName'] = self.physical_database_name
        if self.physical_table_name is not None:
            result['PhysicalTableName'] = self.physical_table_name
        if self.previous_version is not None:
            result['PreviousVersion'] = self.previous_version
        if self.raw_table_name is not None:
            result['RawTableName'] = self.raw_table_name
        result['RouteColumns'] = []
        if self.route_columns is not None:
            for k in self.route_columns:
                result['RouteColumns'].append(k.to_map() if k else None)
        if self.route_effective_column is not None:
            result['RouteEffectiveColumn'] = self.route_effective_column.to_map()
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.rt_engine_type is not None:
            result['RtEngineType'] = self.rt_engine_type
        if self.rt_index_all is not None:
            result['RtIndexAll'] = self.rt_index_all
        if self.rt_mode_type is not None:
            result['RtModeType'] = self.rt_mode_type
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy
        if self.subpartition_column is not None:
            result['SubpartitionColumn'] = self.subpartition_column
        if self.subpartition_count is not None:
            result['SubpartitionCount'] = self.subpartition_count
        if self.subpartition_type is not None:
            result['SubpartitionType'] = self.subpartition_type
        if self.table_engine_name is not None:
            result['TableEngineName'] = self.table_engine_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.tbl_id is not None:
            result['TblId'] = self.tbl_id
        if self.temporary is not None:
            result['Temporary'] = self.temporary
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        if self.view_security_mode is not None:
            result['ViewSecurityMode'] = self.view_security_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveType') is not None:
            self.archive_type = m.get('ArchiveType')
        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = FieldSchemaModel()
                self.cols.append(temp_model.from_map(k))
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Compression') is not None:
            self.compression = m.get('Compression')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DictEncode') is not None:
            self.dict_encode = m.get('DictEncode')
        self.distribute_columns = []
        if m.get('DistributeColumns') is not None:
            for k in m.get('DistributeColumns'):
                temp_model = FieldSchemaModel()
                self.distribute_columns.append(temp_model.from_map(k))
        if m.get('DistributeType') is not None:
            self.distribute_type = m.get('DistributeType')
        if m.get('EnableDfs') is not None:
            self.enable_dfs = m.get('EnableDfs')
        if m.get('HotPartitionCount') is not None:
            self.hot_partition_count = m.get('HotPartitionCount')
        self.indexes = []
        if m.get('Indexes') is not None:
            for k in m.get('Indexes'):
                temp_model = CstoreIndexModel()
                self.indexes.append(temp_model.from_map(k))
        if m.get('IsAllIndex') is not None:
            self.is_all_index = m.get('IsAllIndex')
        if m.get('IsFulltextDict') is not None:
            self.is_fulltext_dict = m.get('IsFulltextDict')
        if m.get('MaxColumnId') is not None:
            self.max_column_id = m.get('MaxColumnId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PartitionColumn') is not None:
            self.partition_column = m.get('PartitionColumn')
        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = FieldSchemaModel()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')
        if m.get('PhysicalDatabaseName') is not None:
            self.physical_database_name = m.get('PhysicalDatabaseName')
        if m.get('PhysicalTableName') is not None:
            self.physical_table_name = m.get('PhysicalTableName')
        if m.get('PreviousVersion') is not None:
            self.previous_version = m.get('PreviousVersion')
        if m.get('RawTableName') is not None:
            self.raw_table_name = m.get('RawTableName')
        self.route_columns = []
        if m.get('RouteColumns') is not None:
            for k in m.get('RouteColumns'):
                temp_model = FieldSchemaModel()
                self.route_columns.append(temp_model.from_map(k))
        if m.get('RouteEffectiveColumn') is not None:
            temp_model = FieldSchemaModel()
            self.route_effective_column = temp_model.from_map(m['RouteEffectiveColumn'])
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('RtEngineType') is not None:
            self.rt_engine_type = m.get('RtEngineType')
        if m.get('RtIndexAll') is not None:
            self.rt_index_all = m.get('RtIndexAll')
        if m.get('RtModeType') is not None:
            self.rt_mode_type = m.get('RtModeType')
        if m.get('Sd') is not None:
            temp_model = StorageDescriptorModel()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('StoragePolicy') is not None:
            self.storage_policy = m.get('StoragePolicy')
        if m.get('SubpartitionColumn') is not None:
            self.subpartition_column = m.get('SubpartitionColumn')
        if m.get('SubpartitionCount') is not None:
            self.subpartition_count = m.get('SubpartitionCount')
        if m.get('SubpartitionType') is not None:
            self.subpartition_type = m.get('SubpartitionType')
        if m.get('TableEngineName') is not None:
            self.table_engine_name = m.get('TableEngineName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('TblId') is not None:
            self.tbl_id = m.get('TblId')
        if m.get('Temporary') is not None:
            self.temporary = m.get('Temporary')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        if m.get('ViewSecurityMode') is not None:
            self.view_security_mode = m.get('ViewSecurityMode')
        return self


class TableSummaryModel(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        owner: str = None,
        sql: str = None,
        schema_name: str = None,
        table_name: str = None,
        table_size: int = None,
        table_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.owner = owner
        self.sql = sql
        self.schema_name = schema_name
        self.table_name = table_name
        self.table_size = table_size
        self.table_type = table_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_size is not None:
            result['TableSize'] = self.table_size
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class AllocateClusterPublicConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbcluster_id: str = None,
    ):
        self.connection_string_prefix = connection_string_prefix
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class AllocateClusterPublicConnectionResponseBody(TeaModel):
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


class AllocateClusterPublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateClusterPublicConnectionResponseBody = None,
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
            temp_model = AllocateClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        ram_user: str = None,
    ):
        self.account_name = account_name
        self.dbcluster_id = dbcluster_id
        self.ram_user = ram_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.ram_user is not None:
            result['RamUser'] = self.ram_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RamUser') is not None:
            self.ram_user = m.get('RamUser')
        return self


class BindAccountResponseBody(TeaModel):
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


class BindAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAccountResponseBody = None,
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
            temp_model = BindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckBindRamUserRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckBindRamUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckBindRamUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckBindRamUserResponseBody = None,
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
            temp_model = CheckBindRamUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        account_type: str = None,
        dbcluster_id: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_password = account_password
        self.account_type = account_type
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class CreateAccountResponseBody(TeaModel):
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


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccountResponseBody = None,
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
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBClusterRequest(TeaModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_description: str = None,
        dbcluster_network_type: str = None,
        dbcluster_version: str = None,
        enable_default_resource_pool: bool = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        storage_resource: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.compute_resource = compute_resource
        self.dbcluster_description = dbcluster_description
        self.dbcluster_network_type = dbcluster_network_type
        self.dbcluster_version = dbcluster_version
        self.enable_default_resource_pool = enable_default_resource_pool
        self.pay_type = pay_type
        self.period = period
        self.region_id = region_id
        self.storage_resource = storage_resource
        self.used_time = used_time
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version
        if self.enable_default_resource_pool is not None:
            result['EnableDefaultResourcePool'] = self.enable_default_resource_pool
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')
        if m.get('EnableDefaultResourcePool') is not None:
            self.enable_default_resource_pool = m.get('EnableDefaultResourcePool')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.order_id = order_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBClusterResponseBody = None,
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
            temp_model = CreateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_type: str = None,
        max_compute_resource: str = None,
        min_compute_resource: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.group_name = group_name
        self.group_type = group_type
        self.max_compute_resource = max_compute_resource
        self.min_compute_resource = min_compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        return self


class CreateDBResourceGroupResponseBody(TeaModel):
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


class CreateDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBResourceGroupResponseBody = None,
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
            temp_model = CreateDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOssSubDirectoryRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        path: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateOssSubDirectoryResponseBodyData(TeaModel):
    def __init__(
        self,
        client_crc: int = None,
        etag: str = None,
        request_id: str = None,
        server_crc: int = None,
    ):
        self.client_crc = client_crc
        self.etag = etag
        self.request_id = request_id
        self.server_crc = server_crc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_crc is not None:
            result['ClientCRC'] = self.client_crc
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_crc is not None:
            result['ServerCRC'] = self.server_crc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientCRC') is not None:
            self.client_crc = m.get('ClientCRC')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerCRC') is not None:
            self.server_crc = m.get('ServerCRC')
        return self


class CreateOssSubDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateOssSubDirectoryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
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
        if m.get('Data') is not None:
            temp_model = CreateOssSubDirectoryResponseBodyData()
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


class CreateOssSubDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOssSubDirectoryResponseBody = None,
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
            temp_model = CreateOssSubDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSparkTemplateRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        dbcluster_id: str = None,
        name: str = None,
        parent_id: int = None,
        type: str = None,
    ):
        self.app_type = app_type
        self.dbcluster_id = dbcluster_id
        self.name = name
        self.parent_id = parent_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateSparkTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        succeeded: bool = None,
    ):
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class CreateSparkTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateSparkTemplateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateSparkTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSparkTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSparkTemplateResponseBody = None,
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
            temp_model = CreateSparkTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
    ):
        self.account_name = account_name
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DeleteAccountResponseBody(TeaModel):
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


class DeleteAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccountResponseBody = None,
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
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBClusterResponseBody = None,
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
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DeleteDBResourceGroupResponseBody(TeaModel):
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


class DeleteDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBResourceGroupResponseBody = None,
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
            temp_model = DeleteDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProcessInstanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        process_instance_id: int = None,
        project_code: int = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.process_instance_id = process_instance_id
        self.project_code = project_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id
        if self.project_code is not None:
            result['ProjectCode'] = self.project_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')
        if m.get('ProjectCode') is not None:
            self.project_code = m.get('ProjectCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteProcessInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProcessInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProcessInstanceResponseBody = None,
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
            temp_model = DeleteProcessInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSparkTemplateRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteSparkTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        succeeded: bool = None,
    ):
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class DeleteSparkTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteSparkTemplateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteSparkTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSparkTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSparkTemplateResponseBody = None,
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
            temp_model = DeleteSparkTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSparkTemplateFileRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteSparkTemplateFileResponseBodyData(TeaModel):
    def __init__(
        self,
        succeeded: bool = None,
    ):
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class DeleteSparkTemplateFileResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteSparkTemplateFileResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteSparkTemplateFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSparkTemplateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSparkTemplateFileResponseBody = None,
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
            temp_model = DeleteSparkTemplateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        owner_id: str = None,
    ):
        self.account_name = account_name
        self.dbcluster_id = dbcluster_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAccountsResponseBodyAccountListDBAccount(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        ram_users: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_status = account_status
        self.account_type = account_type
        self.ram_users = ram_users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.ram_users is not None:
            result['RamUsers'] = self.ram_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('RamUsers') is not None:
            self.ram_users = m.get('RamUsers')
        return self


class DescribeAccountsResponseBodyAccountList(TeaModel):
    def __init__(
        self,
        dbaccount: List[DescribeAccountsResponseBodyAccountListDBAccount] = None,
    ):
        self.dbaccount = dbaccount

    def validate(self):
        if self.dbaccount:
            for k in self.dbaccount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBAccount'] = []
        if self.dbaccount is not None:
            for k in self.dbaccount:
                result['DBAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbaccount = []
        if m.get('DBAccount') is not None:
            for k in m.get('DBAccount'):
                temp_model = DescribeAccountsResponseBodyAccountListDBAccount()
                self.dbaccount.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(
        self,
        account_list: DescribeAccountsResponseBodyAccountList = None,
        request_id: str = None,
    ):
        self.account_list = account_list
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            self.account_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_list is not None:
            result['AccountList'] = self.account_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountList') is not None:
            temp_model = DescribeAccountsResponseBodyAccountList()
            self.account_list = temp_model.from_map(m['AccountList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountsResponseBody = None,
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdbMySqlColumnsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        schema: str = None,
        table_name: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        self.schema = schema
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAdbMySqlColumnsResponseBodyColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAdbMySqlColumnsResponseBody(TeaModel):
    def __init__(
        self,
        columns: List[DescribeAdbMySqlColumnsResponseBodyColumns] = None,
        message: str = None,
        request_id: str = None,
        schema: str = None,
        success: bool = None,
        table_name: str = None,
    ):
        self.columns = columns
        self.message = message
        self.request_id = request_id
        self.schema = schema
        self.success = success
        self.table_name = table_name

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.success is not None:
            result['Success'] = self.success
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = DescribeAdbMySqlColumnsResponseBodyColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAdbMySqlColumnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdbMySqlColumnsResponseBody = None,
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
            temp_model = DescribeAdbMySqlColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdbMySqlSchemasRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAdbMySqlSchemasResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        schemas: List[str] = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.schemas = schemas
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schemas is not None:
            result['Schemas'] = self.schemas
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schemas') is not None:
            self.schemas = m.get('Schemas')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAdbMySqlSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdbMySqlSchemasResponseBody = None,
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
            temp_model = DescribeAdbMySqlSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdbMySqlTablesRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        schema: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class DescribeAdbMySqlTablesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        schema: str = None,
        success: bool = None,
        tables: List[str] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.schema = schema
        self.success = success
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.success is not None:
            result['Success'] = self.success
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class DescribeAdbMySqlTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdbMySqlTablesResponseBody = None,
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
            temp_model = DescribeAdbMySqlTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApsActionLogsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        keyword: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        proxy_user: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        stage: str = None,
        start_time: str = None,
        state: str = None,
        workload_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.keyword = keyword
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.proxy_user = proxy_user
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.stage = stage
        self.start_time = start_time
        self.state = state
        self.workload_id = workload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.stage is not None:
            result['Stage'] = self.stage
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        return self


class DescribeApsActionLogsResponseBodyActionLogs(TeaModel):
    def __init__(
        self,
        context: str = None,
        stage: str = None,
        state: str = None,
        time: str = None,
    ):
        self.context = context
        self.stage = stage
        self.state = state
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        if self.stage is not None:
            result['Stage'] = self.stage
        if self.state is not None:
            result['State'] = self.state
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeApsActionLogsResponseBody(TeaModel):
    def __init__(
        self,
        action_logs: List[DescribeApsActionLogsResponseBodyActionLogs] = None,
        dbcluster_id: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
        workload_id: str = None,
    ):
        self.action_logs = action_logs
        self.dbcluster_id = dbcluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.workload_id = workload_id

    def validate(self):
        if self.action_logs:
            for k in self.action_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActionLogs'] = []
        if self.action_logs is not None:
            for k in self.action_logs:
                result['ActionLogs'].append(k.to_map() if k else None)
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_logs = []
        if m.get('ActionLogs') is not None:
            for k in m.get('ActionLogs'):
                temp_model = DescribeApsActionLogsResponseBodyActionLogs()
                self.action_logs.append(temp_model.from_map(k))
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        return self


class DescribeApsActionLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApsActionLogsResponseBody = None,
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
            temp_model = DescribeApsActionLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApsResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeApsResourceGroupsResponseBodyDataResourceGroups(TeaModel):
    def __init__(
        self,
        available: bool = None,
        cu_options: List[int] = None,
        group_name: str = None,
        group_type: str = None,
        max_compute_resource: int = None,
        min_compute_resource: int = None,
    ):
        self.available = available
        self.cu_options = cu_options
        self.group_name = group_name
        self.group_type = group_type
        self.max_compute_resource = max_compute_resource
        self.min_compute_resource = min_compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.cu_options is not None:
            result['CuOptions'] = self.cu_options
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('CuOptions') is not None:
            self.cu_options = m.get('CuOptions')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        return self


class DescribeApsResourceGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        resource_groups: List[DescribeApsResourceGroupsResponseBodyDataResourceGroups] = None,
        step: int = None,
    ):
        self.resource_groups = resource_groups
        self.step = step

    def validate(self):
        if self.resource_groups:
            for k in self.resource_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k in self.resource_groups:
                result['ResourceGroups'].append(k.to_map() if k else None)
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k in m.get('ResourceGroups'):
                temp_model = DescribeApsResourceGroupsResponseBodyDataResourceGroups()
                self.resource_groups.append(temp_model.from_map(k))
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApsResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeApsResourceGroupsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
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
        if m.get('Data') is not None:
            temp_model = DescribeApsResourceGroupsResponseBodyData()
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


class DescribeApsResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApsResourceGroupsResponseBody = None,
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
            temp_model = DescribeApsResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogConfigRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAuditLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        audit_log_status: str = None,
        dbcluster_id: str = None,
        request_id: str = None,
    ):
        self.audit_log_status = audit_log_status
        self.dbcluster_id = dbcluster_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAuditLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditLogConfigResponseBody = None,
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
            temp_model = DescribeAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogRecordsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        host_address: str = None,
        order: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        proxy_user: str = None,
        query_keyword: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sql_type: str = None,
        start_time: str = None,
        succeed: str = None,
        user: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.dbname = dbname
        self.end_time = end_time
        self.host_address = host_address
        self.order = order
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.proxy_user = proxy_user
        self.query_keyword = query_keyword
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sql_type = sql_type
        self.start_time = start_time
        self.succeed = succeed
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.order is not None:
            result['Order'] = self.order
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeAuditLogRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        conn_id: str = None,
        dbname: str = None,
        execute_time: str = None,
        host_address: str = None,
        process_id: str = None,
        sqltext: str = None,
        sqltype: str = None,
        succeed: str = None,
        total_time: str = None,
        user: str = None,
    ):
        self.conn_id = conn_id
        self.dbname = dbname
        self.execute_time = execute_time
        self.host_address = host_address
        self.process_id = process_id
        self.sqltext = sqltext
        self.sqltype = sqltype
        self.succeed = succeed
        self.total_time = total_time
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_id is not None:
            result['ConnId'] = self.conn_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnId') is not None:
            self.conn_id = m.get('ConnId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeAuditLogRecordsResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: List[DescribeAuditLogRecordsResponseBodyItems] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeAuditLogRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditLogRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditLogRecordsResponseBody = None,
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
            temp_model = DescribeAuditLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        enable_backup_log: str = None,
        log_backup_retention_period: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        request_id: str = None,
    ):
        self.backup_retention_period = backup_retention_period
        self.enable_backup_log = enable_backup_log
        self.log_backup_retention_period = log_backup_retention_period
        self.preferred_backup_period = preferred_backup_period
        self.preferred_backup_time = preferred_backup_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPolicyResponseBody = None,
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.backup_id = backup_id
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupsResponseBodyItemsBackup(TeaModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_method: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_type: str = None,
        dbcluster_id: str = None,
    ):
        self.backup_end_time = backup_end_time
        self.backup_id = backup_id
        self.backup_method = backup_method
        self.backup_size = backup_size
        self.backup_start_time = backup_start_time
        self.backup_type = backup_type
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeBackupsResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup: List[DescribeBackupsResponseBodyItemsBackup] = None,
    ):
        self.backup = backup

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k in m.get('Backup'):
                temp_model = DescribeBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeBackupsResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeBackupsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupsResponseBody = None,
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterAccessWhiteListRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        resource_owner_account: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DescribeClusterAccessWhiteListResponseBodyItemsIPArray(TeaModel):
    def __init__(
        self,
        dbcluster_iparray_attribute: str = None,
        dbcluster_iparray_name: str = None,
        security_iplist: str = None,
    ):
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        self.dbcluster_iparray_name = dbcluster_iparray_name
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeClusterAccessWhiteListResponseBodyItems(TeaModel):
    def __init__(
        self,
        iparray: List[DescribeClusterAccessWhiteListResponseBodyItemsIPArray] = None,
    ):
        self.iparray = iparray

    def validate(self):
        if self.iparray:
            for k in self.iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IPArray'] = []
        if self.iparray is not None:
            for k in self.iparray:
                result['IPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.iparray = []
        if m.get('IPArray') is not None:
            for k in m.get('IPArray'):
                temp_model = DescribeClusterAccessWhiteListResponseBodyItemsIPArray()
                self.iparray.append(temp_model.from_map(k))
        return self


class DescribeClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeClusterAccessWhiteListResponseBodyItems = None,
        request_id: str = None,
    ):
        self.items = items
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeClusterAccessWhiteListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterAccessWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterAccessWhiteListResponseBody = None,
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
            temp_model = DescribeClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterNetInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeClusterNetInfoResponseBodyItemsAddress(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        connection_string_prefix: str = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        self.connection_string = connection_string
        self.connection_string_prefix = connection_string_prefix
        self.ipaddress = ipaddress
        self.net_type = net_type
        self.port = port
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeClusterNetInfoResponseBodyItems(TeaModel):
    def __init__(
        self,
        address: List[DescribeClusterNetInfoResponseBodyItemsAddress] = None,
    ):
        self.address = address

    def validate(self):
        if self.address:
            for k in self.address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Address'] = []
        if self.address is not None:
            for k in self.address:
                result['Address'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address = []
        if m.get('Address') is not None:
            for k in m.get('Address'):
                temp_model = DescribeClusterNetInfoResponseBodyItemsAddress()
                self.address.append(temp_model.from_map(k))
        return self


class DescribeClusterNetInfoResponseBody(TeaModel):
    def __init__(
        self,
        cluster_network_type: str = None,
        items: DescribeClusterNetInfoResponseBodyItems = None,
        request_id: str = None,
    ):
        self.cluster_network_type = cluster_network_type
        self.items = items
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('Items') is not None:
            temp_model = DescribeClusterNetInfoResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterNetInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterNetInfoResponseBody = None,
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
            temp_model = DescribeClusterNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAttributeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeDBClusterAttributeResponseBodyItemsDBCluster(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        compute_resource: str = None,
        compute_resource_total: str = None,
        connection_string: str = None,
        creation_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbcluster_type: str = None,
        dbversion: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        expired: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_time: str = None,
        mode: str = None,
        pay_type: str = None,
        port: int = None,
        region_id: str = None,
        reserved_acu: str = None,
        resource_group_id: str = None,
        storage_resource: str = None,
        storage_resource_total: str = None,
        user_enistatus: bool = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.commodity_code = commodity_code
        self.compute_resource = compute_resource
        self.compute_resource_total = compute_resource_total
        self.connection_string = connection_string
        self.creation_time = creation_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_network_type = dbcluster_network_type
        self.dbcluster_status = dbcluster_status
        self.dbcluster_type = dbcluster_type
        self.dbversion = dbversion
        self.engine = engine
        self.engine_version = engine_version
        self.expire_time = expire_time
        self.expired = expired
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.maintain_time = maintain_time
        self.mode = mode
        self.pay_type = pay_type
        self.port = port
        self.region_id = region_id
        self.reserved_acu = reserved_acu
        self.resource_group_id = resource_group_id
        self.storage_resource = storage_resource
        self.storage_resource_total = storage_resource_total
        self.user_enistatus = user_enistatus
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.compute_resource_total is not None:
            result['ComputeResourceTotal'] = self.compute_resource_total
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserved_acu is not None:
            result['ReservedACU'] = self.reserved_acu
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.storage_resource_total is not None:
            result['StorageResourceTotal'] = self.storage_resource_total
        if self.user_enistatus is not None:
            result['UserENIStatus'] = self.user_enistatus
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('ComputeResourceTotal') is not None:
            self.compute_resource_total = m.get('ComputeResourceTotal')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReservedACU') is not None:
            self.reserved_acu = m.get('ReservedACU')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('StorageResourceTotal') is not None:
            self.storage_resource_total = m.get('StorageResourceTotal')
        if m.get('UserENIStatus') is not None:
            self.user_enistatus = m.get('UserENIStatus')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClusterAttributeResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbcluster: List[DescribeDBClusterAttributeResponseBodyItemsDBCluster] = None,
    ):
        self.dbcluster = dbcluster

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClusterAttributeResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAttributeResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBClusterAttributeResponseBodyItems = None,
        request_id: str = None,
    ):
        self.items = items
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterAttributeResponseBody = None,
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
            temp_model = DescribeDBClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterForecastRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        metric_type: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.metric_type = metric_type
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterForecastResponseBodyPerformancesSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: str = None,
    ):
        self.name = name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeDBClusterForecastResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        key: str = None,
        series: List[DescribeDBClusterForecastResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        self.key = key
        self.series = series
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterForecastResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterForecastResponseBody(TeaModel):
    def __init__(
        self,
        performances: List[DescribeDBClusterForecastResponseBodyPerformances] = None,
        request_id: str = None,
    ):
        self.performances = performances
        self.request_id = request_id

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterForecastResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterForecastResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterForecastResponseBody = None,
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
            temp_model = DescribeDBClusterForecastResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterHealthStatusRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBClusterHealthStatusResponseBodyCS(TeaModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        self.active_count = active_count
        self.expected_count = expected_count
        self.risk_count = risk_count
        self.status = status
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.status is not None:
            result['Status'] = self.status
        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')
        return self


class DescribeDBClusterHealthStatusResponseBodyExecutor(TeaModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        self.active_count = active_count
        self.expected_count = expected_count
        self.risk_count = risk_count
        self.status = status
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.status is not None:
            result['Status'] = self.status
        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')
        return self


class DescribeDBClusterHealthStatusResponseBodyWorker(TeaModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        self.active_count = active_count
        self.expected_count = expected_count
        self.risk_count = risk_count
        self.status = status
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.status is not None:
            result['Status'] = self.status
        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')
        return self


class DescribeDBClusterHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        cs: DescribeDBClusterHealthStatusResponseBodyCS = None,
        executor: DescribeDBClusterHealthStatusResponseBodyExecutor = None,
        instance_status: str = None,
        request_id: str = None,
        worker: DescribeDBClusterHealthStatusResponseBodyWorker = None,
    ):
        self.cs = cs
        self.executor = executor
        self.instance_status = instance_status
        self.request_id = request_id
        self.worker = worker

    def validate(self):
        if self.cs:
            self.cs.validate()
        if self.executor:
            self.executor.validate()
        if self.worker:
            self.worker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs is not None:
            result['CS'] = self.cs.to_map()
        if self.executor is not None:
            result['Executor'] = self.executor.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.worker is not None:
            result['Worker'] = self.worker.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CS') is not None:
            temp_model = DescribeDBClusterHealthStatusResponseBodyCS()
            self.cs = temp_model.from_map(m['CS'])
        if m.get('Executor') is not None:
            temp_model = DescribeDBClusterHealthStatusResponseBodyExecutor()
            self.executor = temp_model.from_map(m['Executor'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Worker') is not None:
            temp_model = DescribeDBClusterHealthStatusResponseBodyWorker()
            self.worker = temp_model.from_map(m['Worker'])
        return self


class DescribeDBClusterHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterHealthStatusResponseBody = None,
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
            temp_model = DescribeDBClusterHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        region_id: str = None,
        resource_pools: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.key = key
        self.region_id = region_id
        self.resource_pools = resource_pools
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_pools is not None:
            result['ResourcePools'] = self.resource_pools
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourcePools') is not None:
            self.resource_pools = m.get('ResourcePools')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformancesSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        tags: str = None,
        values: List[str] = None,
    ):
        self.name = name
        self.tags = tags
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        key: str = None,
        series: List[DescribeDBClusterPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        self.key = key
        self.series = series
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performances: List[DescribeDBClusterPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.performances = performances
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterPerformanceResponseBody = None,
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
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClustersRequest(TeaModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_ids: str = None,
        dbcluster_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.dbcluster_description = dbcluster_description
        self.dbcluster_ids = dbcluster_ids
        self.dbcluster_status = dbcluster_status
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBClustersResponseBodyItemsDBCluster(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        compute_resource: str = None,
        connection_string: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbcluster_type: str = None,
        dbversion: str = None,
        engine: str = None,
        expire_time: str = None,
        expired: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        mode: str = None,
        pay_type: str = None,
        port: str = None,
        region_id: str = None,
        reserved_acu: str = None,
        resource_group_id: str = None,
        storage_resource: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.commodity_code = commodity_code
        self.compute_resource = compute_resource
        self.connection_string = connection_string
        self.create_time = create_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_network_type = dbcluster_network_type
        self.dbcluster_status = dbcluster_status
        self.dbcluster_type = dbcluster_type
        self.dbversion = dbversion
        self.engine = engine
        self.expire_time = expire_time
        self.expired = expired
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.mode = mode
        self.pay_type = pay_type
        self.port = port
        self.region_id = region_id
        self.reserved_acu = reserved_acu
        self.resource_group_id = resource_group_id
        self.storage_resource = storage_resource
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserved_acu is not None:
            result['ReservedACU'] = self.reserved_acu
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReservedACU') is not None:
            self.reserved_acu = m.get('ReservedACU')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClustersResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbcluster: List[DescribeDBClustersResponseBodyItemsDBCluster] = None,
    ):
        self.dbcluster = dbcluster

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClustersResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBClustersResponseBodyItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBClustersResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClustersResponseBody = None,
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
            temp_model = DescribeDBClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_type: str = None,
        resource_owner_account: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.group_name = group_name
        self.group_type = group_type
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DescribeDBResourceGroupResponseBodyGroupsInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        elastic_min_compute_resource: str = None,
        group_name: str = None,
        group_type: str = None,
        group_users: str = None,
        max_compute_resource: str = None,
        min_compute_resource: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.elastic_min_compute_resource = elastic_min_compute_resource
        self.group_name = group_name
        self.group_type = group_type
        self.group_users = group_users
        self.max_compute_resource = max_compute_resource
        self.min_compute_resource = min_compute_resource
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.elastic_min_compute_resource is not None:
            result['ElasticMinComputeResource'] = self.elastic_min_compute_resource
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_users is not None:
            result['GroupUsers'] = self.group_users
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ElasticMinComputeResource') is not None:
            self.elastic_min_compute_resource = m.get('ElasticMinComputeResource')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupUsers') is not None:
            self.group_users = m.get('GroupUsers')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDBResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        groups_info: List[DescribeDBResourceGroupResponseBodyGroupsInfo] = None,
        request_id: str = None,
    ):
        self.groups_info = groups_info
        self.request_id = request_id

    def validate(self):
        if self.groups_info:
            for k in self.groups_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupsInfo'] = []
        if self.groups_info is not None:
            for k in self.groups_info:
                result['GroupsInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups_info = []
        if m.get('GroupsInfo') is not None:
            for k in m.get('GroupsInfo'):
                temp_model = DescribeDBResourceGroupResponseBodyGroupsInfo()
                self.groups_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBResourceGroupResponseBody = None,
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
            temp_model = DescribeDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisDimensionsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        lang: str = None,
        query_condition: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.lang = lang
        self.query_condition = query_condition
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDiagnosisDimensionsResponseBody(TeaModel):
    def __init__(
        self,
        client_ips: List[str] = None,
        databases: List[str] = None,
        request_id: str = None,
        resource_groups: List[str] = None,
        user_names: List[str] = None,
    ):
        self.client_ips = client_ips
        self.databases = databases
        self.request_id = request_id
        self.resource_groups = resource_groups
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ips is not None:
            result['ClientIps'] = self.client_ips
        if self.databases is not None:
            result['Databases'] = self.databases
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups
        if self.user_names is not None:
            result['UserNames'] = self.user_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIps') is not None:
            self.client_ips = m.get('ClientIps')
        if m.get('Databases') is not None:
            self.databases = m.get('Databases')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroups') is not None:
            self.resource_groups = m.get('ResourceGroups')
        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')
        return self


class DescribeDiagnosisDimensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisDimensionsResponseBody = None,
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
            temp_model = DescribeDiagnosisDimensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisRecordsRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        dbcluster_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        max_peak_memory: int = None,
        max_scan_size: int = None,
        min_peak_memory: int = None,
        min_scan_size: int = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        pattern_id: str = None,
        query_condition: str = None,
        region_id: str = None,
        resource_group: str = None,
        start_time: str = None,
        user_name: str = None,
    ):
        self.client_ip = client_ip
        self.dbcluster_id = dbcluster_id
        self.database = database
        self.end_time = end_time
        self.keyword = keyword
        self.lang = lang
        self.max_peak_memory = max_peak_memory
        self.max_scan_size = max_scan_size
        self.min_peak_memory = min_peak_memory
        self.min_scan_size = min_scan_size
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.pattern_id = pattern_id
        self.query_condition = query_condition
        self.region_id = region_id
        self.resource_group = resource_group
        self.start_time = start_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.min_peak_memory is not None:
            result['MinPeakMemory'] = self.min_peak_memory
        if self.min_scan_size is not None:
            result['MinScanSize'] = self.min_scan_size
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('MinPeakMemory') is not None:
            self.min_peak_memory = m.get('MinPeakMemory')
        if m.get('MinScanSize') is not None:
            self.min_scan_size = m.get('MinScanSize')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDiagnosisRecordsResponseBodyQuerys(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        cost: int = None,
        database: str = None,
        etl_write_rows: int = None,
        execution_time: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        peak_memory: int = None,
        process_id: str = None,
        queue_time: int = None,
        rc_host: str = None,
        resource_cost_rank: int = None,
        resource_group: str = None,
        sql: str = None,
        sqltruncated: bool = None,
        sqltruncated_threshold: int = None,
        scan_rows: int = None,
        scan_size: int = None,
        start_time: int = None,
        status: str = None,
        total_planning_time: int = None,
        total_stages: int = None,
        user_name: str = None,
    ):
        self.client_ip = client_ip
        self.cost = cost
        self.database = database
        self.etl_write_rows = etl_write_rows
        self.execution_time = execution_time
        self.output_data_size = output_data_size
        self.output_rows = output_rows
        self.peak_memory = peak_memory
        self.process_id = process_id
        self.queue_time = queue_time
        self.rc_host = rc_host
        self.resource_cost_rank = resource_cost_rank
        self.resource_group = resource_group
        self.sql = sql
        self.sqltruncated = sqltruncated
        self.sqltruncated_threshold = sqltruncated_threshold
        self.scan_rows = scan_rows
        self.scan_size = scan_size
        self.start_time = start_time
        self.status = status
        self.total_planning_time = total_planning_time
        self.total_stages = total_stages
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.database is not None:
            result['Database'] = self.database
        if self.etl_write_rows is not None:
            result['EtlWriteRows'] = self.etl_write_rows
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rc_host is not None:
            result['RcHost'] = self.rc_host
        if self.resource_cost_rank is not None:
            result['ResourceCostRank'] = self.resource_cost_rank
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.sqltruncated is not None:
            result['SQLTruncated'] = self.sqltruncated
        if self.sqltruncated_threshold is not None:
            result['SQLTruncatedThreshold'] = self.sqltruncated_threshold
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_planning_time is not None:
            result['TotalPlanningTime'] = self.total_planning_time
        if self.total_stages is not None:
            result['TotalStages'] = self.total_stages
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EtlWriteRows') is not None:
            self.etl_write_rows = m.get('EtlWriteRows')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RcHost') is not None:
            self.rc_host = m.get('RcHost')
        if m.get('ResourceCostRank') is not None:
            self.resource_cost_rank = m.get('ResourceCostRank')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('SQLTruncated') is not None:
            self.sqltruncated = m.get('SQLTruncated')
        if m.get('SQLTruncatedThreshold') is not None:
            self.sqltruncated_threshold = m.get('SQLTruncatedThreshold')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalPlanningTime') is not None:
            self.total_planning_time = m.get('TotalPlanningTime')
        if m.get('TotalStages') is not None:
            self.total_stages = m.get('TotalStages')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDiagnosisRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        querys: List[DescribeDiagnosisRecordsResponseBodyQuerys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.querys = querys
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.querys:
            for k in self.querys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Querys'] = []
        if self.querys is not None:
            for k in self.querys:
                result['Querys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.querys = []
        if m.get('Querys') is not None:
            for k in m.get('Querys'):
                temp_model = DescribeDiagnosisRecordsResponseBodyQuerys()
                self.querys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiagnosisRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisRecordsResponseBody = None,
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
            temp_model = DescribeDiagnosisRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisSQLInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        lang: str = None,
        process_id: str = None,
        process_rc_host: str = None,
        process_start_time: int = None,
        process_state: str = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.lang = lang
        self.process_id = process_id
        self.process_rc_host = process_rc_host
        self.process_start_time = process_start_time
        self.process_state = process_state
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.process_rc_host is not None:
            result['ProcessRcHost'] = self.process_rc_host
        if self.process_start_time is not None:
            result['ProcessStartTime'] = self.process_start_time
        if self.process_state is not None:
            result['ProcessState'] = self.process_state
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('ProcessRcHost') is not None:
            self.process_rc_host = m.get('ProcessRcHost')
        if m.get('ProcessStartTime') is not None:
            self.process_start_time = m.get('ProcessStartTime')
        if m.get('ProcessState') is not None:
            self.process_state = m.get('ProcessState')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDiagnosisSQLInfoResponseBodyStageInfos(TeaModel):
    def __init__(
        self,
        input_data_size: int = None,
        input_rows: int = None,
        operator_cost: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        peak_memory: int = None,
        progress: float = None,
        stage_id: str = None,
        state: str = None,
    ):
        self.input_data_size = input_data_size
        self.input_rows = input_rows
        self.operator_cost = operator_cost
        self.output_data_size = output_data_size
        self.output_rows = output_rows
        self.peak_memory = peak_memory
        self.progress = progress
        self.stage_id = stage_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_data_size is not None:
            result['InputDataSize'] = self.input_data_size
        if self.input_rows is not None:
            result['InputRows'] = self.input_rows
        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost
        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputDataSize') is not None:
            self.input_data_size = m.get('InputDataSize')
        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')
        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')
        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeDiagnosisSQLInfoResponseBody(TeaModel):
    def __init__(
        self,
        diagnosis_sqlinfo: str = None,
        request_id: str = None,
        stage_infos: List[DescribeDiagnosisSQLInfoResponseBodyStageInfos] = None,
    ):
        self.diagnosis_sqlinfo = diagnosis_sqlinfo
        self.request_id = request_id
        self.stage_infos = stage_infos

    def validate(self):
        if self.stage_infos:
            for k in self.stage_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnosis_sqlinfo is not None:
            result['DiagnosisSQLInfo'] = self.diagnosis_sqlinfo
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StageInfos'] = []
        if self.stage_infos is not None:
            for k in self.stage_infos:
                result['StageInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosisSQLInfo') is not None:
            self.diagnosis_sqlinfo = m.get('DiagnosisSQLInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stage_infos = []
        if m.get('StageInfos') is not None:
            for k in m.get('StageInfos'):
                temp_model = DescribeDiagnosisSQLInfoResponseBodyStageInfos()
                self.stage_infos.append(temp_model.from_map(k))
        return self


class DescribeDiagnosisSQLInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisSQLInfoResponseBody = None,
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
            temp_model = DescribeDiagnosisSQLInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadRecordsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.lang = lang
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDownloadRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        download_id: int = None,
        exception_msg: str = None,
        file_name: str = None,
        status: str = None,
        url: str = None,
    ):
        self.download_id = download_id
        self.exception_msg = exception_msg
        self.file_name = file_name
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDownloadRecordsResponseBody(TeaModel):
    def __init__(
        self,
        records: List[DescribeDownloadRecordsResponseBodyRecords] = None,
        request_id: str = None,
    ):
        self.records = records
        self.request_id = request_id

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDownloadRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDownloadRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadRecordsResponseBody = None,
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
            temp_model = DescribeDownloadRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePatternPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        pattern_id: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.key = key
        self.pattern_id = pattern_id
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePatternPerformanceResponseBodyPerformancesSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        self.name = name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribePatternPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        key: str = None,
        series: List[DescribePatternPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        self.key = key
        self.series = series
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribePatternPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribePatternPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        performances: List[DescribePatternPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.performances = performances
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribePatternPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePatternPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePatternPerformanceResponseBody = None,
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
            temp_model = DescribePatternPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.accept_language = accept_language
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        vpc_enabled: bool = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.vpc_enabled = vpc_enabled
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
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeRegionsResponseBodyRegionsRegionZonesZone] = None,
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
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        zones: DescribeRegionsResponseBodyRegionsRegionZones = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

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
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
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
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPatternAttributeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        lang: str = None,
        pattern_id: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.lang = lang
        self.pattern_id = pattern_id
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSQLPatternAttributeResponseBodyPatternDetail(TeaModel):
    def __init__(
        self,
        average_memory: str = None,
        average_query_time: str = None,
        query_count: int = None,
        sqlpattern: str = None,
        total_query_time: str = None,
    ):
        self.average_memory = average_memory
        self.average_query_time = average_query_time
        self.query_count = query_count
        self.sqlpattern = sqlpattern
        self.total_query_time = total_query_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_memory is not None:
            result['AverageMemory'] = self.average_memory
        if self.average_query_time is not None:
            result['AverageQueryTime'] = self.average_query_time
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.sqlpattern is not None:
            result['SQLPattern'] = self.sqlpattern
        if self.total_query_time is not None:
            result['TotalQueryTime'] = self.total_query_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageMemory') is not None:
            self.average_memory = m.get('AverageMemory')
        if m.get('AverageQueryTime') is not None:
            self.average_query_time = m.get('AverageQueryTime')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('SQLPattern') is not None:
            self.sqlpattern = m.get('SQLPattern')
        if m.get('TotalQueryTime') is not None:
            self.total_query_time = m.get('TotalQueryTime')
        return self


class DescribeSQLPatternAttributeResponseBody(TeaModel):
    def __init__(
        self,
        pattern_detail: DescribeSQLPatternAttributeResponseBodyPatternDetail = None,
        request_id: str = None,
    ):
        self.pattern_detail = pattern_detail
        self.request_id = request_id

    def validate(self):
        if self.pattern_detail:
            self.pattern_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern_detail is not None:
            result['PatternDetail'] = self.pattern_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatternDetail') is not None:
            temp_model = DescribeSQLPatternAttributeResponseBodyPatternDetail()
            self.pattern_detail = temp_model.from_map(m['PatternDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSQLPatternAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLPatternAttributeResponseBody = None,
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
            temp_model = DescribeSQLPatternAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPatternsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.keyword = keyword
        self.lang = lang
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSQLPatternsResponseBodyPatternDetails(TeaModel):
    def __init__(
        self,
        access_ip: str = None,
        average_execution_time: float = None,
        average_peak_memory: float = None,
        average_query_time: float = None,
        average_scan_size: float = None,
        blockable: bool = None,
        failed_count: int = None,
        max_execution_time: int = None,
        max_peak_memory: int = None,
        max_query_time: int = None,
        max_scan_size: int = None,
        pattern_creation_time: str = None,
        pattern_id: str = None,
        query_count: int = None,
        sqlpattern: str = None,
        tables: str = None,
        user: str = None,
    ):
        self.access_ip = access_ip
        self.average_execution_time = average_execution_time
        self.average_peak_memory = average_peak_memory
        self.average_query_time = average_query_time
        self.average_scan_size = average_scan_size
        self.blockable = blockable
        self.failed_count = failed_count
        self.max_execution_time = max_execution_time
        self.max_peak_memory = max_peak_memory
        self.max_query_time = max_query_time
        self.max_scan_size = max_scan_size
        self.pattern_creation_time = pattern_creation_time
        self.pattern_id = pattern_id
        self.query_count = query_count
        self.sqlpattern = sqlpattern
        self.tables = tables
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip
        if self.average_execution_time is not None:
            result['AverageExecutionTime'] = self.average_execution_time
        if self.average_peak_memory is not None:
            result['AveragePeakMemory'] = self.average_peak_memory
        if self.average_query_time is not None:
            result['AverageQueryTime'] = self.average_query_time
        if self.average_scan_size is not None:
            result['AverageScanSize'] = self.average_scan_size
        if self.blockable is not None:
            result['Blockable'] = self.blockable
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.max_execution_time is not None:
            result['MaxExecutionTime'] = self.max_execution_time
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_query_time is not None:
            result['MaxQueryTime'] = self.max_query_time
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.pattern_creation_time is not None:
            result['PatternCreationTime'] = self.pattern_creation_time
        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.sqlpattern is not None:
            result['SQLPattern'] = self.sqlpattern
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')
        if m.get('AverageExecutionTime') is not None:
            self.average_execution_time = m.get('AverageExecutionTime')
        if m.get('AveragePeakMemory') is not None:
            self.average_peak_memory = m.get('AveragePeakMemory')
        if m.get('AverageQueryTime') is not None:
            self.average_query_time = m.get('AverageQueryTime')
        if m.get('AverageScanSize') is not None:
            self.average_scan_size = m.get('AverageScanSize')
        if m.get('Blockable') is not None:
            self.blockable = m.get('Blockable')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('MaxExecutionTime') is not None:
            self.max_execution_time = m.get('MaxExecutionTime')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxQueryTime') is not None:
            self.max_query_time = m.get('MaxQueryTime')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('PatternCreationTime') is not None:
            self.pattern_creation_time = m.get('PatternCreationTime')
        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('SQLPattern') is not None:
            self.sqlpattern = m.get('SQLPattern')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLPatternsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pattern_details: List[DescribeSQLPatternsResponseBodyPatternDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.pattern_details = pattern_details
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.pattern_details:
            for k in self.pattern_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PatternDetails'] = []
        if self.pattern_details is not None:
            for k in self.pattern_details:
                result['PatternDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.pattern_details = []
        if m.get('PatternDetails') is not None:
            for k in m.get('PatternDetails'):
                temp_model = DescribeSQLPatternsResponseBodyPatternDetails()
                self.pattern_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSQLPatternsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLPatternsResponseBody = None,
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
            temp_model = DescribeSQLPatternsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSparkCodeLogRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        job_id: int = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.job_id = job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSparkCodeLogResponseBody(TeaModel):
    def __init__(
        self,
        log: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.log = log
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log is not None:
            result['Log'] = self.log
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Log') is not None:
            self.log = m.get('Log')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSparkCodeLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSparkCodeLogResponseBody = None,
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
            temp_model = DescribeSparkCodeLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSparkCodeOutputRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        job_id: int = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.job_id = job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSparkCodeOutputResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        output: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.output = output
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSparkCodeOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSparkCodeOutputResponseBody = None,
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
            temp_model = DescribeSparkCodeOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSparkCodeWebUiRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        job_id: int = None,
        region_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.job_id = job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSparkCodeWebUiResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        url: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeSparkCodeWebUiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSparkCodeWebUiResponseBody = None,
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
            temp_model = DescribeSparkCodeWebUiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSqlPatternRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sql_pattern: str = None,
        start_time: str = None,
        type: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.sql_pattern = sql_pattern
        self.start_time = start_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sql_pattern is not None:
            result['SqlPattern'] = self.sql_pattern
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SqlPattern') is not None:
            self.sql_pattern = m.get('SqlPattern')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSqlPatternResponseBodyItems(TeaModel):
    def __init__(
        self,
        access_ip: str = None,
        avg_cpu_time: str = None,
        avg_peak_memory: str = None,
        avg_scan_size: str = None,
        avg_stage_count: str = None,
        avg_task_count: str = None,
        instance_name: str = None,
        max_cpu_time: str = None,
        max_peak_memory: str = None,
        max_scan_size: str = None,
        max_stage_count: str = None,
        max_task_count: str = None,
        pattern: str = None,
        query_count: str = None,
        report_date: str = None,
        user: str = None,
    ):
        self.access_ip = access_ip
        self.avg_cpu_time = avg_cpu_time
        self.avg_peak_memory = avg_peak_memory
        self.avg_scan_size = avg_scan_size
        self.avg_stage_count = avg_stage_count
        self.avg_task_count = avg_task_count
        self.instance_name = instance_name
        self.max_cpu_time = max_cpu_time
        self.max_peak_memory = max_peak_memory
        self.max_scan_size = max_scan_size
        self.max_stage_count = max_stage_count
        self.max_task_count = max_task_count
        self.pattern = pattern
        self.query_count = query_count
        self.report_date = report_date
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_ip is not None:
            result['AccessIP'] = self.access_ip
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.avg_peak_memory is not None:
            result['AvgPeakMemory'] = self.avg_peak_memory
        if self.avg_scan_size is not None:
            result['AvgScanSize'] = self.avg_scan_size
        if self.avg_stage_count is not None:
            result['AvgStageCount'] = self.avg_stage_count
        if self.avg_task_count is not None:
            result['AvgTaskCount'] = self.avg_task_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.max_stage_count is not None:
            result['MaxStageCount'] = self.max_stage_count
        if self.max_task_count is not None:
            result['MaxTaskCount'] = self.max_task_count
        if self.pattern is not None:
            result['Pattern'] = self.pattern
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.report_date is not None:
            result['ReportDate'] = self.report_date
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIP') is not None:
            self.access_ip = m.get('AccessIP')
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('AvgPeakMemory') is not None:
            self.avg_peak_memory = m.get('AvgPeakMemory')
        if m.get('AvgScanSize') is not None:
            self.avg_scan_size = m.get('AvgScanSize')
        if m.get('AvgStageCount') is not None:
            self.avg_stage_count = m.get('AvgStageCount')
        if m.get('AvgTaskCount') is not None:
            self.avg_task_count = m.get('AvgTaskCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('MaxStageCount') is not None:
            self.max_stage_count = m.get('MaxStageCount')
        if m.get('MaxTaskCount') is not None:
            self.max_task_count = m.get('MaxTaskCount')
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSqlPatternResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeSqlPatternResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSqlPatternResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSqlPatternResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSqlPatternResponseBody = None,
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
            temp_model = DescribeSqlPatternResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTableAccessCountRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
        table_name: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTableAccessCountResponseBodyItems(TeaModel):
    def __init__(
        self,
        access_count: str = None,
        instance_name: str = None,
        report_date: str = None,
        table_name: str = None,
        table_schema: str = None,
    ):
        self.access_count = access_count
        self.instance_name = instance_name
        self.report_date = report_date
        self.table_name = table_name
        self.table_schema = table_schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_count is not None:
            result['AccessCount'] = self.access_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.report_date is not None:
            result['ReportDate'] = self.report_date
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        return self


class DescribeTableAccessCountResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeTableAccessCountResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTableAccessCountResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTableAccessCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTableAccessCountResponseBody = None,
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
            temp_model = DescribeTableAccessCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadDiagnosisRecordsRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        dbcluster_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        max_peak_memory: int = None,
        max_scan_size: int = None,
        min_peak_memory: int = None,
        min_scan_size: int = None,
        query_condition: str = None,
        region_id: str = None,
        resource_group: str = None,
        start_time: str = None,
        user_name: str = None,
    ):
        self.client_ip = client_ip
        self.dbcluster_id = dbcluster_id
        self.database = database
        self.end_time = end_time
        self.keyword = keyword
        self.lang = lang
        self.max_peak_memory = max_peak_memory
        self.max_scan_size = max_scan_size
        self.min_peak_memory = min_peak_memory
        self.min_scan_size = min_scan_size
        self.query_condition = query_condition
        self.region_id = region_id
        self.resource_group = resource_group
        self.start_time = start_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.min_peak_memory is not None:
            result['MinPeakMemory'] = self.min_peak_memory
        if self.min_scan_size is not None:
            result['MinScanSize'] = self.min_scan_size
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('MinPeakMemory') is not None:
            self.min_peak_memory = m.get('MinPeakMemory')
        if m.get('MinScanSize') is not None:
            self.min_scan_size = m.get('MinScanSize')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DownloadDiagnosisRecordsResponseBody(TeaModel):
    def __init__(
        self,
        download_id: int = None,
        request_id: str = None,
    ):
        self.download_id = download_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadDiagnosisRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadDiagnosisRecordsResponseBody = None,
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
            temp_model = DownloadDiagnosisRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLakehouseValidResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        groups_info: str = None,
    ):
        self.groups_info = groups_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.groups_info is not None:
            result['GroupsInfo'] = self.groups_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupsInfo') is not None:
            self.groups_info = m.get('GroupsInfo')
        return self


class GetLakehouseValidResourceGroupsResponseBodyDataValidPoolsInfo(TeaModel):
    def __init__(
        self,
        available: bool = None,
        cu_options: List[int] = None,
        group_name: str = None,
        group_type: str = None,
        max_compute_resource: str = None,
        min_compute_resource: str = None,
    ):
        self.available = available
        self.cu_options = cu_options
        self.group_name = group_name
        self.group_type = group_type
        self.max_compute_resource = max_compute_resource
        self.min_compute_resource = min_compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.cu_options is not None:
            result['CuOptions'] = self.cu_options
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('CuOptions') is not None:
            self.cu_options = m.get('CuOptions')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        return self


class GetLakehouseValidResourceGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        lakehouse_min_compute_resource: int = None,
        valid_pools_info: List[GetLakehouseValidResourceGroupsResponseBodyDataValidPoolsInfo] = None,
    ):
        self.lakehouse_min_compute_resource = lakehouse_min_compute_resource
        self.valid_pools_info = valid_pools_info

    def validate(self):
        if self.valid_pools_info:
            for k in self.valid_pools_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lakehouse_min_compute_resource is not None:
            result['LakehouseMinComputeResource'] = self.lakehouse_min_compute_resource
        result['ValidPoolsInfo'] = []
        if self.valid_pools_info is not None:
            for k in self.valid_pools_info:
                result['ValidPoolsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LakehouseMinComputeResource') is not None:
            self.lakehouse_min_compute_resource = m.get('LakehouseMinComputeResource')
        self.valid_pools_info = []
        if m.get('ValidPoolsInfo') is not None:
            for k in m.get('ValidPoolsInfo'):
                temp_model = GetLakehouseValidResourceGroupsResponseBodyDataValidPoolsInfo()
                self.valid_pools_info.append(temp_model.from_map(k))
        return self


class GetLakehouseValidResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetLakehouseValidResourceGroupsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
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
        if m.get('Data') is not None:
            temp_model = GetLakehouseValidResourceGroupsResponseBodyData()
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


class GetLakehouseValidResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLakehouseValidResourceGroupsResponseBody = None,
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
            temp_model = GetLakehouseValidResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkAppAttemptLogRequest(TeaModel):
    def __init__(
        self,
        attempt_id: str = None,
        log_length: int = None,
    ):
        self.attempt_id = attempt_id
        self.log_length = log_length

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.log_length is not None:
            result['LogLength'] = self.log_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('LogLength') is not None:
            self.log_length = m.get('LogLength')
        return self


class GetSparkAppAttemptLogResponseBodyData(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        log_content: str = None,
        message: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.log_content = log_content
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.log_content is not None:
            result['LogContent'] = self.log_content
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetSparkAppAttemptLogResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkAppAttemptLogResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkAppAttemptLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkAppAttemptLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkAppAttemptLogResponseBody = None,
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
            temp_model = GetSparkAppAttemptLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkAppInfoRequest(TeaModel):
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


class GetSparkAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: SparkAppInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SparkAppInfo()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkAppInfoResponseBody = None,
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
            temp_model = GetSparkAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkAppLogRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        log_length: int = None,
    ):
        self.app_id = app_id
        self.log_length = log_length

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.log_length is not None:
            result['LogLength'] = self.log_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LogLength') is not None:
            self.log_length = m.get('LogLength')
        return self


class GetSparkAppLogResponseBodyData(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        log_content: str = None,
        message: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.log_content = log_content
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.log_content is not None:
            result['LogContent'] = self.log_content
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetSparkAppLogResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkAppLogResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkAppLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkAppLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkAppLogResponseBody = None,
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
            temp_model = GetSparkAppLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkAppMetricsRequest(TeaModel):
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


class GetSparkAppMetricsResponseBodyDataScanMetrics(TeaModel):
    def __init__(
        self,
        output_rows_count: int = None,
        total_read_file_size_in_byte: int = None,
    ):
        self.output_rows_count = output_rows_count
        self.total_read_file_size_in_byte = total_read_file_size_in_byte

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_rows_count is not None:
            result['OutputRowsCount'] = self.output_rows_count
        if self.total_read_file_size_in_byte is not None:
            result['TotalReadFileSizeInByte'] = self.total_read_file_size_in_byte
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputRowsCount') is not None:
            self.output_rows_count = m.get('OutputRowsCount')
        if m.get('TotalReadFileSizeInByte') is not None:
            self.total_read_file_size_in_byte = m.get('TotalReadFileSizeInByte')
        return self


class GetSparkAppMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attempt_id: str = None,
        event_log_path: str = None,
        finished: bool = None,
        scan_metrics: GetSparkAppMetricsResponseBodyDataScanMetrics = None,
    ):
        self.app_id = app_id
        self.attempt_id = attempt_id
        self.event_log_path = event_log_path
        self.finished = finished
        self.scan_metrics = scan_metrics

    def validate(self):
        if self.scan_metrics:
            self.scan_metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.event_log_path is not None:
            result['EventLogPath'] = self.event_log_path
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.scan_metrics is not None:
            result['ScanMetrics'] = self.scan_metrics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('EventLogPath') is not None:
            self.event_log_path = m.get('EventLogPath')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('ScanMetrics') is not None:
            temp_model = GetSparkAppMetricsResponseBodyDataScanMetrics()
            self.scan_metrics = temp_model.from_map(m['ScanMetrics'])
        return self


class GetSparkAppMetricsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkAppMetricsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkAppMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkAppMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkAppMetricsResponseBody = None,
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
            temp_model = GetSparkAppMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkAppStateRequest(TeaModel):
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


class GetSparkAppStateResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        dbcluster_id: str = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.dbcluster_id = dbcluster_id
        self.message = message
        self.state = state

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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetSparkAppStateResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkAppStateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkAppStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkAppStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkAppStateResponseBody = None,
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
            temp_model = GetSparkAppStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkAppWebUiAddressRequest(TeaModel):
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


class GetSparkAppWebUiAddressResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        dbcluster_id: str = None,
        expiration_time_in_millis: int = None,
        web_ui_address: str = None,
    ):
        self.app_id = app_id
        self.dbcluster_id = dbcluster_id
        self.expiration_time_in_millis = expiration_time_in_millis
        self.web_ui_address = web_ui_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.expiration_time_in_millis is not None:
            result['ExpirationTimeInMillis'] = self.expiration_time_in_millis
        if self.web_ui_address is not None:
            result['WebUiAddress'] = self.web_ui_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ExpirationTimeInMillis') is not None:
            self.expiration_time_in_millis = m.get('ExpirationTimeInMillis')
        if m.get('WebUiAddress') is not None:
            self.web_ui_address = m.get('WebUiAddress')
        return self


class GetSparkAppWebUiAddressResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkAppWebUiAddressResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkAppWebUiAddressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkAppWebUiAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkAppWebUiAddressResponseBody = None,
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
            temp_model = GetSparkAppWebUiAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkConfigLogPathRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class GetSparkConfigLogPathResponseBodyData(TeaModel):
    def __init__(
        self,
        default_log_path: str = None,
        is_log_path_exists: bool = None,
        modified_timestamp: str = None,
        modified_uid: str = None,
        recorded_log_path: str = None,
    ):
        self.default_log_path = default_log_path
        self.is_log_path_exists = is_log_path_exists
        self.modified_timestamp = modified_timestamp
        self.modified_uid = modified_uid
        self.recorded_log_path = recorded_log_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_log_path is not None:
            result['DefaultLogPath'] = self.default_log_path
        if self.is_log_path_exists is not None:
            result['IsLogPathExists'] = self.is_log_path_exists
        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp
        if self.modified_uid is not None:
            result['ModifiedUid'] = self.modified_uid
        if self.recorded_log_path is not None:
            result['RecordedLogPath'] = self.recorded_log_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultLogPath') is not None:
            self.default_log_path = m.get('DefaultLogPath')
        if m.get('IsLogPathExists') is not None:
            self.is_log_path_exists = m.get('IsLogPathExists')
        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')
        if m.get('ModifiedUid') is not None:
            self.modified_uid = m.get('ModifiedUid')
        if m.get('RecordedLogPath') is not None:
            self.recorded_log_path = m.get('RecordedLogPath')
        return self


class GetSparkConfigLogPathResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkConfigLogPathResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkConfigLogPathResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkConfigLogPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkConfigLogPathResponseBody = None,
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
            temp_model = GetSparkConfigLogPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkLogAnalyzeTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetSparkLogAnalyzeTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: SparkAnalyzeLogTask = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SparkAnalyzeLogTask()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkLogAnalyzeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkLogAnalyzeTaskResponseBody = None,
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
            temp_model = GetSparkLogAnalyzeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkSQLEngineStateRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        resource_group_name: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class GetSparkSQLEngineStateResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        config: str = None,
        jars: str = None,
        max_executor: str = None,
        min_executor: str = None,
        slot_num: str = None,
        state: str = None,
        submitted_time_in_millis: str = None,
    ):
        self.app_id = app_id
        self.config = config
        self.jars = jars
        self.max_executor = max_executor
        self.min_executor = min_executor
        self.slot_num = slot_num
        self.state = state
        self.submitted_time_in_millis = submitted_time_in_millis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config is not None:
            result['Config'] = self.config
        if self.jars is not None:
            result['Jars'] = self.jars
        if self.max_executor is not None:
            result['MaxExecutor'] = self.max_executor
        if self.min_executor is not None:
            result['MinExecutor'] = self.min_executor
        if self.slot_num is not None:
            result['SlotNum'] = self.slot_num
        if self.state is not None:
            result['State'] = self.state
        if self.submitted_time_in_millis is not None:
            result['SubmittedTimeInMillis'] = self.submitted_time_in_millis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Jars') is not None:
            self.jars = m.get('Jars')
        if m.get('MaxExecutor') is not None:
            self.max_executor = m.get('MaxExecutor')
        if m.get('MinExecutor') is not None:
            self.min_executor = m.get('MinExecutor')
        if m.get('SlotNum') is not None:
            self.slot_num = m.get('SlotNum')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SubmittedTimeInMillis') is not None:
            self.submitted_time_in_millis = m.get('SubmittedTimeInMillis')
        return self


class GetSparkSQLEngineStateResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkSQLEngineStateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkSQLEngineStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkSQLEngineStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkSQLEngineStateResponseBody = None,
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
            temp_model = GetSparkSQLEngineStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkTemplateFileContentRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetSparkTemplateFileContentResponseBodyData(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        content: str = None,
        id: int = None,
        resource_group_name: str = None,
        type: str = None,
    ):
        self.app_type = app_type
        self.content = content
        self.id = id
        self.resource_group_name = resource_group_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSparkTemplateFileContentResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkTemplateFileContentResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkTemplateFileContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkTemplateFileContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkTemplateFileContentResponseBody = None,
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
            temp_model = GetSparkTemplateFileContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkTemplateFolderTreeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class GetSparkTemplateFolderTreeResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkTemplateFolderTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkTemplateFolderTreeResponseBody = None,
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
            temp_model = GetSparkTemplateFolderTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkTemplateFullTreeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class GetSparkTemplateFullTreeResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkTemplateFullTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkTemplateFullTreeResponseBody = None,
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
            temp_model = GetSparkTemplateFullTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetViewDDLRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        schema_name: str = None,
        view_name: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        self.schema_name = schema_name
        self.view_name = view_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.view_name is not None:
            result['ViewName'] = self.view_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')
        return self


class GetViewDDLResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sql: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sql is not None:
            result['SQL'] = self.sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        return self


class GetViewDDLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetViewDDLResponseBody = None,
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
            temp_model = GetViewDDLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillSparkAppRequest(TeaModel):
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


class KillSparkAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        dbcluster_id: str = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.dbcluster_id = dbcluster_id
        self.message = message
        self.state = state

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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class KillSparkAppResponseBody(TeaModel):
    def __init__(
        self,
        data: KillSparkAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = KillSparkAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillSparkAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillSparkAppResponseBody = None,
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
            temp_model = KillSparkAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillSparkLogAnalyzeTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class KillSparkLogAnalyzeTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: SparkAnalyzeLogTask = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SparkAnalyzeLogTask()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillSparkLogAnalyzeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillSparkLogAnalyzeTaskResponseBody = None,
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
            temp_model = KillSparkLogAnalyzeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillSparkSQLEngineRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        resource_group_name: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class KillSparkSQLEngineResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillSparkSQLEngineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillSparkSQLEngineResponseBody = None,
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
            temp_model = KillSparkSQLEngineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSparkAppAttemptsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSparkAppAttemptsResponseBodyData(TeaModel):
    def __init__(
        self,
        attempt_info_list: List[SparkAttemptInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.attempt_info_list = attempt_info_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.attempt_info_list:
            for k in self.attempt_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttemptInfoList'] = []
        if self.attempt_info_list is not None:
            for k in self.attempt_info_list:
                result['AttemptInfoList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attempt_info_list = []
        if m.get('AttemptInfoList') is not None:
            for k in m.get('AttemptInfoList'):
                temp_model = SparkAttemptInfo()
                self.attempt_info_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSparkAppAttemptsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListSparkAppAttemptsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSparkAppAttemptsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSparkAppAttemptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSparkAppAttemptsResponseBody = None,
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
            temp_model = ListSparkAppAttemptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSparkAppsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_name: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class ListSparkAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_info_list: List[SparkAppInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.app_info_list = app_info_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = SparkAppInfo()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSparkAppsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListSparkAppsResponseBodyData = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSparkAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSparkAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSparkAppsResponseBody = None,
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
            temp_model = ListSparkAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSparkLogAnalyzeTasksRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSparkLogAnalyzeTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        task_list: List[SparkAnalyzeLogTask] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.task_list = task_list
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = SparkAnalyzeLogTask()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSparkLogAnalyzeTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: ListSparkLogAnalyzeTasksResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSparkLogAnalyzeTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSparkLogAnalyzeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSparkLogAnalyzeTasksResponseBody = None,
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
            temp_model = ListSparkLogAnalyzeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSparkTemplateFileIdsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ListSparkTemplateFileIdsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSparkTemplateFileIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSparkTemplateFileIdsResponseBody = None,
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
            temp_model = ListSparkTemplateFileIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        dbcluster_id: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
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


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountDescriptionResponseBody = None,
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
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAuditLogConfigRequest(TeaModel):
    def __init__(
        self,
        audit_log_status: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.audit_log_status = audit_log_status
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyAuditLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        update_succeed: bool = None,
    ):
        self.request_id = request_id
        self.update_succeed = update_succeed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_succeed is not None:
            result['UpdateSucceed'] = self.update_succeed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateSucceed') is not None:
            self.update_succeed = m.get('UpdateSucceed')
        return self


class ModifyAuditLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAuditLogConfigResponseBody = None,
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
            temp_model = ModifyAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        backup_retention_period: str = None,
        dbcluster_id: str = None,
        enable_backup_log: str = None,
        log_backup_retention_period: int = None,
        owner_account: str = None,
        owner_id: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.backup_retention_period = backup_retention_period
        self.dbcluster_id = dbcluster_id
        self.enable_backup_log = enable_backup_log
        self.log_backup_retention_period = log_backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.preferred_backup_period = preferred_backup_period
        self.preferred_backup_time = preferred_backup_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
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


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupPolicyResponseBody = None,
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
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterAccessWhiteListRequest(TeaModel):
    def __init__(
        self,
        dbcluster_iparray_attribute: str = None,
        dbcluster_iparray_name: str = None,
        dbcluster_id: str = None,
        modify_mode: str = None,
        security_ips: str = None,
    ):
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        self.dbcluster_iparray_name = dbcluster_iparray_name
        self.dbcluster_id = dbcluster_id
        self.modify_mode = modify_mode
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifyClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyClusterAccessWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterAccessWhiteListResponseBody = None,
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
            temp_model = ModifyClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterConnectionStringRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        current_connection_string: str = None,
        dbcluster_id: str = None,
        port: int = None,
    ):
        self.connection_string_prefix = connection_string_prefix
        self.current_connection_string = current_connection_string
        self.dbcluster_id = dbcluster_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyClusterConnectionStringResponseBody(TeaModel):
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


class ModifyClusterConnectionStringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterConnectionStringResponseBody = None,
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
            temp_model = ModifyClusterConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterRequest(TeaModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        storage_resource: str = None,
    ):
        self.compute_resource = compute_resource
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.storage_resource = storage_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        return self


class ModifyDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterResponseBody = None,
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
            temp_model = ModifyDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
    ):
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ModifyDBClusterDescriptionResponseBody(TeaModel):
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


class ModifyDBClusterDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterDescriptionResponseBody = None,
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
            temp_model = ModifyDBClusterDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterMaintainTimeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        maintain_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.maintain_time = maintain_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        return self


class ModifyDBClusterMaintainTimeResponseBody(TeaModel):
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


class ModifyDBClusterMaintainTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterMaintainTimeResponseBody = None,
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
            temp_model = ModifyDBClusterMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_type: str = None,
        max_compute_resource: str = None,
        min_compute_resource: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.group_name = group_name
        self.group_type = group_type
        self.max_compute_resource = max_compute_resource
        self.min_compute_resource = min_compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        return self


class ModifyDBResourceGroupResponseBody(TeaModel):
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


class ModifyDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBResourceGroupResponseBody = None,
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
            temp_model = ModifyDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadSparkAppMetricsRequest(TeaModel):
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


class PreloadSparkAppMetricsResponseBodyDataScanMetrics(TeaModel):
    def __init__(
        self,
        output_rows_count: int = None,
        total_read_file_size_in_byte: int = None,
    ):
        self.output_rows_count = output_rows_count
        self.total_read_file_size_in_byte = total_read_file_size_in_byte

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_rows_count is not None:
            result['OutputRowsCount'] = self.output_rows_count
        if self.total_read_file_size_in_byte is not None:
            result['TotalReadFileSizeInByte'] = self.total_read_file_size_in_byte
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputRowsCount') is not None:
            self.output_rows_count = m.get('OutputRowsCount')
        if m.get('TotalReadFileSizeInByte') is not None:
            self.total_read_file_size_in_byte = m.get('TotalReadFileSizeInByte')
        return self


class PreloadSparkAppMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attempt_id: str = None,
        event_log_path: str = None,
        finished: bool = None,
        scan_metrics: PreloadSparkAppMetricsResponseBodyDataScanMetrics = None,
    ):
        self.app_id = app_id
        self.attempt_id = attempt_id
        self.event_log_path = event_log_path
        self.finished = finished
        self.scan_metrics = scan_metrics

    def validate(self):
        if self.scan_metrics:
            self.scan_metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.event_log_path is not None:
            result['EventLogPath'] = self.event_log_path
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.scan_metrics is not None:
            result['ScanMetrics'] = self.scan_metrics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('EventLogPath') is not None:
            self.event_log_path = m.get('EventLogPath')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('ScanMetrics') is not None:
            temp_model = PreloadSparkAppMetricsResponseBodyDataScanMetrics()
            self.scan_metrics = temp_model.from_map(m['ScanMetrics'])
        return self


class PreloadSparkAppMetricsResponseBody(TeaModel):
    def __init__(
        self,
        data: PreloadSparkAppMetricsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = PreloadSparkAppMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreloadSparkAppMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PreloadSparkAppMetricsResponseBody = None,
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
            temp_model = PreloadSparkAppMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterPublicConnectionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ReleaseClusterPublicConnectionResponseBody(TeaModel):
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


class ReleaseClusterPublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseClusterPublicConnectionResponseBody = None,
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
            temp_model = ReleaseClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        dbcluster_id: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_password = account_password
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
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


class ResetAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAccountPasswordResponseBody = None,
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
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSparkAppLogRootPathRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        oss_log_path: str = None,
        use_default_oss: bool = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.oss_log_path = oss_log_path
        self.use_default_oss = use_default_oss

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.oss_log_path is not None:
            result['OssLogPath'] = self.oss_log_path
        if self.use_default_oss is not None:
            result['UseDefaultOss'] = self.use_default_oss
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OssLogPath') is not None:
            self.oss_log_path = m.get('OssLogPath')
        if m.get('UseDefaultOss') is not None:
            self.use_default_oss = m.get('UseDefaultOss')
        return self


class SetSparkAppLogRootPathResponseBodyData(TeaModel):
    def __init__(
        self,
        default_log_path: str = None,
        is_log_path_exists: bool = None,
        modified_timestamp: str = None,
        modified_uid: str = None,
        recorded_log_path: str = None,
    ):
        self.default_log_path = default_log_path
        self.is_log_path_exists = is_log_path_exists
        self.modified_timestamp = modified_timestamp
        self.modified_uid = modified_uid
        self.recorded_log_path = recorded_log_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_log_path is not None:
            result['DefaultLogPath'] = self.default_log_path
        if self.is_log_path_exists is not None:
            result['IsLogPathExists'] = self.is_log_path_exists
        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp
        if self.modified_uid is not None:
            result['ModifiedUid'] = self.modified_uid
        if self.recorded_log_path is not None:
            result['RecordedLogPath'] = self.recorded_log_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultLogPath') is not None:
            self.default_log_path = m.get('DefaultLogPath')
        if m.get('IsLogPathExists') is not None:
            self.is_log_path_exists = m.get('IsLogPathExists')
        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')
        if m.get('ModifiedUid') is not None:
            self.modified_uid = m.get('ModifiedUid')
        if m.get('RecordedLogPath') is not None:
            self.recorded_log_path = m.get('RecordedLogPath')
        return self


class SetSparkAppLogRootPathResponseBody(TeaModel):
    def __init__(
        self,
        data: SetSparkAppLogRootPathResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SetSparkAppLogRootPathResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSparkAppLogRootPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSparkAppLogRootPathResponseBody = None,
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
            temp_model = SetSparkAppLogRootPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSparkSQLEngineRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        dbcluster_id: str = None,
        jars: str = None,
        max_executor: int = None,
        min_executor: int = None,
        resource_group_name: str = None,
        slot_num: int = None,
    ):
        self.config = config
        self.dbcluster_id = dbcluster_id
        self.jars = jars
        self.max_executor = max_executor
        self.min_executor = min_executor
        self.resource_group_name = resource_group_name
        self.slot_num = slot_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.jars is not None:
            result['Jars'] = self.jars
        if self.max_executor is not None:
            result['MaxExecutor'] = self.max_executor
        if self.min_executor is not None:
            result['MinExecutor'] = self.min_executor
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.slot_num is not None:
            result['SlotNum'] = self.slot_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Jars') is not None:
            self.jars = m.get('Jars')
        if m.get('MaxExecutor') is not None:
            self.max_executor = m.get('MaxExecutor')
        if m.get('MinExecutor') is not None:
            self.min_executor = m.get('MinExecutor')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('SlotNum') is not None:
            self.slot_num = m.get('SlotNum')
        return self


class StartSparkSQLEngineResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.state = state

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
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class StartSparkSQLEngineResponseBody(TeaModel):
    def __init__(
        self,
        data: StartSparkSQLEngineResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StartSparkSQLEngineResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartSparkSQLEngineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSparkSQLEngineResponseBody = None,
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
            temp_model = StartSparkSQLEngineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSparkAppRequest(TeaModel):
    def __init__(
        self,
        agent_source: str = None,
        agent_version: str = None,
        app_name: str = None,
        app_type: str = None,
        dbcluster_id: str = None,
        data: str = None,
        resource_group_name: str = None,
        template_file_id: int = None,
    ):
        self.agent_source = agent_source
        self.agent_version = agent_version
        self.app_name = app_name
        self.app_type = app_type
        self.dbcluster_id = dbcluster_id
        self.data = data
        self.resource_group_name = resource_group_name
        self.template_file_id = template_file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_source is not None:
            result['AgentSource'] = self.agent_source
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.data is not None:
            result['Data'] = self.data
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.template_file_id is not None:
            result['TemplateFileId'] = self.template_file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentSource') is not None:
            self.agent_source = m.get('AgentSource')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('TemplateFileId') is not None:
            self.template_file_id = m.get('TemplateFileId')
        return self


class SubmitSparkAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.message = message
        self.state = state

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
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SubmitSparkAppResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitSparkAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitSparkAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSparkAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSparkAppResponseBody = None,
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
            temp_model = SubmitSparkAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSparkLogAnalyzeTaskRequest(TeaModel):
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


class SubmitSparkLogAnalyzeTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: SparkAnalyzeLogTask = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SparkAnalyzeLogTask()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSparkLogAnalyzeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSparkLogAnalyzeTaskResponseBody = None,
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
            temp_model = SubmitSparkLogAnalyzeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
    ):
        self.account_name = account_name
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class UnbindAccountResponseBody(TeaModel):
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


class UnbindAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindAccountResponseBody = None,
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
            temp_model = UnbindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSparkTemplateFileRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        dbcluster_id: str = None,
        id: int = None,
        resource_group_name: str = None,
    ):
        self.content = content
        self.dbcluster_id = dbcluster_id
        self.id = id
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class UpdateSparkTemplateFileResponseBodyData(TeaModel):
    def __init__(
        self,
        succeeded: bool = None,
    ):
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class UpdateSparkTemplateFileResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateSparkTemplateFileResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateSparkTemplateFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSparkTemplateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSparkTemplateFileResponseBody = None,
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
            temp_model = UpdateSparkTemplateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


