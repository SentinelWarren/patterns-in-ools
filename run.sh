#!/bin/bash
start=`date +%s`

printf "\nRunning Python version tests : \n"
python3 -m pytest python/

# printf "\nRunning Ruby version tests : \n"

# printf "\nRunning Java version tests : \n"

# printf "\nRunning JavaScript version tests : \n"

# printf "\nRunning PHP version tests : \n"

# printf "\nRunning Scala version tests : \n"

# printf "\nRunning C++ version tests : \n"

# printf "\nRunning Go version tests : \n"

# printf "\nRunning C# version tests : \n"

# printf "\nRunning Kotlin version tests : \n"

# printf "\nRunning Dart version tests : \n"

# printf "\nRunning TypeScript version tests : \n"

# printf "\nRunning Swift version tests : \n"

end=`date +%s`
runtime=$((end-start))
printf "\n"
echo "Script ran in $runtime seconds"
