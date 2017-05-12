MAX_PB=26
COUNTER=2

while [ $COUNTER -lt $MAX_PB ]
do

  PB="../example/$COUNTER-playbook.yml"
  if [ -f $PB ]
  then
    rm $PB
  fi

  COUNTER=$((COUNTER + 1))

done
