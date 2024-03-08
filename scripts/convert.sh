#!/usr/bin/bash

source /group/clas12/packages/setup.sh
module load clas12/pro
module load java


/group/clas12/packages/graalvm/22.2.0_java17/bin/java -DCLAS12DIR=$COATJAVA -cp /volatile/clas12/sangbaek/fastMC/clas12fastMC/target/*:$COATJAVA/lib/clas/*:$COATJAVA/lib/utils/* clas12.fastMC.ProcessMC -convert $1 -o $1.hipo
/group/clas12/packages/graalvm/22.2.0_java17/bin/java -DCLAS12DIR=$COATJAVA -cp /volatile/clas12/sangbaek/fastMC/clas12fastMC/target/*:$COATJAVA/lib/clas/*:$COATJAVA/lib/utils/* clas12.fastMC.ProcessMC -fastmc $1.hipo -o $1.fastmc.hipo
