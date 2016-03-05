countryArray=()
while IFS=$'\t' read c; do
        countryArray+=("$c")                                                       
done

for i in "${!countryArray[@]}" ; do
    if [[ "${countryArray[$i]}" =~ [aA] ]] ; then 
        unset countryArray[$i]
    fi
  done

if [ "${#countryArray[@]}" -eq 0 ] ; then
    echo ""
else 
    for c in "${countryArray[@]}" ; do
        echo "$c"
    done
fi