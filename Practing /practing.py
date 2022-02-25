task_dict["status_variables"]["Status4"] = "CCBP_INTLD_NEW_SCHOLARSHIP_APPROVED_AND_MESSAGE_SENT"
task_dict_utils = method_objects_dict["task_dict_utils"]

main_gof_uuid = task_dict_utils.get_plain_gof_uuid(
   gof_id="CCBP_INTLD_NEW_SCHOLARSHIP_DETAILS_GOF"
)

scholarship_details_uuid = task_dict_utils.get_or_create_plain_gof_uuid(
   gof_id="CCBP_INTLD_NEW_SCHOLARSHIP_GOF"
)

task_dict_utils.link_parent_gof_uuid_with_child_gof_uuid(
   parent_gof_uuid=main_gof_uuid, child_gof_uuid=scholarship_details_uuid
)

scholarship_details_dict = {
   "CCBP_INTLD_NEW_SCHLR_STATUS_FIELD": "Approved & Message sent"
}

task_dict_utils.update_field_responses_in_gof_uuid(
   scholarship_details_uuid, scholarship_details_dict
)

message_template_name = method_objects_dict["transition_task_dict_utils"].get_single_gof_field_response(
   "CCBP_INTLD_NEW_LEAD_WHATSAPP_MESSAGE_TEMPLATE_GOF", "CCBP_INTLD_WHATSAPP_MESSAGE_TEMPLATE_FIELD"
)

coupon_config_id = method_objects_dict["transition_task_dict_utils"].get_single_gof_field_response(
   "CCBP_INTLD_NEW_LOAD_DISCOUNT_GOF", "CCBP_INTLD_NEW_DISCOUNT_COUPON_CONFIG_ID_FIELD"
)

message_template_plugin_id = ''
template_field_responses = {}

if message_template_name == 'Reg. Open Seat Reserved':
    message_template_plugin_id = "REG_OPEN_SEAT_RES_MESSAGE_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Reg. Open Seat Reserved")
elif message_template_name == 'Reg. Open Seat Not Reserved':
    message_template_plugin_id = "REG_OPEN_SEAT_NOT_RES_MSG_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Reg. Open Seat Not Reserved")
elif message_template_name == 'Reg. Closed Seat Reserved':
    message_template_plugin_id = "REG_CLOSED_SEAT_RES_MSG_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Reg. Closed Seat Reserved")
elif message_template_name == 'Reg. Closed Seat Not Reserved':
    message_template_plugin_id = "REG_CLOSED_SEAT_NOT_RES_MSG_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Reg. Closed Seat Not Reserved")
elif message_template_name == 'Day Before Reg. Open Seat Reserve':
    message_template_plugin_id = "DAY_BEFORE_SEAT_RES_MSG_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Day Before Reg. Open Seat Reserve")
elif message_template_name == 'Day Before Reg. Open Seat Not Reserved':
    message_template_plugin_id = "DAY_BEFORE_SEAT_NOT_RES_MSG_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Day Before Reg. Open Seat Not Reserved")
elif message_template_name == 'Batch Start Seat Reserved':
    message_template_plugin_id = "BATCH_START_SEAT_RES_MSG_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Batch Start Seat Reserved")
elif message_template_name == 'Batch Start Seat Not Reserved':
    message_template_plugin_id = "BATCH_START_SEAT_NOT_RES_MSG_PLUGIN_ACTION_ID"
    template_field_responses = get_template_field_responses(template_id="Batch Start Seat Not Reserved")

existing_coupon_code = task_dict_utils.get_single_gof_field_response("CCBP_INTLD_NEW_SCHOLARSHIP_GOF", "CCBP_INTLD_NEW_SCHOLARSHIP_DISCOUNT_COUPON_FIELD")
whatsapp_message_sent_status = task_dict_utils.get_single_gof_field_response("CCBP_INTLD_NEW_LEAD_WHATSAPP_MESSAGE_STATUS_GOF", "CCBP_INTLD_STATUS_FIELD")

if not existing_coupon_code:
    approve_scholarship = method_objects_dict["approve_intensive_lead_scholarship"]
    coupon_code = approve_scholarship(coupon_config_id, task_id)

    task_dict_utils.create_or_update_single_gof_with_field_dict(
        "CCBP_INTLD_NEW_SCHOLARSHIP_GOF", {"CCBP_INTLD_NEW_SCHOLARSHIP_DISCOUNT_COUPON_FIELD": coupon_code}
    )
    scholarship_details_dict = {
        "CCBP_INTLD_NEW_SCHLR_STATUS_FIELD": "Approved & Message sent"
    }
    task_dict_utils.update_field_responses_in_gof_uuid(
        scholarship_details_uuid, scholarship_details_dict
    )
    plugin_service = method_objects_dict["plugin_service"]
    plugin_action_id = message_template_plugin_id
    plugin_service.send_whatsapp_message(
        task_id=task_id, plugin_action_id=plugin_action_id,
        field_responses=template_field_responses
    )