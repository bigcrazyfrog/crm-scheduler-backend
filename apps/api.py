from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse

from ninja import NinjaAPI

from apps.algorithm.api.routers import add_algorithms_router
from config.settings import DEBUG

# from apps.auth_jwt.api.routers import add_auth_router
# from apps.auth_jwt.middlewares import HTTPJWTAuth
from apps.cabinets.api.routers import add_cabinets_router
from apps.doctors.api.routers import add_doctors_router
from apps.intervals.api.routers import add_intervals_router

# from apps.users.api.routers import add_users_router


def get_api() -> NinjaAPI:
    """Assembly point of general API."""
    # auth = [HTTPJWTAuth()]

    api = NinjaAPI(
        title="REDROCK.SCHEDULER.BACKEND",
        version="0.1.0",
        description="The best API",
        # auth=auth,
    )

    # add_auth_router(api=api)
    # add_users_router(api=api)
    add_doctors_router(api=api)
    add_cabinets_router(api=api)
    add_intervals_router(api=api)
    add_algorithms_router(api=api)

    return api


# General NinjaAPI object using as REST API
ninja_api = get_api()


@ninja_api.exception_handler(ValidationError)
def validation_error_handler(request: HttpRequest, exc) -> HttpResponse:
    """Handler for unexpected `ValidationError`."""
    return ninja_api.create_response(
        request,
        {"message": str(exc) if DEBUG else "Data is not valid"},
        status=422,
    )


@ninja_api.exception_handler(Exception)
def exception_handler(request: HttpRequest, exc) -> HttpResponse:
    """Handler for unexpected error."""
    return ninja_api.create_response(
        request,
        {"message": str(exc) if DEBUG else "Unexpected error"},
        status=500,
    )
