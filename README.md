## Process To Run The Application

STEP 1

clone the repository onto your local machine


STEP 2

open anaconda prompt

STEP 3

To create a conda environment run the following command on anaconda prompt.

```
conda create -n eda python=3.7.9
```

STEP 4

To activate the environment

```
conda activate eda
```

STEP 5

Install the necessary libraries

```
pip install -r requirements.txt
```

STEP 6

Run the application

```
streamlit run app.py
```

STEP 7 (Optional)

Use the dataset called Automobile_data.csv from the repository to view the functioning of comprehensive data analysis. Otherwise due to a large number of rows and columns, the generated reports may take time.


### Deployed App

The app can also be viewed using this link, but comprehensive data analysis of larger datasets is not possible due to memory constraints. So it is better to use the above method and run the app through a local machine.

https://share.streamlit.io/charvijindal/automobile_trends/app.py

