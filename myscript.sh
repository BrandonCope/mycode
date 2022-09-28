#!/bin/bash

#prompts user
promptUser(){
    echo "Input your name to create User, then press enter to add user: "
    read USR
    echo "What group does the user belong to?"
    read GRP
}

#creating user/group and adding user to group
createUser(){
#creates user
echo "-------------------------"
echo "Creating User!"
echo "-------------------------"
sleep 1
sudo useradd $USR
id $USR
echo ""

#creates group
echo "-------------------------"
echo "Creating group!"
echo "-------------------------"
sleep 1
sudo groupadd $GRP
echo ""

#modifies user to append to group
echo "-------------------------"
echo "Adding $USR to $GRP"
echo "-------------------------"
sleep 1
sudo usermod -aG $GRP $USR
echo ""

#inform user process was complete
echo "-------------------------"
echo "Congrats $USR was added to $GRP.  Process Compelete!"
echo "-------------------------"
id $USR
echo ""
}

#prompts user to end session
quit(){
    echo "Would you like to end the session? (Type exit)"
    read QUIT
}

#controls order, and loops until user decides to quit
while [ "$QUIT" != "exit" ]
do
    promptUser
    quit
    createUser
done

echo "Thank you for using our services!"
