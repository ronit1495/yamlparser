from distutils.log import error, info
import yamlparser,logging

logger=logging.getLogger() 

def intializerCreate(read_dict, enviornmnet, region):
    metadata = read_dict["metadata"]
    #helm common details and values
    helm = read_dict["common"]["helm"],read_dict[enviornmnet][region]["helm"]

    if("notifications" in read_dict[enviornmnet][region]):
        notifications = read_dict[enviornmnet][region]["notifications"]
    else:
        notifications = read_dict["common"]["notifications"]            
    if("repo" in read_dict[enviornmnet][region]):
        repo = read_dict[enviornmnet][region]["repo"]
    else:
        repo = read_dict["common"]["repo"]

    #json build
    data_set = {"enviornment": enviornmnet, "region": region,"configuration": [metadata],"helm": helm,"notifications": notifications,"repo": repo}
    return data_set

def intializerCreateCommon(read_dict,enviornmnet,region):
    logger.warning("Exception occured since enviornment and region does not exist, hence initialized file with common values.")
    data_set_common = {"enviornment": enviornmnet, "region": region,"configuration": read_dict["metadata"],"helm": read_dict["common"]["helm"],"notifications": read_dict["common"]["notifications"],"repo": read_dict["common"]["repo"]}
    return data_set_common