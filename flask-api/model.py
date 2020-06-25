#!/usr/bin/env python
# coding: utf-8

# Import libraries
import joblib
import numpy as np
import pandas as pd
import sklearn
from joblib import dump, load
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler

# Names of columns
columns = ['relative_compactness', 'surface_area', 'wall_area', 'roof_area', 'overall_height',
           'orientation', 'glazing_area', 'glazing_area_distribution', 'heating_load', 'cooling_load']

# Read data
df = pd.read_excel(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx', names=columns, header=0)

# Split data to X and y
X = df.drop(['heating_load', 'cooling_load'], axis=1)
y = df[['heating_load', 'cooling_load']]

# Split to X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)

# Create a standard scaler
scaler = StandardScaler()

# Create an Extra tree regressor with the known best parameters
# {'max_depth': 8, 'min_samples_leaf': 5, 'min_samples_split': 22, 'n_estimators': 44}
etr = ExtraTreesRegressor(max_depth=8, min_samples_leaf=5,
                          min_samples_split=22, n_estimators=44, random_state=0)

# create a pipeline to wrap the scaler and regressor
pipe = make_pipeline(scaler, etr)

# Train the pipeline
pipe.fit(X_train, y_train)

# Saving the model
dump(pipe, 'model.joblib')
