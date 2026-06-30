greeting(){
    echo Hello $1
    echo Hello $2
    echo Hello $1 and $2
    echo Hello $3 # $3 does not exist 
}

greeting 'Peter' 'Fernando'