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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Document(BaseModel):
    """
    Document Entity
    """ # noqa: E501
    activity_object_id: Optional[StrictInt] = Field(default=None, alias="ActivityObjectId")
    author: Optional[StrictStr] = Field(default=None, description="The person who created the work product or document.", alias="Author")
    content_repository_document_internal_id: Optional[StrictStr] = Field(default=None, description="The internal ID of the content repository document.", alias="ContentRepositoryDocumentInternalId")
    create_date: Optional[datetime] = Field(default=None, description="The date this document was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this document.", alias="CreateUser")
    deliverable: Optional[StrictBool] = Field(default=None, description="The flag that indicates that the work product or document is a project deliverable.", alias="Deliverable")
    description: Optional[StrictStr] = Field(default=None, description="The narrative description of the work product or document.", alias="Description")
    document_category_name: Optional[StrictStr] = Field(default=None, description="The name of the associated document category.", alias="DocumentCategoryName")
    document_category_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated document category.", alias="DocumentCategoryObjectId")
    document_status_code_name: Optional[StrictStr] = Field(default=None, description="The name of the associated document status code.", alias="DocumentStatusCodeName")
    document_status_code_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated document status code.", alias="DocumentStatusCodeObjectId")
    document_type: Optional[StrictStr] = Field(default=None, description="The type of document: 'Non-Collaboration' or 'Collaboration'.", alias="DocumentType")
    guid: Optional[StrictStr] = Field(default=None, description="The globally unique ID generated by the system.", alias="GUID")
    is_baseline: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a Project or Baseline", alias="IsBaseline")
    is_template: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a template Project.", alias="IsTemplate")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this document was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this document.", alias="LastUpdateUser")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    parent_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the parent document of this document in the hierarchy.", alias="ParentObjectId")
    private_location: Optional[StrictStr] = Field(default=None, description="The work product or document's private file location.", alias="PrivateLocation")
    project_id: Optional[StrictStr] = Field(default=None, description="The short code that uniquely identifies the project.", alias="ProjectId")
    project_object_id: StrictInt = Field(description="The unique ID of the associated project.", alias="ProjectObjectId")
    public_location: Optional[StrictStr] = Field(default=None, description="The work product or document's publicly-accessible file location.", alias="PublicLocation")
    reference_number: Optional[StrictStr] = Field(default=None, description="The work product or document's reference or catalog number.", alias="ReferenceNumber")
    resource_id: Optional[StrictStr] = Field(default=None, description="The short code that uniquely identifies the associated resource.", alias="ResourceId")
    resource_name: Optional[StrictStr] = Field(default=None, description="The name of the associated resource.", alias="ResourceName")
    resource_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated resource.", alias="ResourceObjectId")
    revision_date: Optional[datetime] = Field(default=None, description="The date of the work product or document's last update.", alias="RevisionDate")
    sequence_number: Optional[StrictInt] = Field(default=None, description="The sequence number for sorting.", alias="SequenceNumber")
    title: StrictStr = Field(description="The title or name of a project work product or document.", alias="Title")
    version: Optional[StrictStr] = Field(default=None, description="The work product or document's version number.", alias="Version")
    __properties: ClassVar[List[str]] = ["ActivityObjectId", "Author", "ContentRepositoryDocumentInternalId", "CreateDate", "CreateUser", "Deliverable", "Description", "DocumentCategoryName", "DocumentCategoryObjectId", "DocumentStatusCodeName", "DocumentStatusCodeObjectId", "DocumentType", "GUID", "IsBaseline", "IsTemplate", "LastUpdateDate", "LastUpdateUser", "ObjectId", "ParentObjectId", "PrivateLocation", "ProjectId", "ProjectObjectId", "PublicLocation", "ReferenceNumber", "ResourceId", "ResourceName", "ResourceObjectId", "RevisionDate", "SequenceNumber", "Title", "Version"]

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
        """Create an instance of Document from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ActivityObjectId": obj.get("ActivityObjectId"),
            "Author": obj.get("Author"),
            "ContentRepositoryDocumentInternalId": obj.get("ContentRepositoryDocumentInternalId"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "Deliverable": obj.get("Deliverable"),
            "Description": obj.get("Description"),
            "DocumentCategoryName": obj.get("DocumentCategoryName"),
            "DocumentCategoryObjectId": obj.get("DocumentCategoryObjectId"),
            "DocumentStatusCodeName": obj.get("DocumentStatusCodeName"),
            "DocumentStatusCodeObjectId": obj.get("DocumentStatusCodeObjectId"),
            "DocumentType": obj.get("DocumentType"),
            "GUID": obj.get("GUID"),
            "IsBaseline": obj.get("IsBaseline"),
            "IsTemplate": obj.get("IsTemplate"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "ObjectId": obj.get("ObjectId"),
            "ParentObjectId": obj.get("ParentObjectId"),
            "PrivateLocation": obj.get("PrivateLocation"),
            "ProjectId": obj.get("ProjectId"),
            "ProjectObjectId": obj.get("ProjectObjectId"),
            "PublicLocation": obj.get("PublicLocation"),
            "ReferenceNumber": obj.get("ReferenceNumber"),
            "ResourceId": obj.get("ResourceId"),
            "ResourceName": obj.get("ResourceName"),
            "ResourceObjectId": obj.get("ResourceObjectId"),
            "RevisionDate": obj.get("RevisionDate"),
            "SequenceNumber": obj.get("SequenceNumber"),
            "Title": obj.get("Title"),
            "Version": obj.get("Version")
        })
        return _obj


