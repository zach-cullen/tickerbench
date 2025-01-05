
# Running Locally

## Prerequisites
* python 3.8
* venv
* make

### Install dependencies
```
make install
```

### Start the collector
```
make run
```

### Trigger the collector by http
```
curl -X POST http://localhost:5000/run_collector
```
