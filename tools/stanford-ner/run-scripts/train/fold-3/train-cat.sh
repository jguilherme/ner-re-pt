#!/bin/bash

java -d64 -Xmx6g -cp ../../stanford-corenlp.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop "../../../props/fold-3/cat.prop"