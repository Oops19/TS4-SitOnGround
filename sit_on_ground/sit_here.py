#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from ts4lib.utils.tuning_helper import TuningHelper


class SitHere:

    def __init__(self):
        th = TuningHelper()
        tunings = th.get_tuning_dict('TUNING', ['testSet_SkirtOrDress_False', ])
        for tuning_id, tuning_data in tunings.items():
            instance_manager, manager, key, tuning_name = tuning_data
    @staticmethod
    @CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_TERRAIN_LOAD)
    class RegisterSitOnGround(CommonScriptObjectInteractionHandler):
        @property
        def interactions_to_add(self) -> Tuple[int]:
            interactions: Tuple = (
                0x1F7E2F5DD41B3F0A,  # 'Kneel Here'
                0x38A8B3B444755099,  # 'Sit Cross Legged Here'
            )
            return interactions

        def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
            return True


SitHere()
