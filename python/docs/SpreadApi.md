# openapi_client.SpreadApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_activity_spread**](SpreadApi.md#read_activity_spread) | **GET** /spread/activitySpread | ReadActivitySpread
[**read_cbs_resource_spread**](SpreadApi.md#read_cbs_resource_spread) | **GET** /spread/cbsExpenseSpread | ReadCBSExpenseSpread
[**read_cbs_resource_spread1**](SpreadApi.md#read_cbs_resource_spread1) | **GET** /spread/cbsResourceSpread | ReadCBSResourceSpread
[**read_eps_spread**](SpreadApi.md#read_eps_spread) | **GET** /spread/epsSpread | ReadEPSSpread
[**read_project_resource_spread**](SpreadApi.md#read_project_resource_spread) | **GET** /spread/projectResourceSpread | ReadProjectResourceSpread
[**read_project_role_spread**](SpreadApi.md#read_project_role_spread) | **GET** /spread/projectRoleSpread | ReadProjectRoleSpread
[**read_project_spread**](SpreadApi.md#read_project_spread) | **GET** /spread/projectSpread | ReadProjectSpread
[**read_resource_assignment_spread**](SpreadApi.md#read_resource_assignment_spread) | **GET** /spread/resourceAssignmentSpread | ReadResourceAssignmentSpread
[**read_wbs_expense_spread**](SpreadApi.md#read_wbs_expense_spread) | **GET** /spread/wbsExpenseSpread | ReadWBSExpenseSpread
[**read_wbs_resource_spread**](SpreadApi.md#read_wbs_resource_spread) | **GET** /spread/wbsResourceSpread | ReadWBSResourceSpread
[**read_wbs_role_spread**](SpreadApi.md#read_wbs_role_spread) | **GET** /spread/wbsRoleSpread | ReadWBSRoleSpread
[**read_wbs_spread**](SpreadApi.md#read_wbs_spread) | **GET** /spread/wbsSpread | ReadWBSSpread
[**update_resource_assignment_spread**](SpreadApi.md#update_resource_assignment_spread) | **PUT** /spread/resourceAssignmentSpread | Update ResourceAssignmentSpread


# **read_activity_spread**
> List[ReadActivitySpreadResponse] read_activity_spread(activity_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadActivitySpread

Reads the live activity spread data from the specified activities.

### Example


```python
import openapi_client
from openapi_client.models.read_activity_spread_response import ReadActivitySpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    activity_object_id = '4835,4845' # str | ActivityObjectId's to load
    period_type = 'WEEK' # str | PeriodType to load
    spread_field = 'ActualCost,ActualExpenseCost,ActualLaborCost,ActualLaborUnits,ActualMaterialCost,ActualNonLaborCost,ActualNonLaborUnits,ActualTotalCost,AtCompletionExpenseCost,AtCompletionLaborCost,AtCompletionLaborUnits,AtCompletionMaterialCost,AtCompletionNonLaborCost,AtCompletionNonLaborUnits,AtCompletionTotalCost,Baseline1ActualExpenseCost,Baseline1ActualLaborCost,Baseline1ActualLaborUnits,Baseline1ActualMaterialCost,Baseline1ActualNonLaborCost,Baseline1ActualNonLaborUnits,Baseline1ActualTotalCost,Baseline1PlannedExpenseCost,Baseline1PlannedLaborCost,Baseline1PlannedLaborUnits,Baseline1PlannedMaterialCost,Baseline1PlannedNonLaborCost,Baseline1PlannedNonLaborUnits,Baseline1PlannedTotalCost,BaselineActualExpenseCost,BaselineActualLaborCost,BaselineActualLaborUnits,BaselineActualMaterialCost,BaselineActualNonLaborCost,BaselineActualNonLaborUnits,BaselineActualTotalCost,BaselinePlannedExpenseCost,BaselinePlannedLaborCost,BaselinePlannedLaborUnits,BaselinePlannedMaterialCost,BaselinePlannedNonLaborCost,BaselinePlannedNonLaborUnits,BaselinePlannedTotalCost,EarnedValueCost,EarnedValueLaborUnits,EstimateAtCompletionCost,EstimateAtCompletionLaborUnits,EstimateToCompleteCost,EstimateToCompleteLaborUnits,PlannedExpenseCost,PlannedLaborCost,PlannedLaborUnits,PlannedMaterialCost,PlannedNonLaborCost,PlannedNonLaborUnits,PlannedTotalCost,PlannedValueCost,PlannedValueLaborUnits,RemainingExpenseCost,RemainingLaborCost,RemainingLaborUnits,RemainingLateExpenseCost,RemainingLateLaborCost,RemainingLateLaborUnits,RemainingLateMaterialCost,RemainingLateNonLaborCost,RemainingLateNonLaborUnits,RemainingLateTotalCost,RemainingMaterialCost,RemainingNonLaborCost,RemainingNonLaborUnits,RemainingTotalCost' # str | SpreadField's to load
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadActivitySpread
        api_response = api_instance.read_activity_spread(activity_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_activity_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_activity_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_object_id** | **str**| ActivityObjectId&#39;s to load | 
 **period_type** | **str**| PeriodType to load | 
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadActivitySpreadResponse]**](ReadActivitySpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cbs_resource_spread**
> List[ReadCBSExpenseSpreadResponse] read_cbs_resource_spread(spread_field, project_object_id=project_object_id, baseline_ids=baseline_ids, period_type=period_type, authorization=authorization)

ReadCBSExpenseSpread

Reads the summarized CBS spreads of the specified project resources

### Example


```python
import openapi_client
from openapi_client.models.read_cbs_expense_spread_response import ReadCBSExpenseSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    spread_field = 'ActualCost,ActualUnits,AtCompletionCost,AtCompletionUnits,PlannedCost,PlannedUnits,RemainingCost,RemainingUnits' # str | SpreadField's to load
    project_object_id = '4835,4845' # str | ProjectObjectId's to load (optional)
    baseline_ids = '7027,7037' # str | BaselineIds's to load (optional)
    period_type = 'WEEK' # str | PeriodType to load (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadCBSExpenseSpread
        api_response = api_instance.read_cbs_resource_spread(spread_field, project_object_id=project_object_id, baseline_ids=baseline_ids, period_type=period_type, authorization=authorization)
        print("The response of SpreadApi->read_cbs_resource_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_cbs_resource_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **project_object_id** | **str**| ProjectObjectId&#39;s to load | [optional] 
 **baseline_ids** | **str**| BaselineIds&#39;s to load | [optional] 
 **period_type** | **str**| PeriodType to load | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadCBSExpenseSpreadResponse]**](ReadCBSExpenseSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cbs_resource_spread1**
> List[ReadCBSResourceSpreadResponse] read_cbs_resource_spread1(spread_field, project_object_id=project_object_id, baseline_ids=baseline_ids, period_type=period_type, summary_date_field=summary_date_field, authorization=authorization)

ReadCBSResourceSpread

Reads the summarized CBS spreads of the specified Project Resources

### Example


```python
import openapi_client
from openapi_client.models.read_cbs_resource_spread_response import ReadCBSResourceSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    spread_field = 'ActualCost,ActualUnits,AtCompletionCost,AtCompletionUnits,PlannedCost,PlannedUnits,RemainingCost,RemainingUnits' # str | SpreadField's to load
    project_object_id = '4835,4845' # str | ProjectObjectId's to load (optional)
    baseline_ids = '7027,7037' # str | BaselineIds's to load (optional)
    period_type = 'WEEK' # str | PeriodType to load (optional)
    summary_date_field = 'summary_date_field_example' # str | SummaryDateField (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadCBSResourceSpread
        api_response = api_instance.read_cbs_resource_spread1(spread_field, project_object_id=project_object_id, baseline_ids=baseline_ids, period_type=period_type, summary_date_field=summary_date_field, authorization=authorization)
        print("The response of SpreadApi->read_cbs_resource_spread1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_cbs_resource_spread1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **project_object_id** | **str**| ProjectObjectId&#39;s to load | [optional] 
 **baseline_ids** | **str**| BaselineIds&#39;s to load | [optional] 
 **period_type** | **str**| PeriodType to load | [optional] 
 **summary_date_field** | **str**| SummaryDateField | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadCBSResourceSpreadResponse]**](ReadCBSResourceSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_eps_spread**
> List[ReadEPSSpreadResponse] read_eps_spread(eps_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadEPSSpread

Reads the summarized spread data from the specified EPS objects.

### Example


```python
import openapi_client
from openapi_client.models.read_eps_spread_response import ReadEPSSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    eps_object_id = '4835,4845' # str | EPSObjectId's to load
    period_type = 'WEEK' # str | PeriodType to load
    spread_field = 'ActualCost,ActualExpenseCost,ActualLaborCost,ActualLaborUnits,ActualMaterialCost,ActualNonlaborCost,ActualNonlaborUnits,ActualTotalCost,AtCompletionExpenseCost,AtCompletionLaborCost,AtCompletionLaborUnits,AtCompletionMaterialCost,AtCompletionNonlaborCost,AtCompletionNonlaborUnits,AtCompletionTotalCost,BaselinePlannedExpenseCost,BaselinePlannedLaborCost,BaselinePlannedLaborUnits,BaselinePlannedMaterialCost,BaselinePlannedNonlaborCost,BaselinePlannedNonlaborUnits,BaselinePlannedTotalCost,EarnedValueCost,EarnedValueLaborUnits,EstimateAtCompletionCost,EstimateAtCompletionLaborUnits,EstimateToCompleteCost,EstimateToCompleteLaborUnits,PeriodActualCost,PeriodActualExpenseCost,PeriodActualLaborCost,PeriodActualLaborUnits,PeriodActualMaterialCost,PeriodActualNonLaborCost,PeriodActualNonLaborUnits,PeriodAtCompletionExpenseCost,PeriodAtCompletionLaborCost,PeriodAtCompletionLaborUnits,PeriodAtCompletionMaterialCost,PeriodAtCompletionNonLaborCost,PeriodAtCompletionNonLaborUnits,PeriodAtCompletionTotalCost,PeriodEarnedValueCost,PeriodEarnedValueLaborUnits,PeriodEstimateAtCompletionCost,PeriodEstimateAtCompletionLaborUnits,PeriodPlannedValueCost,PeriodPlannedValueLaborUnits,PlannedExpenseCost,PlannedLaborCost,PlannedLaborUnits,PlannedMaterialCost,PlannedNonlaborCost,PlannedNonlaborUnits,PlannedTotalCost,PlannedValueCost,PlannedValueLaborUnits,RemainingExpenseCost,RemainingLaborCost,RemainingLaborUnits,RemainingLateExpenseCost,RemainingLateLaborCost,RemainingLateLaborUnits,RemainingLateMaterialCost,RemainingLateNonlaborCost,RemainingLateNonlaborUnits,RemainingLateTotalCost,RemainingMaterialCost,RemainingNonlaborCost,RemainingNonlaborUnits,RemainingTotalCost' # str | SpreadField's to load
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadEPSSpread
        api_response = api_instance.read_eps_spread(eps_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_eps_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_eps_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_object_id** | **str**| EPSObjectId&#39;s to load | 
 **period_type** | **str**| PeriodType to load | 
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadEPSSpreadResponse]**](ReadEPSSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_resource_spread**
> List[ReadProjectResourceSpreadResponse] read_project_resource_spread(spread_field, project_object_id=project_object_id, resource_object_id=resource_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadProjectResourceSpread

Reads the summarized spreads of the specified Project Resources

### Example


```python
import openapi_client
from openapi_client.models.read_project_resource_spread_response import ReadProjectResourceSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    spread_field = 'ActualCost,ActualOvertimeCost,ActualOvertimeUnits,ActualRegularCost,ActualRegularUnits,ActualUnits,AtCompletionCost,AtCompletionUnits,Limit,PeriodActualCost,PeriodActualUnits,PeriodAtCompletionCost,PeriodAtCompletionUnits,PlannedCost,PlannedUnits,RemainingCost,RemainingLateCost,RemainingLateUnits,RemainingUnits,StaffedActualCost,StaffedActualOvertimeCost,StaffedActualOvertimeUnits,StaffedActualRegularCost,StaffedActualRegularUnits,StaffedActualUnits,StaffedAtCompletionCost,StaffedAtCompletionUnits,StaffedPlannedCost,StaffedPlannedUnits,StaffedRemainingCost,StaffedRemainingLateCost,StaffedRemainingLateUnits,StaffedRemainingUnits,UnstaffedActualCost,UnstaffedActualOvertimeCost,UnstaffedActualOvertimeUnits,UnstaffedActualRegularCost,UnstaffedActualRegularUnits,UnstaffedActualUnits,UnstaffedAtCompletionCost,UnstaffedAtCompletionUnits,UnstaffedPlannedCost,UnstaffedPlannedUnits,UnstaffedRemainingCost,UnstaffedRemainingLateCost,UnstaffedRemainingLateUnits,UnstaffedRemainingUnits' # str | SpreadField's to load
    project_object_id = '4835,4845' # str | ProjectObjectId's to load (optional)
    resource_object_id = '7027,7037' # str | ResourceObjectId's to load (optional)
    period_type = 'WEEK' # str | PeriodType to load (optional)
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadProjectResourceSpread
        api_response = api_instance.read_project_resource_spread(spread_field, project_object_id=project_object_id, resource_object_id=resource_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_project_resource_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_project_resource_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **project_object_id** | **str**| ProjectObjectId&#39;s to load | [optional] 
 **resource_object_id** | **str**| ResourceObjectId&#39;s to load | [optional] 
 **period_type** | **str**| PeriodType to load | [optional] 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadProjectResourceSpreadResponse]**](ReadProjectResourceSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_role_spread**
> List[ReadProjectRoleSpreadResponse] read_project_role_spread(spread_field, project_object_id=project_object_id, role_object_id=role_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadProjectRoleSpread

Reads the spreads of the specified role assignments to the activities from the specified projects.

### Example


```python
import openapi_client
from openapi_client.models.read_project_role_spread_response import ReadProjectRoleSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    spread_field = 'ActualCost,ActualOvertimeCost,ActualOvertimeUnits,ActualRegularCost,ActualRegularUnits,ActualUnits,AtCompletionCost,AtCompletionUnits,Limit,PeriodActualCost,PeriodActualUnits,PeriodAtCompletionCost,PeriodAtCompletionUnits,PlannedCost,PlannedUnits,RemainingCost,RemainingLateCost,RemainingLateUnits,RemainingUnits,StaffedActualCost,StaffedActualOvertimeCost,StaffedActualOvertimeUnits,StaffedActualRegularCost,StaffedActualRegularUnits,StaffedActualUnits,StaffedAtCompletionCost,StaffedAtCompletionUnits,StaffedPlannedCost,StaffedPlannedUnits,StaffedRemainingCost,StaffedRemainingLateCost,StaffedRemainingLateUnits,StaffedRemainingUnits,UnstaffedActualCost,UnstaffedActualOvertimeCost,UnstaffedActualOvertimeUnits,UnstaffedActualRegularCost,UnstaffedActualRegularUnits,UnstaffedActualUnits,UnstaffedAtCompletionCost,UnstaffedAtCompletionUnits,UnstaffedPlannedCost,UnstaffedPlannedUnits,UnstaffedRemainingCost,UnstaffedRemainingLateCost,UnstaffedRemainingLateUnits,UnstaffedRemainingUnits' # str | SpreadField's to load
    project_object_id = '4835,4845' # str | ProjectObjectId's to load (optional)
    role_object_id = '7027,7037' # str | RoleObjectId's to load (optional)
    period_type = 'WEEK' # str | PeriodType to load (optional)
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadProjectRoleSpread
        api_response = api_instance.read_project_role_spread(spread_field, project_object_id=project_object_id, role_object_id=role_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_project_role_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_project_role_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **project_object_id** | **str**| ProjectObjectId&#39;s to load | [optional] 
 **role_object_id** | **str**| RoleObjectId&#39;s to load | [optional] 
 **period_type** | **str**| PeriodType to load | [optional] 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadProjectRoleSpreadResponse]**](ReadProjectRoleSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_spread**
> List[ReadProjectSpreadResponse] read_project_spread(project_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadProjectSpread

Reads the summarized spreads for the specified projects.

### Example


```python
import openapi_client
from openapi_client.models.read_project_spread_response import ReadProjectSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    project_object_id = '4835,4845' # str | ProjectObjectId's to load
    period_type = 'WEEK' # str | PeriodType to load
    spread_field = 'ActualCost,ActualExpenseCost,ActualLaborCost,ActualLaborUnits,ActualMaterialCost,ActualNonlaborCost,ActualNonlaborUnits,ActualTotalCost,AtCompletionExpenseCost,AtCompletionLaborCost,AtCompletionLaborUnits,AtCompletionMaterialCost,AtCompletionNonlaborCost,AtCompletionNonlaborUnits,AtCompletionTotalCost,BaselinePlannedExpenseCost,BaselinePlannedLaborCost,BaselinePlannedLaborUnits,BaselinePlannedMaterialCost,BaselinePlannedNonlaborCost,BaselinePlannedNonlaborUnits,BaselinePlannedTotalCost,EarnedValueCost,EarnedValueLaborUnits,EstimateAtCompletionCost,EstimateAtCompletionLaborUnits,EstimateToCompleteCost,EstimateToCompleteLaborUnits,PeriodActualCost,PeriodActualExpenseCost,PeriodActualLaborCost,PeriodActualLaborUnits,PeriodActualMaterialCost,PeriodActualNonLaborCost,PeriodActualNonLaborUnits,PeriodAtCompletionExpenseCost,PeriodAtCompletionLaborCost,PeriodAtCompletionLaborUnits,PeriodAtCompletionMaterialCost,PeriodAtCompletionNonLaborCost,PeriodAtCompletionNonLaborUnits,PeriodAtCompletionTotalCost,PeriodEarnedValueCost,PeriodEarnedValueLaborUnits,PeriodEstimateAtCompletionCost,PeriodEstimateAtCompletionLaborUnits,PeriodPlannedValueCost,PeriodPlannedValueLaborUnits,PlannedExpenseCost,PlannedLaborCost,PlannedLaborUnits,PlannedMaterialCost,PlannedNonlaborCost,PlannedNonlaborUnits,PlannedTotalCost,PlannedValueCost,PlannedValueLaborUnits,RemainingExpenseCost,RemainingLaborCost,RemainingLaborUnits,RemainingLateExpenseCost,RemainingLateLaborCost,RemainingLateLaborUnits,RemainingLateMaterialCost,RemainingLateNonlaborCost,RemainingLateNonlaborUnits,RemainingLateTotalCost,RemainingMaterialCost,RemainingNonlaborCost,RemainingNonlaborUnits,RemainingTotalCost' # str | SpreadField's to load
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadProjectSpread
        api_response = api_instance.read_project_spread(project_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_project_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_project_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_object_id** | **str**| ProjectObjectId&#39;s to load | 
 **period_type** | **str**| PeriodType to load | 
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadProjectSpreadResponse]**](ReadProjectSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_resource_assignment_spread**
> List[ReadResourceAssignmentSpreadResponse] read_resource_assignment_spread(resource_assignment_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadResourceAssignmentSpread

Reads the live resource assignment spread data from the specified resource assignment.

### Example


```python
import openapi_client
from openapi_client.models.read_resource_assignment_spread_response import ReadResourceAssignmentSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    resource_assignment_object_id = '4835,4845' # str | ResourceAssignmentObjectId's to load
    period_type = 'WEEK' # str | PeriodType to load
    spread_field = 'ActualCost,ActualOvertimeCost,ActualOvertimeUnits,ActualRegularCost,ActualRegularUnits,ActualUnits,AtCompletionCost,AtCompletionUnits,PlannedCost,PlannedUnits,RemainingCost,RemainingLateCost,RemainingLateUnits,RemainingUnits,StaffedRemainingCost,StaffedRemainingLateCost,StaffedRemainingLateUnits,StaffedRemainingUnits,UnstaffedRemainingCost,UnstaffedRemainingLateCost,UnstaffedRemainingLateUnits,UnstaffedRemainingUnits,PeriodActualCost,PeriodActualUnits,PeriodAtCompletionCost,PeriodAtCompletionUnits' # str | SpreadField's to load
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadResourceAssignmentSpread
        api_response = api_instance.read_resource_assignment_spread(resource_assignment_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_resource_assignment_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_resource_assignment_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_object_id** | **str**| ResourceAssignmentObjectId&#39;s to load | 
 **period_type** | **str**| PeriodType to load | 
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadResourceAssignmentSpreadResponse]**](ReadResourceAssignmentSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_wbs_expense_spread**
> List[ReadWBSExpenseSpreadResponse] read_wbs_expense_spread(spread_field, wbs_object_id=wbs_object_id, expense_category_object_id=expense_category_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadWBSExpenseSpread

Reads the summarized WBS spreads of the specified project resources

### Example


```python
import openapi_client
from openapi_client.models.read_wbs_expense_spread_response import ReadWBSExpenseSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    spread_field = 'ActualCost,AtCompletionCost,PlannedCost,RemainingCost' # str | SpreadField's to load
    wbs_object_id = '4835,4845' # str | WBSObjectId's to load (optional)
    expense_category_object_id = '7027,7037' # str | ExpenseCategoryObjectId's to load (optional)
    period_type = 'WEEK' # str | PeriodType to load (optional)
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadWBSExpenseSpread
        api_response = api_instance.read_wbs_expense_spread(spread_field, wbs_object_id=wbs_object_id, expense_category_object_id=expense_category_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_wbs_expense_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_wbs_expense_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **wbs_object_id** | **str**| WBSObjectId&#39;s to load | [optional] 
 **expense_category_object_id** | **str**| ExpenseCategoryObjectId&#39;s to load | [optional] 
 **period_type** | **str**| PeriodType to load | [optional] 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadWBSExpenseSpreadResponse]**](ReadWBSExpenseSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_wbs_resource_spread**
> List[ReadWBSResourceSpreadResponse] read_wbs_resource_spread(spread_field, wbs_object_id=wbs_object_id, resource_object_id=resource_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadWBSResourceSpread

Reads the summarized spreads of the Resources for the specified WBS.

### Example


```python
import openapi_client
from openapi_client.models.read_wbs_resource_spread_response import ReadWBSResourceSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    spread_field = 'ActualCost,ActualOvertimeCost,ActualOvertimeUnits,ActualRegularCost,ActualRegularUnits,ActualUnits,AtCompletionCost,AtCompletionUnits,Limit,PeriodActualCost,PeriodActualUnits,PeriodAtCompletionCost,PeriodAtCompletionUnits,PlannedCost,PlannedUnits,RemainingCost,RemainingLateCost,RemainingLateUnits,RemainingUnits,StaffedActualCost,StaffedActualOvertimeCost,StaffedActualOvertimeUnits,StaffedActualRegularCost,StaffedActualRegularUnits,StaffedActualUnits,StaffedAtCompletionCost,StaffedAtCompletionUnits,StaffedPlannedCost,StaffedPlannedUnits,StaffedRemainingCost,StaffedRemainingLateCost,StaffedRemainingLateUnits,StaffedRemainingUnits,UnstaffedActualCost,UnstaffedActualOvertimeCost,UnstaffedActualOvertimeUnits,UnstaffedActualRegularCost,UnstaffedActualRegularUnits,UnstaffedActualUnits,UnstaffedAtCompletionCost,UnstaffedAtCompletionUnits,UnstaffedPlannedCost,UnstaffedPlannedUnits,UnstaffedRemainingCost,UnstaffedRemainingLateCost,UnstaffedRemainingLateUnits,UnstaffedRemainingUnits' # str | SpreadField's to load
    wbs_object_id = '4835,4845' # str | WBSObjectId's to load (optional)
    resource_object_id = '7027,7037' # str | ResourceObjectId's to load (optional)
    period_type = 'WEEK' # str | PeriodType to load (optional)
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadWBSResourceSpread
        api_response = api_instance.read_wbs_resource_spread(spread_field, wbs_object_id=wbs_object_id, resource_object_id=resource_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_wbs_resource_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_wbs_resource_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **wbs_object_id** | **str**| WBSObjectId&#39;s to load | [optional] 
 **resource_object_id** | **str**| ResourceObjectId&#39;s to load | [optional] 
 **period_type** | **str**| PeriodType to load | [optional] 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadWBSResourceSpreadResponse]**](ReadWBSResourceSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_wbs_role_spread**
> List[ReadWBSRoleSpreadResponse] read_wbs_role_spread(spread_field, wbs_object_id=wbs_object_id, role_object_id=role_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadWBSRoleSpread

Reads the spreads of the specified role assignments to the activities from the specified WBS.

### Example


```python
import openapi_client
from openapi_client.models.read_wbs_role_spread_response import ReadWBSRoleSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    spread_field = 'ActualCost,ActualOvertimeCost,ActualOvertimeUnits,ActualRegularCost,ActualRegularUnits,ActualUnits,AtCompletionCost,AtCompletionUnits,Limit,PeriodActualCost,PeriodActualUnits,PeriodAtCompletionCost,PeriodAtCompletionUnits,PlannedCost,PlannedUnitsRemainingCost,RemainingLateCost,RemainingLateUnits,RemainingUnits,StaffedActualCost,StaffedActualOvertimeCost,StaffedActualOvertimeUnits,StaffedActualRegularCost,StaffedActualRegularUnits,StaffedActualUnits,StaffedAtCompletionCost,StaffedAtCompletionUnits,StaffedPlannedCost,StaffedPlannedUnits,StaffedRemainingCost,StaffedRemainingLateCost,StaffedRemainingLateUnits,StaffedRemainingUnits,UnstaffedActualCost,UnstaffedActualOvertimeCost,UnstaffedActualOvertimeUnits,UnstaffedActualRegularCost,UnstaffedActualRegularUnits,UnstaffedActualUnits,UnstaffedAtCompletionCost,UnstaffedAtCompletionUnits,UnstaffedPlannedCost,UnstaffedPlannedUnits,UnstaffedRemainingCost,UnstaffedRemainingLateCost,UnstaffedRemainingLateUnits,UnstaffedRemainingUnits' # str | SpreadField's to load
    wbs_object_id = '4835,4845' # str | WBSObjectId's to load (optional)
    role_object_id = '7027,7037' # str | RoleObjectId's to load (optional)
    period_type = 'WEEK' # str | PeriodType to load (optional)
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadWBSRoleSpread
        api_response = api_instance.read_wbs_role_spread(spread_field, wbs_object_id=wbs_object_id, role_object_id=role_object_id, period_type=period_type, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_wbs_role_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_wbs_role_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **wbs_object_id** | **str**| WBSObjectId&#39;s to load | [optional] 
 **role_object_id** | **str**| RoleObjectId&#39;s to load | [optional] 
 **period_type** | **str**| PeriodType to load | [optional] 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadWBSRoleSpreadResponse]**](ReadWBSRoleSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_wbs_spread**
> List[ReadWBSSpreadResponse] read_wbs_spread(wbs_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)

ReadWBSSpread

Reads the summarized WBS spread data for the specified WBS spread.

### Example


```python
import openapi_client
from openapi_client.models.read_wbs_spread_response import ReadWBSSpreadResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    wbs_object_id = '12345,89656' # str | WBSObjectId's to load
    period_type = 'WEEK' # str | PeriodType to load
    spread_field = 'ActualCost,ActualExpenseCost,ActualLaborCost,ActualLaborUnits,ActualMaterialCost,ActualNonlaborCost,ActualNonlaborUnits,ActualTotalCost,AtCompletionExpenseCost,AtCompletionLaborCost,AtCompletionLaborUnits,AtCompletionMaterialCost,AtCompletionNonlaborCost,AtCompletionNonlaborUnits,AtCompletionTotalCost,BaselinePlannedExpenseCost,BaselinePlannedLaborCost,BaselinePlannedLaborUnits,BaselinePlannedMaterialCost,BaselinePlannedNonlaborCost,BaselinePlannedNonlaborUnits,BaselinePlannedTotalCost,EarnedValueCost,EarnedValueLaborUnits,EstimateAtCompletionCost,EstimateAtCompletionLaborUnits,EstimateToCompleteCost,EstimateToCompleteLaborUnits,PeriodActualCost,PeriodActualExpenseCost,PeriodActualLaborCost,PeriodActualLaborUnits,PeriodActualMaterialCost,PeriodActualNonLaborCost,PeriodActualNonLaborUnits,PeriodAtCompletionExpenseCost,PeriodAtCompletionLaborCost,PeriodAtCompletionLaborUnits,PeriodAtCompletionMaterialCost,PeriodAtCompletionNonLaborCost,PeriodAtCompletionNonLaborUnits,PeriodAtCompletionTotalCost,PeriodEarnedValueCost,PeriodEarnedValueLaborUnits,PeriodEstimateAtCompletionCost,PeriodEstimateAtCompletionLaborUnits,PeriodPlannedValueCost,PeriodPlannedValueLaborUnits,PlannedExpenseCost,PlannedLaborCost,PlannedLaborUnits,PlannedMaterialCost,PlannedNonlaborCost,PlannedNonlaborUnits,PlannedTotalCost,PlannedValueCost,PlannedValueLaborUnits,RemainingExpenseCost,RemainingLaborCost,RemainingLaborUnits,RemainingLateExpenseCost,RemainingLateLaborCost,RemainingLateLaborUnits,RemainingLateMaterialCost,RemainingLateNonlaborCost,RemainingLateNonlaborUnits,RemainingLateTotalCost,RemainingMaterialCost,RemainingNonlaborCost,RemainingNonlaborUnits,RemainingTotalCost' # str | SpreadField's to load
    start_date = 'start_date_example' # str | StartDate (optional)
    end_date = 'end_date_example' # str | EndDate (optional)
    include_cumulative = 'include_cumulative_example' # str | IncludeCumulative to load : Supported values - true, false (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadWBSSpread
        api_response = api_instance.read_wbs_spread(wbs_object_id, period_type, spread_field, start_date=start_date, end_date=end_date, include_cumulative=include_cumulative, authorization=authorization)
        print("The response of SpreadApi->read_wbs_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->read_wbs_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wbs_object_id** | **str**| WBSObjectId&#39;s to load | 
 **period_type** | **str**| PeriodType to load | 
 **spread_field** | **str**| SpreadField&#39;s to load | 
 **start_date** | **str**| StartDate | [optional] 
 **end_date** | **str**| EndDate | [optional] 
 **include_cumulative** | **str**| IncludeCumulative to load : Supported values - true, false | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ReadWBSSpreadResponse]**](ReadWBSSpreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_assignment_spread**
> bool update_resource_assignment_spread(update_resource_assignment_spread, authorization=authorization)

Update ResourceAssignmentSpread

Send a request to this endpoint to update one or more ResourceAssignmentSpread. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpreadApi(api_client)
    update_resource_assignment_spread = {'key': openapi_client.UpdateResourceAssignmentSpread()} # UpdateResourceAssignmentSpread | ResourceAssignmentSpread object.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceAssignmentSpread
        api_response = api_instance.update_resource_assignment_spread(update_resource_assignment_spread, authorization=authorization)
        print("The response of SpreadApi->update_resource_assignment_spread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadApi->update_resource_assignment_spread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_resource_assignment_spread** | [**UpdateResourceAssignmentSpread**](UpdateResourceAssignmentSpread.md)| ResourceAssignmentSpread object. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

