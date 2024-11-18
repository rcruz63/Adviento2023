#!/bin/bash

# Navegar al directorio 'adv2023'
cd adv2023

# Encontrar el directorio con el número más alto 'dia?'
last_day=$(ls -d dia* | sed 's/dia//g' | sort -n | tail -1)


echo "El último día es $last_day"

# Extraer el número del nombre del directorio
last_day_number=${last_day#dia}

echo "El número del último día es $last_day_number"

# Sumar uno al número extraído
new_day_number=$((last_day_number + 1))

echo "El número del nuevo día es $new_day_number"

# Crear un nuevo directorio con el nombre 'dia' seguido del número obtenido
new_day="dia$new_day_number"
mkdir $new_day

cp ../template/README_DIAX_ES.md ../README_DIA${new_day_number}_ES.md
cp ../template/README_DIAX_EN.md ../README_DIA${new_day_number}_EN.md
cp ../template/diaX/diaX.py $new_day/dia${new_day_number}.py
cp ../template/diaX/dataX_1.txt $new_day/data${new_day_number}_1.txt
cp ../template/diaX/dataX_2.txt $new_day/data${new_day_number}_2.txt
cp ../template/diaX/testX_1.txt $new_day/test${new_day_number}_1.txt
cp ../template/diaX/testX_2.txt $new_day/test${new_day_number}_2.txt
# Navegar al nuevo directorio
cd $new_day

# Para cada archivo .py, reemplazar todas las ocurrencias de 'X' en el contenido del archivo por el número obtenido
for file in *.py; do
    sed -i '' "s/X/${new_day_number}/g" "$file"
done

cd ../..