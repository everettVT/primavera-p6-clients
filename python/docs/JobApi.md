# openapi_client.JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_actual**](JobApi.md#apply_actual) | **POST** /job/applyActuals | Apply Actual
[**cancel_job**](JobApi.md#cancel_job) | **POST** /job/cancelJob | CancelJob
[**get_current_jobs**](JobApi.md#get_current_jobs) | **POST** /job/getCurrentJobs | GetCurrentJobs
[**level**](JobApi.md#level) | **POST** /job/level | Leveling Project
[**read_job_log**](JobApi.md#read_job_log) | **POST** /job/readJobLog | ReadJobLog
[**read_job_status**](JobApi.md#read_job_status) | **POST** /job/readJobStatus | ReadJobStatus
[**recalculate_assignment_costs**](JobApi.md#recalculate_assignment_costs) | **POST** /job/recalculateAssignmentCosts | RecalculateAssignmentCosts
[**schedule**](JobApi.md#schedule) | **POST** /job/schedule | Schedule Project
[**schedule1**](JobApi.md#schedule1) | **POST** /job/updateBaseline | Update Baseline
[**send_to_unifier**](JobApi.md#send_to_unifier) | **POST** /job/scheduleCheck | ScheduleCheck
[**send_to_unifier1**](JobApi.md#send_to_unifier1) | **POST** /job/sendToUnifier | SendToUnifier
[**store_period_performance**](JobApi.md#store_period_performance) | **POST** /job/storePeriodPerformance | StorePeriodPerformance
[**summarize_eps**](JobApi.md#summarize_eps) | **POST** /job/summarizeCBS | Summarize CBS
[**summarize_eps1**](JobApi.md#summarize_eps1) | **POST** /job/summarizeEPS | Summarize EPS
[**summarize_project**](JobApi.md#summarize_project) | **POST** /job/summarizeProject | Summarize Project


# **apply_actual**
> JobServiceResponse apply_actual(apply_actuals, authorization=authorization)

Apply Actual

Asynchronously applies actuals to a project.

### Example


```python
import openapi_client
from openapi_client.models.apply_actuals import ApplyActuals
from openapi_client.models.job_service_response import JobServiceResponse
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
    api_instance = openapi_client.JobApi(api_client)
    apply_actuals = [openapi_client.ApplyActuals()] # List[ApplyActuals] | A list of project objects 
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Apply Actual
        api_response = api_instance.apply_actual(apply_actuals, authorization=authorization)
        print("The response of JobApi->apply_actual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->apply_actual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_actuals** | [**List[ApplyActuals]**](ApplyActuals.md)| A list of project objects  | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_job**
> JobServiceResponse cancel_job(cancel_job, authorization=authorization)

CancelJob

Cancels an asynchronous job initiated by P6 EPPM Web Services or the P6 Integration API.

### Example


```python
import openapi_client
from openapi_client.models.cancel_job import CancelJob
from openapi_client.models.job_service_response import JobServiceResponse
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
    api_instance = openapi_client.JobApi(api_client)
    cancel_job = [openapi_client.CancelJob()] # List[CancelJob] | A list of project objects for recalculateAssignmentCosts service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # CancelJob
        api_response = api_instance.cancel_job(cancel_job, authorization=authorization)
        print("The response of JobApi->cancel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_job** | [**List[CancelJob]**](CancelJob.md)| A list of project objects for recalculateAssignmentCosts service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_jobs**
> CurrentJobResponse get_current_jobs(request_body, authorization=authorization)

GetCurrentJobs

Retrieves job information for current asynchronous jobs of this user.

### Example


```python
import openapi_client
from openapi_client.models.current_job_response import CurrentJobResponse
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
    api_instance = openapi_client.JobApi(api_client)
    request_body = ['request_body_example'] # List[str] | A list of project objects for recalculateAssignmentCosts service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # GetCurrentJobs
        api_response = api_instance.get_current_jobs(request_body, authorization=authorization)
        print("The response of JobApi->get_current_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_current_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| A list of project objects for recalculateAssignmentCosts service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CurrentJobResponse**](CurrentJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **level**
> JobServiceResponse level(level, authorization=authorization)

Leveling Project

 Asynchronously levels a project. Resource leveling is a process that helps you identify overallocated resources. Then you can reassign work to other resources if necessary to ensure that sufficient resources are available to perform the activities in your project according to the plan.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.level import Level
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
    api_instance = openapi_client.JobApi(api_client)
    level = [openapi_client.Level()] # List[Level] | A list of project objects for Level service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Leveling Project
        api_response = api_instance.level(level, authorization=authorization)
        print("The response of JobApi->level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**List[Level]**](Level.md)| A list of project objects for Level service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_job_log**
> ReadJobLogResponse read_job_log(read_job_log, authorization=authorization)

ReadJobLog

Retrieves the log of an asynchronous job initiated by P6 EPPM Web Services or the Integration API.

### Example


```python
import openapi_client
from openapi_client.models.read_job_log import ReadJobLog
from openapi_client.models.read_job_log_response import ReadJobLogResponse
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
    api_instance = openapi_client.JobApi(api_client)
    read_job_log = [openapi_client.ReadJobLog()] # List[ReadJobLog] | A list of project objects for recalculateAssignmentCosts service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadJobLog
        api_response = api_instance.read_job_log(read_job_log, authorization=authorization)
        print("The response of JobApi->read_job_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->read_job_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_job_log** | [**List[ReadJobLog]**](ReadJobLog.md)| A list of project objects for recalculateAssignmentCosts service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**ReadJobLogResponse**](ReadJobLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_job_status**
> ReadJobLogResponse read_job_status(read_job_status_response, authorization=authorization)

ReadJobStatus

Retrieves the status of an asynchronous job initiated by P6 EPPM Web Services or the Integration API.

### Example


```python
import openapi_client
from openapi_client.models.read_job_log_response import ReadJobLogResponse
from openapi_client.models.read_job_status_response import ReadJobStatusResponse
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
    api_instance = openapi_client.JobApi(api_client)
    read_job_status_response = [openapi_client.ReadJobStatusResponse()] # List[ReadJobStatusResponse] | 
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ReadJobStatus
        api_response = api_instance.read_job_status(read_job_status_response, authorization=authorization)
        print("The response of JobApi->read_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->read_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_job_status_response** | [**List[ReadJobStatusResponse]**](ReadJobStatusResponse.md)|  | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**ReadJobLogResponse**](ReadJobLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_assignment_costs**
> JobServiceResponse recalculate_assignment_costs(recalculate_assignment_costs, authorization=authorization)

RecalculateAssignmentCosts

Asynchronously updates the resource and role assignment costs for the activities in the specified project.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.recalculate_assignment_costs import RecalculateAssignmentCosts
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
    api_instance = openapi_client.JobApi(api_client)
    recalculate_assignment_costs = [openapi_client.RecalculateAssignmentCosts()] # List[RecalculateAssignmentCosts] | A list of project objects for recalculateAssignmentCosts service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # RecalculateAssignmentCosts
        api_response = api_instance.recalculate_assignment_costs(recalculate_assignment_costs, authorization=authorization)
        print("The response of JobApi->recalculate_assignment_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->recalculate_assignment_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recalculate_assignment_costs** | [**List[RecalculateAssignmentCosts]**](RecalculateAssignmentCosts.md)| A list of project objects for recalculateAssignmentCosts service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule**
> JobServiceResponse schedule(schedule, authorization=authorization)

Schedule Project

Asynchronously schedules a project.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.schedule import Schedule
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
    api_instance = openapi_client.JobApi(api_client)
    schedule = [openapi_client.Schedule()] # List[Schedule] | A list of project objects for Schedule service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Schedule Project
        api_response = api_instance.schedule(schedule, authorization=authorization)
        print("The response of JobApi->schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**List[Schedule]**](Schedule.md)| A list of project objects for Schedule service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule1**
> JobServiceResponse schedule1(update_baseline, authorization=authorization)

Update Baseline

Updates the baseline of a project.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.update_baseline import UpdateBaseline
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
    api_instance = openapi_client.JobApi(api_client)
    update_baseline = [openapi_client.UpdateBaseline()] # List[UpdateBaseline] | A list of project objects for Schedule service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update Baseline
        api_response = api_instance.schedule1(update_baseline, authorization=authorization)
        print("The response of JobApi->schedule1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->schedule1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_baseline** | [**List[UpdateBaseline]**](UpdateBaseline.md)| A list of project objects for Schedule service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_to_unifier**
> JobServiceResponse send_to_unifier(schedule_check, authorization=authorization)

ScheduleCheck

Starts the Check Schedule job service on a project.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.schedule_check import ScheduleCheck
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
    api_instance = openapi_client.JobApi(api_client)
    schedule_check = [openapi_client.ScheduleCheck()] # List[ScheduleCheck] | 
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # ScheduleCheck
        api_response = api_instance.send_to_unifier(schedule_check, authorization=authorization)
        print("The response of JobApi->send_to_unifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->send_to_unifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_check** | [**List[ScheduleCheck]**](ScheduleCheck.md)|  | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_to_unifier1**
> JobServiceResponse send_to_unifier1(send_to_unifier, authorization=authorization)

SendToUnifier

Asynchronously summarizes a project.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.send_to_unifier import SendToUnifier
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
    api_instance = openapi_client.JobApi(api_client)
    send_to_unifier = [openapi_client.SendToUnifier()] # List[SendToUnifier] | A list of project that you want to send to Primavera Unifier.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # SendToUnifier
        api_response = api_instance.send_to_unifier1(send_to_unifier, authorization=authorization)
        print("The response of JobApi->send_to_unifier1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->send_to_unifier1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_to_unifier** | [**List[SendToUnifier]**](SendToUnifier.md)| A list of project that you want to send to Primavera Unifier. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_period_performance**
> JobServiceResponse store_period_performance(store_period_performance, authorization=authorization)

StorePeriodPerformance

Asynchronously stores period performance for a single project.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.store_period_performance import StorePeriodPerformance
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
    api_instance = openapi_client.JobApi(api_client)
    store_period_performance = [openapi_client.StorePeriodPerformance()] # List[StorePeriodPerformance] | A list of project objects for recalculateAssignmentCosts service
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # StorePeriodPerformance
        api_response = api_instance.store_period_performance(store_period_performance, authorization=authorization)
        print("The response of JobApi->store_period_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->store_period_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_period_performance** | [**List[StorePeriodPerformance]**](StorePeriodPerformance.md)| A list of project objects for recalculateAssignmentCosts service | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summarize_eps**
> JobServiceResponse summarize_eps(summarize_cbs, authorization=authorization)

Summarize CBS

 Asynchronously summarizes a EPS.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.summarize_cbs import SummarizeCBS
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
    api_instance = openapi_client.JobApi(api_client)
    summarize_cbs = [openapi_client.SummarizeCBS()] # List[SummarizeCBS] | A list of summarise EPS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Summarize CBS
        api_response = api_instance.summarize_eps(summarize_cbs, authorization=authorization)
        print("The response of JobApi->summarize_eps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->summarize_eps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarize_cbs** | [**List[SummarizeCBS]**](SummarizeCBS.md)| A list of summarise EPS objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summarize_eps1**
> JobServiceResponse summarize_eps1(summarize_eps, authorization=authorization)

Summarize EPS

 Asynchronously summarizes a EPS.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.summarize_eps import SummarizeEPS
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
    api_instance = openapi_client.JobApi(api_client)
    summarize_eps = [openapi_client.SummarizeEPS()] # List[SummarizeEPS] | A list of summarise EPS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Summarize EPS
        api_response = api_instance.summarize_eps1(summarize_eps, authorization=authorization)
        print("The response of JobApi->summarize_eps1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->summarize_eps1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarize_eps** | [**List[SummarizeEPS]**](SummarizeEPS.md)| A list of summarise EPS objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summarize_project**
> JobServiceResponse summarize_project(summarize_project, authorization=authorization)

Summarize Project

 Asynchronously summarizes a project.

### Example


```python
import openapi_client
from openapi_client.models.job_service_response import JobServiceResponse
from openapi_client.models.summarize_project import SummarizeProject
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
    api_instance = openapi_client.JobApi(api_client)
    summarize_project = [openapi_client.SummarizeProject()] # List[SummarizeProject] | A list of summarise project objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Summarize Project
        api_response = api_instance.summarize_project(summarize_project, authorization=authorization)
        print("The response of JobApi->summarize_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->summarize_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarize_project** | [**List[SummarizeProject]**](SummarizeProject.md)| A list of summarise project objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**JobServiceResponse**](JobServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

