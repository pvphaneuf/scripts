sudo docker run -e --NotebookApp.token='' --user root -e JUPYTER_ENABLE_LAB=yes -p 8888:8888 -v /home/phaneuf:/home/jovyan/work jupyter/datascience-notebook
