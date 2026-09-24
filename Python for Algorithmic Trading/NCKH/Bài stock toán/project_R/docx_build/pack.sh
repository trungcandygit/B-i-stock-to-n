#!/bin/bash
# pack.sh <dir> <out.docx>
set -e
cd "$1"; rm -f "$2"
zip -qX "$2" '[Content_Types].xml'
zip -qXr "$2" . -x '[Content_Types].xml'
