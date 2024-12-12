# openapi_client.ProjectSpendingPlanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_spending_plan**](ProjectSpendingPlanApi.md#create_project_spending_plan) | **POST** /projectSpendingPlan | Create ProjectSpendingPlan
[**delete_project_spending_plan**](ProjectSpendingPlanApi.md#delete_project_spending_plan) | **DELETE** /projectSpendingPlan | Delete ProjectSpendingPlan
[**get_project_spending_plan**](ProjectSpendingPlanApi.md#get_project_spending_plan) | **GET** /projectSpendingPlan | Read ProjectSpendingPlan
[**get_project_spending_plan_field_length**](ProjectSpendingPlanApi.md#get_project_spending_plan_field_length) | **GET** /projectSpendingPlan/getFieldLength/{fieldName} | View ProjectSpendingPlan Field Length
[**get_project_spending_plan_fields**](ProjectSpendingPlanApi.md#get_project_spending_plan_fields) | **GET** /projectSpendingPlan/fields | View ProjectSpendingPlan fields
[**update_project_spending_plan**](ProjectSpendingPlanApi.md#update_project_spending_plan) | **PUT** /projectSpendingPlan | Update ProjectSpendingPlan


# **create_project_spending_plan**
> str create_project_spending_plan(project_spending_plan, authorization=authorization)

Create ProjectSpendingPlan

Send a request to this endpoint to create one or more ProjectSpendingPlan. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_spending_plan import ProjectSpendingPlan
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
    api_instance = openapi_client.ProjectSpendingPlanApi(api_client)
    project_spending_plan = [openapi_client.ProjectSpendingPlan()] # List[ProjectSpendingPlan] | A list of projectspendingplan objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectSpendingPlan
        api_response = api_instance.create_project_spending_plan(project_spending_plan, authorization=authorization)
        print("The response of ProjectSpendingPlanApi->create_project_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSpendingPlanApi->create_project_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_spending_plan** | [**List[ProjectSpendingPlan]**](ProjectSpendingPlan.md)| A list of projectspendingplan objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**str**

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

# **delete_project_spending_plan**
> bool delete_project_spending_plan(object_id, authorization=authorization)

Delete ProjectSpendingPlan

Send a request to this endpoint to delete one or more ProjectSpendingPlan. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectSpendingPlanApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectspendingplan.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectSpendingPlan
        api_response = api_instance.delete_project_spending_plan(object_id, authorization=authorization)
        print("The response of ProjectSpendingPlanApi->delete_project_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSpendingPlanApi->delete_project_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectspendingplan. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**bool**

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

# **get_project_spending_plan**
> List[ProjectSpendingPlan] get_project_spending_plan(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectSpendingPlan

Reads ProjectSpendingPlan objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_spending_plan import ProjectSpendingPlan
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
    api_instance = openapi_client.ProjectSpendingPlanApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectSpendingPlan
        api_response = api_instance.get_project_spending_plan(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectSpendingPlanApi->get_project_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSpendingPlanApi->get_project_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectSpendingPlan]**](ProjectSpendingPlan.md)

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

# **get_project_spending_plan_field_length**
> str get_project_spending_plan_field_length(field_name, authorization=authorization)

View ProjectSpendingPlan Field Length

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
    api_instance = openapi_client.ProjectSpendingPlanApi(api_client)
    field_name = 'field_name_example' # str | An projectspendingplan field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectSpendingPlan Field Length
        api_response = api_instance.get_project_spending_plan_field_length(field_name, authorization=authorization)
        print("The response of ProjectSpendingPlanApi->get_project_spending_plan_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSpendingPlanApi->get_project_spending_plan_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectspendingplan field. | 
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

# **get_project_spending_plan_fields**
> str get_project_spending_plan_fields()

View ProjectSpendingPlan fields

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
    api_instance = openapi_client.ProjectSpendingPlanApi(api_client)

    try:
        # View ProjectSpendingPlan fields
        api_response = api_instance.get_project_spending_plan_fields()
        print("The response of ProjectSpendingPlanApi->get_project_spending_plan_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSpendingPlanApi->get_project_spending_plan_fields: %s\n" % e)
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

# **update_project_spending_plan**
> bool update_project_spending_plan(project_spending_plan, authorization=authorization)

Update ProjectSpendingPlan

Send a request to this endpoint to update one or more ProjectSpendingPlan. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_spending_plan import ProjectSpendingPlan
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
    api_instance = openapi_client.ProjectSpendingPlanApi(api_client)
    project_spending_plan = [openapi_client.ProjectSpendingPlan()] # List[ProjectSpendingPlan] | A list of projectspendingplan objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectSpendingPlan
        api_response = api_instance.update_project_spending_plan(project_spending_plan, authorization=authorization)
        print("The response of ProjectSpendingPlanApi->update_project_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSpendingPlanApi->update_project_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_spending_plan** | [**List[ProjectSpendingPlan]**](ProjectSpendingPlan.md)| A list of projectspendingplan objects. | 
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

