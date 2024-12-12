# openapi_client.ExportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_files**](ExportApi.md#download_files) | **POST** /export/downloadFiles | Download Files
[**export_impdar_project**](ExportApi.md#export_impdar_project) | **POST** /export/exportIpmdarProject | Export ImpdarProject
[**export_project**](ExportApi.md#export_project) | **POST** /export/exportProjects | Export Projects
[**export_project1**](ExportApi.md#export_project1) | **POST** /export/exportProject | Export Project


# **download_files**
> DownloadFilesResponse download_files(download_files, authorization=authorization)

Download Files

Download Files

### Example


```python
import openapi_client
from openapi_client.models.download_files import DownloadFiles
from openapi_client.models.download_files_response import DownloadFilesResponse
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
    api_instance = openapi_client.ExportApi(api_client)
    download_files = openapi_client.DownloadFiles() # DownloadFiles | Downloads one or more files.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Download Files
        api_response = api_instance.download_files(download_files, authorization=authorization)
        print("The response of ExportApi->download_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->download_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_files** | [**DownloadFiles**](DownloadFiles.md)| Downloads one or more files. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**DownloadFilesResponse**](DownloadFilesResponse.md)

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

# **export_impdar_project**
> export_impdar_project(export_ipmdar_project, authorization=authorization)

Export ImpdarProject

Export ImpdarProject

### Example


```python
import openapi_client
from openapi_client.models.export_ipmdar_project import ExportIpmdarProject
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
    api_instance = openapi_client.ExportApi(api_client)
    export_ipmdar_project = openapi_client.ExportIpmdarProject() # ExportIpmdarProject | Exports an ImpdarProject to an XML file.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Export ImpdarProject
        api_instance.export_impdar_project(export_ipmdar_project, authorization=authorization)
    except Exception as e:
        print("Exception when calling ExportApi->export_impdar_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_ipmdar_project** | [**ExportIpmdarProject**](ExportIpmdarProject.md)| Exports an ImpdarProject to an XML file. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

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

# **export_project**
> export_project(export_projects, authorization=authorization)

Export Projects

Export Projects

### Example


```python
import openapi_client
from openapi_client.models.export_projects import ExportProjects
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
    api_instance = openapi_client.ExportApi(api_client)
    export_projects = openapi_client.ExportProjects() # ExportProjects | Exports one or more projects to an XML file. When you call the ExportProjects operation, you can specify one to many ProjectObjectID elements.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Export Projects
        api_instance.export_project(export_projects, authorization=authorization)
    except Exception as e:
        print("Exception when calling ExportApi->export_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_projects** | [**ExportProjects**](ExportProjects.md)| Exports one or more projects to an XML file. When you call the ExportProjects operation, you can specify one to many ProjectObjectID elements. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

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

# **export_project1**
> export_project1(export_project, authorization=authorization)

Export Project

Export Project

### Example


```python
import openapi_client
from openapi_client.models.export_project import ExportProject
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
    api_instance = openapi_client.ExportApi(api_client)
    export_project = openapi_client.ExportProject() # ExportProject | Exports a project to an XML file.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Export Project
        api_instance.export_project1(export_project, authorization=authorization)
    except Exception as e:
        print("Exception when calling ExportApi->export_project1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_project** | [**ExportProject**](ExportProject.md)| Exports a project to an XML file. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

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

