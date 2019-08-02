for file in ./*.py
do
  if [[ -f $file ]]; then
    if [ $file != "./__init__.py" ]; then
      echo "RUNNING TEST: $file"
      python $file -v
    fi
  fi
done
