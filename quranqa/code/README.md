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

## [Submission checker script](https://gitlab.com/bigirqu/quranqa/-/blob/main/code/quranqa22_submission_checker.py)

It is mandatory to use this script to verify your ***run file*** (prior to submission) with respect to the file name, the correctness of its format, utf-8 encoding, number of answers per question (not to exceed 5), names of the key fields, etc. 

The expected run file is in **JSON** format. It has a list of passage-question ids (pq_id) along with their respective ranked lists of returned answers. For each passage-question pair, the system should return **up to 5** predicted answers, along with their ranks and estimated scores. Only the **ranks** are used in the evaluation (**not** the estimated scores). The run file format is shown below.

The name of each submitted run file should follow the below **naming format**. 

<**TeamID_RunID.json**>

such that:

* **TeamID** can be an alphanumeric with a length between 3 and 9 characters

* **RunID**  can be an alphanumeric with a length between 2 and 9 characters

For example, *bigIR_run01.json*

#### Format of the Run File

~~~
{
    "38:41-44_105": [
        {
            "answer": "أيوب",
            "rank": 1,
            "score": 0.9586813087043423
        },
        {
            "answer": "إنه أواب",
            "rank": 2,
            "score": 0.014768138560114058
        },
        {
            "answer": "ولا تحنث إنا وجدناه صابرا نعم العبد إنه أواب",
            "rank": 3,
            "score": 0.0052241458173706255
        },
        {
            "answer": "واذكر عبدنا أيوب",
            "rank": 4,
            "score": 0.0026888978292958256
        },
        {
            "answer": "ولا تحنث إنا وجدناه صابرا",
            "rank": 5,
            "score": 0.002568017979036094
        }
    ],
    "74:32-48_330": [
        {
            "answer": "كل نفس بما كسبت رهينة",
            "rank": 1,
            "score": 0.7335555760226602
        },
        {
            "answer": "لمن شاء منكم أن يتقدم أو يتأخر . كل نفس بما كسبت رهينة",
            "rank": 2,
            "score": 0.19330937303913176
        },
        {
            "answer": "لمن شاء منكم أن يتقدم أو يتأخر",
            "rank": 3,
            "score": 0.07103693247802075 
        }     
    ]    
}
~~~
Here is an example of executing the submission checker script:

```
python quranqa22_submission_checker.py
    --run_file= .../runs/teamId_run01.json
```

## [Evaluation (scorer) script](https://gitlab.com/bigirqu/quranqa/-/blob/main/code/quranqa22_eval.py)

This task is evaluated as a ranking task. To give credit to a QA system that may retrieve an answer (not necessarily at the first rank) that does not fully match one of the gold answers but partially matches it, we use **partial Reciprocal Rank** (**pRR**) measure [1]. It is a variant of the traditional Reciprocal Rank evaluation metric that considers partial matching. pRR is the **official** evaluation measure of this shared task.

We will also report **Exact Match** (**EM**) and **F1@1**, which are evaluation metrics applied only on the top predicted answer. The EM metric is a binary measure that rewards a system only if the top predicted answer exactly matches one of the gold answers. Whereas, the F1@1 metric measures the token overlap between the top predicted answer and the best matching gold answer [2].

To get an overall evaluation score, each of the above measures is averaged over all questions. 

Here is an example of executing the evaluation script:

```
python quranqa22_eval.py
    --gold_answers_file=.../datasets/qrcd_v1.1_dev.jsonl
    --run_file=.../runs/teamId_run01.json
```

## References
[1] Malhas, R. and Elsayed, T. [AyaTEC: Building a Reusable Verse-Based Test Collection for Arabic Question Answering on the Holy Qur’an.](https://dl.acm.org/doi/abs/10.1145/3400396?casa_token=Ob_vJqUxU9sAAAAA:hN1Bq2_VSfPYsAFZdJvzFbe4GkkjG-bA-wNN0Bo6AiNAytpeafqg2Y6_FvWSbfjQirsW1sHAQhBs-w) ACM Transactions on Asian and Low-Resource Language Information Processing (TALLIP), 19(6), pp.1-21, 2020.

[2] Rajpurkar, P., Zhang, J., Lopyrev, K. and Liang, P. [SQuAD: 100, 000+ Questions for Machine Comprehension of Text.](https://aclanthology.org/D16-1264/) In EMNLP 2016.
