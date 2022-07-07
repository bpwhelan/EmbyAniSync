#!/bin/bash
echo "Updating EmbyAniSync"
wget https://github.com/RickDB/EmbyAniSync/archive/master.zip &&\
unzip master.zip &&\
rm master.zip &&\
cp -f /EmbyAniSync-master/*.py /embyanisync
cp -f /EmbyAniSync-master/requirements.txt /embyanisync/requirements.txt
rm -rf /EmbyAniSync-master
cd /embyanisync &&\
python -m pip install -r requirements.txt &&\
cd ..
echo "Update completed successfully"