# openapi_client.RiskCategoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_category**](RiskCategoryApi.md#create_risk_category) | **POST** /riskCategory | Create RiskCategories
[**delete_risk_category**](RiskCategoryApi.md#delete_risk_category) | **DELETE** /riskCategory | Delete RiskCategories
[**get_risk_category**](RiskCategoryApi.md#get_risk_category) | **GET** /riskCategory | Read RiskCategories
[**get_risk_category_field_length**](RiskCategoryApi.md#get_risk_category_field_length) | **GET** /riskCategory/getFieldLength/{fieldName} | View RiskCategory Field Length
[**get_risk_category_fields**](RiskCategoryApi.md#get_risk_category_fields) | **GET** /riskCategory/fields | View RiskCategory fields
[**update_risk_category**](RiskCategoryApi.md#update_risk_category) | **PUT** /riskCategory | Update RiskCategories


# **create_risk_category**
> str create_risk_category(risk_category, authorization=authorization)

Create RiskCategories

Send a request to this endpoint to create one or more riskCategory. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.risk_category import RiskCategory
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
    api_instance = openapi_client.RiskCategoryApi(api_client)
    risk_category = [openapi_client.RiskCategory()] # List[RiskCategory] | A list of riskCategory objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskCategories
        api_response = api_instance.create_risk_category(risk_category, authorization=authorization)
        print("The response of RiskCategoryApi->create_risk_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskCategoryApi->create_risk_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_category** | [**List[RiskCategory]**](RiskCategory.md)| A list of riskCategory objects. | 
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

# **delete_risk_category**
> bool delete_risk_category(authorization=authorization, object_id=object_id)

Delete RiskCategories

Send a request to this endpoint to delete one or more riskCategory. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.RiskCategoryApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of riskCategory. (optional)

    try:
        # Delete RiskCategories
        api_response = api_instance.delete_risk_category(authorization=authorization, object_id=object_id)
        print("The response of RiskCategoryApi->delete_risk_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskCategoryApi->delete_risk_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of riskCategory. | [optional] 

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

# **get_risk_category**
> List[RiskCategory] get_risk_category(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskCategories

Reads RiskCategory objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_category import RiskCategory
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
    api_instance = openapi_client.RiskCategoryApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskCategories
        api_response = api_instance.get_risk_category(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskCategoryApi->get_risk_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskCategoryApi->get_risk_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskCategory]**](RiskCategory.md)

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

# **get_risk_category_field_length**
> str get_risk_category_field_length(field_name, authorization=authorization)

View RiskCategory Field Length

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
    api_instance = openapi_client.RiskCategoryApi(api_client)
    field_name = 'field_name_example' # str | A riskCategory field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskCategory Field Length
        api_response = api_instance.get_risk_category_field_length(field_name, authorization=authorization)
        print("The response of RiskCategoryApi->get_risk_category_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskCategoryApi->get_risk_category_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskCategory field. | 
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

# **get_risk_category_fields**
> str get_risk_category_fields()

View RiskCategory fields

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
    api_instance = openapi_client.RiskCategoryApi(api_client)

    try:
        # View RiskCategory fields
        api_response = api_instance.get_risk_category_fields()
        print("The response of RiskCategoryApi->get_risk_category_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskCategoryApi->get_risk_category_fields: %s\n" % e)
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

# **update_risk_category**
> bool update_risk_category(risk_category, authorization=authorization)

Update RiskCategories

Send a request to this endpoint to update one or more riskCategory. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_category import RiskCategory
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
    api_instance = openapi_client.RiskCategoryApi(api_client)
    risk_category = [openapi_client.RiskCategory()] # List[RiskCategory] | A list of riskCategory objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskCategories
        api_response = api_instance.update_risk_category(risk_category, authorization=authorization)
        print("The response of RiskCategoryApi->update_risk_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskCategoryApi->update_risk_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_category** | [**List[RiskCategory]**](RiskCategory.md)| A list of riskCategory objects. | 
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

