import configparser


def parse_file():
    parser = configparser.ConfigParser()
    parser.read("input_file.txt")

    models_for_check = parser.get("input", "models_for_check")
    threshold = parser.get("input", "threshold")
    directory_with_test_files = parser.get("input", "directory_with_test_files")
    time_to_check_new_files = parser.get("input", "time_to_check_mew_files")

    models_for_check = models_for_check.split(', ')
    threshold = float(threshold)
    time_to_check_new_files = int(time_to_check_new_files)

    return models_for_check, threshold, directory_with_test_files, time_to_check_new_files
