echo  "{ \"type\": \"FeatureCollection\", \"features\": [" > $2

#query tramos
cat $1 |  jq -c '. | {"type": "Feature","geometry" :{"type": "Point","coordinates":[.loc[0],.loc[1]]},"properties":{_id,city,pop,state}}' >> $2

#close GeoJSON
echo "]}" >> $2

#add comas
sed -i '' 's/$/,/g' $2