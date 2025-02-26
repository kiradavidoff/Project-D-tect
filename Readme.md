# Project D-Tect
## Description

## Instalation

### Prerequisite

This project has been developed and tested using **python 3.10.6.**

### Instalation of repository and libraries

#### 1. Clone the GitHub repository
```bash
git clone https://github.com/kiradavidoff/Project-D-tect.git
cd Project-D-tect
```

#### 2. Create virtual environment

```bash
pyenv install 3.10.6 #install python version (if necessary)
pyenv virtualenv 3.10.6 Project-D-tect
pyenv local Project-D-tect
mkdir raw_data #if not added directly
```

#### 3. Downloading required libraries

with `setup.py` :

```bash
pip install .
```
if it doesn't work download it directly from `requirements.txt`:
```bash
pip install -r requirements.txt
```



## Repository structure
project-directory/
│── Data/
    ├── dimensions.csv
│   ├── raw_data
        ├── grid_sizes.csv
        ├── sample_submission.csv
        ├── sixteen_band 
            ├── images.tif
        ├── three_band
            ├── images.tif
            ├──... 
        ├── train_geojson_v3
            ├── image
                ├── category.geojson
                ├──...
            ├──...
│   ├── processed_data
        ├── sixteen_band_geo_proc
            ├── Class 1
            ├── ...
        ├── sixteen_band_proc
        ├── three_band_geo_proc
            ├── Class 1
                ├── category.jpg
            ├── ...
        ├── three_band_prproc
            ├── image.jpg
            ├──  ...
       
│── dtect
    ├── Data_preparation
        ├── preprocessing.py
        ├── transformation.py
    ├── main.py
    ├── Model
        ├── early_stopping.py
        ├── model_1.py
        ├── model_2.py
        ├── model_3.py
        ├── registry.py
        ├── Unet_v0.py
        
├── Notebooks
│── src/
│── README.md
│── main.py

## How to run

1. Data Preparation

``` bash
python dtect/Data_preparation/preprocessing.py  #preprocesing of images
python dtect/Data_preparation/transformation.py #transformation of geojson
```

2. Training model
