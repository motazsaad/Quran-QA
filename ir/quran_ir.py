import read_write_qrcd as q_reader
# import gensim

train_data_file = './quranqa/datasets/qrcd_v1.1_train.jsonl'
train = q_reader.load_jsonl(train_data_file)
print(train[0])

for qa in train[:3]:
    verses = qa.get('passage').split('.')
    print(verses)
    question = qa.get('question')
    print(question)


