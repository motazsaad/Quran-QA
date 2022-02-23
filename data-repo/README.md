# Qur'an QA 2022 Shared Task!

This repository contains the following:
* The [*QRCD* (Qur'anic Reading Comprehension Dataset)](https://gitlab.com/bigirqu/quranqa/-/tree/main/datasets)
* A [*reader* script](https://gitlab.com/bigirqu/quranqa/-/tree/main/code) for the dataset.

QRCD is composed of 1,093 tuples of question-passage pairs that are coupled with their extracted answers to constitute 1,337 question-passage-answer triplets. The distribution of the dataset into training, development and test sets is shown below.


| **Dataset** | **%** | **# Question-Passage  Pairs** | **# Question-Passage-Answer  Triplets** |
|-------------|:-----:|:-----------------------------:|:---------------------------------------:|
| Training    |  65%  |              710              |                   861                   |
| Development |  10%  |              109              |                   128                   |
| Test        |  25%  |              274              |                   348                   |
| All         |  100% |              1,093            |                  1,337                  |


To simplify the structure of the dataset, each tuple contains one passage, one question and a list that may contain one or more answers to that question, as shown in [this figure](https://gitlab.com/bigirqu/quranqa/-/blob/main/datasets/README.md). 

The source of the Qur'anic text in QRCD is the [Tanzil project download page](https://tanzil.net/download/), which provides verified versions of the Holy Qur'an in several scripting styles. We have chosen the *simple-clean* text style. 

## Installation

Before executing any of the given scripts, perform the following steps:

1. Clone this project with HTTPS or SSH.

    Clone with HTTPS
    ~~~
    $ git clone https://gitlab.com/bigirqu/quranqa.git
    ~~~

    Clone with SSH
    ```
    $ git clone git@gitlab.com:bigirqu/quranqa.git
    ```

2. Create a virtual environment for the project using venv or conda and activate it.


3. pip install the packages in the ['requirements.txt'](https://gitlab.com/bigirqu/quranqa/-/blob/main/requirements.txt).

    ```
    $ pip install -r /path/to/requirements.txt
    ```

## [Reader script](https://gitlab.com/bigirqu/quranqa/-/blob/main/code/read_write_qrcd.py)

The script simply reads the tuples in the **JSONL** formated QRCD dataset into object instances of the `PassageQuestion` class and  then writes them back to another JSONL file. 

To execute the reader script:

    ```
    python read_write_qrcd.py
        --input_file=.../datasets/qrcd_v1.1_train.jsonl
        --output_file=.../temp_file.jsonl
    ```

