from functools import wraps
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import datetime


def handle_request(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except ObjectDoesNotExist as e:
            error_message = str(e).strip() or e.__class__.__name__.replace("DoesNotExist", "")
            if not error_message or error_message == "DoesNotExist":
                model_name = view_func.__name__.replace("get_", "").capitalize()
            else:
                model_name = error_message.split(" ")[0]
            return Response(
                {'data': None, 'error': f'{model_name} not found.', 'details': None, 'status_code': status.HTTP_404_NOT_FOUND, 'time': datetime.now().isoformat()},
                status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            return Response(
                {'data': None, 'error': 'Validation Error', 'details': e.detail if hasattr(e, 'detail') else str(e), 'status_code': status.HTTP_400_BAD_REQUEST, 'time': datetime.now().isoformat()},
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError as e:
            return Response(
                {'data': None, 'error': 'Database Integrity Error', 'details': str(e), 'status_code': status.HTTP_400_BAD_REQUEST, 'time': datetime.now().isoformat()},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'data': None, 'error': 'Internal Server Error', 'details': str(e), 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'time': datetime.now().isoformat()},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return wrapper


def AResponse(data=None, details=None, error=None, status_code=status.HTTP_200_OK):
    """
    Standardized API response format
    """
    return Response({
        'data': data,
        'details': details,
        'error': error,
        'status_code': status_code,
        'time': datetime.now().isoformat()
    }, status=status_code)