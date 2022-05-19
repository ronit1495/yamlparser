import json,yamlparser,logging

logger=logging.getLogger() 

def jsonBuilder(data_set):
    with open('config.json', 'w') as f:
            json.dump(data_set,f,indent=1)
            json_dump = json.dumps(data_set,indent=1)
            logger.info("Configuration file has been generated for the given input file.\n")
            print("***************************************\n")
            print(json_dump)
            print("***************************************\n")
            f.close()