# model1.py
import pandas as pd
import numpy as np

#Path: /Users/boncui/Desktop/Projects/Personal Projects/brain-tumor/data/brain_tumor_dataset.csv
data = pd.read_csv("../data/brain_tumor_dataset.csv")

#Let's do some fucking data exploration
# print(data.head())
# print(data.info)
print(data.columns)

"""
   Patient_ID  Age  Gender Tumor_Type  Tumor_Size  Location        Histology  ... Surgery_Performed Chemotherapy Survival_Rate Tumor_Growth_Rate Family_History MRI_Result Follow_Up_Required
0           1   73    Male  Malignant    5.375612  Temporal      Astrocytoma  ...                No           No     51.312579          0.111876             No   Positive                Yes
1           2   26    Male     Benign    4.847098  Parietal     Glioblastoma  ...               Yes          Yes     46.373273          2.165736            Yes   Positive                Yes
2           3   31    Male     Benign    5.588391  Parietal       Meningioma  ...                No           No     47.072221          1.884228             No   Negative                 No
3           4   29    Male  Malignant    1.436600  Temporal  Medulloblastoma  ...                No          Yes     51.853634          1.283342            Yes   Negative                 No
4           5   54  Female     Benign    2.417506  Parietal     Glioblastoma  ...                No          Yes     54.708987          2.069477             No   Positive                Yes

<bound method DataFrame.info of        Patient_ID  Age  Gender Tumor_Type  Tumor_Size  Location        Histology  ... Surgery_Performed Chemotherapy Survival_Rate Tumor_Growth_Rate Family_History MRI_Result Follow_Up_Required
0               1   73    Male  Malignant    5.375612  Temporal      Astrocytoma  ...                No           No     51.312579          0.111876             No   Positive                Yes
1               2   26    Male     Benign    4.847098  Parietal     Glioblastoma  ...               Yes          Yes     46.373273          2.165736            Yes   Positive                Yes
2               3   31    Male     Benign    5.588391  Parietal       Meningioma  ...                No           No     47.072221          1.884228             No   Negative                 No
3               4   29    Male  Malignant    1.436600  Temporal  Medulloblastoma  ...                No          Yes     51.853634          1.283342            Yes   Negative                 No
4               5   54  Female     Benign    2.417506  Parietal     Glioblastoma  ...                No          Yes     54.708987          2.069477             No   Positive                Yes
...           ...  ...     ...        ...         ...       ...              ...  ...               ...          ...           ...               ...            ...        ...                ...
19995       19996   21    Male  Malignant    9.612013  Parietal  Medulloblastoma  ...                No          Yes     58.229662          0.353806             No   Negative                Yes
19996       19997   32  Female     Benign    1.543560  Temporal       Meningioma  ...               Yes           No     77.706856          2.341074             No   Positive                 No
19997       19998   57  Female     Benign    3.618634  Temporal  Medulloblastoma  ...                No          Yes     89.543803          2.332881             No   Positive                Yes
19998       19999   68    Male  Malignant    8.519086  Parietal     Glioblastoma  ...               Yes          Yes     83.306781          2.387202             No   Positive                 No
19999       20000   61    Male     Benign    9.716768  Temporal  Medulloblastoma  ...                No           No     47.433468          2.464077            Yes   Negative                Yes

"""

data_columns =['Patient_ID', 'Age', 'Gender', 'Tumor_Type', 'Tumor_Size', 'Location',
       'Histology', 'Stage', 'Symptom_1', 'Symptom_2', 'Symptom_3',
       'Radiation_Treatment', 'Surgery_Performed', 'Chemotherapy',
       'Survival_Rate', 'Tumor_Growth_Rate', 'Family_History', 'MRI_Result',
       'Follow_Up_Required'
       ]

#NOTES


