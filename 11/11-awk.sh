cat ../hightemp.txt | awk '{gsub("\t", " ", $0); print $0}'
