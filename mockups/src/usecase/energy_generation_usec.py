import logging
import time
from jsonschema import validate

class EnergyGenerationUseCase:
    def __init__(self,repo):
        self.repo = repo

    def __error_desc(self,e):
        error_id = str(time.time_ns())
        error_desc = 'EnergyGenerationUseCase error_id:|' + error_id + '|'
        logger = logging.getLogger('EnergyGenerationUseCase Validation')
        logger.error(error_desc + str(e))
        return error_desc

    def execute(self,request):
        #Log request:
        logger = logging.getLogger('EnergyGenerationUseCase Execute')
        logger.debug(str(request))
        #Validate schema:
        request_validation = {
            "type": "object",
            "properties": {
                "from_time": {"type": "string"},
                "to_time": {"type": "string"},
                "site_id": {"type": "number"},
                "kvp": {"type": "number"},
                "energy": {"type": "number"},
            },
            "required": ["site_id", "kvp"],
            "additionalProperties": True
        }
        #Validate request if error return description:
        try:
            validate(instance=request, schema=request_validation)
        except Exception as e:
            return {'error':self.__error_desc(e)}

        try:
            #Buisness logic here
            result = self.repo.energy_generation(request)
            #Buisness logic here

            return result

        except Exception as e:
            return {'error':self.__error_desc(e)}