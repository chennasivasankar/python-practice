task_dict_utils = method_objects_dict["task_dict_utils"]
stage_moving_from_ready = task_dict_utils.get_field_response(
    parent_gof_id=None,
    parent_gof_order=None,
    gof_id="CANDIDATES_SELECTION_2_VIDEO_SUBMISSION_RATING_GOF",
    gof_order=0,
    field_id="CS_2_VIDEO_SUBMISSION_MOVE_TO_FIELD"
)

video_evaluation_score = total_score_of_first_evelation_score(
    task_dict_utils=task_dict_utils
)

average_score = get_2nd_video_evaluation_average_score(
    task_dict_utils=task_dict_utils
)
task_dict_utils.update_or_create_field_with_response(
    parent_gof_id=None,
    parent_gof_order=None,
    gof_id="CS_2_VIDEO_SUBMISSION_TOTAL_SCORE_GOF",
    gof_order=0,
    field_id="CANDIDATES_SELECTION_2_VID_AVERAGE_RATINGS_FIELD",
    response=average_score
)
total_average_score = 0
div_average_1and_2 = 0
if average_score:
    total_average_score += average_score
    div_average_1and_2 += 1
if video_evaluation_score:
    total_average_score += video_evaluation_score
    div_average_1and_2 += 1
if total_average_score:
    overall_rating = round(total_average_score/div_average_1and_2, 2)
task_dict_utils.update_or_create_field_with_response(
    parent_gof_id=None,
    parent_gof_order=None,
    gof_id="CS_2_VIDEO_SUBMISSION_TOTAL_SCORE_GOF",
    gof_order=0,
    field_id="CANDIDATES_SELECTION_2_VID_OVERALL_RATING_FIELD",
    response=overall_rating
)

if stage_moving_from_ready == "Ready for 2nd evaluation":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_READY_FOR_2ST_EVALUATION_STAGE"
elif stage_moving_from_ready == "Rejected":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_REJECTED_STAGE"
elif stage_moving_from_ready == "Ready for final evaluation":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_READY_FOR_FINAL_EVALUATION_STAGE"
elif stage_moving_from_ready == "Ready to Evaluate":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_READY_TO_EVALUATE_STAGE"
elif stage_moving_from_ready == "Ready For 1st Evaluation":
    task_dict["status_variables"]["Status1"] = "CANDIDATES_SELECTION_READY_FOR_1ST_EVALUATION_STAGE"