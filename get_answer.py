from catboost import CatBoostClassifier
import pandas as pd


def get_final_df(data_for_test, attack_models_names):
    model = CatBoostClassifier()
    final_df = pd.DataFrame()
    for count_models in range(len(attack_models_names)):
        result_for_one_model = [0 for _ in range(len(data_for_test))]
        model.load_model(attack_models_names[count_models], format='cbm')
        proba_for_all_frames = model.predict_proba(data_for_test)
        count_frames = 0
        while count_frames < len(data_for_test):
            result_for_one_model[count_frames] = proba_for_all_frames[count_frames][1]
            count_frames += 1
        final_df.loc[:, attack_models_names[count_models]] = list(result_for_one_model)
    return final_df.T


def get_result_each_frame(data_for_test, attack_models_names, threshold):
    final_df = get_final_df(data_for_test, attack_models_names)
    model_names = final_df.idxmax()
    model_probs = final_df.max()
    for i in range(len(model_probs)):
        if model_probs[i] <= threshold:
            model_names[i] = 'Normal'
    return model_names, model_probs
