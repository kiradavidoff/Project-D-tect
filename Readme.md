# Project D-Tect
## Description

**D-Tect** is a machine learning project to segment satellite images to recognize categories such as buildings, roads, and water sources. The segmentation task was accomplished using a U-Net architecture, a type of deep learning model well-suited for image segmentation.

The project was completed in a 10-day period as part of the Le Wagon Data Science and AI Bootcamp, where we applied various techniques from data preprocessing to model training, testing, and evaluation.

This project was made by:
- Kira Davidoff
- Guillaume Lugol
- Malo Guede
- Paul Diguet



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
│   ├── raw_data/
        ├── grid_sizes.csv
        ├── sample_submission.csv
        ├── sixteen_band/
            ├── images.tif
        ├── three_band/
            ├── images.tif
            ├──... 
        ├── train_geojson_v3/
            ├── image/
                ├── category.geojson
                ├──...
            ├──...
│   ├── processed_data/
        ├── sixteen_band_geo_proc/
            ├── Class 1
            ├── ...
        ├── sixteen_band_proc/
        ├── three_band_geo_proc/
            ├── Class 1
                ├── category.jpg
            ├── ...
        ├── three_band_prproc/
            ├── image.jpg
            ├──  ...
       
│── dtect/
    ├── Data_preparation/
        ├── preprocessing.py
        ├── transformation.py
    ├── main.py
    ├── Model/
        ├── early_stopping.py
        ├── model_1.py
        ├── model_2.py
        ├── model_3.py
        ├── registry.py
        ├── Unet_v0.py
        
├── Notebooks/
│── Requirements.py
│── setup.py
│── README.md


## Data

### Downloading Data

```bash
# Go to the raw data
cd ~/raw_data

# Download the dataset 
kaggle competitions download -c dstl-satellite-imagery-feature-detection #assuming kaggle API already sorted

```

### Data structure

│── Data/
    ├── dimensions.csv
│   ├── raw_data/
        ├── grid_sizes.csv
        ├── sample_submission.csv
        ├── sixteen_band/
            ├── images.tif
        ├── three_band/
            ├── images.tif
            ├──... 
        ├── train_geojson_v3/
            ├── image/
                ├── category.geojson
                ├──...
            ├──...
│   ├── processed_data/ 
        ├── sixteen_band_geo_proc/
            ├── Class 1
            ├── ...
        ├── sixteen_band_proc/
        ├── three_band_geo_proc/
            ├── Class 1
                ├── category.jpg
            ├── ...
        ├── three_band_prproc/
            ├── image.jpg
            ├──  ...

--> To get processed data go to data preparation section \
--> As of now we only work with three_band images 

## Models
| Model Name | Description |
|----------|----------|
| model_1   |Baseline Autoencoder/ Decoder model (not used in final training) | 
| model_3  | Initial UNET model [1] (not used in final training)  | 
| UNet_v0  | Final UNET model [1] |



## How to run

### 1. Data Preparation

``` bash
python dtect/Data_preparation/preprocessing.py  #preprocesing of images
python dtect/Data_preparation/transformation.py #transformation of geojson
```

### 2. Training model 

``` bash
python dtect/main.py
```

## License

Data License:  https://www.kaggle.com/competitions/dstl-satellite-imagery-feature-detection/rules#7-competition-data 

## References
[1] Erdem, Fırat, and Uğur Avdan. "Comparison of different U-net models for building extraction from high-resolution aerial imagery." International Journal of Environment and Geoinformatics 7.3 (2020): 221-227.

