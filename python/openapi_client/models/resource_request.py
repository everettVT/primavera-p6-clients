# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.resource_request_criterion import ResourceRequestCriterion
from typing import Optional, Set
from typing_extensions import Self

class ResourceRequest(BaseModel):
    """
    ResourceRequest
    """ # noqa: E501
    finish_date: Optional[datetime] = Field(default=None, alias="FinishDate")
    match_all_criteria: Optional[StrictBool] = Field(default=None, alias="MatchAllCriteria")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    requested_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RequestedUnits")
    sequence_number: Optional[StrictInt] = Field(default=None, alias="SequenceNumber")
    show_only_labor_resources: Optional[StrictBool] = Field(default=None, alias="ShowOnlyLaborResources")
    show_overallocated_resources: Optional[StrictBool] = Field(default=None, alias="ShowOverallocatedResources")
    sort_results_by_availability: Optional[StrictBool] = Field(default=None, alias="SortResultsByAvailability")
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    use_activity_dates: Optional[StrictBool] = Field(default=None, alias="UseActivityDates")
    resource_request_criterion: Optional[List[ResourceRequestCriterion]] = Field(default=None, alias="ResourceRequestCriterion")
    __properties: ClassVar[List[str]] = ["FinishDate", "MatchAllCriteria", "Name", "RequestedUnits", "SequenceNumber", "ShowOnlyLaborResources", "ShowOverallocatedResources", "SortResultsByAvailability", "StartDate", "UseActivityDates", "ResourceRequestCriterion"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResourceRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in resource_request_criterion (list)
        _items = []
        if self.resource_request_criterion:
            for _item_resource_request_criterion in self.resource_request_criterion:
                if _item_resource_request_criterion:
                    _items.append(_item_resource_request_criterion.to_dict())
            _dict['ResourceRequestCriterion'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResourceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "FinishDate": obj.get("FinishDate"),
            "MatchAllCriteria": obj.get("MatchAllCriteria"),
            "Name": obj.get("Name"),
            "RequestedUnits": obj.get("RequestedUnits"),
            "SequenceNumber": obj.get("SequenceNumber"),
            "ShowOnlyLaborResources": obj.get("ShowOnlyLaborResources"),
            "ShowOverallocatedResources": obj.get("ShowOverallocatedResources"),
            "SortResultsByAvailability": obj.get("SortResultsByAvailability"),
            "StartDate": obj.get("StartDate"),
            "UseActivityDates": obj.get("UseActivityDates"),
            "ResourceRequestCriterion": [ResourceRequestCriterion.from_dict(_item) for _item in obj["ResourceRequestCriterion"]] if obj.get("ResourceRequestCriterion") is not None else None
        })
        return _obj


