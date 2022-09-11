import logging
import time
from jsonschema import validate

class $classUseCase:
    def __init__(self,repo):
        self.repo = repo

    def __error_desc(self,e):
        error_id = str(time.time_ns())
        error_desc = '$classUseCase error_id:|' + error_id + '|'
        logger = logging.getLogger('$classUseCase Validation')
        logger.error(error_desc + str(e))
        return error_desc

    def execute(self,request):
        #Log request:
        logger = logging.getLogger('$classUseCase Execute')
        logger.debug(str(request))
        #Validate schema:
        request_validation = {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "description": {"type": "string"},
            },
            #"required": ["id", "data"],
            "additionalProperties": True
        }
        #Validate request if error return description:
        try:
            validate(instance=request, schema=request_validation)
        except Exception as e:
            return {'error':self.__error_desc(e)}

        try:
            #Buisness logic here
            result = self.repo.$methodUseCase(request)
            #Buisness logic here

            return result

        except Exception as e:
            return {'error':self.__error_desc(e)}