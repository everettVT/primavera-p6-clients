# DownloadFilesResponse

DownloadFilesResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_files** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.download_files_response import DownloadFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadFilesResponse from a JSON string
download_files_response_instance = DownloadFilesResponse.from_json(json)
# print the JSON string representation of the object
print(DownloadFilesResponse.to_json())

# convert the object into a dict
download_files_response_dict = download_files_response_instance.to_dict()
# create an instance of DownloadFilesResponse from a dict
download_files_response_from_dict = DownloadFilesResponse.from_dict(download_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


