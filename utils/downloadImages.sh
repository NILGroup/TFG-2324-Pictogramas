#!/bin/sh

DOWNLOAD_DIR="downloads"

function download_id() {
    local id="$1"

    echo "Download ${id}"
    wget "https://api.arasaac.org/v1/pictograms/${id}?download=false" -O "${DOWNLOAD_DIR}/${id}.png"
}

ID_LIST=$(cat arasaac.json | grep "_id" | cut -d" " -f6 | cut -d"," -f1)

mkdir -p "${DOWNLOAD_DIR}"
for id in ${ID_LIST}; do
    download_id ${id}
done