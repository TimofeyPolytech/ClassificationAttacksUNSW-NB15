import os
import pandas as pd
import data_preproccesing as dp
import get_answer as ga
import result_info as ri
import parse_input as pi
import time


models_for_check, threshold, directory_with_test_files, time_to_check_new_files = pi.parse_file()

checked_files = []

while True:
    all_files = os.listdir(directory_with_test_files)
    flag_system_worked = 0

    for file in all_files:
        if os.path.splitext(file)[1] == '.csv':
            if file not in checked_files:
                checked_files.append(file)
                data = pd.read_csv(directory_with_test_files + '\\' + file, sep=',')
                data, src_ip, dst_ip, src_port, dst_port = dp.data_preproc(data)
                triggered_model, triggered_model_proba = ga.get_result_each_frame(data, models_for_check, threshold)
                ri.write_result_info(src_ip, dst_ip, src_port, dst_port, triggered_model, triggered_model_proba,
                                     directory_with_test_files + '\\' + os.path.splitext(file)[0])
                flag_system_worked = 1
    if flag_system_worked == 1:
        continue
    else:
        time.sleep(time_to_check_new_files)
