.PHONY: env
env:

conda env create -f environment.yml 
conda activate ligo
python -m ipykernel install --user --name ligo --display-name "IPython Ligo(2.7)"


.PHONY: html
html:

jupyter-book build .


.PHONY: html-hub
html-hub:

jupyter-book config sphinx .
sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
cd _build/html 
python -m http.server


.PHONY: clean
clean:

@echo "Deleting png image files in figures."
rm -f figurs/*.png
@echo "Deleting the wav audio files in adudio."
rm -f audio/*.wav
@echo "Deleting the data files."
rm -rf data/*
@echo "Cleaning _build folder."
rm -rf _build/*