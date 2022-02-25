task_dict_utils = method_objects_dict["task_dict_utils"]

field_one_score = getting_first_field_average_score()
field_two_score = getting_second_field_average_score()
field_three_score = getting_third_field_average_score()
field_four_score = getting_fourth_field_average_score()
field_five_score = getting_fifth_field_average_score()
field_six_score = getting_sixth_field_average_score()
field_seven_score = getting_seventh_field_average_score()
field_eight_score = getting_eighth_field_average_score()
field_nine_score = getting_ninth_field_average_score()
field_ten_score = getting_tenthth_field_average_score()

sum_of_total_fields = float(field_one_score)+float(field_two_score)+float(field_three_score)+float(field_four_score)+float(field_five_score)+float(field_six_score)+float(field_seven_score)+float(field_eight_score)+float(field_nine_score)+float(field_ten_score)
if sum_of_total_fields > 0:
    average_score_of_all_fields = float(sum_of_total_fields/10)
else:
    average_score_of_all_fields = 0
return round(average_score_of_all_fields, 2)