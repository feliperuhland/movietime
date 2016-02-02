#!/bin/sh

set -e

sh scripts/clean.sh
sh scripts/crawl.sh
sh scripts/web.sh
