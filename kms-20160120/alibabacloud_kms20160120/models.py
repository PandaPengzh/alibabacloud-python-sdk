# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AsymmetricDecryptRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        ciphertext_blob: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The decryption algorithm.
        self.algorithm = algorithm
        # The ciphertext that you want to decrypt.
        # 
        # > 
        # *   The value is encoded in Base64.
        # *   You can call the [AsymmetricEncrypt](~~148131~~) operation to generate the ciphertext.
        self.ciphertext_blob = ciphertext_blob
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id
        # The version ID of the CMK. The ID must be globally unique.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricDecryptResponseBody(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The version ID of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id
        # The Base64-encoded plaintext that is generated after decryption.
        self.plaintext = plaintext
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AsymmetricDecryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsymmetricDecryptResponseBody = None,
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
            temp_model = AsymmetricDecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricEncryptRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        key_id: str = None,
        key_version_id: str = None,
        plaintext: str = None,
    ):
        # The encryption algorithm.
        self.algorithm = algorithm
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id
        # The version ID of the CMK. The ID must be globally unique.
        # 
        # >  You can call the [ListKeyVersions](~~133966~~) operation to query the versions of a CMK. The ID of a version is specified by the KeyVersionId parameter.
        self.key_version_id = key_version_id
        # The plaintext that you want to encrypt. The plaintext must be Base64-encoded.
        self.plaintext = plaintext

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class AsymmetricEncryptResponseBody(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
    ):
        # The Base64-encoded ciphertext that was generated after encryption.
        self.ciphertext_blob = ciphertext_blob
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The version ID of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AsymmetricEncryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsymmetricEncryptResponseBody = None,
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
            temp_model = AsymmetricEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricSignRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        digest: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The signature algorithm.
        self.algorithm = algorithm
        # The digest that is generated for the original message by using a hash algorithm. The hash algorithm is specified by the Algorithm parameter.
        # 
        # > 
        # *   The value is encoded in Base64.
        # *   For more information about how to calculate message digests, see the **Preprocess signature: compute a message digest** section of the [Generate and verify a signature by using an asymmetric CMK](~~148146~~) topic.
        self.digest = digest
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id
        # The version ID of the CMK. The ID must be globally unique.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricSignResponseBody(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
        value: str = None,
    ):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The version ID of the CMK. The ID must be globally unique.
        self.key_version_id = key_version_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The calculated signature.
        # 
        # >  The value is encoded in Base64.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AsymmetricSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsymmetricSignResponseBody = None,
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
            temp_model = AsymmetricSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricVerifyRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        digest: str = None,
        key_id: str = None,
        key_version_id: str = None,
        value: str = None,
    ):
        # The signature algorithm.
        self.algorithm = algorithm
        # The digest that is generated for the original message by using a hash algorithm. The hash algorithm is specified by the **Algorithm** parameter.
        # 
        # >  The value is encoded in Base64.
        self.digest = digest
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id
        # The version ID of the CMK. The ID must be globally unique.
        self.key_version_id = key_version_id
        # The signature value to be verified.
        # 
        # >  The value is encoded in Base64.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AsymmetricVerifyResponseBody(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
        value: bool = None,
    ):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The version ID of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the signature passed the verification.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AsymmetricVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsymmetricVerifyResponseBody = None,
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
            temp_model = AsymmetricVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelKeyDeletionRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class CancelKeyDeletionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class CancelKeyDeletionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelKeyDeletionResponseBody = None,
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
            temp_model = CancelKeyDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePrivateKeyDecryptRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        certificate_id: str = None,
        ciphertext_blob: str = None,
    ):
        # The encryption algorithm. Valid values:
        # 
        # *   RSAES_OAEP_SHA\_1
        # 
        # *   RSAES_OAEP_SHA\_256
        # 
        # *   SM2PKE
        # 
        # > The SM2PKE encryption algorithm is supported only in regions in mainland China. In these regions, managed hardware security modules (HSMs) are used. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id
        # The data that you want to decrypt.
        # 
        # The value is encoded in Base64.
        self.ciphertext_blob = ciphertext_blob

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        return self


class CertificatePrivateKeyDecryptResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The plaintext after data is decrypted.
        # 
        # The value is encoded in Base64.
        self.plaintext = plaintext
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CertificatePrivateKeyDecryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CertificatePrivateKeyDecryptResponseBody = None,
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
            temp_model = CertificatePrivateKeyDecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePrivateKeySignRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        certificate_id: str = None,
        message: str = None,
        message_type: str = None,
    ):
        # The signature algorithm. Valid values:
        # 
        # *   RSA_PKCS1\_SHA\_256
        # 
        # *   RSA_PSS_SHA\_256
        # 
        # *   ECDSA_SHA\_256
        # 
        # *   SM2DSA
        # 
        # >* The SM2DSA signature algorithm is supported only in regions where managed hardware security modules (HSMs) are used in mainland China. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id
        # The data to be signed.
        # 
        # The value is encoded in Base64. For example, if the hexadecimal data that you want to sign is `[0x31, 0x32, 0x33, 0x34]`, the Base64-encoded data is `MTIzNA==`.
        # 
        # If the MessageType parameter is set to RAW, the size of the data must be less than or equal to 4 KB.
        # 
        # If the size of the data is greater than 4 KB, you can set the MessageType parameter to DIGEST and set the Message parameter to the digest of the data. The digest is also called hash value. You can compute the digest of the data on an on-premises machine. Certificates Manager uses the digest that you compute in your own certificate application system. The message digest algorithm that you use must match the specified signature algorithm. Comply with the following mapping between signature algorithms and message digest algorithms:
        # 
        # *   If the signature algorithm is RSA_PKCS1\_SHA\_256, RSA_PSS_SHA\_256, or ECDSA_SHA\_256, the message digest algorithm must be SHA-256.
        # *   If the signature algorithm is SM2DSA, the message digest algorithm must be SM3.
        # 
        # >  If the key type of the certificate is EC_SM2 and the MessageType parameter is set to DIGEST, the value of the Message parameter is `e` that is described in GB/T 32918.2-2016 6.1.
        self.message = message
        # The type of the message. Valid values:
        # 
        # *   RAW: the raw data. This is the default value.
        # *   DIGEST: the message digest (hash value) of the raw data.
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class CertificatePrivateKeySignResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        request_id: str = None,
        signature_value: str = None,
    ):
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The signature value.
        # 
        # The value is encoded in Base64.
        self.signature_value = signature_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        return self


class CertificatePrivateKeySignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CertificatePrivateKeySignResponseBody = None,
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
            temp_model = CertificatePrivateKeySignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePublicKeyEncryptRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        certificate_id: str = None,
        plaintext: str = None,
    ):
        # The encryption algorithm. Valid values:
        # 
        # *   RSAES_OAEP_SHA\_1
        # 
        # *   RSAES_OAEP_SHA\_256
        # 
        # *   SM2PKE
        # 
        # >The SM2PKE encryption algorithm is supported only in regions in mainland China. In these regions, managed hardware security modules (HSMs) are used. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id
        # The data that you want to encrypt.
        # 
        # The value is encoded in Base64. For example, if the hexadecimal data that you want to encrypt is `[0x31, 0x32, 0x33, 0x34]`, the Base64-encoded data is `MTIzNA==`.
        # 
        # The size of data that can be encrypted varies based on the encryption algorithm that you use:
        # 
        # *   RSAES_OAEP_SHA\_1: 214 bytes
        # *   RSAES_OAEP_SHA\_256: 190 bytes
        # *   SM2PKE: 6,047 bytes
        # 
        # If the size of data that you want to encrypt exceeds the preceding limits, you can call the [GenerateDataKey](~~28948~~) operation to generate a data key to encrypt the data. Then, call the CertificatePublicKeyEncrypt operation to encrypt the data key.
        self.plaintext = plaintext

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class CertificatePublicKeyEncryptResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        ciphertext_blob: str = None,
        request_id: str = None,
    ):
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The ciphertext.
        # 
        # The value is encoded in Base64.
        self.ciphertext_blob = ciphertext_blob
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CertificatePublicKeyEncryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CertificatePublicKeyEncryptResponseBody = None,
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
            temp_model = CertificatePublicKeyEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePublicKeyVerifyRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        certificate_id: str = None,
        message: str = None,
        message_type: str = None,
        signature_value: str = None,
    ):
        # The signature algorithm. Valid values:
        # 
        # *   RSA_PKCS1\_SHA\_256
        # 
        # *   RSA_PSS_SHA\_256
        # 
        # *   ECDSA_SHA\_256
        # 
        # *   SM2DSA
        # 
        # > The SM2DSA signature algorithm is supported only in regions where managed hardware security modules (HSMs) are used in the Chinese mainland. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id
        # The raw data that is signed.
        # 
        # The value is encoded in Base64. For example, if the raw data in the hexadecimal format is `[0x31, 0x32, 0x33, 0x34]`, set this parameter to the Base64-encoded value `MTIzNA==`.
        # 
        # If the MessageType parameter is set to RAW, the size of the data must be less than or equal to 4 KB.
        # 
        # If the size of the data is greater than 4 KB, you can set the MessageType parameter to DIGEST and set the Message parameter to the digest of the data. The digest is also called hash value. You can compute the digest of the data on an on-premises device. Certificates Manager uses the digest that you compute in your own certificate application system. The message digest algorithm that you use must match the specified signature algorithm. Comply with the following mapping between signature algorithms and message digest algorithms:
        # 
        # *   If the signature algorithm is RSA_PKCS1\_SHA\_256, RSA_PSS_SHA\_256, or ECDSA_SHA\_256, the message digest algorithm must be SHA-256.
        # *   If the signature algorithm is SM2DSA, the message digest algorithm must be SM3.
        # 
        # >  If the key type of the certificate is EC_SM2 and the MessageType parameter is set to DIGEST, the value of the Message parameter is `e` that is described in GB/T 32918.2-2016 6.1.
        self.message = message
        # The type of the message. Valid values:
        # 
        # *   RAW: the raw data. This is the default value.
        # *   DIGEST: the message digest (hash value) of the raw data.
        self.message_type = message_type
        # The signature value.
        # 
        # The value is encoded in Base64.
        self.signature_value = signature_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        return self


class CertificatePublicKeyVerifyResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        request_id: str = None,
        signature_valid: bool = None,
    ):
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The verification result. Valid values:
        # 
        # *   true: The signature is valid.
        # *   false: The signature is invalid.
        self.signature_valid = signature_valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_valid is not None:
            result['SignatureValid'] = self.signature_valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureValid') is not None:
            self.signature_valid = m.get('SignatureValid')
        return self


class CertificatePublicKeyVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CertificatePublicKeyVerifyResponseBody = None,
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
            temp_model = CertificatePublicKeyVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        key_id: str = None,
    ):
        # The alias of the CMK.
        # 
        # The alias must be 1 to 255 characters in length and must contain the prefix `alias/`. The alias cannot be prefixed with the reserved word `alias/acs`.
        self.alias_name = alias_name
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class CreateAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class CreateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAliasResponseBody = None,
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
            temp_model = CreateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateRequest(TeaModel):
    def __init__(
        self,
        exportable_private_key: bool = None,
        key_spec: str = None,
        subject: str = None,
        subject_alternative_names: Dict[str, Any] = None,
    ):
        # Specifies whether the private key of the certificate can be exported for use. Valid values:
        # 
        # *   true: The private key of the certificate can be exported for use. This is the default value.
        # *   false: The private key of the certificate cannot be exported for use. We recommend that you set this parameter to false to protect keys with a higher security level.
        self.exportable_private_key = exportable_private_key
        # The type of the key. Valid values:
        # 
        # *   RSA\_2048
        # *   EC_P256
        # *   EC_SM2
        self.key_spec = key_spec
        # The certificate subject, which is the owner of the certificate.
        # 
        # Specify the value in the distinguished name (DN) format, as defined in [RFC 2253](https://tools.ietf.org/html/rfc2253?spm=a2c4g.11186623.2.13.265f1a1cGFCn3Q). A DN is a sequence of relative distinguished names (RDNs).
        # 
        # RDNs are key-value pairs in the format of `attribute1=value1,attribute2=value2`. Separate multiple RDNs with commas (,).
        # 
        # The Subject parameter consists of the following fields:
        # 
        # *   CN: required. The name of the certificate subject.
        # *   C: required. The two-character country or region code in the [ISO 3166-1](https://www.iso.org/obp/ui/#search/code/) standard. For example, CN indicates China.
        # *   O: required. The legal name of the enterprise, company, organization, or institution.
        # *   OU: required. The name of the department.
        # *   ST: optional. The name of the province, municipality, autonomous region, or special administrative region.
        # *   L: optional. The name of the city.
        self.subject = subject
        # The subject alternative names.
        # 
        # A domain name list is supported. A maximum of 10 domain names are supported.
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exportable_private_key is not None:
            result['ExportablePrivateKey'] = self.exportable_private_key
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportablePrivateKey') is not None:
            self.exportable_private_key = m.get('ExportablePrivateKey')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('SubjectAlternativeNames')
        return self


