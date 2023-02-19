# build_files.sh
MYFILE="$(dirname "$(realpath "$0")")" + 'requirements.txt'
pip install -r MYFILE
python3.9 manage.py collectstatic