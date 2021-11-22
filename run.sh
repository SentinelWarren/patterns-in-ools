#!/bin/bash
start=`date +%s`

printf "\nRunning the Python version : \n"
pytest pytthon

# printf "\nRunning the Ruby version : \n"

# printf "\nRunning the Java version : \n"

# printf "\nRunning the JavaScript version : \n"

# printf "\nRunning the PHP version : \n"

# printf "\nRunning the Scala version : \n"

# printf "\nRunning the C++ version : \n"

# printf "\nRunning the Go version : \n"

# printf "\nRunning the C# version : \n"

# printf "\nRunning the Kotlin version : \n"

# printf "\nRunning the Dart Version : \n"

# printf "\nRunning the TypeScript version : \n"

# printf "\nRunning the Swift version : \n"

end=`date +%s`
runtime=$((end-start))
printf "\n"
echo "Script ran in $runtime seconds"
