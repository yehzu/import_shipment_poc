BASE=$1

cd $BASE
mkdir -p adapters entities factories ports/gateways ports/in_bound ports/out_bound presenters use_cases
touch adapters/__init__.py entities/__init__.py factories/__init__.py ports/gateways/__init__.py ports/in_bound/__init__.py ports/out_bound/__init__.py presenters/__init__.py use_cases/__init__.py

