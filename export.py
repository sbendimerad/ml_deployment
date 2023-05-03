from joblib import load

from use import feature_USE_fct

pipe = load('trained_use_logreg.joblib')
print(pipe)