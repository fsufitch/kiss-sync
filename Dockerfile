###########
# NodeJS 20 - Custom Install
###########

FROM fedora:37 AS nodejs_install

WORKDIR /opt
RUN dnf install -y xz && \
    rm -rf /var/cache/dnf
RUN curl -LO 'https://nodejs.org/dist/v20.2.0/node-v20.2.0-linux-x64.tar.xz' && \
    tar xvf node-*.tar.xz && \
    rm node*.tar.xz && \
    mv node-* node

###########
# DEVCONTAINER
##########
FROM fedora:37 AS devcontainer

# Install stuff necessary for a reasonable CLI
COPY devcontainer-packages.txt /opt
RUN dnf install -y $(cat /opt/devcontainer-packages.txt) && \
    rm -rf /var/cache/dnf

# Set up the devcontainer user
RUN useradd -ms /bin/bash developer
RUN echo "developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/developer
WORKDIR /home/developer
USER developer

# Create a user-space Python virtualenv
RUN python3 -m venv /home/developer/root
ENV PATH=/home/developer/root/bin:$PATH
RUN /home/developer/root/bin/pip install -U pip && \
    /home/developer/root/bin/pip install -U poetry

COPY --chown=developer:developer ./.bashrc.d /home/developer/.bashrc.d

COPY --chown=developer:developer --from=nodejs_install /opt/node /home/developer/root/node
ENV PATH=/home/developer/root/node/bin:$PATH

CMD ["echo", "devcontainer should have its command overridden by the IDE"]

