task_dict_utils = method_objects_dict["task_dict_utils"]

stage_moving = task_dict_utils.get_field_response(
    parent_gof_id=None,
    parent_gof_order=None,
    gof_id="CANDIDATES_SELECTION_VIDEO_SUBMISSION_GOF",
    gof_order=0,
    field_id="CANDIDATES_SELECTION_VS_VIDEO_MOVE_TO_FIELD"
)

stage_moving_from_ready = task_dict_utils.get_field_response(
    parent_gof_id="CANDIDATES_SELECTION_READY_TO_EVALUATE_GOF",
    parent_gof_order=0,
    gof_id="CANDIDATES_SELECTION_READY_TO_EVALUATE_GOF",
    gof_order=0,
    field_id="CANDIDATES_SELECTION_READY_TO_EVALUATE_FIELD"
)
if stage_moving_from_ready == "Need 2nd opinion":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_NEED_SECOND_OPINION_STAGE"
elif stage_moving_from_ready == "Ready for 1st evaluation":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_READY_FOR_1ST_EVALUATION_STAGE"
elif stage_moving_from_ready == "Rejected":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_REJECTED_STAGE"
elif stage_moving_from_ready == "Ready to Evaluate":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_READY_TO_EVALUATE_STAGE"
elif stage_moving == "Ready to evaluate":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_READY_TO_EVALUATE_STAGE"
elif stage_moving == "Irrelavant submission":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_IRRELEVANT_SUBMISSION_STAGE"
elif stage_moving == "No access":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_NO_ACCESS_STAGE"
elif stage_moving == "Yet to Clean Submission":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_YET_TO_CLEAN_SUBMISSION_STAGE"