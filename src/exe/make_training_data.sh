. src/exe/install.sh

if test $# -eq 1
then
   python src/make_preprocessed_data/create_training_data.py $1
elif test $# -eq 2
then
   python src/make_preprocessed_data/create_training_data.py $1 $2

else
   python src/make_preprocessed_data/create_training_data.py
fi

