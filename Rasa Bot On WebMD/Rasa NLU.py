# Not appreciated to use python script instead use Rasa commands through CLI 

# import os
# from rasa.train import train_nlu

# modules=['NLU_model']
# MODULES_BASE_DIR='models'
# for module_name in modules:
#     module_directory = os.path.join(MODULES_BASE_DIR, module_name)
#     config_file = 'config.yml'
#     nlu_data = 'data/nlu'

#     train_nlu(
#         config=config_file,
#         nlu_data=nlu_data,
#         output=module_directory,
#         fixed_model_name=module_name,
#     )