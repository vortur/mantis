import logging
import time
from jsonschema import validate
from src.entity.current_generation_enti import CurrentGeneration

class CurrentGenerationUseCase:
    def __init__(self,repo):
        self.repo = repo

    def __error_desc(self,e):
        error_id = str(time.time_ns())
        error_desc = 'CurrentGenerationUseCase error_id:|' + error_id + '|'
        logger = logging.getLogger('CurrentGenerationUseCase Validation')
        logger.error(error_desc + str(e))
        return error_desc

    def execute(self,request):
        #Log request:
        logger = logging.getLogger('CurrentGenerationUseCase Execute')
        logger.debug(str(request))
        #Validate schema:
        request_validation = {
            "type": "object",
            "properties": {
                "site_id": {"type": "number"},
                "power": {"type": "number"},
            },
            "required": ["site_id", "power"],
            "additionalProperties": True
        }
        #Validate request if error return description:
        try:
            validate(instance=request, schema=request_validation)
        except Exception as e:
            return {'error':self.__error_desc(e)}

        try:
            CurrentGeneration(site_id=request['site_id'], power = request['power'])
            return request

        except Exception as e:
            return {'error':self.__error_desc(e)}