#!/bin/bash
FileName="README.md"
echo "<pre>" > $FileName
tree >> $FileName
echo "</pre>" >> $FileName