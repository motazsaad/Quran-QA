import requests 
import read_write_qrcd as q_reader


train_data_file = '../quranqa/datasets/qrcd_v1.1_train.jsonl'
train = q_reader.load_jsonl(train_data_file)

def prepare_data(data_item):
    result = {}
    result['pq_id'] = data_item['pq_id']
    result['passages'] = [ver.strip() for ver in data_item.get('passages').split('.') if ver.strip()]
    return result



print(train[0])
print(prepare_data(train[0]))
url = 'http://localhost:8983/solr/qa_core/update/json/docs' 
# r = requests.post()