#!/bin/bash

for r in {0..3}
do
	python "../src/split_train_test.py" "../outputs/sigarra-corpus-clean.xml" "sigarra" $r
done