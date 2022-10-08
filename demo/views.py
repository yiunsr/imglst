#-*- coding: utf-8 -*-
import logging
import json
import sys, traceback
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

from imglst.ErrClass import  ErrClass
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from facemorpher import locator, warper, blender
import base64

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import JsonResponse

from util.face_landmark_detection import face_landmark
from facemorpher.morpher import morph_image


logger = logging.getLogger('django_log')

# https://fadeit.dk/blog/2015/04/30/python3-flask-pil-in-memory-image/
# memory 를 파일 처럼 사용하는 법
def _base64(img, img_format):
    buffer = BytesIO()
    img.save(buffer, format= img_format)
    return base64.b64encode(buffer.getvalue()).decode("utf-8") 

def _alpha_image(img, points):
    mask = blender.mask_from_points(img.shape[:2], points)
    return np.dstack((img, mask))

@requires_csrf_token
def sample(request):
    try: 
        logger.info("/demo/sample")
        if request.path.startswith("/rest") == False:
            c = {}
            response = TemplateResponse(request, 'sample.html', c)
            response.render()
            return response

    except Exception as e:
        logger.error(traceback.format_exc() )
        return ErrClass('UNKNWON_ERROR').response()

@csrf_exempt
def landmark(request):
    try: 
        logger.info("/demo/landmark")
        img_file = request.FILES["img"]

        img_np = np.asarray(bytearray(img_file.file.getvalue()), dtype=np.uint8)
        img_cv = cv2.imdecode(img_np, 0 )  # @UndefinedVariable

        (box, img_point_list) = face_landmark(img_cv)

        # http://stackoverflow.com/questions/37210655/opencv-detect-face-landmarks-ear-chin-ear-line
        face_points = img_point_list[17:68]
        mouth_points = img_point_list[48:61]
        right_brow_point = img_point_list[17:22]
        left_brow_point = img_point_list[22:27]
        right_eye_points = img_point_list[36:42]
        left_eye_points = img_point_list[42:48]
        nose_points = img_point_list[27:35]
        jaw_points = img_point_list[0:17]
        chin_points = img_point_list[6:11]

        result = {}
        result['error'] = ErrClass('NOERROR').toDict()
        result['img_points'] = img_point_list
        result['face_points'] = face_points
        result['mouth_points'] = mouth_points
        result['right_brow_point'] = right_brow_point
        result['left_brow_point'] = left_brow_point
        result['right_eye_points'] = right_eye_points
        result['left_eye_points'] = left_eye_points
        result['nose_points'] = nose_points
        result['jaw_points'] = jaw_points
        result['chin_points'] = chin_points

        return HttpResponse(json.dumps(result), content_type="application/json")
    except Exception as e:
        logger.error(traceback.format_exc() )
        return ErrClass('UNKNWON_ERROR').response()

def get_new_size(width, height):
    small_size = min(width, height)
    if small_size < 200:
        return (False, width, height)
    zoom = small_size / 200
    new_width = int(width / zoom)
    new_height = int(height / zoom)
    return (True, new_width, new_height)

@csrf_exempt
def morhping(request):
    try: 
        logger.info("/demo/morhping")
        img_file_01 = request.FILES["left"]
        img_file_01 = Image.open(img_file_01) ## JPEG YUV 로 된 이미지 처리를 위해 PIL Image 를 한 번거친다. 
        (need_resize, new_width, new_height) = get_new_size(img_file_01.width, img_file_01.height)
        if need_resize:
           img_file_01 = img_file_01.resize((new_width, new_height))
        img_file_01 = img_file_01.convert("RGB") 
        img_cv_01 = np.array(img_file_01)

        img_file_02 = request.FILES["right"]
        img_file_02 = Image.open( img_file_02 )
        (need_resize, new_width, new_height) = get_new_size(img_file_02.width, img_file_02.height)
        if need_resize:
            img_file_02 = img_file_02.resize((new_width, new_height))
        img_file_02 = img_file_02.convert( "RGB" )
        img_cv_02 = np.array(img_file_02)

        percent  =  request.POST.get("percent", "50")
        percent = int(percent) / 100.0

        (_, img_point_list_01) = face_landmark(img_cv_01)
        img_point_list_np_01 = np.array( img_point_list_01 )

        (_, img_point_list_02) = face_landmark(img_cv_02)
        img_point_list_np_02 = np.array( img_point_list_02 )

        # width = max(img_cv_01.shape[0], img_cv_02.shape[0] )
        # height = max(img_cv_01.shape[1] , img_cv_02.shape[1] )
        height = max(img_cv_01.shape[0], img_cv_02.shape[0] )
        width = max(img_cv_01.shape[1] , img_cv_02.shape[1] )

        average_face = morph_image(img_cv_01, img_point_list_np_01, img_cv_02, img_point_list_np_02, percent, width, height)
        result_img = Image.fromarray(average_face)
        result_img =  "data:image/png;base64," + _base64( result_img , img_format = "png" )

        # 최종적으로는 아래 링크를 이용해 average_face 를 실제 사진에 넣어야 한다. 
        # https://www.learnopencv.com/face-swap-using-opencv-c-python/

        result = {}
        result['error'] = ErrClass('NOERROR').toDict()
        result['img'] = result_img
        return HttpResponse(json.dumps(result), content_type="application/json")

    except Exception as e:
        logger.error(traceback.format_exc() )
        return ErrClass('UNKNWON_ERROR').response()

