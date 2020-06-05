fileplaylist=$1
timetorecord=$2
outputfile=$3
tmp=$(mktemp -d)
n=0
for url in $(grep -v "^#" "$fileplaylist")
do
ffmpeg -t $timetorecord -i "$url" -f rawvideo -pix_fmt rgb24 -vf framerate=25,scale=768x576 $tmp/${n}_video.raw -ar 43200 -ac 1 -f mulaw $tmp/${n}_audio.raw
n=$(expr $n + 1)
done
n=$(expr $n - 1)
for n in $(seq 0 $n)
do
php $MYGIST/secam/rgb2secam.php 768 < $tmp/${n}_video.raw > $tmp/${n}_video.secam
rm $tmp/${n}_video.raw
python $MYGIST/radio/avmerge.py 43200 768x576 25 4< $tmp/${n}_audio.raw 7< $tmp/${n}_video.secam | python $MYGIST/radio/radiosend.py $(expr $n \* 10000) $(expr $n \* 10000 + 10000) 16 > $tmp/${n}.radio
rm $tmp/${n}_audio.raw $tmp/${n}_video.secam
done
paste -d "\n" $tmp/*.radio | sed "/^$/d" | zstd -v -22 --ultra > "${outputfile}.radio.zstd"
rm -r $tmp
