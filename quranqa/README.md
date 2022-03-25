# Qur'an QA 2022 Shared Task!

This repository contains the following:
* The [*QRCD* (Qur'anic Reading Comprehension Dataset)](https://gitlab.com/bigirqu/quranqa/-/tree/main/datasets)
* A [*reader* script](https://gitlab.com/bigirqu/quranqa/-/tree/main/code) for the dataset.
* A [*submission checker* script]( https://gitlab.com/bigirqu/quranqa/-/tree/main/code) for checking the correctness of run files to be submitted. 
* An [*evaluation* (or *scorer*) script]( https://gitlab.com/bigirqu/quranqa/-/tree/main/code).

QRCD is composed of 1,093 tuples of question-passage pairs that are coupled with their extracted answers to constitute 1,337 question-passage-answer triplets. The distribution of the dataset into training, development and test sets is shown below.


| **Dataset** | **%** | **# Question-Passage  Pairs** | **# Question-Passage-Answer  Triplets** |
|-------------|:-----:|:-----------------------------:|:---------------------------------------:|
| Training    |  65%  |              710              |                   861                   |
| Development |  10%  |              109              |                   128                   |
| Test        |  25%  |              274              |                   348                   |
| All         |  100% |              1,093            |                  1,337                  |


To simplify the structure of the dataset, each tuple contains one passage, one question and a list that may contain one or more answers to that question, as shown in [this figure](https://gitlab.com/bigirqu/quranqa/-/blob/main/datasets/README.md). 

Each Qur’anic passage in *QRCD* may have more than one occurrence; and each *passage occurrence* is paired with a different question. Likewise, each question in *QRCD* may have more than one occurrence; and each *question occurrence* is paired with a different Qur’anic passage.

The source of the Qur'anic text in QRCD is the [Tanzil project download page](https://tanzil.net/download/), which provides verified versions of the Holy Qur'an in several scripting styles. We have chosen the *simple-clean* text style. 
