countryArray=()
while IFS=$'\t' read c; do
        countryArray+=("$c")                                                       
done
dotArray=("${countryArray[@]/[A-Z]/\.}")
echo ${dotArray[@]}