# setup solr inside a docker container 

```
docker pull solr 
docker run --name mysolr -d -p 8983:8983 -v D:\Motaz\solr_vol -t /var/solr
docker exec -it --user=solr mysolr bin/solr create_core -c qa_core
```


