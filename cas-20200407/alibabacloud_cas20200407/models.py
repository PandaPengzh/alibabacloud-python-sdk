# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CancelCertificateForPackageRequestRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CancelCertificateForPackageRequestResponseBody(TeaModel):
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


class CancelCertificateForPackageRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCertificateForPackageRequestResponseBody = None,
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
            temp_model = CancelCertificateForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRequestRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CancelOrderRequestResponseBody(TeaModel):
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


class CancelOrderRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOrderRequestResponseBody = None,
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
            temp_model = CancelOrderRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateForPackageRequestRequest(TeaModel):
    def __init__(
        self,
        company_name: str = None,
        csr: str = None,
        domain: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        username: str = None,
        validate_type: str = None,
    ):
        self.company_name = company_name
        self.csr = csr
        self.domain = domain
        self.email = email
        self.phone = phone
        self.product_code = product_code
        self.username = username
        self.validate_type = validate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateForPackageRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
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


class CreateCertificateForPackageRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateForPackageRequestResponseBody = None,
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
            temp_model = CreateCertificateForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        username: str = None,
        validate_type: str = None,
    ):
        self.domain = domain
        self.email = email
        self.phone = phone
        self.product_code = product_code
        self.username = username
        self.validate_type = validate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
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


class CreateCertificateRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateRequestResponseBody = None,
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
            temp_model = CreateCertificateRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateWithCsrRequestRequest(TeaModel):
    def __init__(
        self,
        csr: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        username: str = None,
        validate_type: str = None,
    ):
        self.csr = csr
        self.email = email
        self.phone = phone
        self.product_code = product_code
        self.username = username
        self.validate_type = validate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateWithCsrRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
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


class CreateCertificateWithCsrRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateWithCsrRequestResponseBody = None,
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
            temp_model = CreateCertificateWithCsrRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertificateRequestRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteCertificateRequestResponseBody(TeaModel):
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


class DeleteCertificateRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCertificateRequestResponseBody = None,
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
            temp_model = DeleteCertificateRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePCACertRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DeletePCACertResponseBody(TeaModel):
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


class DeletePCACertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePCACertResponseBody = None,
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
            temp_model = DeletePCACertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateStateRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DescribeCertificateStateResponseBody(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        content: str = None,
        domain: str = None,
        private_key: str = None,
        record_domain: str = None,
        record_type: str = None,
        record_value: str = None,
        request_id: str = None,
        type: str = None,
        uri: str = None,
        validate_type: str = None,
    ):
        self.certificate = certificate
        self.content = content
        self.domain = domain
        self.private_key = private_key
        self.record_domain = record_domain
        self.record_type = record_type
        self.record_value = record_value
        self.request_id = request_id
        self.type = type
        self.uri = uri
        self.validate_type = validate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.content is not None:
            result['Content'] = self.content
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.record_domain is not None:
            result['RecordDomain'] = self.record_domain
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.record_value is not None:
            result['RecordValue'] = self.record_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RecordDomain') is not None:
            self.record_domain = m.get('RecordDomain')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('RecordValue') is not None:
            self.record_value = m.get('RecordValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class DescribeCertificateStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCertificateStateResponseBody = None,
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
            temp_model = DescribeCertificateStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackageStateRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
    ):
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribePackageStateResponseBody(TeaModel):
    def __init__(
        self,
        issued_count: int = None,
        product_code: str = None,
        request_id: str = None,
        total_count: int = None,
        used_count: int = None,
    ):
        self.issued_count = issued_count
        self.product_code = product_code
        self.request_id = request_id
        self.total_count = total_count
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issued_count is not None:
            result['IssuedCount'] = self.issued_count
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssuedCount') is not None:
            self.issued_count = m.get('IssuedCount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribePackageStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackageStateResponseBody = None,
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
            temp_model = DescribePackageStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCertRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        key_word: str = None,
        show_size: int = None,
        status: str = None,
        warehouse_id: int = None,
    ):
        self.current_page = current_page
        self.key_word = key_word
        self.show_size = show_size
        self.status = status
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.status is not None:
            result['Status'] = self.status
        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')
        return self


