import logging
import time
from jsonschema import validate
from src.entity.current_usage_enti import CurrentUsage

class CurrentUsageUseCase:
    def __init__(self,repo):
        self.repo = repo

    def __error_desc(self,e):
        error_id = str(time.time_ns())
        error_desc = 'CurrentUsageUseCase error_id:|' + error_id + '|'
        logger = logging.getLogger('CurrentUsageUseCase Validation')
        logger.error(error_desc + str(e))
        return error_desc

    def execute(self,request):
        #Log request:
        logger = logging.getLogger('CurrentUsageUseCase Execute')
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
            CurrentUsage(site_id=request['site_id'], power = request['power'])
            return request

        except Exception as e:
            return {'error':self.__error_desc(e)}