FROM jupyter/datascience-notebook

USER root

COPY requirements.txt /tmp/

RUN apt update -y && apt install yarn -y && apt-get update -y && sudo apt-get install nodejs npm -y --no-install-recommends \
    && apt-get -y clean \
    && pip install -r /tmp/requirements.txt \
#    && jupyter labextension install @jupyterlab/toc \ # runtime error
    && jupyter serverextension enable --py jupyterlab

# matplotlib font
COPY font/ipaexg.ttf /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/
RUN echo font.family : IPAexGothic > /home/jovyan/.config/matplotlib/matplotlibrc && \
    rm /home/jovyan/.cache/matplotlib/fontlist-v310.json

# jupyterlab theme setting
RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension && \
    echo '{"theme":"JupyterLab Dark", "theme-scrollbars": true}' > \
     /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings
     
