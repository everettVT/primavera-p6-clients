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
from typing import Optional, Set
from typing_extensions import Self

class GlobalPreferences(BaseModel):
    """
    GlobalPreferences Entity
    """ # noqa: E501
    allow_approved_ts_rejection: Optional[StrictBool] = Field(default=None, alias="AllowApprovedTSRejection")
    always_launch_online_help: Optional[StrictBool] = Field(default=None, description="The flag indicating that Online Help should be launched whenever a user accesses help.", alias="AlwaysLaunchOnlineHelp")
    base_currency_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the currency.", alias="BaseCurrencyObjectId")
    contract_management_url: Optional[StrictStr] = Field(default=None, description="This is the URL of the Contract Management application.", alias="ContractManagementURL")
    create_date: Optional[datetime] = Field(default=None, description="The date this global preferences was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this global preferences.", alias="CreateUser")
    custom_label1: Optional[StrictStr] = Field(default=None, description="The custom (user-defined) text that will be inserted into any report containing the Custom Label 1 global variable text cell, when printed.", alias="CustomLabel1")
    custom_label2: Optional[StrictStr] = Field(default=None, description="The custom (user-defined) text that will be inserted into any report containing the Custom Label 2 global variable text cell, when printed.", alias="CustomLabel2")
    custom_label3: Optional[StrictStr] = Field(default=None, description="The custom (user-defined) text that will be inserted into any report containing the Custom Label 3 global variable text cell, when printed.", alias="CustomLabel3")
    day_abbreviation: Optional[StrictStr] = Field(default=None, description="The abbreviation character for time periods of days. This abbreviation is used for displaying time units and durations in the user's selected display formats.", alias="DayAbbreviation")
    default_duration: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The planned duration assigned to new activities by default.", alias="DefaultDuration")
    default_timesheet_approval_manager: Optional[StrictInt] = Field(default=None, description="The unique ID of the resource manager assigned to approve timesheets for new resources by default.", alias="DefaultTimesheetApprovalManager")
    eppm_consent_message: Optional[StrictStr] = Field(default=None, alias="EPPMConsentMessage")
    eppm_enable_consent: Optional[StrictStr] = Field(default=None, alias="EPPMEnableConsent")
    ev_estimate_to_complete_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The user-defined performance factor, PF, for computing earned-value estimate-to-complete. ETC is computed as PF * ( BAC - earned value). This value is assigned to new projects by default. It can be modified for each project WBS element.", alias="EVEstimateToCompleteFactor")
    ev_estimate_to_complete_technique: Optional[StrictStr] = Field(default=None, description="The technique for computing earned-value estimate-to-complete. This setting is assigned to new projects by default. It can be modified for each project WBS element.", alias="EVEstimateToCompleteTechnique")
    ev_performance_pct_complete_custom_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The user-defined percent complete for computing earned value for activities within the WBS. A value of, say, 25 means that 25% of the planned amount is earned when the activity is started and the remainder is earned when the activity is completed. This value is assigned to new projects by default. It can be modified for each project WBS element.", alias="EVPerformancePctCompleteCustomPct")
    ev_performance_pct_complete_technique: Optional[StrictStr] = Field(default=None, description="The technique used for computing earned-value percent complete. This setting is assigned to new projects by default. It can be modified for each project WBS element.", alias="EVPerformancePctCompleteTechnique")
    earned_value_calculation: Optional[StrictStr] = Field(default=None, description="The flag indicating which values to use when calculating earned value when using a primary baseline. Valid values are 'At Completion Values with Current Dates', 'Planned Values with Planned Dates', and 'Planned Values with Current Dates'.", alias="EarnedValueCalculation")
    email_notify_ts_rejection: Optional[StrictBool] = Field(default=None, alias="EmailNotifyTSRejection")
    enable_password_policy: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether the password policy is enforced.", alias="EnablePasswordPolicy")
    enable_ts_audit: Optional[StrictBool] = Field(default=None, description="The flag indicating whether to track timesheet submission, approval, and rejection. When you set this option, the application saves each user who reviews a timesheet, and when the timesheet was reviewed. This information can be viewed by loading TimesheetAudit business objects.", alias="EnableTSAudit")
    enable_web_services_ip_check: Optional[StrictBool] = Field(default=None, alias="EnableWebServicesIPCheck")
    enable_whats_new_dialog: Optional[StrictBool] = Field(default=None, alias="EnableWhatsNewDialog")
    exception_site_list: Optional[StrictStr] = Field(default=None, alias="ExceptionSiteList")
    footer_label1: Optional[StrictStr] = Field(default=None, description="The first footer for reports. The Project Management application allows up to three different footer text strings that can be optionally placed at the bottom of all reports using the report writer.", alias="FooterLabel1")
    footer_label2: Optional[StrictStr] = Field(default=None, description="The second footer for reports. The Project Management application allows up to three different footer text strings that can be optionally placed at the bottom of all reports using the report writer.", alias="FooterLabel2")
    footer_label3: Optional[StrictStr] = Field(default=None, description="The third footer for reports. The Project Management application allows up to three different footer text strings that can be optionally placed at the bottom of all reports using the report writer.", alias="FooterLabel3")
    gateway_api_url: Optional[StrictStr] = Field(default=None, description="The Primavera Gateway URL that will allow you to integrate other products with P6 and P6 Professional.", alias="GatewayApiUrl")
    gateway_export_erp_sync_name: Optional[StrictStr] = Field(default=None, description="The synchronization for exporting to ERP.", alias="GatewayExportERPSyncName")
    gateway_export_unifier_sync_name: Optional[StrictStr] = Field(default=None, description="The synchronization for exporting to Primavera Unifier.", alias="GatewayExportUnifierSyncName")
    gateway_import_erp_sync_name: Optional[StrictStr] = Field(default=None, description="The synchronization for importing to ERP.", alias="GatewayImportERPSyncName")
    gateway_import_unifier_sync_name: Optional[StrictStr] = Field(default=None, description="The synchronization for importing to Primavera Unifier.", alias="GatewayImportUnifierSyncName")
    gateway_p6_deployment_name: Optional[StrictStr] = Field(default=None, description="The name for the P6 deployment to be integrated with Primavera Gateway.", alias="GatewayP6DeploymentName")
    gateway_password: Optional[StrictStr] = Field(default=None, description="The password for integration.", alias="GatewayPassword")
    gateway_unifier_enabled: Optional[StrictBool] = Field(default=None, description="This is the flag to enable Unifier through Gateway.", alias="GatewayUnifierEnabled")
    gateway_username: Optional[StrictStr] = Field(default=None, description="The username for integration.", alias="GatewayUsername")
    header_label1: Optional[StrictStr] = Field(default=None, description="The first header for reports. The Project Management application allows up to three different header text strings that can be optionally placed at the top of all reports using the report writer.", alias="HeaderLabel1")
    header_label2: Optional[StrictStr] = Field(default=None, description="The second header for reports. The Project Management application allows up to three different header text strings that can be optionally placed at the top of all reports using the report writer.", alias="HeaderLabel2")
    header_label3: Optional[StrictStr] = Field(default=None, description="The third header for reports. The Project Management application allows up to three different header text strings that can be optionally placed at the top of all reports using the report writer.", alias="HeaderLabel3")
    hour_abbreviation: Optional[StrictStr] = Field(default=None, description="The abbreviation character for time periods of hours. This abbreviation is used for displaying time units and durations in the user's selected display formats.", alias="HourAbbreviation")
    hours_per_day: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of work hours per day. This conversion factor is used for displaying time units and durations in the user's selected display formats.", alias="HoursPerDay")
    hours_per_month: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of work hours per month. This conversion factor is used for displaying time units and durations in the user's selected display formats.", alias="HoursPerMonth")
    hours_per_week: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of work hours per week. This conversion factor is used for displaying time units and durations in the user's selected display formats.", alias="HoursPerWeek")
    hours_per_year: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of work hours per year. This conversion factor is used for displaying time units and durations in the user's selected display formats.", alias="HoursPerYear")
    ip_site_list: Optional[StrictStr] = Field(default=None, alias="IPSiteList")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this global preferences was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this global preferences.", alias="LastUpdateUser")
    log_hours_after_actual_finish: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities for dates after the activities' actual finish dates.", alias="LogHoursAfterActualFinish")
    log_hours_before_actual_start: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities for dates prior to the activities' actual start dates.", alias="LogHoursBeforeActualStart")
    log_hours_completed_activities: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities that are already marked as completed.", alias="LogHoursCompletedActivities")
    log_hours_in_future: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether the user can log hours in the future.", alias="LogHoursInFuture")
    log_hours_not_started_activities: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities that are still marked as Not started.", alias="LogHoursNotStartedActivities")
    max_activity_code_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels that can be created in activity code hierarchies in the Project Management application. The API ignores this setting when creating activity codes.", alias="MaxActivityCodeTreeLevels")
    max_activity_codes_per_project: Optional[StrictInt] = Field(default=None, description="The maximum number of project-level activity user codes that can be created per project.", alias="MaxActivityCodesPerProject")
    max_activity_id_length: Optional[StrictInt] = Field(default=None, description="The maximum number of characters allowed for activity IDs.", alias="MaxActivityIdLength")
    max_assignment_code_tree_level_cnt: Optional[StrictInt] = Field(default=None, alias="MaxAssignmentCodeTreeLevelCnt")
    max_baselines_per_project: Optional[StrictInt] = Field(default=None, description="The maximum number of baselines that can be created per project.", alias="MaxBaselinesPerProject")
    max_cost_account_length: Optional[StrictInt] = Field(default=None, description="The maximum number of characters allowed for cost account IDs (at each level in the cost account tree).", alias="MaxCostAccountLength")
    max_cost_account_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels that can be created in the cost account hierarchy in the Project Management application. The API ignores this setting when creating cost accounts.", alias="MaxCostAccountTreeLevels")
    max_fp_calendar_count: Optional[StrictInt] = Field(default=None, alias="MaxFPCalendarCount")
    max_obs_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels that can be created in OBS hierarchies in the Project Management application. The API ignores this setting when creating OBS objects.", alias="MaxOBSTreeLevels")
    max_project_code_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels in the project category hierarchy in the Project Management application. The API ignores this setting when creating project codes.", alias="MaxProjectCodeTreeLevels")
    max_project_id_length: Optional[StrictInt] = Field(default=None, description="The maximum number characters allowed for project IDs.", alias="MaxProjectIdLength")
    max_resource_code_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels in the resource code hierarchy in the Project Management application. The API ignores this setting when creating resource codes.", alias="MaxResourceCodeTreeLevels")
    max_resource_id_length: Optional[StrictInt] = Field(default=None, description="The maximum number of characters allowed for resource IDs (at each level in the resource tree).", alias="MaxResourceIdLength")
    max_resource_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels that can be created in the resource hierarchy.", alias="MaxResourceTreeLevels")
    max_role_code_tree_level_cnt: Optional[StrictInt] = Field(default=None, alias="MaxRoleCodeTreeLevelCnt")
    max_role_id_length: Optional[StrictInt] = Field(default=None, description="The maximum number characters allowed for role IDs.", alias="MaxRoleIdLength")
    max_role_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels in the role hierarchy in the Project Management application. The API ignores this setting when creating roles.", alias="MaxRoleTreeLevels")
    max_timesheet_resource_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum hours a resource can enter per day for all of their assigned activities.", alias="MaxTimesheetResourceHours")
    max_wbs_code_length: Optional[StrictInt] = Field(default=None, description="The maximum number of characters allowed for WBS codes (at each level in the WBS tree).", alias="MaxWBSCodeLength")
    max_wbs_tree_levels: Optional[StrictInt] = Field(default=None, description="The maximum number of levels that can be created in WBS hierarchies.", alias="MaxWBSTreeLevels")
    maximum_baselines_copied_with_project: Optional[StrictInt] = Field(default=None, description="The number of baseline projects that can be copied with a project.", alias="MaximumBaselinesCopiedWithProject")
    minute_abbreviation: Optional[StrictStr] = Field(default=None, description="The abbreviation character for time periods of minutes. This abbreviation is used for displaying time units and durations in the user's selected display formats.", alias="MinuteAbbreviation")
    month_abbreviation: Optional[StrictStr] = Field(default=None, description="The abbreviation character for time periods of months. This abbreviation is used for displaying time units and durations in the user's selected display formats.", alias="MonthAbbreviation")
    number_of_accessible_future_timesheets: Optional[StrictInt] = Field(default=None, description="The number of future timesheets that timesheet application users are allowed to access.", alias="NumberOfAccessibleFutureTimesheets")
    number_of_accessible_past_timesheets: Optional[StrictInt] = Field(default=None, alias="NumberOfAccessiblePastTimesheets")
    private_ip_allow_list: Optional[StrictStr] = Field(default=None, alias="PrivateIPAllowList")
    report_enable_lazy_load: Optional[StrictBool] = Field(default=None, alias="ReportEnableLazyLoad")
    resources_can_assign_themselves_to_activities: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether timesheet application users are allowed to assign themselves to activities in this project.", alias="ResourcesCanAssignThemselvesToActivities")
    resources_can_assign_themselves_to_activities_outside_their_obs_access: Optional[StrictBool] = Field(default=None, alias="ResourcesCanAssignThemselvesToActivitiesOutsideTheirOBSAccess")
    start_day_of_week: Optional[StrictInt] = Field(default=None, description="The starting day of the week as displayed in all calendars.", alias="StartDayOfWeek")
    summarize_by_calendar: Optional[StrictBool] = Field(default=None, description="The flag indicating whether to summarize by calendar .", alias="SummarizeByCalendar")
    summarize_by_financial_periods: Optional[StrictBool] = Field(default=None, description="The flag indicating whether to summarize the EPS, project or WBS by financial periods.", alias="SummarizeByFinancialPeriods")
    summary_resource_spread_interval: Optional[StrictStr] = Field(default=None, description="The interval in which resource and role level spreads are summarized and stored. Valid values are 'Month' and 'Week'. This setting is used by the Summarizer job service.", alias="SummaryResourceSpreadInterval")
    summary_wbs_spread_interval: Optional[StrictStr] = Field(default=None, description="The interval in which WBS level spreads are summarized and stored. Valid values are 'Month' and 'Week'. This setting is used by the Summarizer job service.", alias="SummaryWBSSpreadInterval")
    team_member_consent_message: Optional[StrictStr] = Field(default=None, alias="TeamMemberConsentMessage")
    team_member_enable_consent: Optional[StrictStr] = Field(default=None, alias="TeamMemberEnableConsent")
    time_window_completed_activities: Optional[StrictInt] = Field(default=None, description="The time window (days) to access completed activities in the timesheet application, assigned to new resources by default.", alias="TimeWindowCompletedActivities")
    time_window_not_started_activities: Optional[StrictInt] = Field(default=None, description="The time window (days) to access not started activities in the timesheet application, assigned to new resources by default.", alias="TimeWindowNotStartedActivities")
    timesheet_approval_level: Optional[StrictInt] = Field(default=None, description="The number of approval levels required for timesheets (0, 1, or 2) before timesheets hours are applied to activities as actuals.", alias="TimesheetApprovalLevel")
    timesheet_decimal_digits: Optional[StrictInt] = Field(default=None, description="The number of decimal digits for recording hours in timesheets.", alias="TimesheetDecimalDigits")
    timesheet_interval: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether timesheet application users enter timesheet hours daily or by entire timesheet reporting period.", alias="TimesheetInterval")
    timesheet_period_ends_on_day: Optional[StrictStr] = Field(default=None, description="The end day of time sheet period used in time sheet application. Valid values are: 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' and 'Saturday'.", alias="TimesheetPeriodEndsOnDay")
    timesheet_period_type: Optional[StrictStr] = Field(default=None, description="The time period used in time sheet application. Valid values are: 'Every Week', 'Every Two Weeks', 'Every Four Weeks' and 'Every Month'.", alias="TimesheetPeriodType")
    unifier_auth_code: Optional[StrictStr] = Field(default=None, alias="UnifierAuthCode")
    unifier_company_short_name: Optional[StrictStr] = Field(default=None, alias="UnifierCompanyShortName")
    unifier_integration_password: Optional[StrictStr] = Field(default=None, alias="UnifierIntegrationPassword")
    unifier_integration_user_name: Optional[StrictStr] = Field(default=None, alias="UnifierIntegrationUserName")
    unifier_web_service_url: Optional[StrictStr] = Field(default=None, alias="UnifierWebServiceURL")
    use_calendar_time_periods_flag: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether the system uses the hours per time period defined in the calendar.If this flag is true, the system uses the hours per time period settings that are defined in the calendar.If this flag is false, the system uses the hours per time period from the global preferences.", alias="UseCalendarTimePeriodsFlag")
    use_max_timesheet_resource_hours: Optional[StrictBool] = Field(default=None, description="The flag indicating whether to restrict the number of hours a user can enter to the limit specified in MaxTimesheetResourceHours.", alias="UseMaxTimesheetResourceHours")
    use_project_manager_approval: Optional[StrictStr] = Field(default=None, description="The flag that indicates the approval sequence, if any, required for level 2 timesheet approvals. For example, project managers must approve before resource manager do, or vice versa.", alias="UseProjectManagerApproval")
    use_timesheets: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether new resources use timesheets by default.", alias="UseTimesheets")
    version_for_whats_new: Optional[StrictStr] = Field(default=None, alias="VersionForWhatsNew")
    wbs_category_label: Optional[StrictStr] = Field(default=None, description="The dynamic label used for the WBS category. Project Planner allows the system administrator to dynamically label the WBS category.", alias="WBSCategoryLabel")
    wbs_code_separator: Optional[StrictStr] = Field(default=None, description="The character used for separating code fields for the cost account tree. This is also the WBS code separator for new projects by default.", alias="WBSCodeSeparator")
    week_abbreviation: Optional[StrictStr] = Field(default=None, description="The abbreviation character for time periods of weeks. This abbreviation is used for displaying time units and durations in the user's selected display formats.", alias="WeekAbbreviation")
    year_abbreviation: Optional[StrictStr] = Field(default=None, description="The abbreviation character for time periods of years. This abbreviation is used for displaying time units and durations in the user's selected display formats.", alias="YearAbbreviation")
    __properties: ClassVar[List[str]] = ["AllowApprovedTSRejection", "AlwaysLaunchOnlineHelp", "BaseCurrencyObjectId", "ContractManagementURL", "CreateDate", "CreateUser", "CustomLabel1", "CustomLabel2", "CustomLabel3", "DayAbbreviation", "DefaultDuration", "DefaultTimesheetApprovalManager", "EPPMConsentMessage", "EPPMEnableConsent", "EVEstimateToCompleteFactor", "EVEstimateToCompleteTechnique", "EVPerformancePctCompleteCustomPct", "EVPerformancePctCompleteTechnique", "EarnedValueCalculation", "EmailNotifyTSRejection", "EnablePasswordPolicy", "EnableTSAudit", "EnableWebServicesIPCheck", "EnableWhatsNewDialog", "ExceptionSiteList", "FooterLabel1", "FooterLabel2", "FooterLabel3", "GatewayApiUrl", "GatewayExportERPSyncName", "GatewayExportUnifierSyncName", "GatewayImportERPSyncName", "GatewayImportUnifierSyncName", "GatewayP6DeploymentName", "GatewayPassword", "GatewayUnifierEnabled", "GatewayUsername", "HeaderLabel1", "HeaderLabel2", "HeaderLabel3", "HourAbbreviation", "HoursPerDay", "HoursPerMonth", "HoursPerWeek", "HoursPerYear", "IPSiteList", "LastUpdateDate", "LastUpdateUser", "LogHoursAfterActualFinish", "LogHoursBeforeActualStart", "LogHoursCompletedActivities", "LogHoursInFuture", "LogHoursNotStartedActivities", "MaxActivityCodeTreeLevels", "MaxActivityCodesPerProject", "MaxActivityIdLength", "MaxAssignmentCodeTreeLevelCnt", "MaxBaselinesPerProject", "MaxCostAccountLength", "MaxCostAccountTreeLevels", "MaxFPCalendarCount", "MaxOBSTreeLevels", "MaxProjectCodeTreeLevels", "MaxProjectIdLength", "MaxResourceCodeTreeLevels", "MaxResourceIdLength", "MaxResourceTreeLevels", "MaxRoleCodeTreeLevelCnt", "MaxRoleIdLength", "MaxRoleTreeLevels", "MaxTimesheetResourceHours", "MaxWBSCodeLength", "MaxWBSTreeLevels", "MaximumBaselinesCopiedWithProject", "MinuteAbbreviation", "MonthAbbreviation", "NumberOfAccessibleFutureTimesheets", "NumberOfAccessiblePastTimesheets", "PrivateIPAllowList", "ReportEnableLazyLoad", "ResourcesCanAssignThemselvesToActivities", "ResourcesCanAssignThemselvesToActivitiesOutsideTheirOBSAccess", "StartDayOfWeek", "SummarizeByCalendar", "SummarizeByFinancialPeriods", "SummaryResourceSpreadInterval", "SummaryWBSSpreadInterval", "TeamMemberConsentMessage", "TeamMemberEnableConsent", "TimeWindowCompletedActivities", "TimeWindowNotStartedActivities", "TimesheetApprovalLevel", "TimesheetDecimalDigits", "TimesheetInterval", "TimesheetPeriodEndsOnDay", "TimesheetPeriodType", "UnifierAuthCode", "UnifierCompanyShortName", "UnifierIntegrationPassword", "UnifierIntegrationUserName", "UnifierWebServiceURL", "UseCalendarTimePeriodsFlag", "UseMaxTimesheetResourceHours", "UseProjectManagerApproval", "UseTimesheets", "VersionForWhatsNew", "WBSCategoryLabel", "WBSCodeSeparator", "WeekAbbreviation", "YearAbbreviation"]

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
        """Create an instance of GlobalPreferences from a JSON string"""
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
        """Create an instance of GlobalPreferences from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AllowApprovedTSRejection": obj.get("AllowApprovedTSRejection"),
            "AlwaysLaunchOnlineHelp": obj.get("AlwaysLaunchOnlineHelp"),
            "BaseCurrencyObjectId": obj.get("BaseCurrencyObjectId"),
            "ContractManagementURL": obj.get("ContractManagementURL"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "CustomLabel1": obj.get("CustomLabel1"),
            "CustomLabel2": obj.get("CustomLabel2"),
            "CustomLabel3": obj.get("CustomLabel3"),
            "DayAbbreviation": obj.get("DayAbbreviation"),
            "DefaultDuration": obj.get("DefaultDuration"),
            "DefaultTimesheetApprovalManager": obj.get("DefaultTimesheetApprovalManager"),
            "EPPMConsentMessage": obj.get("EPPMConsentMessage"),
            "EPPMEnableConsent": obj.get("EPPMEnableConsent"),
            "EVEstimateToCompleteFactor": obj.get("EVEstimateToCompleteFactor"),
            "EVEstimateToCompleteTechnique": obj.get("EVEstimateToCompleteTechnique"),
            "EVPerformancePctCompleteCustomPct": obj.get("EVPerformancePctCompleteCustomPct"),
            "EVPerformancePctCompleteTechnique": obj.get("EVPerformancePctCompleteTechnique"),
            "EarnedValueCalculation": obj.get("EarnedValueCalculation"),
            "EmailNotifyTSRejection": obj.get("EmailNotifyTSRejection"),
            "EnablePasswordPolicy": obj.get("EnablePasswordPolicy"),
            "EnableTSAudit": obj.get("EnableTSAudit"),
            "EnableWebServicesIPCheck": obj.get("EnableWebServicesIPCheck"),
            "EnableWhatsNewDialog": obj.get("EnableWhatsNewDialog"),
            "ExceptionSiteList": obj.get("ExceptionSiteList"),
            "FooterLabel1": obj.get("FooterLabel1"),
            "FooterLabel2": obj.get("FooterLabel2"),
            "FooterLabel3": obj.get("FooterLabel3"),
            "GatewayApiUrl": obj.get("GatewayApiUrl"),
            "GatewayExportERPSyncName": obj.get("GatewayExportERPSyncName"),
            "GatewayExportUnifierSyncName": obj.get("GatewayExportUnifierSyncName"),
            "GatewayImportERPSyncName": obj.get("GatewayImportERPSyncName"),
            "GatewayImportUnifierSyncName": obj.get("GatewayImportUnifierSyncName"),
            "GatewayP6DeploymentName": obj.get("GatewayP6DeploymentName"),
            "GatewayPassword": obj.get("GatewayPassword"),
            "GatewayUnifierEnabled": obj.get("GatewayUnifierEnabled"),
            "GatewayUsername": obj.get("GatewayUsername"),
            "HeaderLabel1": obj.get("HeaderLabel1"),
            "HeaderLabel2": obj.get("HeaderLabel2"),
            "HeaderLabel3": obj.get("HeaderLabel3"),
            "HourAbbreviation": obj.get("HourAbbreviation"),
            "HoursPerDay": obj.get("HoursPerDay"),
            "HoursPerMonth": obj.get("HoursPerMonth"),
            "HoursPerWeek": obj.get("HoursPerWeek"),
            "HoursPerYear": obj.get("HoursPerYear"),
            "IPSiteList": obj.get("IPSiteList"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "LogHoursAfterActualFinish": obj.get("LogHoursAfterActualFinish"),
            "LogHoursBeforeActualStart": obj.get("LogHoursBeforeActualStart"),
            "LogHoursCompletedActivities": obj.get("LogHoursCompletedActivities"),
            "LogHoursInFuture": obj.get("LogHoursInFuture"),
            "LogHoursNotStartedActivities": obj.get("LogHoursNotStartedActivities"),
            "MaxActivityCodeTreeLevels": obj.get("MaxActivityCodeTreeLevels"),
            "MaxActivityCodesPerProject": obj.get("MaxActivityCodesPerProject"),
            "MaxActivityIdLength": obj.get("MaxActivityIdLength"),
            "MaxAssignmentCodeTreeLevelCnt": obj.get("MaxAssignmentCodeTreeLevelCnt"),
            "MaxBaselinesPerProject": obj.get("MaxBaselinesPerProject"),
            "MaxCostAccountLength": obj.get("MaxCostAccountLength"),
            "MaxCostAccountTreeLevels": obj.get("MaxCostAccountTreeLevels"),
            "MaxFPCalendarCount": obj.get("MaxFPCalendarCount"),
            "MaxOBSTreeLevels": obj.get("MaxOBSTreeLevels"),
            "MaxProjectCodeTreeLevels": obj.get("MaxProjectCodeTreeLevels"),
            "MaxProjectIdLength": obj.get("MaxProjectIdLength"),
            "MaxResourceCodeTreeLevels": obj.get("MaxResourceCodeTreeLevels"),
            "MaxResourceIdLength": obj.get("MaxResourceIdLength"),
            "MaxResourceTreeLevels": obj.get("MaxResourceTreeLevels"),
            "MaxRoleCodeTreeLevelCnt": obj.get("MaxRoleCodeTreeLevelCnt"),
            "MaxRoleIdLength": obj.get("MaxRoleIdLength"),
            "MaxRoleTreeLevels": obj.get("MaxRoleTreeLevels"),
            "MaxTimesheetResourceHours": obj.get("MaxTimesheetResourceHours"),
            "MaxWBSCodeLength": obj.get("MaxWBSCodeLength"),
            "MaxWBSTreeLevels": obj.get("MaxWBSTreeLevels"),
            "MaximumBaselinesCopiedWithProject": obj.get("MaximumBaselinesCopiedWithProject"),
            "MinuteAbbreviation": obj.get("MinuteAbbreviation"),
            "MonthAbbreviation": obj.get("MonthAbbreviation"),
            "NumberOfAccessibleFutureTimesheets": obj.get("NumberOfAccessibleFutureTimesheets"),
            "NumberOfAccessiblePastTimesheets": obj.get("NumberOfAccessiblePastTimesheets"),
            "PrivateIPAllowList": obj.get("PrivateIPAllowList"),
            "ReportEnableLazyLoad": obj.get("ReportEnableLazyLoad"),
            "ResourcesCanAssignThemselvesToActivities": obj.get("ResourcesCanAssignThemselvesToActivities"),
            "ResourcesCanAssignThemselvesToActivitiesOutsideTheirOBSAccess": obj.get("ResourcesCanAssignThemselvesToActivitiesOutsideTheirOBSAccess"),
            "StartDayOfWeek": obj.get("StartDayOfWeek"),
            "SummarizeByCalendar": obj.get("SummarizeByCalendar"),
            "SummarizeByFinancialPeriods": obj.get("SummarizeByFinancialPeriods"),
            "SummaryResourceSpreadInterval": obj.get("SummaryResourceSpreadInterval"),
            "SummaryWBSSpreadInterval": obj.get("SummaryWBSSpreadInterval"),
            "TeamMemberConsentMessage": obj.get("TeamMemberConsentMessage"),
            "TeamMemberEnableConsent": obj.get("TeamMemberEnableConsent"),
            "TimeWindowCompletedActivities": obj.get("TimeWindowCompletedActivities"),
            "TimeWindowNotStartedActivities": obj.get("TimeWindowNotStartedActivities"),
            "TimesheetApprovalLevel": obj.get("TimesheetApprovalLevel"),
            "TimesheetDecimalDigits": obj.get("TimesheetDecimalDigits"),
            "TimesheetInterval": obj.get("TimesheetInterval"),
            "TimesheetPeriodEndsOnDay": obj.get("TimesheetPeriodEndsOnDay"),
            "TimesheetPeriodType": obj.get("TimesheetPeriodType"),
            "UnifierAuthCode": obj.get("UnifierAuthCode"),
            "UnifierCompanyShortName": obj.get("UnifierCompanyShortName"),
            "UnifierIntegrationPassword": obj.get("UnifierIntegrationPassword"),
            "UnifierIntegrationUserName": obj.get("UnifierIntegrationUserName"),
            "UnifierWebServiceURL": obj.get("UnifierWebServiceURL"),
            "UseCalendarTimePeriodsFlag": obj.get("UseCalendarTimePeriodsFlag"),
            "UseMaxTimesheetResourceHours": obj.get("UseMaxTimesheetResourceHours"),
            "UseProjectManagerApproval": obj.get("UseProjectManagerApproval"),
            "UseTimesheets": obj.get("UseTimesheets"),
            "VersionForWhatsNew": obj.get("VersionForWhatsNew"),
            "WBSCategoryLabel": obj.get("WBSCategoryLabel"),
            "WBSCodeSeparator": obj.get("WBSCodeSeparator"),
            "WeekAbbreviation": obj.get("WeekAbbreviation"),
            "YearAbbreviation": obj.get("YearAbbreviation")
        })
        return _obj