class CreateCertificateShrinkRequest(TeaModel):
    def __init__(
        self,
        exportable_private_key: bool = None,
        key_spec: str = None,
        subject: str = None,
        subject_alternative_names_shrink: str = None,
    ):
        # Specifies whether the private key of the certificate can be exported for use. Valid values:
        # 
        # *   true: The private key of the certificate can be exported for use. This is the default value.
        # *   false: The private key of the certificate cannot be exported for use. We recommend that you set this parameter to false to protect keys with a higher security level.
        self.exportable_private_key = exportable_private_key
        # The type of the key. Valid values:
        # 
        # *   RSA\_2048
        # *   EC_P256
        # *   EC_SM2
        self.key_spec = key_spec
        # The certificate subject, which is the owner of the certificate.
        # 
        # Specify the value in the distinguished name (DN) format, as defined in [RFC 2253](https://tools.ietf.org/html/rfc2253?spm=a2c4g.11186623.2.13.265f1a1cGFCn3Q). A DN is a sequence of relative distinguished names (RDNs).
        # 
        # RDNs are key-value pairs in the format of `attribute1=value1,attribute2=value2`. Separate multiple RDNs with commas (,).
        # 
        # The Subject parameter consists of the following fields:
        # 
        # *   CN: required. The name of the certificate subject.
        # *   C: required. The two-character country or region code in the [ISO 3166-1](https://www.iso.org/obp/ui/#search/code/) standard. For example, CN indicates China.
        # *   O: required. The legal name of the enterprise, company, organization, or institution.
        # *   OU: required. The name of the department.
        # *   ST: optional. The name of the province, municipality, autonomous region, or special administrative region.
        # *   L: optional. The name of the city.
        self.subject = subject
        # The subject alternative names.
        # 
        # A domain name list is supported. A maximum of 10 domain names are supported.
        self.subject_alternative_names_shrink = subject_alternative_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exportable_private_key is not None:
            result['ExportablePrivateKey'] = self.exportable_private_key
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names_shrink is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportablePrivateKey') is not None:
            self.exportable_private_key = m.get('ExportablePrivateKey')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names_shrink = m.get('SubjectAlternativeNames')
        return self


