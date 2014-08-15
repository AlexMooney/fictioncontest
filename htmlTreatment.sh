#!/bin/bash
for f in 20*html; do grep " class=\"contest\"" $f | html2markdown | sed 's/!\[#\].*\.png)//' > $f.txt; done
