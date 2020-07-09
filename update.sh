# The version uploaded by twine must be the same you just created
# (GO CHANGE IT IN SETUP.PY)
sudo python setup.py sdist bdist_wheel
twine upload dist/hepkit-1.1.1*
sudo pip install hepkit --upgrade