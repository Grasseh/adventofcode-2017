echo "Running coverage.py"
for file in solvers/*
do
    if [ -f "$file" ]
    then
        python3 -m coverage run -a $file --exclude=numpy/*
    fi
done
echo "Wrote coverage to .coverage"
