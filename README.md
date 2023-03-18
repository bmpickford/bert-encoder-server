# bert-encoder-server

> Expose [sentence_transformers](https://pypi.org/project/sentence-transformers/) as a HTTP server

### Running
`docker-compose up --build -d`

### Usage

#### Single sentence request
```bash
curl -X POST "127.0.0.1:5000/" -d '{ "sentences": ["hello!"] }'
```

#### Single sentence response
```json
{"count":1,"embeddings":[[ <sentence_embedding> ]]}
```

#### Multiple sentence request
```bash
curl -X POST "127.0.0.1:5000/" -d '{ "sentences": ["hello!", "world"] }'
```
```json
{"count":2,"embeddings":[[ <sentence_embedding> ],[ <sentence_embedding> ]]}
```

### Configuration
|Key|Default|Available Options|
|--|--|--|
|MODEL|all-MiniLM-L6-v2|https://huggingface.co/sentence-transformers#models|
|PORT|5000| |