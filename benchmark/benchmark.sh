MAX_PB=26
COUNTER=2
PB_TEMPLATE=example/1-playbook.yml

cd $(git rev-parse --show-toplevel)

cp src/withdocker/*docker-compose* .git/hooks/
cp src/withdocker/pre-commit-hook.example .git/hooks/pre-commit-docker
cp src/nodocker/pre-commit-hook.example .git/hooks/pre-commit-nodocker

BM_FILE=benchmark/benchmark.$(date +"%Y.%m.%d.%H.%M")
echo playbooks,docker-real,docker-user,docker-sys,nodocker-real,nodocker-user,nodocker-sys > $BM_FILE

while [ $COUNTER -lt $MAX_PB ]
do

  echo "Run $COUNTER"

  PB="example/$COUNTER-playbook.yml"
  if [ ! -f $PB ]
  then
    cp $PB_TEMPLATE $PB
  fi
  git add $PB
  
  DOCKER_BM_TIMES=$((time .git/hooks/pre-commit-docker) 2>&1 > benchmark/benchmark-docker-${COUNTER}.err.log | grep -oP "\d+[.]\d+" | awk '{ printf ","$0 }')
  NODOCKER_BM_TIMES=$((time .git/hooks/pre-commit-nodocker) 2>&1 > benchmark/benchmark-nodocker-${COUNTER}.err.log | grep -oP "\d+[.]\d+" | awk '{ printf ","$0 }')

  echo $COUNTER$DOCKER_BM_TIMES$NODOCKER_BM_TIMES >> $BM_FILE

  COUNTER=$((COUNTER + 1))

done
