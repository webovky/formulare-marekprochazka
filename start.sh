#!/bin/sh
# * nainstaluje virtuální prostředí
# * nainstaluje závislosti přes PIP
# * zakáže v Gitu .env
# * smaže se
############################################################

DIRNAME=$(dirname $0)

cd $DIRNAME

python3 -m venv .venv-${DIRNAME}
source .venv-${DIRNAME}/bin/activate
pip install -U pip
pip install -r requirements.txt


git rm --cached .env

echo "Můžu se smazat? Y/n"
read anone
if [[ $anone != n ]]; then
    echo rm $0
else
    echo "... no dobře, ale být tebou, tak bych mě vymazal!"
fi
