# kiss-sync

Keep-It-Stupid-Simple File Syncing

## Build Binaries

    python -m poetry install --with=dev

Windows:

    python -m poetry run pyinstaller -y \
        --name kiss_sync \
        --specpath build \
        --add-data 'kiss_sync/gui/dist;kiss_sync/gui/dist' \
        kiss_sync/__main__.py
