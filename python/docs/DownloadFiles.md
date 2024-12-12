# DownloadFiles

DownloadFiles Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_type** | **str** | Specifies the job type. | [optional] 
**job_name** | **List[str]** | Specifies the job name. | [optional] 
**start_date** | **datetime** | The start date of the file download. | [optional] 
**end_date** | **datetime** | The end date of the file download. | [optional] 

## Example

```python
from openapi_client.models.download_files import DownloadFiles

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadFiles from a JSON string
download_files_instance = DownloadFiles.from_json(json)
# print the JSON string representation of the object
print(DownloadFiles.to_json())

# convert the object into a dict
download_files_dict = download_files_instance.to_dict()
# create an instance of DownloadFiles from a dict
download_files_from_dict = DownloadFiles.from_dict(download_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


