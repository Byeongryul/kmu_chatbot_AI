. src/exe/install.sh

if test $# -eq 1
then
    python src/make_preprocessed_data/create_pretraining_data.py $1
else
    python src/make_preprocessed_data/create_pretraining_data.py
fi