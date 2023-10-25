A classification system for attacks presented in the UNSW-NB15 dataset (https://research.unsw.edu.au/projects/unsw-nb15-dataset).
The system works to recognize three attacks:
- Exploits;
- Generic;
- Reconnaissance.

The trained models are presdtated in this repository.

The system works as follows:
1) first, the "input.txt" file is filled in, in which it is necessary to specify:
- the name of the models on which we want to test the traffic;
- the threshold value of the probability at which the frame will be classified as an attack;
- the directory where new files are received;
- the time in seconds for which the system goes to sleep;
2) run the system, which will do everything automatically and for each test file will write a resulting json file containing the following information for each frame classified as an attack:
- IP-source;
- IP-destination;
- source port;
- destination port;
- model_name;
- model_probability.

Models were trained using CatBoost, features were selected using feature importance.
On test data, the system shows an accuracy ≈95% for multiclass classification of three attacks among normal traffic.
