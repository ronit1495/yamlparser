# Config YAML Parser

## What does it do ?
Python script to reduce a user's YAML file to a single environment/region combination according to input parameters.
* Script reads YAML file from disk.
* Script accepts three inputs: a environment, a region and YAML file
location.
* Script uses configuration under the common key if the environment and/or
region input parameter does not exist as a key in the YAML file.
* Script sorts the keys of the reduced config alphabetically after
service_name, team_name and cost_center.
* Script outputs reduced configuration as a JSON file.
* Script uploads JSON file to an S3 bucket and has exponential backoff.
retry logic that will fail if the upload does not complete in 10m.

## Requirements

1. Install pre-requiremnets.

        `pip3 install -r requirements.txt`

2. Use `aws configure` to set up the aws environment for S3 access.
3. Create a bucket called _config-uploader_ with correct polices attached for user and bucket. More details [here](https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2).

Note: Tested on macOS Big Sur(v11.6.5) and intel chipset.

## Usage

1. Yaml parser is a python CLI tool.
2. `python3 yamlparser.py` expects 3 arguments, 
    * First argument `-e <environment>`
    * Second argument `-r <region>`
    * Third argument (mandatory argument) `-p <YAML-file-path>`.
    
    Note: Pass absolute path in case the YAML is not present in project folder.

    **Complete command**: `python3 yamlparser.py -e <env> -r <region> -p <yaml_path>`
    
3. Use: `python3 yamlparser.py -h` for any help.
4. Example usage: `python3 yamlparser.py -e production -r va6 -p sample.yaml`


## Sub-Modules
* s3Connector - Methods to connect,upload and download files from S3.
* initalizer - Methods to parse given YAML file and returns a dictionary.
* builder - Method which reads dictionary as input and builds a json file out of it.

## Files
* `config.json` - Actual output of _yamlparser_ that is uploaded to s3.
* `sample.yaml` - Contains an example yaml to be used for parsing.
* `sample.json` -  Contains an example json of expected output.
* `downloaded_config.json` - Actual output file downloaded from S3 when method `s3Downloader()` is called. (Currently not called anywhere as no use case)
* `debug.json` - Contains all the logs generated when _yamlparser_ is used.


## Reference
* Command line argument function: [here](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
* Read yaml to dictionary: [here](https://fedingo.com/how-to-read-yaml-file-to-dict-in-python/)
* Initalizer: _none_
* Builder: [here](https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/)
* s3Connector: [here](https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2)

### Code Author and owner: 
* github username: ronit1495
* email: kumarronit1495@gmail.com
 