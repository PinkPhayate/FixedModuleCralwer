# FixedModuleCrawler

## Discription
This repository extracts fixed module(that had bug).

## Target Software
- Apache Solr
	- we can get module name, that is fixed in each version-up, written in [this web] (https://lucene.apache.org/solr/7_0_1/changes/Changes.html)

## Environment

- python above 3.6
- required module is revealed in requirement.txt

## command example
```
# Extract in all versions
python crawler_solr_main.py

# Extract specified one version 
python src/crawler_solr_main.py spec v6.6.0
```

