#!/usr/bin/env bash

printf "rmarkdown::render('credit-scoring-exam-01.Rmd', output_format='pdf_document')" | R --vanilla --quiet
