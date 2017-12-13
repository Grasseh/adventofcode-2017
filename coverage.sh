echo "Running coverage.py"
for file in solvers/*
do
    if [ -f "$file" ]
    then
        echo >>$file
        echo "if __name__ == '__main__':" >>$file
        echo "    unittest.main()" >>$file
        python3 -m coverage run -a $file 
    fi
done
echo "Wrote coverage to .coverage"
