import logging
import time
from jsonschema import validate

class EnergyUsageUseCase:
    def __init__(self,repo):
        self.repo = repo

    def __error_desc(self,e):
        error_id = str(time.time_ns())
        error_desc = 'EnergyUsageUseCase error_id:|' + error_id + '|'
        logger = logging.getLogger('EnergyUsageUseCase Validation')
        logger.error(error_desc + str(e))
        return error_desc

    def execute(self,request):
        #Log request:
        logger = logging.getLogger('EnergyUsageUseCase Execute')
        logger.debug(str(request))
        #Validate schema:
        request_validation = {
            "type": "object",
            "properties": {
                "from_time": {"type": "string"},
                "to_time": {"type": "string"},
                "site_id": {"type": "number"},
                "kw_max": {"type": "number"},
                "energy": {"type": "number"},
            },
            "required": ["site_id", "kw_max"],
            "additionalProperties": True
        }
        #Validate request if error return description:
        try:
            validate(instance=request, schema=request_validation)
        except Exception as e:
            return {'error':self.__error_desc(e)}

        try:
            #Buisness logic here
            result = self.repo.energy_usage(request)
            #Buisness logic here

            return result

        except Exception as e:
            return {'error':self.__error_desc(e)}