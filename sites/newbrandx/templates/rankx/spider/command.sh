#!/bin/bash

grep 'g_page_config' output.txt| awk '{for(i=3;i<=NF;i++) print $i}' | tr -d '\n'| sed 's#;##g' >data
