recid=$(cat repo/recid.txt)
echo $recid
cernopendata-client get-file-locations --recid $recid --protocol xrootd > repo/production_output.txt