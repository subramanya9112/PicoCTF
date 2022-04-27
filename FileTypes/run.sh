#!/bin/sh
sudo apt install sharutils 
sh ./Flag.pdf
ar xv flag 
mv flag flag.cpio
cpio --file flag.cpio --extract
rm flag.cpio
bzip2 -d flag
mv flag.out flag.gz
gunzip flag.gz
lzip -d flag
rm flag
mv flag.out flag.lz4
lz4 -d flag.lz4
rm flag.lz4
mv flag flag.lzma
lzma -d flag.lzma
mv flag flag.lzop
lzop -d flag.lzop
rm flag.lzop
lzip -d flag
mv flag.out flag.xz
xz -d flag.xz
cat flag | xxd -r -p 
rm flag
