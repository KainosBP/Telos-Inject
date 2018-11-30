#!/bin/bash
#
# Script by J.T. Buice - KainosBP.com
#
SUM=0
INPUT=tlos_inject.csv
OLDIFS=$IFS
IFS=,
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read name key liquid cpu bw tokenamt
do
echo /telos/telos2.6/build/programs/teclos/teclos -u http://127.0.0.1:8888 system newaccount -x 100 --transfer --stake-net "\""$bw TLOS"\""  --stake-cpu "\""$cpu TLOS"\"" --buy-ram-kbytes 4 eosio $name $key -f | bash -
#echo /telos2/telos2.5/build/programs/teclos/teclos -u http://127.0.0.1:8888 transfer eosio $name "\""$liquid TLOS"\"" | bash -
done < $INPUT
IFS=$OLDIFS
