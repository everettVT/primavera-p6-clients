# openapi_client.ProjectPortfolioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_portfolio**](ProjectPortfolioApi.md#create_project_portfolio) | **POST** /projectPortfolio | Create ProjectPortfolio
[**delete_project_portfolio**](ProjectPortfolioApi.md#delete_project_portfolio) | **DELETE** /projectPortfolio | Delete ProjectPortfolio
[**get_project_portfolio**](ProjectPortfolioApi.md#get_project_portfolio) | **GET** /projectPortfolio | Read ProjectPortfolio
[**get_project_portfolio_field_length**](ProjectPortfolioApi.md#get_project_portfolio_field_length) | **GET** /projectPortfolio/getFieldLength/{fieldName} | View ProjectPortfolio Field Length
[**get_project_portfolio_fields**](ProjectPortfolioApi.md#get_project_portfolio_fields) | **GET** /projectPortfolio/fields | View ProjectPortfolio fields
[**update_project_portfolio**](ProjectPortfolioApi.md#update_project_portfolio) | **PUT** /projectPortfolio | Update ProjectPortfolio


# **create_project_portfolio**
> str create_project_portfolio(project_portfolio, authorization=authorization)

Create ProjectPortfolio

Send a request to this endpoint to create one or more ProjectPortfolio. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_portfolio import ProjectPortfolio
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
    api_instance = openapi_client.ProjectPortfolioApi(api_client)
    project_portfolio = [openapi_client.ProjectPortfolio()] # List[ProjectPortfolio] | A list of projectportfolio objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectPortfolio
        api_response = api_instance.create_project_portfolio(project_portfolio, authorization=authorization)
        print("The response of ProjectPortfolioApi->create_project_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPortfolioApi->create_project_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_portfolio** | [**List[ProjectPortfolio]**](ProjectPortfolio.md)| A list of projectportfolio objects. | 
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

# **delete_project_portfolio**
> bool delete_project_portfolio(object_id, authorization=authorization)

Delete ProjectPortfolio

Send a request to this endpoint to delete one or more ProjectPortfolio. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectPortfolioApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectportfolio.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectPortfolio
        api_response = api_instance.delete_project_portfolio(object_id, authorization=authorization)
        print("The response of ProjectPortfolioApi->delete_project_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPortfolioApi->delete_project_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectportfolio. | 
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

# **get_project_portfolio**
> List[ProjectPortfolio] get_project_portfolio(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectPortfolio

Reads ProjectPortfolio objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_portfolio import ProjectPortfolio
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
    api_instance = openapi_client.ProjectPortfolioApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectPortfolio
        api_response = api_instance.get_project_portfolio(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectPortfolioApi->get_project_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPortfolioApi->get_project_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectPortfolio]**](ProjectPortfolio.md)

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

# **get_project_portfolio_field_length**
> str get_project_portfolio_field_length(field_name, authorization=authorization)

View ProjectPortfolio Field Length

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
    api_instance = openapi_client.ProjectPortfolioApi(api_client)
    field_name = 'field_name_example' # str | Field to retun length
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectPortfolio Field Length
        api_response = api_instance.get_project_portfolio_field_length(field_name, authorization=authorization)
        print("The response of ProjectPortfolioApi->get_project_portfolio_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPortfolioApi->get_project_portfolio_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| Field to retun length | 
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

# **get_project_portfolio_fields**
> str get_project_portfolio_fields()

View ProjectPortfolio fields

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
    api_instance = openapi_client.ProjectPortfolioApi(api_client)

    try:
        # View ProjectPortfolio fields
        api_response = api_instance.get_project_portfolio_fields()
        print("The response of ProjectPortfolioApi->get_project_portfolio_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPortfolioApi->get_project_portfolio_fields: %s\n" % e)
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

# **update_project_portfolio**
> bool update_project_portfolio(project_portfolio, authorization=authorization)

Update ProjectPortfolio

Send a request to this endpoint to update one or more ProjectPortfolio. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_portfolio import ProjectPortfolio
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
    api_instance = openapi_client.ProjectPortfolioApi(api_client)
    project_portfolio = [openapi_client.ProjectPortfolio()] # List[ProjectPortfolio] | A list of projectportfolio objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectPortfolio
        api_response = api_instance.update_project_portfolio(project_portfolio, authorization=authorization)
        print("The response of ProjectPortfolioApi->update_project_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPortfolioApi->update_project_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_portfolio** | [**List[ProjectPortfolio]**](ProjectPortfolio.md)| A list of projectportfolio objects. | 
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

