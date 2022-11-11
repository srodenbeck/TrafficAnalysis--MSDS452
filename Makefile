conda_install:
	conda env create -f environment.yaml
virtual_install:
	python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
format:
	black *.ipynb
lint:
