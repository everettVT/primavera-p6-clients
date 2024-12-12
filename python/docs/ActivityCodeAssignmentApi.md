# openapi_client.ActivityCodeAssignmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_code_assignment**](ActivityCodeAssignmentApi.md#create_activity_code_assignment) | **POST** /activityCodeAssignment | Create ActivityCodeAssignments
[**delete_activity_code_assignment**](ActivityCodeAssignmentApi.md#delete_activity_code_assignment) | **DELETE** /activityCodeAssignment | Delete ActivityCodeAssignments
[**get_activity_code_assignment_field_length**](ActivityCodeAssignmentApi.md#get_activity_code_assignment_field_length) | **GET** /activityCodeAssignment/getFieldLength/{fieldName} | View ActivityCodeAssignment Field Length
[**get_activity_code_assignment_fields**](ActivityCodeAssignmentApi.md#get_activity_code_assignment_fields) | **GET** /activityCodeAssignment/fields | View ActivityCodeAssignment fields
[**get_activity_code_assignments**](ActivityCodeAssignmentApi.md#get_activity_code_assignments) | **GET** /activityCodeAssignment | Read ActivityCodeAssignments
[**update_activity_code_assignment**](ActivityCodeAssignmentApi.md#update_activity_code_assignment) | **PUT** /activityCodeAssignment | Update ActivityCodeAssignments


# **create_activity_code_assignment**
> List[CreateActivityCodeAssignmentsResponse] create_activity_code_assignment(activity_code_assignment, authorization=authorization)

Create ActivityCodeAssignments

Send a request to this endpoint to create one or more activityCodeAssignment. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_code_assignment import ActivityCodeAssignment
from openapi_client.models.create_activity_code_assignments_response import CreateActivityCodeAssignmentsResponse
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
    api_instance = openapi_client.ActivityCodeAssignmentApi(api_client)
    activity_code_assignment = [openapi_client.ActivityCodeAssignment()] # List[ActivityCodeAssignment] | A list of activityCodeAssignment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityCodeAssignments
        api_response = api_instance.create_activity_code_assignment(activity_code_assignment, authorization=authorization)
        print("The response of ActivityCodeAssignmentApi->create_activity_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeAssignmentApi->create_activity_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_code_assignment** | [**List[ActivityCodeAssignment]**](ActivityCodeAssignment.md)| A list of activityCodeAssignment objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateActivityCodeAssignmentsResponse]**](CreateActivityCodeAssignmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity_code_assignment**
> bool delete_activity_code_assignment(activity_code_assignment, authorization=authorization)

Delete ActivityCodeAssignments

Send a request to this endpoint to delete one or more activityCodeAssignment. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.activity_code_assignment import ActivityCodeAssignment
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
    api_instance = openapi_client.ActivityCodeAssignmentApi(api_client)
    activity_code_assignment = [openapi_client.ActivityCodeAssignment()] # List[ActivityCodeAssignment] | <p>A list of activityCodeAssignment objects.<p><p>Required fields: You must supply both the ActivityCodeTypeObjectId and ActivityObjectId fields when you use the Delete ActivityCodeAssignments operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ActivityCodeAssignments
        api_response = api_instance.delete_activity_code_assignment(activity_code_assignment, authorization=authorization)
        print("The response of ActivityCodeAssignmentApi->delete_activity_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeAssignmentApi->delete_activity_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_code_assignment** | [**List[ActivityCodeAssignment]**](ActivityCodeAssignment.md)| &lt;p&gt;A list of activityCodeAssignment objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ActivityCodeTypeObjectId and ActivityObjectId fields when you use the Delete ActivityCodeAssignments operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_activity_code_assignment_field_length**
> str get_activity_code_assignment_field_length(field_name, authorization=authorization)

View ActivityCodeAssignment Field Length

Send a request to this endpoint to load length of variable character fields for a BO.

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
    api_instance = openapi_client.ActivityCodeAssignmentApi(api_client)
    field_name = 'field_name_example' # str | An activityCodeAssignment field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityCodeAssignment Field Length
        api_response = api_instance.get_activity_code_assignment_field_length(field_name, authorization=authorization)
        print("The response of ActivityCodeAssignmentApi->get_activity_code_assignment_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeAssignmentApi->get_activity_code_assignment_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityCodeAssignment field. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**str**

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

# **get_activity_code_assignment_fields**
> str get_activity_code_assignment_fields()

View ActivityCodeAssignment fields

Send a request to this endpoint to load all the fields for a BO.

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
    api_instance = openapi_client.ActivityCodeAssignmentApi(api_client)

    try:
        # View ActivityCodeAssignment fields
        api_response = api_instance.get_activity_code_assignment_fields()
        print("The response of ActivityCodeAssignmentApi->get_activity_code_assignment_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeAssignmentApi->get_activity_code_assignment_fields: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

# **get_activity_code_assignments**
> List[ActivityCodeAssignment] get_activity_code_assignments(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityCodeAssignments

Reads ActivityCodeAssignment objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_code_assignment import ActivityCodeAssignment
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
    api_instance = openapi_client.ActivityCodeAssignmentApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityCodeAssignments
        api_response = api_instance.get_activity_code_assignments(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityCodeAssignmentApi->get_activity_code_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeAssignmentApi->get_activity_code_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityCodeAssignment]**](ActivityCodeAssignment.md)

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

# **update_activity_code_assignment**
> bool update_activity_code_assignment(activity_code_assignment, authorization=authorization)

Update ActivityCodeAssignments

Send a request to this endpoint to update one or more activityCodeAssignment. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_code_assignment import ActivityCodeAssignment
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
    api_instance = openapi_client.ActivityCodeAssignmentApi(api_client)
    activity_code_assignment = [openapi_client.ActivityCodeAssignment()] # List[ActivityCodeAssignment] | <p>A list of activityCodeAssignment objects.<p><p>Required fields: You must supply both the ActivityCodeTypeObjectId and ActivityObjectId fields when you use the Update ActivityCodeAssignments operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityCodeAssignments
        api_response = api_instance.update_activity_code_assignment(activity_code_assignment, authorization=authorization)
        print("The response of ActivityCodeAssignmentApi->update_activity_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeAssignmentApi->update_activity_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_code_assignment** | [**List[ActivityCodeAssignment]**](ActivityCodeAssignment.md)| &lt;p&gt;A list of activityCodeAssignment objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ActivityCodeTypeObjectId and ActivityObjectId fields when you use the Update ActivityCodeAssignments operation. All other fields are optional.&lt;/p&gt; | 
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

