task_dict["status_variables"]["Status1"] = "CUSTOMER_SUCCESS_JRNY_YET_TO_ASSIGN_STAGE"
task_dict_utils = method_objects_dict["task_dict_utils"]

message_template_plugin_id = 'CUSTOMAR_SUCCESS_JOURNEY_MESSAGE_PLUGIN_ACTION_ID'
template_field_responses = {}

plugin_service = method_objects_dict["plugin_service"]
plugin_action_id = message_template_plugin_id
plugin_service.send_whatsapp_message(
    task_id=task_id, plugin_action_id=plugin_action_id,
    field_responses=template_field_responses
)
