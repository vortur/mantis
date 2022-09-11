from argparse import OPTIONAL
from typing import Optional
import logging

from codegen.stringcase import camel_case
from codegen.stringcase import snake_case

def find_in_file(file_path,search_str):
    try:
        with open(file_path) as f:
            if search_str in f.read():
                return True
            else:
                return False
    except FileNotFoundError as e:
        return False

def entity_gen(method_str, build_path):
    LOGFORMAT = "%(asctime)s - %(name)s - [%(process)d/%(threadName)-10s] %(levelname)-8s \"%(filename)s/%(funcName)s:%(lineno)d\" \"%(message)s\""
    logging.basicConfig(format=LOGFORMAT)
    logger = logging.getLogger('Entity Generator')

    class_name_str = camel_case(method_str)

    # Create new entity:
    try:
        with open('./codegen/templates/entity.tpl', 'r') as tmp:
            entity_path = build_path + 'entity/' + method_str + '_enti.py'
            logger.warning("Generating Entity: " + entity_path)
            #Check if there is no same entity:
            if find_in_file(entity_path,class_name_str):
                raise Exception('Entity exists!', class_name_str )

            with open(entity_path, 'w') as fout:
                for line in tmp:
                    updated_line = line.replace('$classUseCase', class_name_str)
                    fout.write(updated_line)
                fout.close()
        tmp.close()
    except Exception as e:
        logger.error(e)