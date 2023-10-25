import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

path_to_file = input("Введите путь до файла, содержащего обучающие данные: ")
df = pd.read_csv(path_to_file, sep=',')
df = df.drop(columns='id')
new_df = df[df['attack_cat'] == 'Normal']
new_df = new_df.reset_index()
new_df = new_df.drop(columns='index')
normal = new_df
attack = df[df['attack_cat'] == 'Exploits']
attack = attack.reset_index()
attack = attack.drop(columns='index')
normal = normal.drop(columns='attack_cat')
attack = attack.drop(columns='attack_cat')
data = pd.concat([attack, normal.sample(n=len(attack))], ignore_index=True)
data = data[['sttl', 'smean', 'sbytes', 'dmean', 'proto', 'dload', 'ct_srv_dst', 'ct_dst_src_ltm', 'ct_srv_src',
                     'sloss', 'service', 'trans_depth', 'ackdat', 'ct_flw_http_mthd', 'synack', 'dwin', 'dbytes',
                     'sload', 'ct_state_ttl', 'dur', 'dttl', 'ct_dst_sport_ltm', 'dloss', 'tcprtt',
                     'response_body_len', 'sjit', 'sinpkt', 'ct_src_dport_ltm', 'djit', 'ct_dst_ltm', 'stcpb', 'dpkts',
                     'state', 'swin', 'dinpkt', 'spkts', 'dtcpb', 'ct_src_ltm', 'label']]
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = CatBoostClassifier(iterations=70, learning_rate=0.06, depth=5, random_seed=0, cat_features=['proto', 'service', 'state'])
model.fit(X_train, y_train)
preds = model.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, preds))
print("Precision: ", precision_score(y_test, preds))
print("Recall: ", recall_score(y_test, preds))
print("F1_score: ", f1_score(y_test, preds))
