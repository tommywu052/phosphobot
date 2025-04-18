# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .calibrate_response_calibration_status import CalibrateResponseCalibrationStatus
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class CalibrateResponse(UniversalBaseModel):
    """
    Response from the calibration endpoint.
    """

    calibration_status: CalibrateResponseCalibrationStatus = pydantic.Field()
    """
    Status of the calibration. Ends when status is success or error.
    """

    current_step: int
    message: str
    total_nb_steps: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