class ListCertResponseBodyCertList(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        before_date: int = None,
        common_name: str = None,
        exist_private_key: bool = None,
        identifier: str = None,
        issuer: str = None,
        sans: str = None,
        source_type: str = None,
        status: str = None,
        wh_id: int = None,
        wh_instance_id: str = None,
    ):
        self.after_date = after_date
        self.before_date = before_date
        self.common_name = common_name
        self.exist_private_key = exist_private_key
        self.identifier = identifier
        self.issuer = issuer
        self.sans = sans
        self.source_type = source_type
        self.status = status
        self.wh_id = wh_id
        self.wh_instance_id = wh_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.exist_private_key is not None:
            result['ExistPrivateKey'] = self.exist_private_key
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.wh_id is not None:
            result['WhId'] = self.wh_id
        if self.wh_instance_id is not None:
            result['WhInstanceId'] = self.wh_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('ExistPrivateKey') is not None:
            self.exist_private_key = m.get('ExistPrivateKey')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WhId') is not None:
            self.wh_id = m.get('WhId')
        if m.get('WhInstanceId') is not None:
            self.wh_instance_id = m.get('WhInstanceId')
        return self


class ListCertResponseBody(TeaModel):
    def __init__(
        self,
        cert_list: List[ListCertResponseBodyCertList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.cert_list = cert_list
        self.current_page = current_page
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = ListCertResponseBodyCertList()
                self.cert_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCertResponseBody = None,
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
            temp_model = ListCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCertWarehouseRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        name: str = None,
        show_size: int = None,
        type: str = None,
    ):
        self.current_page = current_page
        self.instance_id = instance_id
        self.name = name
        self.show_size = show_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCertWarehouseResponseBodyCertWarehouseList(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        is_expired: bool = None,
        name: str = None,
        pca_instance_id: str = None,
        qps: int = None,
        type: str = None,
        wh_id: int = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.is_expired = is_expired
        self.name = name
        self.pca_instance_id = pca_instance_id
        self.qps = qps
        self.type = type
        self.wh_id = wh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.name is not None:
            result['Name'] = self.name
        if self.pca_instance_id is not None:
            result['PcaInstanceId'] = self.pca_instance_id
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.type is not None:
            result['Type'] = self.type
        if self.wh_id is not None:
            result['WhId'] = self.wh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PcaInstanceId') is not None:
            self.pca_instance_id = m.get('PcaInstanceId')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhId') is not None:
            self.wh_id = m.get('WhId')
        return self


class ListCertWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        cert_warehouse_list: List[ListCertWarehouseResponseBodyCertWarehouseList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.cert_warehouse_list = cert_warehouse_list
        self.current_page = current_page
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.cert_warehouse_list:
            for k in self.cert_warehouse_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertWarehouseList'] = []
        if self.cert_warehouse_list is not None:
            for k in self.cert_warehouse_list:
                result['CertWarehouseList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_warehouse_list = []
        if m.get('CertWarehouseList') is not None:
            for k in m.get('CertWarehouseList'):
                temp_model = ListCertWarehouseResponseBodyCertWarehouseList()
                self.cert_warehouse_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCertWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCertWarehouseResponseBody = None,
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
            temp_model = ListCertWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserCertificateOrderRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        keyword: str = None,
        order_type: str = None,
        show_size: int = None,
        status: str = None,
    ):
        self.current_page = current_page
        self.keyword = keyword
        self.order_type = order_type
        self.show_size = show_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListUserCertificateOrderResponseBodyCertificateOrderList(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        aliyun_order_id: int = None,
        buy_date: int = None,
        cert_end_time: int = None,
        cert_start_time: int = None,
        cert_type: str = None,
        domain: str = None,
        domain_count: int = None,
        domain_type: str = None,
        instance_id: str = None,
        order_id: int = None,
        partner_order_id: str = None,
        product_code: str = None,
        product_name: str = None,
        root_brand: str = None,
        source_type: str = None,
        status: str = None,
        trustee_status: str = None,
        wild_domain_count: int = None,
    ):
        self.algorithm = algorithm
        self.aliyun_order_id = aliyun_order_id
        self.buy_date = buy_date
        self.cert_end_time = cert_end_time
        self.cert_start_time = cert_start_time
        self.cert_type = cert_type
        self.domain = domain
        self.domain_count = domain_count
        self.domain_type = domain_type
        self.instance_id = instance_id
        self.order_id = order_id
        self.partner_order_id = partner_order_id
        self.product_code = product_code
        self.product_name = product_name
        self.root_brand = root_brand
        self.source_type = source_type
        self.status = status
        self.trustee_status = trustee_status
        self.wild_domain_count = wild_domain_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.buy_date is not None:
            result['BuyDate'] = self.buy_date
        if self.cert_end_time is not None:
            result['CertEndTime'] = self.cert_end_time
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_order_id is not None:
            result['PartnerOrderId'] = self.partner_order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.root_brand is not None:
            result['RootBrand'] = self.root_brand
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.trustee_status is not None:
            result['TrusteeStatus'] = self.trustee_status
        if self.wild_domain_count is not None:
            result['WildDomainCount'] = self.wild_domain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('BuyDate') is not None:
            self.buy_date = m.get('BuyDate')
        if m.get('CertEndTime') is not None:
            self.cert_end_time = m.get('CertEndTime')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerOrderId') is not None:
            self.partner_order_id = m.get('PartnerOrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RootBrand') is not None:
            self.root_brand = m.get('RootBrand')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrusteeStatus') is not None:
            self.trustee_status = m.get('TrusteeStatus')
        if m.get('WildDomainCount') is not None:
            self.wild_domain_count = m.get('WildDomainCount')
        return self


class ListUserCertificateOrderResponseBody(TeaModel):
    def __init__(
        self,
        certificate_order_list: List[ListUserCertificateOrderResponseBodyCertificateOrderList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.certificate_order_list = certificate_order_list
        self.current_page = current_page
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.certificate_order_list:
            for k in self.certificate_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateOrderList'] = []
        if self.certificate_order_list is not None:
            for k in self.certificate_order_list:
                result['CertificateOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_order_list = []
        if m.get('CertificateOrderList') is not None:
            for k in m.get('CertificateOrderList'):
                temp_model = ListUserCertificateOrderResponseBodyCertificateOrderList()
                self.certificate_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserCertificateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserCertificateOrderResponseBody = None,
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
            temp_model = ListUserCertificateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewCertificateOrderForPackageRequestRequest(TeaModel):
    def __init__(
        self,
        csr: str = None,
        order_id: int = None,
    ):
        self.csr = csr
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewCertificateOrderForPackageRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
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


class RenewCertificateOrderForPackageRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewCertificateOrderForPackageRequestResponseBody = None,
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
            temp_model = RenewCertificateOrderForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SignRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        message: str = None,
        message_type: str = None,
        signing_algorithm: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.message = message
        self.message_type = message_type
        self.signing_algorithm = signing_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signing_algorithm is not None:
            result['SigningAlgorithm'] = self.signing_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')
        return self


class SignResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signature: str = None,
    ):
        self.request_id = request_id
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class SignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SignResponseBody = None,
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
            temp_model = SignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadPCACertRequest(TeaModel):
    def __init__(
        self,
        cert: str = None,
        name: str = None,
        private_key: str = None,
        warehouse_id: int = None,
    ):
        self.cert = cert
        self.name = name
        self.private_key = private_key
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.name is not None:
            result['Name'] = self.name
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')
        return self


class UploadPCACertResponseBody(TeaModel):
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


class UploadPCACertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadPCACertResponseBody = None,
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
            temp_model = UploadPCACertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        message: str = None,
        message_type: str = None,
        signature_value: str = None,
        signing_algorithm: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.message = message
        self.message_type = message_type
        self.signature_value = signature_value
        self.signing_algorithm = signing_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.signing_algorithm is not None:
            result['SigningAlgorithm'] = self.signing_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')
        return self


class VerifyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signature_valid: bool = None,
    ):
        self.request_id = request_id
        self.signature_valid = signature_valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_valid is not None:
            result['SignatureValid'] = self.signature_valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureValid') is not None:
            self.signature_valid = m.get('SignatureValid')
        return self


class VerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyResponseBody = None,
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
            temp_model = VerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


