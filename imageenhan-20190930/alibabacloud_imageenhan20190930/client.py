# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_imageenhan20190930 import models as imageenhan_20190930_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('imageenhan', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def colorize_image(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.ColorizeImageResponse().from_map(self.do_request('ColorizeImage', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def colorize_image_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.colorize_image(request, runtime)

    def colorize_image_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        colorize_image_req = imageenhan_20190930_models.ColorizeImageRequest()
        RPCUtilClient.convert(request, colorize_image_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        colorize_image_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        colorize_image_resp = self.colorize_image(colorize_image_req, runtime)
        return colorize_image_resp

    def erase_person(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.ErasePersonResponse().from_map(self.do_request('ErasePerson', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def erase_person_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.erase_person(request, runtime)

    def erase_person_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        erase_person_req = imageenhan_20190930_models.ErasePersonRequest()
        RPCUtilClient.convert(request, erase_person_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        erase_person_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        erase_person_resp = self.erase_person(erase_person_req, runtime)
        return erase_person_resp

    def generate_dynamic_image(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.GenerateDynamicImageResponse().from_map(self.do_request('GenerateDynamicImage', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def generate_dynamic_image_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_dynamic_image(request, runtime)

    def generate_dynamic_image_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        generate_dynamic_image_req = imageenhan_20190930_models.GenerateDynamicImageRequest()
        RPCUtilClient.convert(request, generate_dynamic_image_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        generate_dynamic_image_req.url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        generate_dynamic_image_resp = self.generate_dynamic_image(generate_dynamic_image_req, runtime)
        return generate_dynamic_image_resp

    def get_async_job_result(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.GetAsyncJobResultResponse().from_map(self.do_request('GetAsyncJobResult', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def get_async_job_result_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result(request, runtime)

    def imitate_photo_style(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.ImitatePhotoStyleResponse().from_map(self.do_request('ImitatePhotoStyle', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def imitate_photo_style_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.imitate_photo_style(request, runtime)

    def imitate_photo_style_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        imitate_photo_style_req = imageenhan_20190930_models.ImitatePhotoStyleRequest()
        RPCUtilClient.convert(request, imitate_photo_style_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        imitate_photo_style_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        imitate_photo_style_resp = self.imitate_photo_style(imitate_photo_style_req, runtime)
        return imitate_photo_style_resp

    def enhance_image_color(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.EnhanceImageColorResponse().from_map(self.do_request('EnhanceImageColor', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def enhance_image_color_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enhance_image_color(request, runtime)

    def enhance_image_color_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        enhance_image_color_req = imageenhan_20190930_models.EnhanceImageColorRequest()
        RPCUtilClient.convert(request, enhance_image_color_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        enhance_image_color_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        enhance_image_color_resp = self.enhance_image_color(enhance_image_color_req, runtime)
        return enhance_image_color_resp

    def recolor_hdimage(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.RecolorHDImageResponse().from_map(self.do_request('RecolorHDImage', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def recolor_hdimage_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recolor_hdimage(request, runtime)

    def recolor_hdimage_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        recolor_hdimage_req = imageenhan_20190930_models.RecolorHDImageRequest()
        RPCUtilClient.convert(request, recolor_hdimage_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        recolor_hdimage_req.url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        recolor_hdimage_resp = self.recolor_hdimage(recolor_hdimage_req, runtime)
        return recolor_hdimage_resp

    def assess_composition(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.AssessCompositionResponse().from_map(self.do_request('AssessComposition', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def assess_composition_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assess_composition(request, runtime)

    def assess_composition_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        assess_composition_req = imageenhan_20190930_models.AssessCompositionRequest()
        RPCUtilClient.convert(request, assess_composition_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        assess_composition_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        assess_composition_resp = self.assess_composition(assess_composition_req, runtime)
        return assess_composition_resp

    def assess_sharpness(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.AssessSharpnessResponse().from_map(self.do_request('AssessSharpness', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def assess_sharpness_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assess_sharpness(request, runtime)

    def assess_sharpness_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        assess_sharpness_req = imageenhan_20190930_models.AssessSharpnessRequest()
        RPCUtilClient.convert(request, assess_sharpness_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        assess_sharpness_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        assess_sharpness_resp = self.assess_sharpness(assess_sharpness_req, runtime)
        return assess_sharpness_resp

    def assess_exposure(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.AssessExposureResponse().from_map(self.do_request('AssessExposure', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def assess_exposure_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assess_exposure(request, runtime)

    def assess_exposure_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        assess_exposure_req = imageenhan_20190930_models.AssessExposureRequest()
        RPCUtilClient.convert(request, assess_exposure_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        assess_exposure_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        assess_exposure_resp = self.assess_exposure(assess_exposure_req, runtime)
        return assess_exposure_resp

    def image_blind_character_watermark(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse().from_map(self.do_request('ImageBlindCharacterWatermark', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def image_blind_character_watermark_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.image_blind_character_watermark(request, runtime)

    def image_blind_character_watermark_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        image_blind_character_watermark_req = imageenhan_20190930_models.ImageBlindCharacterWatermarkRequest()
        RPCUtilClient.convert(request, image_blind_character_watermark_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.origin_image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        image_blind_character_watermark_req.origin_image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        image_blind_character_watermark_resp = self.image_blind_character_watermark(image_blind_character_watermark_req, runtime)
        return image_blind_character_watermark_resp

    def remove_image_subtitles(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.RemoveImageSubtitlesResponse().from_map(self.do_request('RemoveImageSubtitles', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def remove_image_subtitles_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_image_subtitles(request, runtime)

    def remove_image_subtitles_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        remove_image_subtitles_req = imageenhan_20190930_models.RemoveImageSubtitlesRequest()
        RPCUtilClient.convert(request, remove_image_subtitles_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        remove_image_subtitles_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        remove_image_subtitles_resp = self.remove_image_subtitles(remove_image_subtitles_req, runtime)
        return remove_image_subtitles_resp

    def remove_image_watermark(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.RemoveImageWatermarkResponse().from_map(self.do_request('RemoveImageWatermark', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def remove_image_watermark_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_image_watermark(request, runtime)

    def remove_image_watermark_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        remove_image_watermark_req = imageenhan_20190930_models.RemoveImageWatermarkRequest()
        RPCUtilClient.convert(request, remove_image_watermark_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        remove_image_watermark_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        remove_image_watermark_resp = self.remove_image_watermark(remove_image_watermark_req, runtime)
        return remove_image_watermark_resp

    def image_blind_pic_watermark(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.ImageBlindPicWatermarkResponse().from_map(self.do_request('ImageBlindPicWatermark', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def image_blind_pic_watermark_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.image_blind_pic_watermark(request, runtime)

    def image_blind_pic_watermark_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        image_blind_pic_watermark_req = imageenhan_20190930_models.ImageBlindPicWatermarkRequest()
        RPCUtilClient.convert(request, image_blind_pic_watermark_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.origin_image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        image_blind_pic_watermark_req.origin_image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        image_blind_pic_watermark_resp = self.image_blind_pic_watermark(image_blind_pic_watermark_req, runtime)
        return image_blind_pic_watermark_resp

    def intelligent_composition(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.IntelligentCompositionResponse().from_map(self.do_request('IntelligentComposition', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def intelligent_composition_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.intelligent_composition(request, runtime)

    def intelligent_composition_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        intelligent_composition_req = imageenhan_20190930_models.IntelligentCompositionRequest()
        RPCUtilClient.convert(request, intelligent_composition_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        intelligent_composition_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        intelligent_composition_resp = self.intelligent_composition(intelligent_composition_req, runtime)
        return intelligent_composition_resp

    def change_image_size(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.ChangeImageSizeResponse().from_map(self.do_request('ChangeImageSize', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def change_image_size_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_image_size(request, runtime)

    def change_image_size_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        change_image_size_req = imageenhan_20190930_models.ChangeImageSizeRequest()
        RPCUtilClient.convert(request, change_image_size_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        change_image_size_req.url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        change_image_size_resp = self.change_image_size(change_image_size_req, runtime)
        return change_image_size_resp

    def extend_image_style(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.ExtendImageStyleResponse().from_map(self.do_request('ExtendImageStyle', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def extend_image_style_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extend_image_style(request, runtime)

    def make_super_resolution_image(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.MakeSuperResolutionImageResponse().from_map(self.do_request('MakeSuperResolutionImage', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def make_super_resolution_image_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.make_super_resolution_image(request, runtime)

    def make_super_resolution_image_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageenhan',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        make_super_resolution_image_req = imageenhan_20190930_models.MakeSuperResolutionImageRequest()
        RPCUtilClient.convert(request, make_super_resolution_image_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        make_super_resolution_image_req.url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        make_super_resolution_image_resp = self.make_super_resolution_image(make_super_resolution_image_req, runtime)
        return make_super_resolution_image_resp

    def recolor_image(self, request, runtime):
        UtilClient.validate_model(request)
        return imageenhan_20190930_models.RecolorImageResponse().from_map(self.do_request('RecolorImage', 'HTTPS', 'POST', '2019-09-30', 'AK', None, TeaCore.to_map(request), runtime))

    def recolor_image_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recolor_image(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
