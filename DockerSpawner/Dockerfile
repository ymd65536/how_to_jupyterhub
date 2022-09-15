FROM jupyterhub/jupyterhub@sha256:d06deb798fd3a7201cdb5bc186ce4ef0a190ab9cd6937cce16c4a2d456dddd43
COPY requirements.txt /tmp/requirements.txt
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
RUN python3 -m pip install --upgrade pip && python3 -m pip install --no-cache -r /tmp/requirements.txt
