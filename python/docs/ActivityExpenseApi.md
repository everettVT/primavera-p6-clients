# openapi_client.ActivityExpenseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_expense**](ActivityExpenseApi.md#create_activity_expense) | **POST** /activityExpense | Create ActivityExpenses
[**delete_activity_expenses**](ActivityExpenseApi.md#delete_activity_expenses) | **DELETE** /activityExpense | Delete ActivityExpenses
[**get_activity_expense_field_length**](ActivityExpenseApi.md#get_activity_expense_field_length) | **GET** /activityExpense/getFieldLength/{fieldName} | View ActivityExpense Field Length
[**get_activity_expense_fields**](ActivityExpenseApi.md#get_activity_expense_fields) | **GET** /activityExpense/fields | View ActivityExpense fields
[**get_activity_expenses**](ActivityExpenseApi.md#get_activity_expenses) | **GET** /activityExpense | Read ActivityExpenses
[**update_activity_expenses**](ActivityExpenseApi.md#update_activity_expenses) | **PUT** /activityExpense | Update ActivityExpenses


# **create_activity_expense**
> str create_activity_expense(activity_expense, authorization=authorization)

Create ActivityExpenses

Send a request to this endpoint to create one or more activityExpense. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_expense import ActivityExpense
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
    api_instance = openapi_client.ActivityExpenseApi(api_client)
    activity_expense = [openapi_client.ActivityExpense()] # List[ActivityExpense] | A list of activityExpense objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityExpenses
        api_response = api_instance.create_activity_expense(activity_expense, authorization=authorization)
        print("The response of ActivityExpenseApi->create_activity_expense:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityExpenseApi->create_activity_expense: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_expense** | [**List[ActivityExpense]**](ActivityExpense.md)| A list of activityExpense objects. | 
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

# **delete_activity_expenses**
> bool delete_activity_expenses(authorization=authorization, object_id=object_id)

Delete ActivityExpenses

Send a request to this endpoint to delete one or more activityExpense. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityExpenseApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityExpense. (optional)

    try:
        # Delete ActivityExpenses
        api_response = api_instance.delete_activity_expenses(authorization=authorization, object_id=object_id)
        print("The response of ActivityExpenseApi->delete_activity_expenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityExpenseApi->delete_activity_expenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of activityExpense. | [optional] 

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

# **get_activity_expense_field_length**
> str get_activity_expense_field_length(field_name, authorization=authorization)

View ActivityExpense Field Length

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
    api_instance = openapi_client.ActivityExpenseApi(api_client)
    field_name = 'field_name_example' # str | An activityExpense field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityExpense Field Length
        api_response = api_instance.get_activity_expense_field_length(field_name, authorization=authorization)
        print("The response of ActivityExpenseApi->get_activity_expense_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityExpenseApi->get_activity_expense_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityExpense field. | 
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

# **get_activity_expense_fields**
> str get_activity_expense_fields()

View ActivityExpense fields

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
    api_instance = openapi_client.ActivityExpenseApi(api_client)

    try:
        # View ActivityExpense fields
        api_response = api_instance.get_activity_expense_fields()
        print("The response of ActivityExpenseApi->get_activity_expense_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityExpenseApi->get_activity_expense_fields: %s\n" % e)
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

# **get_activity_expenses**
> List[ActivityExpense] get_activity_expenses(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityExpenses

Reads ActivityExpense objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_expense import ActivityExpense
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
    api_instance = openapi_client.ActivityExpenseApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityExpenses
        api_response = api_instance.get_activity_expenses(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityExpenseApi->get_activity_expenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityExpenseApi->get_activity_expenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityExpense]**](ActivityExpense.md)

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

# **update_activity_expenses**
> bool update_activity_expenses(activity_expense, authorization=authorization)

Update ActivityExpenses

Send a request to this endpoint to update one or more activityExpense. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_expense import ActivityExpense
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
    api_instance = openapi_client.ActivityExpenseApi(api_client)
    activity_expense = [openapi_client.ActivityExpense()] # List[ActivityExpense] | A list of activityExpense objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityExpenses
        api_response = api_instance.update_activity_expenses(activity_expense, authorization=authorization)
        print("The response of ActivityExpenseApi->update_activity_expenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityExpenseApi->update_activity_expenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_expense** | [**List[ActivityExpense]**](ActivityExpense.md)| A list of activityExpense objects. | 
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

