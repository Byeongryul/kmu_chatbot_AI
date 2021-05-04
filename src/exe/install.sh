if test -d myvenv
then
    echo "exist"
    . myvenv/Scripts/activate
else
    echo "not exist"
    py -3.7 -m venv myvenv
    . myvenv/Scripts/activate
fi

cd requirements
pip install --upgrade -r requirements.txt
cd ..