class CreateCertificateResponseBody(TeaModel):
    def __init__(
        self,
        arn: str = None,
        certificate_id: str = None,
        csr: str = None,
        request_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the certificate.
        self.arn = arn
        # The ID of the certificate. It is the globally unique identifier (GUID) of the certificate in Certificates Manager.
        self.certificate_id = certificate_id
        # The CSR in the PEM format.
        self.csr = csr
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateResponseBody = None,
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
            temp_model = CreateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyRequest(TeaModel):
    def __init__(
        self,
        dkmsinstance_id: str = None,
        description: str = None,
        enable_automatic_rotation: bool = None,
        key_spec: str = None,
        key_usage: str = None,
        origin: str = None,
        protection_level: str = None,
        rotation_interval: str = None,
    ):
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the CMK.
        # 
        # The description can be 0 to 8,192 characters in length.
        self.description = description
        # Specifies whether to enable automatic key rotation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        # 
        # >  If the Origin parameter is set to EXTERNAL or the KeySpec parameter is set to an asymmetric CMK type, automatic key rotation is not supported.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The type of the CMK. Valid values:
        # 
        # *   Aliyun_AES\_256
        # *   Aliyun_AES\_128
        # *   Aliyun_AES\_192
        # *   Aliyun_SM4
        # *   RSA\_2048
        # *   RSA\_3072
        # *   EC_P256
        # *   EC_P256K
        # *   EC_SM2
        # 
        # > 
        # *   The default type of the CMK is Aliyun_AES\_256.
        # *   Only Dedicated KMS supports Aliyun_AES\_128 and Aliyun_AES\_192.
        self.key_spec = key_spec
        # The usage of the CMK. Valid values:
        # 
        # *   ENCRYPT/DECRYPT: encrypts or decrypts data.
        # *   SIGN/VERIFY: generates or verifies a digital signature.
        # 
        # If the CMK supports signature verification, the default value is SIGN/VERIFY. If the CMK does not support signature verification, the default value is ENCRYPT/DECRYPT.
        self.key_usage = key_usage
        # The source of key material. Valid values:
        # 
        # *   Aliyun_KMS (default value)
        # *   EXTERNAL
        # 
        # > 
        # *   The value of this parameter is case-sensitive.
        # *   If you set the KeySpec parameter to an asymmetric CMK type, you are not allowed to set the Origin parameter to EXTERNAL.
        # *   If you set the Origin parameter to EXTERNAL, you must import key material. For more information, see [Import key material](~~68523~~).
        self.origin = origin
        # The protection level of the CMK. Valid values:
        # 
        # *   SOFTWARE
        # *   HSM
        # 
        # Default value: SOFTWARE.
        # 
        # > 
        # *   The value of this parameter is case-sensitive.
        # *   Assume that you set this parameter to HSM. If you set the Origin parameter to Aliyun_KMS, the CMK is created in a managed HSM. If you set the Origin parameter to EXTERNAL, you can import an external key into the managed HSM.
        self.protection_level = protection_level
        # The period of automatic key rotation. Specify the value in the integer\[unit] format. Unit: d (day), h (hour), m (minute), or s (second). For example, you can use either 7d or 604800s to specify a seven-day period. The period can range from 7 days to 730 days.
        # 
        # >  If you set the EnableAutomaticRotation parameter to true, you must also specify this parameter. If you set the EnableAutomaticRotation parameter to false, you can leave this parameter unspecified.
        self.rotation_interval = rotation_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class CreateKeyResponseBodyKeyMetadata(TeaModel):
    def __init__(
        self,
        arn: str = None,
        automatic_rotation: str = None,
        creation_date: str = None,
        creator: str = None,
        dkmsinstance_id: str = None,
        delete_date: str = None,
        description: str = None,
        key_id: str = None,
        key_spec: str = None,
        key_state: str = None,
        key_usage: str = None,
        last_rotation_date: str = None,
        material_expire_time: str = None,
        next_rotation_date: str = None,
        origin: str = None,
        primary_key_version: str = None,
        protection_level: str = None,
        rotation_interval: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the CMK.
        self.arn = arn
        # Indicates whether automatic key rotation is enabled. Valid values:
        # 
        # *   Enabled: Automatic key rotation is enabled.
        # *   Disabled: Automatic key rotation is disabled.
        # *   Suspended: Automatic key rotation is suspended. For more information, see [Automatic key rotation](~~134270~~).
        # 
        # >  Automatic key rotation is available only for symmetric CMKs.
        self.automatic_rotation = automatic_rotation
        # The date and time when the CMK was created. The time is displayed in UTC.
        self.creation_date = creation_date
        # The creator of the CMK.
        self.creator = creator
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The time when the CMK is scheduled for deletion.
        # 
        # For more information, see [ScheduleKeyDeletion](~~44196~~).
        # 
        # >  This value is returned only when the value of the KeyState parameter is PendingDeletion.
        self.delete_date = delete_date
        # The description of the CMK.
        self.description = description
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id
        # The type of the CMK.
        self.key_spec = key_spec
        # The status of the CMK.
        # 
        # For more information, see [Impact of CMK status on API operations](~~44211~~).
        self.key_state = key_state
        # The usage of the CMK.
        self.key_usage = key_usage
        # The time when the last rotation was performed. The time is displayed in UTC.
        # 
        # For a new CMK, this parameter value is the time when the initial version of the CMK was generated.
        self.last_rotation_date = last_rotation_date
        # The time when the key material expires. The time is displayed in UTC.
        # 
        # If this parameter value is empty, the key material does not expire.
        self.material_expire_time = material_expire_time
        # The time when the next rotation will be performed.
        # 
        # >  This value is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.next_rotation_date = next_rotation_date
        # The source of the key material for the CMK.
        self.origin = origin
        # The ID of the current primary key version of the symmetric CMK.
        # 
        # > 
        # *   The primary key version of a symmetric CMK is an active encryption key. KMS uses the primary key version of a specified CMK to encrypt data.
        # *   This parameter is unavailable for asymmetric CMKs.
        self.primary_key_version = primary_key_version
        # The protection level of the CMK.
        self.protection_level = protection_level
        # The period of automatic key rotation. Unit: seconds. The value is in the format of an integer followed by the letter s. For example, if the rotation period is seven days, this parameter is set to 604800s. This value is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.rotation_interval = rotation_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.key_state is not None:
            result['KeyState'] = self.key_state
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.primary_key_version is not None:
            result['PrimaryKeyVersion'] = self.primary_key_version
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('KeyState') is not None:
            self.key_state = m.get('KeyState')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('PrimaryKeyVersion') is not None:
            self.primary_key_version = m.get('PrimaryKeyVersion')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class CreateKeyResponseBody(TeaModel):
    def __init__(
        self,
        key_metadata: CreateKeyResponseBodyKeyMetadata = None,
        request_id: str = None,
    ):
        # The metadata of the CMK.
        self.key_metadata = key_metadata
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.key_metadata:
            self.key_metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_metadata is not None:
            result['KeyMetadata'] = self.key_metadata.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyMetadata') is not None:
            temp_model = CreateKeyResponseBodyKeyMetadata()
            self.key_metadata = temp_model.from_map(m['KeyMetadata'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKeyResponseBody = None,
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
            temp_model = CreateKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyVersionRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  You can also set the value to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class CreateKeyVersionResponseBodyKeyVersion(TeaModel):
    def __init__(
        self,
        creation_date: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The date and time when the version was created. The time is displayed in UTC.
        self.creation_date = creation_date
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id
        # The ID of the version.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class CreateKeyVersionResponseBody(TeaModel):
    def __init__(
        self,
        key_version: CreateKeyVersionResponseBodyKeyVersion = None,
        request_id: str = None,
    ):
        # The metadata of the version.
        self.key_version = key_version
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.key_version:
            self.key_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyVersion') is not None:
            temp_model = CreateKeyVersionResponseBodyKeyVersion()
            self.key_version = temp_model.from_map(m['KeyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKeyVersionResponseBody = None,
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
            temp_model = CreateKeyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretRequest(TeaModel):
    def __init__(
        self,
        dkmsinstance_id: str = None,
        description: str = None,
        enable_automatic_rotation: bool = None,
        encryption_key_id: str = None,
        extended_config: Dict[str, Any] = None,
        rotation_interval: str = None,
        secret_data: str = None,
        secret_data_type: str = None,
        secret_name: str = None,
        secret_type: str = None,
        tags: str = None,
        version_id: str = None,
    ):
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the secret.
        self.description = description
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # *   true: specifies to enable automatic rotation.
        # *   false: specifies to disable automatic rotation. This is the default value.
        # 
        # >  This parameter is valid if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The ID of the CMK that is used to encrypt the secret value.
        # 
        # If the DKMSInstanceId parameter is empty, Secrets Manager uses a CMK that is created by Dedicated KMS to encrypt and protect secrets. If the DKMSInstanceId parameter is not empty, specify the CMK of the dedicated KMS instance to encrypt and protect secrets.
        # 
        # >  The CMK must be a symmetric CMK.
        self.encryption_key_id = encryption_key_id
        # The extended configuration of the secret. This parameter specifies the properties of the secret of the specific type. The description can be up to 1,024 characters in length.
        # 
        # *   If you set the SecretType parameter to Generic, you do not need to configure this parameter.
        # 
        # *   If you set the SecretType parameter to Rds, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   SingleUser: Secrets Manager manages the ApsaraDB RDS secret in single-account mode. When the secret is rotated, the password of the specified account is reset to a new random password.
        #         *   DoubleUsers: Secrets Manager manages the ApsaraDB RDS secret in dual-account mode. One account is referenced by the ACSCurrent version, and the other account is referenced by the ACSPrevious version. When the secret is rotated, the password of the account referenced by the ACSPrevious version is reset to a new random password. Then, Secrets Manager switches the referenced accounts between the ACSCurrent and ACSPrevious versions.
        # 
        #     *   DBInstanceId: required. The ApsaraDB RDS instance to which the ApsaraDB RDS account belongs.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to RAMCredentials, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Set the value to RamUserAccessKey.
        #     *   UserName: required. The name of the RAM user.
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to ECS, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   Password: the password that is used to log on to the ECS instance.
        #         *   SSHKey: the SSH public key and private key that are used to log on to the ECS instance.
        # 
        #     *   RegionId: required. The ID of the region in which the ECS instance resides.
        # 
        #     *   InstanceId: required. The ID of the ECS instance.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # >  This parameter is required if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.extended_config = extended_config
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).
        # 
        # The value is in the `integer[unit]` format.
        # 
        # The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s indicate a seven-day interval.
        # 
        # >  This parameter is required if you set the EnableAutomaticRotation parameter to true. This parameter is ignored if you set the EnableAutomaticRotation parameter to false or if the EnableAutomaticRotation parameter is not configured.
        self.rotation_interval = rotation_interval
        # The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores the encrypted value in the initial version.
        # 
        # *   If you set the SecretType parameter to Generic that indicates a generic secret, you can customize the secret value.
        # 
        # *   If you set the SecretType parameter to Rds that indicates a managed ApsaraDB RDS secret, the secret value must be in the format of `{"Accounts":[{"AccountName":"","AccountPassword":""}]}`. In the preceding format, `AccountName` indicates the username of the account that is used to connect to your ApsaraDB RDS instance, and `AccountPassword` specifies the password of the account.
        # 
        # *   If you set the SecretType parameter to RAMCredentials that indicates a managed RAM secret, the secret value must be in the format of `{"AccessKeys":[{"AccessKeyId":"","AccessKeySecret":"",}]}`. In the preceding format, `AccessKeyId` indicates the AccessKey ID of the RAM user and `AccessKeySecret` specifies the AccessKey secret of the RAM user. You must specify all the AccessKey pairs of the RAM user.
        # 
        # *   If you set the SecretType parameter to ECS that indicates a managed ECS secret, the secret value must be in one of the following formats:
        # 
        #     *   `{"UserName":"","Password": ""}`: In the format, `UserName` specifies the username that is used to log on to the ECS instance, and `Password` specifies the password that is used to log on to the ECS instance.
        #     *   `{"UserName":"","PublicKey": "", "PrivateKey": ""}`: In the format, `PublicKey` indicates the SSH public key that is used to log on to the ECS instance, and `PrivateKey` specifies the SSH private key that is used to log on to the ECS instance.
        self.secret_data = secret_data
        # The type of the secret value. Valid values:
        # 
        # *   text
        # *   binary
        # 
        # >  If you set the SecretType parameter to Rds, RAMCredentials, or ECS, the SecretDataType parameter must be set to text.
        self.secret_data_type = secret_data_type
        # The name of the secret.
        # 
        # The value must be 1 to 64 characters in length and can contain letters, digits, underscores (\_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        # 
        # *   If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        # *   If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        # *   If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # *   Generic: specifies a generic secret.
        # *   Rds: specifies a managed ApsaraDB RDS secret.
        # *   RAMCredentials: specifies a managed RAM secret.
        # *   ECS: specifies a managed ECS secret.
        self.secret_type = secret_type
        # The tags of the secret.
        self.tags = tags
        # The initial version number. Version numbers are unique in each secret.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateSecretShrinkRequest(TeaModel):
    def __init__(
        self,
        dkmsinstance_id: str = None,
        description: str = None,
        enable_automatic_rotation: bool = None,
        encryption_key_id: str = None,
        extended_config_shrink: str = None,
        rotation_interval: str = None,
        secret_data: str = None,
        secret_data_type: str = None,
        secret_name: str = None,
        secret_type: str = None,
        tags: str = None,
        version_id: str = None,
    ):
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the secret.
        self.description = description
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # *   true: specifies to enable automatic rotation.
        # *   false: specifies to disable automatic rotation. This is the default value.
        # 
        # >  This parameter is valid if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The ID of the CMK that is used to encrypt the secret value.
        # 
        # If the DKMSInstanceId parameter is empty, Secrets Manager uses a CMK that is created by Dedicated KMS to encrypt and protect secrets. If the DKMSInstanceId parameter is not empty, specify the CMK of the dedicated KMS instance to encrypt and protect secrets.
        # 
        # >  The CMK must be a symmetric CMK.
        self.encryption_key_id = encryption_key_id
        # The extended configuration of the secret. This parameter specifies the properties of the secret of the specific type. The description can be up to 1,024 characters in length.
        # 
        # *   If you set the SecretType parameter to Generic, you do not need to configure this parameter.
        # 
        # *   If you set the SecretType parameter to Rds, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   SingleUser: Secrets Manager manages the ApsaraDB RDS secret in single-account mode. When the secret is rotated, the password of the specified account is reset to a new random password.
        #         *   DoubleUsers: Secrets Manager manages the ApsaraDB RDS secret in dual-account mode. One account is referenced by the ACSCurrent version, and the other account is referenced by the ACSPrevious version. When the secret is rotated, the password of the account referenced by the ACSPrevious version is reset to a new random password. Then, Secrets Manager switches the referenced accounts between the ACSCurrent and ACSPrevious versions.
        # 
        #     *   DBInstanceId: required. The ApsaraDB RDS instance to which the ApsaraDB RDS account belongs.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to RAMCredentials, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Set the value to RamUserAccessKey.
        #     *   UserName: required. The name of the RAM user.
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to ECS, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   Password: the password that is used to log on to the ECS instance.
        #         *   SSHKey: the SSH public key and private key that are used to log on to the ECS instance.
        # 
        #     *   RegionId: required. The ID of the region in which the ECS instance resides.
        # 
        #     *   InstanceId: required. The ID of the ECS instance.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # >  This parameter is required if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.extended_config_shrink = extended_config_shrink
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).
        # 
        # The value is in the `integer[unit]` format.
        # 
        # The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s indicate a seven-day interval.
        # 
        # >  This parameter is required if you set the EnableAutomaticRotation parameter to true. This parameter is ignored if you set the EnableAutomaticRotation parameter to false or if the EnableAutomaticRotation parameter is not configured.
        self.rotation_interval = rotation_interval
        # The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores the encrypted value in the initial version.
        # 
        # *   If you set the SecretType parameter to Generic that indicates a generic secret, you can customize the secret value.
        # 
        # *   If you set the SecretType parameter to Rds that indicates a managed ApsaraDB RDS secret, the secret value must be in the format of `{"Accounts":[{"AccountName":"","AccountPassword":""}]}`. In the preceding format, `AccountName` indicates the username of the account that is used to connect to your ApsaraDB RDS instance, and `AccountPassword` specifies the password of the account.
        # 
        # *   If you set the SecretType parameter to RAMCredentials that indicates a managed RAM secret, the secret value must be in the format of `{"AccessKeys":[{"AccessKeyId":"","AccessKeySecret":"",}]}`. In the preceding format, `AccessKeyId` indicates the AccessKey ID of the RAM user and `AccessKeySecret` specifies the AccessKey secret of the RAM user. You must specify all the AccessKey pairs of the RAM user.
        # 
        # *   If you set the SecretType parameter to ECS that indicates a managed ECS secret, the secret value must be in one of the following formats:
        # 
        #     *   `{"UserName":"","Password": ""}`: In the format, `UserName` specifies the username that is used to log on to the ECS instance, and `Password` specifies the password that is used to log on to the ECS instance.
        #     *   `{"UserName":"","PublicKey": "", "PrivateKey": ""}`: In the format, `PublicKey` indicates the SSH public key that is used to log on to the ECS instance, and `PrivateKey` specifies the SSH private key that is used to log on to the ECS instance.
        self.secret_data = secret_data
        # The type of the secret value. Valid values:
        # 
        # *   text
        # *   binary
        # 
        # >  If you set the SecretType parameter to Rds, RAMCredentials, or ECS, the SecretDataType parameter must be set to text.
        self.secret_data_type = secret_data_type
        # The name of the secret.
        # 
        # The value must be 1 to 64 characters in length and can contain letters, digits, underscores (\_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        # 
        # *   If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        # *   If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        # *   If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # *   Generic: specifies a generic secret.
        # *   Rds: specifies a managed ApsaraDB RDS secret.
        # *   RAMCredentials: specifies a managed RAM secret.
        # *   ECS: specifies a managed ECS secret.
        self.secret_type = secret_type
        # The tags of the secret.
        self.tags = tags
        # The initial version number. Version numbers are unique in each secret.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.extended_config_shrink is not None:
            result['ExtendedConfig'] = self.extended_config_shrink
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config_shrink = m.get('ExtendedConfig')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateSecretResponseBody(TeaModel):
    def __init__(
        self,
        arn: str = None,
        automatic_rotation: str = None,
        dkmsinstance_id: str = None,
        extended_config: str = None,
        next_rotation_date: str = None,
        request_id: str = None,
        rotation_interval: str = None,
        secret_name: str = None,
        secret_type: str = None,
        version_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.arn = arn
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.automatic_rotation = automatic_rotation
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The extended configuration of the secret.
        # 
        # >  This parameter is returned if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.extended_config = extended_config
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.next_rotation_date = next_rotation_date
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The interval for automatic rotation.
        # 
        # The value is in the `integer[unit]` format. The value of the `unit` field is fixed as s. For example, if the value is 604800s, automatic rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.rotation_interval = rotation_interval
        # The name of the secret.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        # *   RAMCredentials: indicates a managed RAM secret.
        # *   ECS: indicates a managed ECS secret.
        self.secret_type = secret_type
        # The version number of the secret.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecretResponseBody = None,
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
            temp_model = CreateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecryptRequest(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        encryption_context: Dict[str, Any] = None,
    ):
        # The ciphertext that you want to decrypt.
        # 
        # You can generate the ciphertext by calling the following operations:
        # 
        # *   [GenerateDataKey](~~28948~~)
        # *   [Encrypt](~~28949~~)
        # *   [GenerateDataKeyWithoutPlaintext](~~134043~~)
        self.ciphertext_blob = ciphertext_blob
        # The JSON string that consists of key-value pairs.
        # 
        # >  If you specify the EncryptionContext parameter when you call the [GenerateDataKey](~~28948~~), [Encrypt](~~28949~~), or [GenerateDataKeyWithoutPlaintext](~~134043~~) operation, you must specify the same context when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        return self


class DecryptShrinkRequest(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        encryption_context_shrink: str = None,
    ):
        # The ciphertext that you want to decrypt.
        # 
        # You can generate the ciphertext by calling the following operations:
        # 
        # *   [GenerateDataKey](~~28948~~)
        # *   [Encrypt](~~28949~~)
        # *   [GenerateDataKeyWithoutPlaintext](~~134043~~)
        self.ciphertext_blob = ciphertext_blob
        # The JSON string that consists of key-value pairs.
        # 
        # >  If you specify the EncryptionContext parameter when you call the [GenerateDataKey](~~28948~~), [Encrypt](~~28949~~), or [GenerateDataKeyWithoutPlaintext](~~134043~~) operation, you must specify the same context when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        return self


class DecryptResponseBody(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        # The ID of the customer master key (CMK) that is used to decrypt the ciphertext.
        # 
        # It is the GUID of the CMK.
        self.key_id = key_id
        # The ID of the CMK version that is used to decrypt the ciphertext.
        self.key_version_id = key_version_id
        # The plaintext that is generated after decryption.
        self.plaintext = plaintext
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DecryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DecryptResponseBody = None,
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
            temp_model = DecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAliasRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
    ):
        # The alias that you want to delete.
        # 
        # The value must be 1 to 255 characters in length and must include the alias/ prefix.
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class DeleteAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DeleteAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAliasResponseBody = None,
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
            temp_model = DeleteAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # The ID of the certificate. It is the globally unique identifier (GUID) of the certificate in Alibaba Cloud Certificate Manager.
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class DeleteCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DeleteCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCertificateResponseBody = None,
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
            temp_model = DeleteCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyMaterialRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The globally unique ID of the CMK.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DeleteKeyMaterialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DeleteKeyMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeyMaterialResponseBody = None,
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
            temp_model = DeleteKeyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretRequest(TeaModel):
    def __init__(
        self,
        force_delete_without_recovery: str = None,
        recovery_window_in_days: str = None,
        secret_name: str = None,
    ):
        # Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered.
        # 
        # Valid values:
        # 
        # *   **true**\
        # *   **false** (default value)
        self.force_delete_without_recovery = force_delete_without_recovery
        # Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. Unit: Days.
        self.recovery_window_in_days = recovery_window_in_days
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete_without_recovery is not None:
            result['ForceDeleteWithoutRecovery'] = self.force_delete_without_recovery
        if self.recovery_window_in_days is not None:
            result['RecoveryWindowInDays'] = self.recovery_window_in_days
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDeleteWithoutRecovery') is not None:
            self.force_delete_without_recovery = m.get('ForceDeleteWithoutRecovery')
        if m.get('RecoveryWindowInDays') is not None:
            self.recovery_window_in_days = m.get('RecoveryWindowInDays')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class DeleteSecretResponseBody(TeaModel):
    def __init__(
        self,
        planned_delete_time: str = None,
        request_id: str = None,
        secret_name: str = None,
    ):
        # The time when the secret is scheduled to be deleted.
        self.planned_delete_time = planned_delete_time
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class DeleteSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecretResponseBody = None,
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
            temp_model = DeleteSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountKmsStatusResponseBody(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        request_id: str = None,
    ):
        # The status of KMS within your Alibaba cloud account. Valid values:
        # 
        # *   Enabled: KMS is enabled.
        # 
        # *   NotEnabled: KMS is disabled.
        # 
        # *   InDebt: Your account is overdue, and KMS stops providing services.
        # 
        # > If your Alibaba Cloud account is overdue, top up your account at the earliest opportunity to avoid impacts on your services.
        # 
        # *   Suspended: KMS is suspended.
        self.account_status = account_status
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountKmsStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountKmsStatusResponseBody = None,
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
            temp_model = DescribeAccountKmsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class DescribeCertificateResponseBody(TeaModel):
    def __init__(
        self,
        arn: str = None,
        certificate_id: str = None,
        created_at: str = None,
        exportable_private_key: bool = None,
        issuer: str = None,
        key_spec: str = None,
        not_after: str = None,
        not_before: str = None,
        request_id: str = None,
        serial: str = None,
        signature_algorithm: str = None,
        status: str = None,
        subject: str = None,
        subject_alternative_names: List[str] = None,
        subject_key_identifier: str = None,
        subject_public_key: str = None,
        tags: Dict[str, Any] = None,
        updated_at: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the certificate.
        self.arn = arn
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id
        # The time when the certificate was created.
        self.created_at = created_at
        # Indicates whether the private key of the certificate can be exported for use. Valid values:
        # 
        # *   true: The private key of the certificate can be exported for use. This is the default value.
        # *   false: The private key of the certificate cannot be exported for use.
        self.exportable_private_key = exportable_private_key
        # The certificate issuer in the distinguished name (DN) format.
        self.issuer = issuer
        # The type of the key.
        self.key_spec = key_spec
        # The end of the validity period of the certificate.
        self.not_after = not_after
        # The beginning of the validity period of the certificate.
        self.not_before = not_before
        # The ID of the request.
        self.request_id = request_id
        # The serial number of the certificate.
        self.serial = serial
        # The signature algorithm of the certificate. Valid values:
        # 
        # *   RSA2048-SHA256
        # *   ECDSA-SHA256
        # *   SM2-SM3
        self.signature_algorithm = signature_algorithm
        # The status of the certificate. Valid values:
        # 
        # *   PENDING: The certificate is to be imported.
        # *   ACTIVE: The certificate is enabled.
        # *   INACTIVE: The certificate is disabled.
        # *   REVOKED: The certificate is revoked.
        self.status = status
        # The subject of the certificate, which is in the DN format.
        self.subject = subject
        # The alias of the certificate subject.
        # 
        # A domain name list is supported. A maximum of 10 domain names are supported.
        self.subject_alternative_names = subject_alternative_names
        # The public key identifier of the certificate subject.
        self.subject_key_identifier = subject_key_identifier
        # The public key of the certificate.
        self.subject_public_key = subject_public_key
        # The tag of the certificate.
        self.tags = tags
        # The time when the certificate was updated.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.exportable_private_key is not None:
            result['ExportablePrivateKey'] = self.exportable_private_key
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serial is not None:
            result['Serial'] = self.serial
        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm
        if self.status is not None:
            result['Status'] = self.status
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names
        if self.subject_key_identifier is not None:
            result['SubjectKeyIdentifier'] = self.subject_key_identifier
        if self.subject_public_key is not None:
            result['SubjectPublicKey'] = self.subject_public_key
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ExportablePrivateKey') is not None:
            self.exportable_private_key = m.get('ExportablePrivateKey')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')
        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('SubjectAlternativeNames')
        if m.get('SubjectKeyIdentifier') is not None:
            self.subject_key_identifier = m.get('SubjectKeyIdentifier')
        if m.get('SubjectPublicKey') is not None:
            self.subject_public_key = m.get('SubjectPublicKey')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class DescribeCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCertificateResponseBody = None,
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
            temp_model = DescribeCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DescribeKeyResponseBodyKeyMetadata(TeaModel):
    def __init__(
        self,
        arn: str = None,
        automatic_rotation: str = None,
        creation_date: str = None,
        creator: str = None,
        dkmsinstance_id: str = None,
        delete_date: str = None,
        deletion_protection: str = None,
        deletion_protection_description: str = None,
        description: str = None,
        key_id: str = None,
        key_spec: str = None,
        key_state: str = None,
        key_usage: str = None,
        last_rotation_date: str = None,
        material_expire_time: str = None,
        next_rotation_date: str = None,
        origin: str = None,
        primary_key_version: str = None,
        protection_level: str = None,
        rotation_interval: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the CMK.
        self.arn = arn
        # Indicates whether automatic key rotation is enabled. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        # *   Suspended
        # 
        # For more information, see [Automatic key rotation](~~134270~~).
        # 
        # >  Only symmetric CMKs support automatic key rotation.
        self.automatic_rotation = automatic_rotation
        # The time when the CMK was created. The time is displayed in UTC.
        self.creation_date = creation_date
        # The Alibaba Cloud account that is used to create the CMK.
        self.creator = creator
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The time at which the CMK is scheduled for deletion. The time is displayed in UTC.
        # 
        # For more information, see [ScheduleKeyDeletion](~~44196~~).
        # 
        # >  This parameter is returned only when the value of the KeyState parameter is PendingDeletion.
        self.delete_date = delete_date
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.deletion_protection = deletion_protection
        # The description of deletion protection.
        self.deletion_protection_description = deletion_protection_description
        # The description of the CMK.
        self.description = description
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id
        # The type of the CMK.
        self.key_spec = key_spec
        # The status of the CMK.
        # 
        # For more information, see [Impact of CMK status on API operations](~~44211~~).
        self.key_state = key_state
        # The usage of the CMK.
        self.key_usage = key_usage
        # The time when the last rotation was performed. The time is displayed in UTC. For a new CMK, the value of this parameter is the time when the initial version of the CMK was generated.
        self.last_rotation_date = last_rotation_date
        # The time when the key material expires. The time is displayed in UTC. If this parameter value is empty, the key material does not expire.
        self.material_expire_time = material_expire_time
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.next_rotation_date = next_rotation_date
        # The source of the key material for the CMK.
        self.origin = origin
        # The ID of the current primary key version for the symmetric CMK.
        self.primary_key_version = primary_key_version
        # The protection level of the CMK.
        self.protection_level = protection_level
        # The interval for automatic key rotation.
        # 
        # Unit: seconds.
        # 
        # For example, if the value is 604800s, automatic key rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.rotation_interval = rotation_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.deletion_protection_description is not None:
            result['DeletionProtectionDescription'] = self.deletion_protection_description
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.key_state is not None:
            result['KeyState'] = self.key_state
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.primary_key_version is not None:
            result['PrimaryKeyVersion'] = self.primary_key_version
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('DeletionProtectionDescription') is not None:
            self.deletion_protection_description = m.get('DeletionProtectionDescription')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('KeyState') is not None:
            self.key_state = m.get('KeyState')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('PrimaryKeyVersion') is not None:
            self.primary_key_version = m.get('PrimaryKeyVersion')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class DescribeKeyResponseBody(TeaModel):
    def __init__(
        self,
        key_metadata: DescribeKeyResponseBodyKeyMetadata = None,
        request_id: str = None,
    ):
        # The metadata of the CMK.
        self.key_metadata = key_metadata
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.key_metadata:
            self.key_metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_metadata is not None:
            result['KeyMetadata'] = self.key_metadata.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyMetadata') is not None:
            temp_model = DescribeKeyResponseBodyKeyMetadata()
            self.key_metadata = temp_model.from_map(m['KeyMetadata'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKeyResponseBody = None,
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
            temp_model = DescribeKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyVersionRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The globally unique ID of the CMK.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id
        # The globally unique ID of the CMK version.
        # 
        # You can call the [ListKeyVersions](~~133966~~) operation to query the versions of the CMK.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class DescribeKeyVersionResponseBodyKeyVersion(TeaModel):
    def __init__(
        self,
        creation_date: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The date and time when the CMK version was created. The time is displayed in UTC.
        self.creation_date = creation_date
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter in the request to an alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The globally unique ID of the CMK version.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class DescribeKeyVersionResponseBody(TeaModel):
    def __init__(
        self,
        key_version: DescribeKeyVersionResponseBodyKeyVersion = None,
        request_id: str = None,
    ):
        # The metadata of the CMK version.
        self.key_version = key_version
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.key_version:
            self.key_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyVersion') is not None:
            temp_model = DescribeKeyVersionResponseBodyKeyVersion()
            self.key_version = temp_model.from_map(m['KeyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeKeyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKeyVersionResponseBody = None,
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
            temp_model = DescribeKeyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
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
        # The region.
        self.regions = regions
        # The ID of the request.
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


class DescribeSecretRequest(TeaModel):
    def __init__(
        self,
        fetch_tags: str = None,
        secret_name: str = None,
    ):
        # Specifies whether to return the resource tags of the secret. Valid values:
        # 
        # *   true: The resource tags are returned.
        # *   false: The resource tags are not returned. This is the default value.
        self.fetch_tags = fetch_tags
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class DescribeSecretResponseBodyTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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


class DescribeSecretResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeSecretResponseBodyTagsTag] = None,
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
                temp_model = DescribeSecretResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSecretResponseBody(TeaModel):
    def __init__(
        self,
        arn: str = None,
        automatic_rotation: str = None,
        create_time: str = None,
        dkmsinstance_id: str = None,
        description: str = None,
        encryption_key_id: str = None,
        extended_config: str = None,
        last_rotation_date: str = None,
        next_rotation_date: str = None,
        planned_delete_time: str = None,
        request_id: str = None,
        rotation_interval: str = None,
        secret_name: str = None,
        secret_type: str = None,
        tags: DescribeSecretResponseBodyTags = None,
        update_time: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.arn = arn
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.automatic_rotation = automatic_rotation
        # The time when the secret was created.
        self.create_time = create_time
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the secret.
        self.description = description
        # The ID of the customer master key (CMK) that is used to encrypt the secret value.
        self.encryption_key_id = encryption_key_id
        # The extended configuration of the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed Resource Access Management (RAM) secret, or a managed Elastic Compute Service (ECS) secret.
        self.extended_config = extended_config
        # The time when the last rotation was performed.
        # 
        # >  This parameter is returned if the secret was rotated.
        self.last_rotation_date = last_rotation_date
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned when automatic rotation is enabled.
        self.next_rotation_date = next_rotation_date
        # The time when the secret is scheduled to be deleted.
        self.planned_delete_time = planned_delete_time
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The interval for automatic rotation.
        # 
        # The value is in the `integer[unit]` format. `integer` indicates the length of time. `unit`: indicates the time unit. The value of `unit` is fixed as s. For example, if the value is 604800s, automatic rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned when automatic rotation is enabled.
        self.rotation_interval = rotation_interval
        # The name of the secret.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        # *   RAMCredentials: indicates a managed RAM secret.
        # *   ECS: indicates a managed ECS secret.
        self.secret_type = secret_type
        # The resource tags of the secret.
        # 
        # This parameter is not returned if you set the FetchTags parameter to false or you do not specify the FetchTags parameter.
        self.tags = tags
        # The time when the secret was updated.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            temp_model = DescribeSecretResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecretResponseBody = None,
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
            temp_model = DescribeSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableKeyRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DisableKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DisableKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableKeyResponseBody = None,
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
            temp_model = DisableKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableKeyRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The globally unique ID of the CMK.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class EnableKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class EnableKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableKeyResponseBody = None,
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
            temp_model = EnableKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptRequest(TeaModel):
    def __init__(
        self,
        encryption_context: Dict[str, Any] = None,
        key_id: str = None,
        plaintext: str = None,
    ):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id
        # The plaintext to be encrypted. The plaintext must be Base64 encoded.
        self.plaintext = plaintext

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class EncryptShrinkRequest(TeaModel):
    def __init__(
        self,
        encryption_context_shrink: str = None,
        key_id: str = None,
        plaintext: str = None,
    ):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id
        # The plaintext to be encrypted. The plaintext must be Base64 encoded.
        self.plaintext = plaintext

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class EncryptResponseBody(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
    ):
        # The ciphertext of the data that is encrypted by using the primary CMK version.
        self.ciphertext_blob = ciphertext_blob
        # The globally unique ID of the CMK. If you set the KeyId parameter to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The ID of the key version that is used to encrypt the plaintext. It is the primary version of the CMK.
        self.key_version_id = key_version_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EncryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EncryptResponseBody = None,
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
            temp_model = EncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportDataKeyRequest(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        encryption_context: Dict[str, Any] = None,
        public_key_blob: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # The ciphertext of the data key encrypted by using a CMK.
        self.ciphertext_blob = ciphertext_blob
        # A JSON string that consists of key-value pairs. If you specify this parameter when you use a CMK to encrypt the data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class ExportDataKeyShrinkRequest(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        encryption_context_shrink: str = None,
        public_key_blob: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # The ciphertext of the data key encrypted by using a CMK.
        self.ciphertext_blob = ciphertext_blob
        # A JSON string that consists of key-value pairs. If you specify this parameter when you use a CMK to encrypt the data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class ExportDataKeyResponseBody(TeaModel):
    def __init__(
        self,
        exported_data_key: str = None,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
    ):
        # The data key encrypted by using the public key and then exported.
        self.exported_data_key = exported_data_key
        # The ID of the CMK that is used to decrypt the specified ciphertext of the data key.
        # 
        # This parameter is the globally unique ID of the CMK.
        self.key_id = key_id
        # The ID of the CMK version that is used to decrypt the specified ciphertext of the data key.
        self.key_version_id = key_version_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exported_data_key is not None:
            result['ExportedDataKey'] = self.exported_data_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportedDataKey') is not None:
            self.exported_data_key = m.get('ExportedDataKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportDataKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportDataKeyResponseBody = None,
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
            temp_model = ExportDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAndExportDataKeyRequest(TeaModel):
    def __init__(
        self,
        encryption_context: Dict[str, Any] = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
        public_key_blob: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # A JSON string of key-value pairs. If you specify this parameter here, an equivalent value is required when you decrypt or re-encrypt the data key. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both parameters are not specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class GenerateAndExportDataKeyShrinkRequest(TeaModel):
    def __init__(
        self,
        encryption_context_shrink: str = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
        public_key_blob: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # A JSON string of key-value pairs. If you specify this parameter here, an equivalent value is required when you decrypt or re-encrypt the data key. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both parameters are not specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class GenerateAndExportDataKeyResponseBody(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        exported_data_key: str = None,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
    ):
        # The ciphertext of the data key encrypted by using the primary CMK version.
        self.ciphertext_blob = ciphertext_blob
        # The data key encrypted by using the public key and then exported.
        self.exported_data_key = exported_data_key
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The ID of the CMK version that is used to encrypt the plaintext. It is the primary version of the CMK.
        self.key_version_id = key_version_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.exported_data_key is not None:
            result['ExportedDataKey'] = self.exported_data_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('ExportedDataKey') is not None:
            self.exported_data_key = m.get('ExportedDataKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAndExportDataKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAndExportDataKeyResponseBody = None,
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
            temp_model = GenerateAndExportDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDataKeyRequest(TeaModel):
    def __init__(
        self,
        encryption_context: Dict[str, Any] = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
    ):
        # The JSON string that consists of key-value pairs.
        # 
        # If you specify this parameter, an equivalent value is required when you call the [Decrypt](~~28950~~) operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context
        # The ID of the CMK. The ID must be globally unique.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id
        # The type of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If none of the parameters are specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate. Unit: bytes.
        # 
        # Valid values: 1 to 1024.
        # 
        # Default value:
        # 
        # *   If the KeySpec parameter is set to AES\_256, set the value of the NumberOfBytes parameter to 32.
        # *   If the KeySpec parameter is set to AES\_128, set the value of the NumberOfBytes parameter to 16.
        self.number_of_bytes = number_of_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyShrinkRequest(TeaModel):
    def __init__(
        self,
        encryption_context_shrink: str = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
    ):
        # The JSON string that consists of key-value pairs.
        # 
        # If you specify this parameter, an equivalent value is required when you call the [Decrypt](~~28950~~) operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink
        # The ID of the CMK. The ID must be globally unique.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id
        # The type of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If none of the parameters are specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate. Unit: bytes.
        # 
        # Valid values: 1 to 1024.
        # 
        # Default value:
        # 
        # *   If the KeySpec parameter is set to AES\_256, set the value of the NumberOfBytes parameter to 32.
        # *   If the KeySpec parameter is set to AES\_128, set the value of the NumberOfBytes parameter to 16.
        self.number_of_bytes = number_of_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyResponseBody(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        key_id: str = None,
        key_version_id: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        # The ciphertext of the data key that is encrypted by using the primary version of the specified CMK.
        self.ciphertext_blob = ciphertext_blob
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The ID of the CMK version. The ID must be globally unique.
        self.key_version_id = key_version_id
        # The Base64 encoded plaintext of the data key.
        self.plaintext = plaintext
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateDataKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateDataKeyResponseBody = None,
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
            temp_model = GenerateDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDataKeyWithoutPlaintextRequest(TeaModel):
    def __init__(
        self,
        encryption_context: Dict[str, Any] = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
    ):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see Use aliases.
        self.key_id = key_id
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: 256-bit symmetric key
        # *   AES\_128: 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both of them are not specified, KMS generates a 256-bit data key. If both of them are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyWithoutPlaintextShrinkRequest(TeaModel):
    def __init__(
        self,
        encryption_context_shrink: str = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
    ):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see Use aliases.
        self.key_id = key_id
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: 256-bit symmetric key
        # *   AES\_128: 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both of them are not specified, KMS generates a 256-bit data key. If both of them are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyWithoutPlaintextResponseBody(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
    ):
        # The ciphertext of the data that is encrypted by using the primary CMK version.
        self.ciphertext_blob = ciphertext_blob
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The ID of the key version that is used to encrypt the plaintext. It is the primary version of the CMK.
        self.key_version_id = key_version_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateDataKeyWithoutPlaintextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateDataKeyWithoutPlaintextResponseBody = None,
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
            temp_model = GenerateDataKeyWithoutPlaintextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # The ID of the certificate. It is the globally unique identifier (GUID) of the certificate in Certificates Manager.
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class GetCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        certificate_chain: str = None,
        certificate_id: str = None,
        csr: str = None,
        request_id: str = None,
    ):
        # The certificate in the Privacy Enhanced Mail (PEM) format.
        self.certificate = certificate
        # The certificate chain in the PEM format.
        self.certificate_chain = certificate_chain
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The CSR in the PEM format.
        self.csr = csr
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCertificateResponseBody = None,
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
            temp_model = GetCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersForImportRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # The globally unique ID of the CMK.
        # 
        # >  You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        self.key_id = key_id
        # The algorithm that is used to encrypt key material.
        self.wrapping_algorithm = wrapping_algorithm
        # The type of the public key that is used to encrypt key material.
        self.wrapping_key_spec = wrapping_key_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class GetParametersForImportResponseBody(TeaModel):
    def __init__(
        self,
        import_token: str = None,
        key_id: str = None,
        public_key: str = None,
        request_id: str = None,
        token_expire_time: str = None,
    ):
        # The token that is used to import key material.
        # 
        # The token is valid for 24 hours. The value of this parameter is required when you call the [ImportKeyMaterial](~~68622~~) operation.
        self.import_token = import_token
        # The globally unique ID of the CMK.
        # 
        # The value of this parameter is required when you call the [ImportKeyMaterial](~~68622~~) operation.
        self.key_id = key_id
        # The public key that is used to encrypt key material.
        # 
        # The public key is Base64-encoded.
        self.public_key = public_key
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The time when the token expires.
        self.token_expire_time = token_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_token is not None:
            result['ImportToken'] = self.import_token
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token_expire_time is not None:
            result['TokenExpireTime'] = self.token_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TokenExpireTime') is not None:
            self.token_expire_time = m.get('TokenExpireTime')
        return self


class GetParametersForImportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetParametersForImportResponseBody = None,
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
            temp_model = GetParametersForImportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicKeyRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id
        # The globally unique ID of the CMK version.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class GetPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
        public_key: str = None,
        request_id: str = None,
    ):
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to the alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The version of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id
        # The public key returned in the PEM format.
        self.public_key = public_key
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPublicKeyResponseBody = None,
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
            temp_model = GetPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRandomPasswordRequest(TeaModel):
    def __init__(
        self,
        exclude_characters: str = None,
        exclude_lowercase: str = None,
        exclude_numbers: str = None,
        exclude_punctuation: str = None,
        exclude_uppercase: str = None,
        password_length: str = None,
        require_each_included_type: str = None,
    ):
        # The characters that are not included in the password to be generated.
        # 
        # Valid values:
        # 
        # ` Valid characters: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! \"#$%&\"()*+,-. /:;<=>? @[\] your_project_id} ~  `.
        # 
        # This parameter is empty by default.
        self.exclude_characters = exclude_characters
        # Specifies whether to exclude lowercase letters.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_lowercase = exclude_lowercase
        # Specifies whether to exclude digits.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_numbers = exclude_numbers
        # Specifies whether to exclude special characters.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_punctuation = exclude_punctuation
        # Specifies whether to exclude uppercase letters.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_uppercase = exclude_uppercase
        # The number of bytes that the password to be generated contains.
        # 
        # Valid values: 8 to 128.
        # 
        # Default value: 32
        self.password_length = password_length
        # Specifies whether to include all the preceding character types.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.require_each_included_type = require_each_included_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_characters is not None:
            result['ExcludeCharacters'] = self.exclude_characters
        if self.exclude_lowercase is not None:
            result['ExcludeLowercase'] = self.exclude_lowercase
        if self.exclude_numbers is not None:
            result['ExcludeNumbers'] = self.exclude_numbers
        if self.exclude_punctuation is not None:
            result['ExcludePunctuation'] = self.exclude_punctuation
        if self.exclude_uppercase is not None:
            result['ExcludeUppercase'] = self.exclude_uppercase
        if self.password_length is not None:
            result['PasswordLength'] = self.password_length
        if self.require_each_included_type is not None:
            result['RequireEachIncludedType'] = self.require_each_included_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeCharacters') is not None:
            self.exclude_characters = m.get('ExcludeCharacters')
        if m.get('ExcludeLowercase') is not None:
            self.exclude_lowercase = m.get('ExcludeLowercase')
        if m.get('ExcludeNumbers') is not None:
            self.exclude_numbers = m.get('ExcludeNumbers')
        if m.get('ExcludePunctuation') is not None:
            self.exclude_punctuation = m.get('ExcludePunctuation')
        if m.get('ExcludeUppercase') is not None:
            self.exclude_uppercase = m.get('ExcludeUppercase')
        if m.get('PasswordLength') is not None:
            self.password_length = m.get('PasswordLength')
        if m.get('RequireEachIncludedType') is not None:
            self.require_each_included_type = m.get('RequireEachIncludedType')
        return self


class GetRandomPasswordResponseBody(TeaModel):
    def __init__(
        self,
        random_password: str = None,
        request_id: str = None,
    ):
        # The generated random password.
        self.random_password = random_password
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.random_password is not None:
            result['RandomPassword'] = self.random_password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RandomPassword') is not None:
            self.random_password = m.get('RandomPassword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRandomPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRandomPasswordResponseBody = None,
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
            temp_model = GetRandomPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretValueRequest(TeaModel):
    def __init__(
        self,
        fetch_extended_config: bool = None,
        secret_name: str = None,
        version_id: str = None,
        version_stage: str = None,
    ):
        # Specifies whether to obtain the extended configuration of the secret. Valid values:
        # 
        # *   true
        # *   false: This is the default value.
        # 
        # >  This parameter is ignored for a generic secret.
        self.fetch_extended_config = fetch_extended_config
        # The name of the secret.
        self.secret_name = secret_name
        # The version number of the secret value. If you specify this parameter, Secrets Manager returns the secret value of the specified version.
        # 
        # >  This parameter is ignored for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.version_id = version_id
        # The stage label that marks the secret version. If you specify this parameter, Secrets Manager returns the secret value of the version that is marked with the specified stage label.
        # 
        # Default value: ACSCurrent.
        # 
        # >  For a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret, Secrets Manager can return only the secret value of the version marked with ACSPrevious or ACSCurrent.
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_extended_config is not None:
            result['FetchExtendedConfig'] = self.fetch_extended_config
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchExtendedConfig') is not None:
            self.fetch_extended_config = m.get('FetchExtendedConfig')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class GetSecretValueResponseBodyVersionStages(TeaModel):
    def __init__(
        self,
        version_stage: List[str] = None,
    ):
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class GetSecretValueResponseBody(TeaModel):
    def __init__(
        self,
        automatic_rotation: str = None,
        create_time: str = None,
        extended_config: str = None,
        last_rotation_date: str = None,
        next_rotation_date: str = None,
        request_id: str = None,
        rotation_interval: str = None,
        secret_data: str = None,
        secret_data_type: str = None,
        secret_name: str = None,
        secret_type: str = None,
        version_id: str = None,
        version_stages: GetSecretValueResponseBodyVersionStages = None,
    ):
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.automatic_rotation = automatic_rotation
        # The time when the secret was created.
        self.create_time = create_time
        # The extended configuration of the secret.
        # 
        # >  This parameter is returned if you set the FetchExtendedConfig parameter to true. This parameter is returned only for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.extended_config = extended_config
        # The time when the last rotation was performed.
        # 
        # >  This parameter is returned if the secret was rotated.
        self.last_rotation_date = last_rotation_date
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.next_rotation_date = next_rotation_date
        # The ID of the request.
        self.request_id = request_id
        # The interval for automatic rotation.
        # 
        # The value is in the `integer[unit]` format. The `unit` field has a fixed value of s. For example, if the value is 604800s, automatic rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.rotation_interval = rotation_interval
        # The secret value. Secrets Manager decrypts the ciphertext of the secret value and returns the plaintext of the secret value in this parameter.
        # 
        # *   For a generic secret, the secret value of the specified version is returned.
        # 
        # *   For a managed ApsaraDB RDS secret, the value is returned in the following format:`{"AccountName":"","AccountPassword":""}` .
        # 
        # *   For a managed RAM secret, the secret value is returned in the following format: `{"AccessKeyId":"Adfdsfd","AccessKeySecret":"fdsfdsf","GenerateTimestamp": "2016-03-25T10:42:40Z"}`.
        # 
        # *   For a managed ECS secret, the secret value is returned in one of the following formats:
        # 
        #     *   `{"UserName":"root","Password":"H5asdasdsads****"}`: The secret value is returned in this format if the ECS secret is a password.
        #     *   `{"UserName":"root","PublicKey":"ssh-rsa ****mKwnVix9YTFY9Rs= imported-openssh-key","PrivateKey": "d6bee1cb-2e14-4277-ba6b-73786b21****"}`: The secret value is returned in this format is the ECS secret is a pair of SSH keys. The private key is in the Privacy Enhanced Mail (PEM) format.
        self.secret_data = secret_data
        # The type of the secret value. Valid values:
        # 
        # *   text
        # *   binary
        self.secret_data_type = secret_data_type
        # The name of the secret.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        # *   RAMCredentials: indicates a managed RAM secret.
        # *   ECS: indicates a managed ECS secret.
        self.secret_type = secret_type
        # The version number of the secret value.
        self.version_id = version_id
        # The stage labels that mark the secret versions.
        self.version_stages = version_stages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            temp_model = GetSecretValueResponseBodyVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        return self


class GetSecretValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecretValueResponseBody = None,
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
            temp_model = GetSecretValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyMaterialRequest(TeaModel):
    def __init__(
        self,
        encrypted_key_material: str = None,
        import_token: str = None,
        key_id: str = None,
        key_material_expire_unix: int = None,
    ):
        # Use** GetParametersForImport** the Returned public key and the base64-encoded key material.
        self.encrypted_key_material = encrypted_key_material
        # By calling** GetParametersForImport** the import token.
        self.import_token = import_token
        # The ID of the CMK to be imported.
        self.key_id = key_id
        # The time when the key material expires.
        # 
        # If this parameter is not specified or set this parameter to 0, the key material does not expire.
        # 
        # >  The value cannot be earlier than the time when the API is called (based on the server time).
        self.key_material_expire_unix = key_material_expire_unix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_key_material is not None:
            result['EncryptedKeyMaterial'] = self.encrypted_key_material
        if self.import_token is not None:
            result['ImportToken'] = self.import_token
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_material_expire_unix is not None:
            result['KeyMaterialExpireUnix'] = self.key_material_expire_unix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedKeyMaterial') is not None:
            self.encrypted_key_material = m.get('EncryptedKeyMaterial')
        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyMaterialExpireUnix') is not None:
            self.key_material_expire_unix = m.get('KeyMaterialExpireUnix')
        return self


class ImportKeyMaterialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ImportKeyMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportKeyMaterialResponseBody = None,
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
            temp_model = ImportKeyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliasesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAliasesResponseBodyAliasesAlias(TeaModel):
    def __init__(
        self,
        alias_arn: str = None,
        alias_name: str = None,
        key_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the alias.
        self.alias_arn = alias_arn
        # The ID of the alias.
        self.alias_name = alias_name
        # The CMK to which the alias belongs.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_arn is not None:
            result['AliasArn'] = self.alias_arn
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasArn') is not None:
            self.alias_arn = m.get('AliasArn')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListAliasesResponseBodyAliases(TeaModel):
    def __init__(
        self,
        alias: List[ListAliasesResponseBodyAliasesAlias] = None,
    ):
        self.alias = alias

    def validate(self):
        if self.alias:
            for k in self.alias:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alias'] = []
        if self.alias is not None:
            for k in self.alias:
                result['Alias'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alias = []
        if m.get('Alias') is not None:
            for k in m.get('Alias'):
                temp_model = ListAliasesResponseBodyAliasesAlias()
                self.alias.append(temp_model.from_map(k))
        return self


class ListAliasesResponseBody(TeaModel):
    def __init__(
        self,
        aliases: ListAliasesResponseBodyAliases = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The alias of the user.
        self.aliases = aliases
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned aliases.
        self.total_count = total_count

    def validate(self):
        if self.aliases:
            self.aliases.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['Aliases'] = self.aliases.to_map()
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
        if m.get('Aliases') is not None:
            temp_model = ListAliasesResponseBodyAliases()
            self.aliases = temp_model.from_map(m['Aliases'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliasesResponseBody = None,
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
            temp_model = ListAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliasesByKeyIdRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The globally unique ID of the CMK.
        self.key_id = key_id
        # The number of the page to return.
        # 
        # Valid values: an integer that is greater than 0.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 101.
        # 
        # Default value: 10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAliasesByKeyIdResponseBodyAliasesAlias(TeaModel):
    def __init__(
        self,
        alias_arn: str = None,
        alias_name: str = None,
        key_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the alias.
        self.alias_arn = alias_arn
        # The ID of the alias.
        self.alias_name = alias_name
        # The CMK to which an alias is bound.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_arn is not None:
            result['AliasArn'] = self.alias_arn
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasArn') is not None:
            self.alias_arn = m.get('AliasArn')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListAliasesByKeyIdResponseBodyAliases(TeaModel):
    def __init__(
        self,
        alias: List[ListAliasesByKeyIdResponseBodyAliasesAlias] = None,
    ):
        self.alias = alias

    def validate(self):
        if self.alias:
            for k in self.alias:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alias'] = []
        if self.alias is not None:
            for k in self.alias:
                result['Alias'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alias = []
        if m.get('Alias') is not None:
            for k in m.get('Alias'):
                temp_model = ListAliasesByKeyIdResponseBodyAliasesAlias()
                self.alias.append(temp_model.from_map(k))
        return self


class ListAliasesByKeyIdResponseBody(TeaModel):
    def __init__(
        self,
        aliases: ListAliasesByKeyIdResponseBodyAliases = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of aliases.
        self.aliases = aliases
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of returned CMKs.
        self.total_count = total_count

    def validate(self):
        if self.aliases:
            self.aliases.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['Aliases'] = self.aliases.to_map()
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
        if m.get('Aliases') is not None:
            temp_model = ListAliasesByKeyIdResponseBodyAliases()
            self.aliases = temp_model.from_map(m['Aliases'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAliasesByKeyIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliasesByKeyIdResponseBody = None,
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
            temp_model = ListAliasesByKeyIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeyVersionsRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 101.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListKeyVersionsResponseBodyKeyVersionsKeyVersion(TeaModel):
    def __init__(
        self,
        creation_date: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The date and time when the CMK version was created. The time is displayed in UTC.
        self.creation_date = creation_date
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to the alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The globally unique ID of the CMK version.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class ListKeyVersionsResponseBodyKeyVersions(TeaModel):
    def __init__(
        self,
        key_version: List[ListKeyVersionsResponseBodyKeyVersionsKeyVersion] = None,
    ):
        self.key_version = key_version

    def validate(self):
        if self.key_version:
            for k in self.key_version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyVersion'] = []
        if self.key_version is not None:
            for k in self.key_version:
                result['KeyVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_version = []
        if m.get('KeyVersion') is not None:
            for k in m.get('KeyVersion'):
                temp_model = ListKeyVersionsResponseBodyKeyVersionsKeyVersion()
                self.key_version.append(temp_model.from_map(k))
        return self


class ListKeyVersionsResponseBody(TeaModel):
    def __init__(
        self,
        key_versions: ListKeyVersionsResponseBodyKeyVersions = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of key versions.
        self.key_versions = key_versions
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned key versions.
        self.total_count = total_count

    def validate(self):
        if self.key_versions:
            self.key_versions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_versions is not None:
            result['KeyVersions'] = self.key_versions.to_map()
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
        if m.get('KeyVersions') is not None:
            temp_model = ListKeyVersionsResponseBodyKeyVersions()
            self.key_versions = temp_model.from_map(m['KeyVersions'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKeyVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKeyVersionsResponseBody = None,
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
            temp_model = ListKeyVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeysRequest(TeaModel):
    def __init__(
        self,
        filters: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The CMK filter. The filter consists of one or more key-value pairs. You can specify a maximum of 10 key-value pairs.
        # 
        # *   Key
        # 
        #     *   Description: the property that you want to filter.
        # 
        #     *   Type: string.
        # 
        #     *   Valid values:
        # 
        #         *   KeyState: the status of the CMK.
        #         *   KeySpec: the type of the CMK.
        #         *   KeyUsage: the usage of the CMK.
        #         *   ProtectionLevel: the protection level.
        #         *   CreatorType: the type of the creator.
        # 
        # *   Values
        # 
        #     *   Description: the value to be included after filtering.
        # 
        #     *   Format: string array.
        # 
        #     *   Length: 0 to 10.
        # 
        #     *   Valid values:
        # 
        #         *   When Key is set to KeyState, the value can be Enabled, Disabled, PendingDeletion, or PendingImport.
        # 
        #         *   When Key is set to KeySpec, the value can be Aliyun_AES\_256, Aliyun_SM4, RSA\_2048, EC_P256, EC_P256K, or EC_SM2.
        # 
        #             Note: You can create CMKs of the EC_SM2 or Aliyun_SM4 type only in regions where State Cryptography Administration (SCA)-certified managed HSMs reside. For more information about the regions, see [Supported regions](~~125803~~). If your region does not support EC_SM2 or Aliyun_SM4, the two values are ignored if they are specified.
        # 
        #         *   When Key is set to KeyUsage, the value can be ENCRYPT/DECRYPT or SIGN/VERIFY. ENCRYPT/DECRYPT indicates that the CMK is used to encrypt and decrypt data. SIGN/VERIFY indicates that the CMK is used to generate and verify digital signatures.
        # 
        #         *   When Key is set to ProtectionLevel, the value can be SOFTWARE (software) or HSM (hardware).
        # 
        #             You can set ProtectionLevel to HSM in only specific regions. For more information about the regions, see [Supported regions](~~125803~~). If your region does not support the value HSM, the value is ignored if the value is specified.
        # 
        #         *   If Key is set to CreatorType, the value can be User or Service. User indicates that CMKs created by the current account are queried. Service indicates that CMKs automatically created by other cloud services authorized by the current account are queried.
        # 
        # The logical relationship between different keys is AND, and the logical relationship between multiple items in the same key is OR. Example:
        # 
        # `[ {"Key":"KeyState", "Values":["Enabled","Disabled"]}, {"Key":"KeyState", "Values":["PendingDeletion"]}, {"Key":"KeySpec", "Values":["Aliyun_AES_256"]}]`. In this example, the semantics are:`(KeyState=Enabled OR KeyState=Disabled OR KeyState=PendingDeletion) AND (KeySpec=Aliyun_AES_ 256)`.
        self.filters = filters
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListKeysResponseBodyKeysKey(TeaModel):
    def __init__(
        self,
        key_arn: str = None,
        key_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the CMK.
        self.key_arn = key_arn
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_arn is not None:
            result['KeyArn'] = self.key_arn
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyArn') is not None:
            self.key_arn = m.get('KeyArn')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListKeysResponseBodyKeys(TeaModel):
    def __init__(
        self,
        key: List[ListKeysResponseBodyKeysKey] = None,
    ):
        self.key = key

    def validate(self):
        if self.key:
            for k in self.key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Key'] = []
        if self.key is not None:
            for k in self.key:
                result['Key'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key = []
        if m.get('Key') is not None:
            for k in m.get('Key'):
                temp_model = ListKeysResponseBodyKeysKey()
                self.key.append(temp_model.from_map(k))
        return self


class ListKeysResponseBody(TeaModel):
    def __init__(
        self,
        keys: ListKeysResponseBodyKeys = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the CMKs of the current Alibaba Cloud account in the current region.
        self.keys = keys
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of CMKs.
        self.total_count = total_count

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
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
        if m.get('Keys') is not None:
            temp_model = ListKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKeysResponseBody = None,
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
            temp_model = ListKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTagsRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The globally unique ID of the CMK.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListResourceTagsResponseBodyTagsTag(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The globally unique ID of the CMK.
        self.key_id = key_id
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListResourceTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag: List[ListResourceTagsResponseBodyTagsTag] = None,
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
                temp_model = ListResourceTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListResourceTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: ListResourceTagsResponseBodyTags = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The tags of the CMK.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            temp_model = ListResourceTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class ListResourceTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTagsResponseBody = None,
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
            temp_model = ListResourceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretVersionIdsRequest(TeaModel):
    def __init__(
        self,
        include_deprecated: str = None,
        page_number: int = None,
        page_size: int = None,
        secret_name: str = None,
    ):
        # Specifies whether to return deprecated secret versions.
        # 
        # Valid values:
        # 
        # *   false: no
        # *   true: yes
        # 
        # Default value: false.
        self.include_deprecated = include_deprecated
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_deprecated is not None:
            result['IncludeDeprecated'] = self.include_deprecated
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeDeprecated') is not None:
            self.include_deprecated = m.get('IncludeDeprecated')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages(TeaModel):
    def __init__(
        self,
        version_stage: List[str] = None,
    ):
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class ListSecretVersionIdsResponseBodyVersionIdsVersionId(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        version_id: str = None,
        version_stages: ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages = None,
    ):
        # The time when the secret version was created.
        self.create_time = create_time
        # The version number.
        self.version_id = version_id
        # The stage labels that mark the secret version.
        self.version_stages = version_stages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            temp_model = ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        return self


class ListSecretVersionIdsResponseBodyVersionIds(TeaModel):
    def __init__(
        self,
        version_id: List[ListSecretVersionIdsResponseBodyVersionIdsVersionId] = None,
    ):
        self.version_id = version_id

    def validate(self):
        if self.version_id:
            for k in self.version_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VersionId'] = []
        if self.version_id is not None:
            for k in self.version_id:
                result['VersionId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.version_id = []
        if m.get('VersionId') is not None:
            for k in m.get('VersionId'):
                temp_model = ListSecretVersionIdsResponseBodyVersionIdsVersionId()
                self.version_id.append(temp_model.from_map(k))
        return self


class ListSecretVersionIdsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        secret_name: str = None,
        total_count: int = None,
        version_ids: ListSecretVersionIdsResponseBodyVersionIds = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name
        # The number of entries returned on the current page.
        self.total_count = total_count
        # The list of secret versions.
        self.version_ids = version_ids

    def validate(self):
        if self.version_ids:
            self.version_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VersionIds') is not None:
            temp_model = ListSecretVersionIdsResponseBodyVersionIds()
            self.version_ids = temp_model.from_map(m['VersionIds'])
        return self


class ListSecretVersionIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecretVersionIdsResponseBody = None,
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
            temp_model = ListSecretVersionIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretsRequest(TeaModel):
    def __init__(
        self,
        fetch_tags: str = None,
        filters: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Specifies whether to return the resource tags of the secret. Valid values:
        # 
        # *   true: returns the resource tags.
        # *   false: does not return the resource tags. This is the default value.
        self.fetch_tags = fetch_tags
        # The secret filter. The filter consists of one or more key-value pairs. You can specify one key-value pair or leave this parameter empty. If you use one tag key or tag value to filter resources, up to 4,000 resources can be queried. If you want to query more than 4,000 resources, call the [ListResourceTags](~~120090~~) operation.
        # 
        # *   Key
        # 
        #     *   Description: the property that you want to filter.
        # 
        #     *   Type: string.
        # 
        #     *   Valid values:
        # 
        #         *   SecretName: the secret name.
        #         *   Description: the description of the secret.
        #         *   TagKey: the tag key.
        #         *   TagValue: the tag value.
        # 
        # *   Values
        # 
        #     *   Description: the value to be included after filtering.
        # 
        #     *   Type: string.
        # 
        #     *   Length: 0 to 10.
        # 
        #     *   Valid values:
        # 
        #         *   If the Key field is set to SecretName, the value must be 1 to 192 characters in length and can contain letters, digits, and special characters `_ / + = . @ -`.
        #         *   If the Key field is set to Description, the value must be 1 to 256 characters in length.
        #         *   If the Key field is set to TagKey, the value must be 1 to 256 characters in length and can contain letters, digits, and special characters `/ _ - . + = @ :`.
        #         *   If the Key field is set to TagValue, the value must be 1 to 256 characters in length and can contain letters, numbers, and special characters `/ _ - . + = @ :`.
        # 
        # The logical relationship between values of the Values field in a key-value pair is OR. Example: `[ {"Key":"SecretName", "Values":["sec1","sec2"]}]`. In this example, the semantics are `SecretName=sec 1 OR SecretName=sec 2`.
        self.filters = filters
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSecretsResponseBodySecretListSecretTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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


class ListSecretsResponseBodySecretListSecretTags(TeaModel):
    def __init__(
        self,
        tag: List[ListSecretsResponseBodySecretListSecretTagsTag] = None,
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
                temp_model = ListSecretsResponseBodySecretListSecretTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListSecretsResponseBodySecretListSecret(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        planned_delete_time: str = None,
        secret_name: str = None,
        secret_type: str = None,
        tags: ListSecretsResponseBodySecretListSecretTags = None,
        update_time: str = None,
    ):
        # The time when the secret was created.
        self.create_time = create_time
        # The time when the secret is scheduled to be deleted.
        self.planned_delete_time = planned_delete_time
        # The secret name.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        self.secret_type = secret_type
        # The resource tags of the secret.
        # 
        # This parameter is not returned if you set the FetchTags parameter to false or do not specify the FetchTags parameter.
        self.tags = tags
        # The time when the secret was updated.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            temp_model = ListSecretsResponseBodySecretListSecretTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSecretsResponseBodySecretList(TeaModel):
    def __init__(
        self,
        secret: List[ListSecretsResponseBodySecretListSecret] = None,
    ):
        self.secret = secret

    def validate(self):
        if self.secret:
            for k in self.secret:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Secret'] = []
        if self.secret is not None:
            for k in self.secret:
                result['Secret'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secret = []
        if m.get('Secret') is not None:
            for k in m.get('Secret'):
                temp_model = ListSecretsResponseBodySecretListSecret()
                self.secret.append(temp_model.from_map(k))
        return self


class ListSecretsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        secret_list: ListSecretsResponseBodySecretList = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The list of secrets.
        self.secret_list = secret_list
        # The number of returned secrets.
        self.total_count = total_count

    def validate(self):
        if self.secret_list:
            self.secret_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_list is not None:
            result['SecretList'] = self.secret_list.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretList') is not None:
            temp_model = ListSecretsResponseBodySecretList()
            self.secret_list = temp_model.from_map(m['SecretList'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSecretsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecretsResponseBody = None,
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
            temp_model = ListSecretsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenKmsServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class OpenKmsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenKmsServiceResponseBody = None,
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
            temp_model = OpenKmsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutSecretValueRequest(TeaModel):
    def __init__(
        self,
        secret_data: str = None,
        secret_data_type: str = None,
        secret_name: str = None,
        version_id: str = None,
        version_stages: str = None,
    ):
        # The secret value. The value is encrypted and then stored in the new version.
        self.secret_data = secret_data
        # The type of the secret value. Valid values:
        # 
        # *   text: This is the default value.
        # *   binary
        self.secret_data_type = secret_data_type
        # The name of the secret.
        self.secret_name = secret_name
        # The new version of the secret value. Version numbers must be unique in each secret.
        self.version_id = version_id
        # The stage labels that are used to mark the new version. If you do not specify this parameter, Secrets Manager marks the new version with ACSCurrent.
        self.version_stages = version_stages

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            self.version_stages = m.get('VersionStages')
        return self


class PutSecretValueResponseBodyVersionStages(TeaModel):
    def __init__(
        self,
        version_stage: List[str] = None,
    ):
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class PutSecretValueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_name: str = None,
        version_id: str = None,
        version_stages: PutSecretValueResponseBodyVersionStages = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name
        # The new version of the secret value.
        self.version_id = version_id
        # The stage labels that are used to mark the new version.
        self.version_stages = version_stages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            temp_model = PutSecretValueResponseBodyVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        return self


class PutSecretValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutSecretValueResponseBody = None,
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
            temp_model = PutSecretValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReEncryptRequest(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        destination_encryption_context: Dict[str, Any] = None,
        destination_key_id: str = None,
        source_encryption_algorithm: str = None,
        source_encryption_context: Dict[str, Any] = None,
        source_key_id: str = None,
        source_key_version_id: str = None,
    ):
        # The ciphertext that you want to re-encrypt.
        # 
        # You can set this parameter to the ciphertext that is returned after a symmetric or asymmetric encryption operation.
        # 
        # *   Symmetric encryption: the ciphertext returned after you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation
        # *   Asymmetric encryption: the public key-encrypted ciphertext returned after you call the [GenerateAndExportDataKey](~~176804~~) operation, or the ciphertext encrypted by using the public key of an asymmetric key pair outside KMS
        self.ciphertext_blob = ciphertext_blob
        # A JSON string that consists of key-value pairs. This parameter specifies the EncryptionContext that is used to re-encrypt the decrypted data or data key.
        self.destination_encryption_context = destination_encryption_context
        # The ID of the symmetric CMK that is used to re-encrypt the ciphertext after the ciphertext is decrypted.
        self.destination_key_id = destination_key_id
        # The encryption algorithm based on which the public key is used to encrypt the ciphertext specified by CiphertextBlob. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_encryption_algorithm = source_encryption_algorithm
        # A JSON string that consists of key-value pairs. If you specify EncryptionContext when you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation to encrypt the data or data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        # 
        # >  If you set CiphertextBlob to the ciphertext that is returned after a symmetric encryption operation, specify this parameter.
        self.source_encryption_context = source_encryption_context
        # The ID of the CMK that is used to decrypt the ciphertext.
        # 
        # This parameter is the globally unique ID of the CMK.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_id = source_key_id
        # The ID of the CMK version that is used to decrypt the ciphertext.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_version_id = source_key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.destination_encryption_context is not None:
            result['DestinationEncryptionContext'] = self.destination_encryption_context
        if self.destination_key_id is not None:
            result['DestinationKeyId'] = self.destination_key_id
        if self.source_encryption_algorithm is not None:
            result['SourceEncryptionAlgorithm'] = self.source_encryption_algorithm
        if self.source_encryption_context is not None:
            result['SourceEncryptionContext'] = self.source_encryption_context
        if self.source_key_id is not None:
            result['SourceKeyId'] = self.source_key_id
        if self.source_key_version_id is not None:
            result['SourceKeyVersionId'] = self.source_key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('DestinationEncryptionContext') is not None:
            self.destination_encryption_context = m.get('DestinationEncryptionContext')
        if m.get('DestinationKeyId') is not None:
            self.destination_key_id = m.get('DestinationKeyId')
        if m.get('SourceEncryptionAlgorithm') is not None:
            self.source_encryption_algorithm = m.get('SourceEncryptionAlgorithm')
        if m.get('SourceEncryptionContext') is not None:
            self.source_encryption_context = m.get('SourceEncryptionContext')
        if m.get('SourceKeyId') is not None:
            self.source_key_id = m.get('SourceKeyId')
        if m.get('SourceKeyVersionId') is not None:
            self.source_key_version_id = m.get('SourceKeyVersionId')
        return self


class ReEncryptShrinkRequest(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        destination_encryption_context_shrink: str = None,
        destination_key_id: str = None,
        source_encryption_algorithm: str = None,
        source_encryption_context_shrink: str = None,
        source_key_id: str = None,
        source_key_version_id: str = None,
    ):
        # The ciphertext that you want to re-encrypt.
        # 
        # You can set this parameter to the ciphertext that is returned after a symmetric or asymmetric encryption operation.
        # 
        # *   Symmetric encryption: the ciphertext returned after you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation
        # *   Asymmetric encryption: the public key-encrypted ciphertext returned after you call the [GenerateAndExportDataKey](~~176804~~) operation, or the ciphertext encrypted by using the public key of an asymmetric key pair outside KMS
        self.ciphertext_blob = ciphertext_blob
        # A JSON string that consists of key-value pairs. This parameter specifies the EncryptionContext that is used to re-encrypt the decrypted data or data key.
        self.destination_encryption_context_shrink = destination_encryption_context_shrink
        # The ID of the symmetric CMK that is used to re-encrypt the ciphertext after the ciphertext is decrypted.
        self.destination_key_id = destination_key_id
        # The encryption algorithm based on which the public key is used to encrypt the ciphertext specified by CiphertextBlob. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_encryption_algorithm = source_encryption_algorithm
        # A JSON string that consists of key-value pairs. If you specify EncryptionContext when you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation to encrypt the data or data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        # 
        # >  If you set CiphertextBlob to the ciphertext that is returned after a symmetric encryption operation, specify this parameter.
        self.source_encryption_context_shrink = source_encryption_context_shrink
        # The ID of the CMK that is used to decrypt the ciphertext.
        # 
        # This parameter is the globally unique ID of the CMK.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_id = source_key_id
        # The ID of the CMK version that is used to decrypt the ciphertext.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_version_id = source_key_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.destination_encryption_context_shrink is not None:
            result['DestinationEncryptionContext'] = self.destination_encryption_context_shrink
        if self.destination_key_id is not None:
            result['DestinationKeyId'] = self.destination_key_id
        if self.source_encryption_algorithm is not None:
            result['SourceEncryptionAlgorithm'] = self.source_encryption_algorithm
        if self.source_encryption_context_shrink is not None:
            result['SourceEncryptionContext'] = self.source_encryption_context_shrink
        if self.source_key_id is not None:
            result['SourceKeyId'] = self.source_key_id
        if self.source_key_version_id is not None:
            result['SourceKeyVersionId'] = self.source_key_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('DestinationEncryptionContext') is not None:
            self.destination_encryption_context_shrink = m.get('DestinationEncryptionContext')
        if m.get('DestinationKeyId') is not None:
            self.destination_key_id = m.get('DestinationKeyId')
        if m.get('SourceEncryptionAlgorithm') is not None:
            self.source_encryption_algorithm = m.get('SourceEncryptionAlgorithm')
        if m.get('SourceEncryptionContext') is not None:
            self.source_encryption_context_shrink = m.get('SourceEncryptionContext')
        if m.get('SourceKeyId') is not None:
            self.source_key_id = m.get('SourceKeyId')
        if m.get('SourceKeyVersionId') is not None:
            self.source_key_version_id = m.get('SourceKeyVersionId')
        return self


class ReEncryptResponseBody(TeaModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        key_id: str = None,
        key_version_id: str = None,
        request_id: str = None,
    ):
        # The ciphertext re-encrypted.
        self.ciphertext_blob = ciphertext_blob
        # The ID of the CMK that is used to decrypt the original ciphertext.
        # 
        # This parameter is the globally unique ID of the CMK.
        self.key_id = key_id
        # The ID of the CMK version that is used to decrypt the original ciphertext.
        self.key_version_id = key_version_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReEncryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReEncryptResponseBody = None,
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
            temp_model = ReEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreSecretRequest(TeaModel):
    def __init__(
        self,
        secret_name: str = None,
    ):
        # The name of the secret you want to restore.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class RestoreSecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_name: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class RestoreSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestoreSecretResponseBody = None,
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
            temp_model = RestoreSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RotateSecretRequest(TeaModel):
    def __init__(
        self,
        secret_name: str = None,
        version_id: str = None,
    ):
        # The name of the secret.
        self.secret_name = secret_name
        # The version number of the secret after the secret is rotated.
        # 
        # >  The version number is used to ensure the idempotence of the request. Secrets Manager uses this version number to prevent your application from creating the same version of the secret when the application retries a request. If a version number already exists, Secrets Manager ignores the request for rotation and returns a success message.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RotateSecretResponseBody(TeaModel):
    def __init__(
        self,
        arn: str = None,
        request_id: str = None,
        secret_name: str = None,
        version_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.arn = arn
        # The ID of the request.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name
        # The version number of the secret after the secret is rotated.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RotateSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RotateSecretResponseBody = None,
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
            temp_model = RotateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScheduleKeyDeletionRequest(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        pending_window_in_days: int = None,
    ):
        # The ID of the customer master key (CMK). The ID must be globally unique.
        self.key_id = key_id
        # The scheduled period after which the CMK is deleted. During this period, the CMK is in the PendingDeletion state. After this period ends, you cannot cancel the key deletion task.
        # 
        # Valid values: 7 to 366.
        # 
        # Unit: days.
        self.pending_window_in_days = pending_window_in_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.pending_window_in_days is not None:
            result['PendingWindowInDays'] = self.pending_window_in_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PendingWindowInDays') is not None:
            self.pending_window_in_days = m.get('PendingWindowInDays')
        return self


class ScheduleKeyDeletionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class ScheduleKeyDeletionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScheduleKeyDeletionResponseBody = None,
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
            temp_model = ScheduleKeyDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        deletion_protection_description: str = None,
        enable_deletion_protection: bool = None,
        protected_resource_arn: str = None,
    ):
        # The description of deletion protection.
        # 
        # >  This parameter takes effect only when you set the EnableDeletionProtection parameter to true.
        self.deletion_protection_description = deletion_protection_description
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # *   true: enables deletion protection.
        # *   false: disables deletion protection.
        self.enable_deletion_protection = enable_deletion_protection
        # The ARN of the CMK for which you want to set deletion protection.
        # 
        # You can call the [DescribeKey](~~28952~~) operation to query the CMK ARN.
        self.protected_resource_arn = protected_resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_protection_description is not None:
            result['DeletionProtectionDescription'] = self.deletion_protection_description
        if self.enable_deletion_protection is not None:
            result['EnableDeletionProtection'] = self.enable_deletion_protection
        if self.protected_resource_arn is not None:
            result['ProtectedResourceArn'] = self.protected_resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtectionDescription') is not None:
            self.deletion_protection_description = m.get('DeletionProtectionDescription')
        if m.get('EnableDeletionProtection') is not None:
            self.enable_deletion_protection = m.get('EnableDeletionProtection')
        if m.get('ProtectedResourceArn') is not None:
            self.protected_resource_arn = m.get('ProtectedResourceArn')
        return self


class SetDeletionProtectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class SetDeletionProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDeletionProtectionResponseBody = None,
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
            temp_model = SetDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourceRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        key_id: str = None,
        secret_name: str = None,
        tags: str = None,
    ):
        # The ID of the certificate.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.certificate_id = certificate_id
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.key_id = key_id
        # The name of the secret.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.secret_name = secret_name
        # One or more tags that you want to add. The value is in the array format.
        # 
        # Tag attributes:
        # 
        # *   TagKey: the tag key.
        # *   TagValue: the tag value.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class TagResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourceResponseBody = None,
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
            temp_model = TagResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourceRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        key_id: str = None,
        secret_name: str = None,
        tag_keys: str = None,
    ):
        # The ID of the certificate.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.certificate_id = certificate_id
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.key_id = key_id
        # The name of the secret.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.secret_name = secret_name
        # One or more tag keys. Separate multiple tag keys with commas (,).
        # 
        # You need to specify only the tag keys, not the tag values.
        # 
        # Each tag key must be 1 to 128 bytes in length.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class UntagResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourceResponseBody = None,
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
            temp_model = UntagResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        key_id: str = None,
    ):
        # The alias that you want to bind.
        # 
        # The value must be 1 to 255 characters in length and must include the alias/ prefix.
        self.alias_name = alias_name
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class UpdateAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class UpdateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAliasResponseBody = None,
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
            temp_model = UpdateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCertificateStatusRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        status: str = None,
    ):
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id
        # The status of the certificate. Valid values:
        # 
        # *   INACTIVE: The certificate is disabled.
        # 
        # *   ACTIVE: The certificate is enabled.
        # 
        # *   REVOKED: The certificate is revoked.
        # 
        # > If the certificate is in the REVOKED state, you can use the certificate only to verify a signature, but not to generate a signature.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateCertificateStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class UpdateCertificateStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCertificateStatusResponseBody = None,
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
            temp_model = UpdateCertificateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKeyDescriptionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        key_id: str = None,
    ):
        # The description of the CMK. This description includes the purpose of the CMK, such as the types of data that you want to protect and applications that can use the CMK.
        self.description = description
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class UpdateKeyDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class UpdateKeyDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateKeyDescriptionResponseBody = None,
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
            temp_model = UpdateKeyDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRotationPolicyRequest(TeaModel):
    def __init__(
        self,
        enable_automatic_rotation: bool = None,
        key_id: str = None,
        rotation_interval: str = None,
    ):
        # Specifies whether to enable automatic key rotation. Valid values:
        # 
        # *   true: enables automatic key rotation.
        # *   false: disables automatic key rotation.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The ID of the customer master key (CMK). The ID must be globally unique.
        self.key_id = key_id
        # The period of automatic key rotation. Specify the value in the integer\[unit] format. The following units are supported: d (day), h (hour), m (minute), and s (second). For example, you can use either 7d or 604800s to specify a seven-day period. The period can range from 7 days to 730 days.
        # 
        # >  If you set the EnableAutomaticRotation parameter to true, you must also specify this parameter. If you set the EnableAutomaticRotation parameter to false, you can leave this parameter unspecified.
        self.rotation_interval = rotation_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class UpdateRotationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class UpdateRotationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRotationPolicyResponseBody = None,
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
            temp_model = UpdateRotationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretRequestExtendedConfig(TeaModel):
    def __init__(
        self,
        custom_data: Dict[str, Any] = None,
    ):
        # The custom data in the extended configuration of the secret.
        # 
        # > 
        # *   If this parameter is specified, the existing extended configuration of the secret is updated.
        # *   This parameter is unavailable for generic secrets.
        self.custom_data = custom_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_data is not None:
            result['CustomData'] = self.custom_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')
        return self


class UpdateSecretRequest(TeaModel):
    def __init__(
        self,
        extended_config: UpdateSecretRequestExtendedConfig = None,
        description: str = None,
        secret_name: str = None,
    ):
        self.extended_config = extended_config
        # The description of the secret.
        self.description = description
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        if self.extended_config:
            self.extended_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedConfig') is not None:
            temp_model = UpdateSecretRequestExtendedConfig()
            self.extended_config = temp_model.from_map(m['ExtendedConfig'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretShrinkRequestExtendedConfig(TeaModel):
    def __init__(
        self,
        custom_data: str = None,
    ):
        # The custom data in the extended configuration of the secret.
        # 
        # > 
        # *   If this parameter is specified, the existing extended configuration of the secret is updated.
        # *   This parameter is unavailable for generic secrets.
        self.custom_data = custom_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_data is not None:
            result['CustomData'] = self.custom_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')
        return self


class UpdateSecretShrinkRequest(TeaModel):
    def __init__(
        self,
        extended_config: UpdateSecretShrinkRequestExtendedConfig = None,
        description: str = None,
        secret_name: str = None,
    ):
        self.extended_config = extended_config
        # The description of the secret.
        self.description = description
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        if self.extended_config:
            self.extended_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedConfig') is not None:
            temp_model = UpdateSecretShrinkRequestExtendedConfig()
            self.extended_config = temp_model.from_map(m['ExtendedConfig'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_name: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSecretResponseBody = None,
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
            temp_model = UpdateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretRotationPolicyRequest(TeaModel):
    def __init__(
        self,
        enable_automatic_rotation: bool = None,
        rotation_interval: str = None,
        secret_name: str = None,
    ):
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # *   true: enables automatic rotation.
        # *   false: does not enable automatic rotation. This is the default value.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).
        # 
        # The value is in the `integer[unit]` format.````
        # 
        # The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s indicate a seven-day interval.
        # 
        # >  This parameter is required if you set the EnableAutomaticRotation parameter to true. This parameter is ignored if you set the EnableAutomaticRotation parameter to false or does not specify the EnableAutomaticRotation parameter.
        self.rotation_interval = rotation_interval
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretRotationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_name: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretRotationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSecretRotationPolicyResponseBody = None,
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
            temp_model = UpdateSecretRotationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretVersionStageRequest(TeaModel):
    def __init__(
        self,
        move_to_version: str = None,
        remove_from_version: str = None,
        secret_name: str = None,
        version_stage: str = None,
    ):
        # The version to which you want to apply the specified stage label.
        # 
        # > 
        # *   You must specify at least one of the RemoveFromVersion and MoveToVersion parameters.
        # *   If the VersionStage parameter is set to ACSCurrent or ACSPrevious, this parameter is required.
        self.move_to_version = move_to_version
        # The version from which you want to remove the specified stage label.
        # 
        # >  You must specify at least one of the RemoveFromVersion and MoveToVersion parameters.
        self.remove_from_version = remove_from_version
        # The name of the secret.
        self.secret_name = secret_name
        # The specified stage label. Valid values:
        # 
        # *   ACSCurrent
        # *   ACSPrevious
        # *   Custom stage label
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.move_to_version is not None:
            result['MoveToVersion'] = self.move_to_version
        if self.remove_from_version is not None:
            result['RemoveFromVersion'] = self.remove_from_version
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoveToVersion') is not None:
            self.move_to_version = m.get('MoveToVersion')
        if m.get('RemoveFromVersion') is not None:
            self.remove_from_version = m.get('RemoveFromVersion')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class UpdateSecretVersionStageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_name: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretVersionStageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSecretVersionStageResponseBody = None,
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
            temp_model = UpdateSecretVersionStageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        certificate_chain: str = None,
        certificate_id: str = None,
    ):
        # The certificate issued by the CA, which is in the Privacy Enhanced Mail (PEM) format.
        self.certificate = certificate
        # The certificate chain issued by the CA, which is in the PEM format.
        self.certificate_chain = certificate_chain
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class UploadCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class UploadCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadCertificateResponseBody = None,
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
            temp_model = UploadCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


