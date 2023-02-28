#!/bin/bash
cd models
source venv/scripts/activate
python setup.py sdist bdist_wheel

cp -r -f build dist pydantic_mongo_reusables.egg-info ../backend
cp -r -f build dist pydantic_mongo_reusables.egg-info ../data

cd ..
cd data
source venv/scripts/activate
# the version number must be updated when there is a newer version
pip install --upgrade dist/pydantic_mongo_reusables-0.1.1-py3-none-any.whl

cd ..
cd backend
source venv/scripts/activate
# the version number must be updated when there is a newer version
pip install --upgrade dist/pydantic_mongo_reusables-0.1.1-py3-none-any.whl
