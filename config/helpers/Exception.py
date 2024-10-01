import logging
import os
import sys
import traceback
from django.core.exceptions import RequestDataTooBig, ValidationError
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.forms import model_to_dict
# from django_fsm import TransitionNotAllowed
from rest_framework import status
from rest_framework.response import Response
import logging

def exception(e):
    try:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
        logging.error(f' Error: {e}  Error Type:  {exc_type}  Module Name: {fname} Line No : {exc_tb.tb_lineno}')
    except Exception :
        logging.error(e)


def custom_rest_exception_handler(exc, context):
    """ Custom rest api exception handler """
    from rest_framework import exceptions
    from rest_framework.views import exception_handler, set_rollback
    response = exception_handler(exc, context)
    err_msg = str(exc)
    if isinstance(exc, RequestDataTooBig):
        return Response({'message': 'too big data or file upload'}, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

    if isinstance(exc, ProtectedError):
        data = {'message': ' Not able to delete, there are links to this record and is protected.'}
        traceback.print_exc()
        set_rollback()
        return Response(data, status=status.HTTP_412_PRECONDITION_FAILED)

    if isinstance(exc, IntegrityError) and ('already exists' in err_msg or 'must make a unique set' in err_msg or
                                            'must be unique' in err_msg):
        data = {'message': 'duplicate unique key'}
        set_rollback()
        return Response(data, status=status.HTTP_409_CONFLICT)
    # if isinstance(exc, TransitionNotAllowed):
    #     return Response({'message': 'Transition not allowed. Check with system admin'},
    #                     status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
    if response is None:
        if isinstance(exc, ValidationError):
            return Response(exc.message_dict, status=status.HTTP_400_BAD_REQUEST)
        traceback.print_exc()
        return Response({'message': 'unexpected server error. Check with system admin'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)

    if isinstance(exc, exceptions.NotAuthenticated):
        response.status_code = status.HTTP_401_UNAUTHORIZED
    elif isinstance(exc, exceptions.ValidationError) and (
            'already exists' in err_msg or 'must make a unique set' in err_msg or 'must be unique' in err_msg):
        response.status_code = status.HTTP_409_CONFLICT

    if response is not None:
        # if 'detail' key is present, change it to 'error' or whatever you want
        if response.data.get('detail', None):
            response.data['message'] = response.data.get('detail')
            del response.data['detail']

    return response
