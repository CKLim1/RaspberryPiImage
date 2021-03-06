#!/bin/bash
# setgroup.sh groupname
# Set the group name in /etc/hosts, /etc/hostname and /home/pi/TP-IoT/*.py

#test="/Users/Luppy/Raspberry Pi"
test=""

# Update hosts and hostname files.
groupname="${1:?Specify a group name e.g. g88}"
file1="${test}/etc/hosts"
file2="${test}/etc/hostname"

echo sudo sed -i.bak s/g88/${groupname}/g "${file1}"
echo sudo sed -i.bak s/g88/${groupname}/g "${file2}"

sudo sed -i.bak s/g88/${groupname}/g "${file1}"
sudo sed -i.bak s/g88/${groupname}/g "${file2}"

echo Updated group ${groupname} in ${file1}, ${file2}

# Update all files in /home/pi/TP-IoT.
shopt -s nullglob
FILES=/home/pi/TP-IoT/*.py
for f in $FILES
do
  # Change the old style g88_pi naming to g88pi.
  echo sed -i s/g88_/${groupname}/g "${f}"
  sed -i s/g88_/${groupname}/g "${f}"

  # Change the new style g88pi naming.
  echo sed -i s/g88/${groupname}/g "${f}"
  sed -i s/g88/${groupname}/g "${f}"
done

# Check server for any updates.
cd /tmp
curl https://raw.githubusercontent.com/lupyuen/AWSIOT/master/update/update.sh>update.sh
chmod +x update.sh
./update.sh
