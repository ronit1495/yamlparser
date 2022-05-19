#!/usr/bin/python
from asyncio.log import logger
from importlib.metadata import metadata
import sys, getopt, yaml, json, boto3, initalizer, s3Connector,builder,logging

#Setup basic logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        # Please use debug.log to check log history
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger() 

# Create command line argument based trigger
def main(argv):
    enviornmnet = ''
    region = ''
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"he:r:p:",["env=","region=","ifile="])
    except getopt.GetoptError:
        logger.error('Use: python3 yamlparser.py -e env -r region -p yaml_path')
        sys.exit(2)
    for opt, arg in opts:
        # Help menu for the CLI
        if opt == '-h':
         logger.info('python3 yamlparser.py -e <env> -r <region> -p <yaml_path> \n where \n -e = environment \n -r = region \n -p = absolute path of the yaml file \n')
         sys.exit()
        elif opt in ("-e", "--env"):
         enviornmnet = arg
        elif opt in ("-r","--region"):
            region = arg
        elif opt in ("-p","--ifile"):
            inputfile = arg
    print('Environment is ', enviornmnet)
    print('Region is ', region)
    print('Inputfile is ', inputfile,"\n")

    # Read and store the yaml file in dictionary
    with open(inputfile,"r") as stream:
        try:
            read_dict = yaml.safe_load(stream)
            logger.info("Succefully read the yaml.")
        except yaml.YAMLError as exc:
            logger.error(exc)

    # Try block to check if env and region and other key exists
    try:
    #initialize json data
        logger.info("Initailise data for config creation.")
        data_set = initalizer.intializerCreate(read_dict, enviornmnet, region)
        
        # Build and populate the json config dump
        logger.info("Build the JSON output for passed configuration.")
        builder.jsonBuilder(data_set)

        # S3 Uploader call
        logger.info("Upload to S3 Bucket started")
        s3Connector.s3Uploader()

    except:
        # Initialize json data with common values
        logger.info("Initailise data for config creation.")
        data_set_common = initalizer.intializerCreateCommon(read_dict,enviornmnet,region)
        
        # Build and populate the json config dump
        logger.info("Build the JSON output for passed configuration.")
        builder.jsonBuilder(data_set_common)
        
        # S3 Uploader call
        logger.info("Upload to S3 Bucket started")
        s3Connector.s3Uploader()
        exit()

if __name__ == "__main__":
   main(sys.argv[1:])