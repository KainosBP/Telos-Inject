#!/bin/bash
INPUT=tlos_genesis_snapshot_inject.csv
OLDIFS=$IFS
IFS=,
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read line eth name token stake liquid key
do
echo /telos2/telos2.3/build/programs/teclos/teclos -u http://127.0.0.1:8889 system newaccount -x 100 --transfer --stake-net "\""$stake TLOS"\""  --stake-cpu "\""$stake TLOS"\"" --buy-ram-kbytes 4 eosio $name $key -f | bash -
#echo /telos2/telos2.2/build/programs/teclos/teclos -u http://127.0.0.1:8889 transfer eosio $name "\""$liquid TLOS"\"" | bash -
done < $INPUT
IFS=$OLDIFS
