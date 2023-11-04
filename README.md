# NLP Project
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Build an LSTM model to generate (predict) Trump speeches</h2>
  <a href="https://www.epf.fr/en">
    <img src="https://upload.wikimedia.org/wikipedia/fr/e/e9/EPF_logo_2021.png" alt="Logo" width="211" height="179">
  </a>
  <p align="center">
    NLP Project done in the context of the EPF NLP course
    <br />
    <a href="https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project/issues">Request Feature</a>
  </p>
</div>

<!-- BADGE -->
</p>
<p align="center">
  <a href="https://www.python.org/">
    <img alt="Python" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
    </a>
<a href="https://www.tensorflow.org/">
  <img alt="Tensor" src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
    </a>
<a href="https://www.tensorflow.org/">
  <img alt="Linkedin" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
    </a>
<a href="https://www.tensorflow.org/">
    <img alt="Keras" src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logoColor=white">
        </a>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents
 
- [NLP Project](#nlp-project)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
  - [Built With](#built-with)
  - [Instructions to run](#instructions-to-run)
  - [Dataset](#dataset)
  - [Model](#model)

<!-- ABOUT THE PROJECT -->
## About The Project

By looking for an intresting dataset to work on, I found a dataset containing all the Rally Speeches of Donald Trump during 2019-2020, so during his second presidential campaign. 
Trump is a controversial person, and I think it can be very funny to be able to generate his speeches, generate speeches for an other context... Create a AI with Trump's """personality"""...

![alt text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHkzMTN4dmYwdWs2anVvNm1vMDV3eXZkNGw4cWZwa2pxM3RvanVkcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L4fv5eLVk6geaVmkaO/giphy.gif)

## Built With

* [Python](https://www.python.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Numpy](https://numpy.org/)

## Instructions to run
 
1. Clone the repo
```sh
git clone https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project.git
```
2. Install the [requirements](https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project/blob/master/requirements.txt)
```sh
pip install -r requirements.txt
```
3. Run the notbooks
For the EDA : Lunch the EDA.ipynb [notebook](https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project/blob/master/EDA.ipynb)

    For the baseline model : Lunch the baseline.ipynb [notebook](https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project/blob/master/baseline.ipynb)

## Dataset

The dataset is composed of 35 speeches of Donald Trump, each speech is in a .txt file. The dataset was found on kaggle : https://www.kaggle.com/christianlillelund/donald-trumps-rallies

Here is an an Exploratory data analysis that I did on the dataset : [EDA](https://github.com/Thibault-GILLARD/Trump_TextGeneration_NLP_Project/blob/master/EDA.ipynb)


## Model
![alt text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW92OWJuMWF0aGY2dmJoZWcxc2wwcDdkcjE3ZjYza2FxZmNwankzYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/w9t0aFMjahdxpKKvzN/giphy.gif)