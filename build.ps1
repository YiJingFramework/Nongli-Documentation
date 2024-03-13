Remove-Item ./build -Recurse
sphinx-build -M html ./source ./build
Read-Host "Enter anything to continue"
Invoke-Item ./build/html
