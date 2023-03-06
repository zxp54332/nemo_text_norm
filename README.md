# NeMo Text Normalization
現有專案位置：台北 27 server `/home/laurence_chen/project/ML_NeMo`

## Prerequisites

Tested on Python 3.8
```bash
pip install -r requirements.txt
```

## Convert Text
```JSON
{
  "text": "Tom XI is my father"
   輸出: "norm_text": "Tom eleventh is my father"
}
```

## Docker
```bash
sudo docker build --no-cache -t "ponddy/eng_text_norm" -f Dockerfile .
sudo docker run --name eng_text_norm_web -d -p 5151:5252 ponddy/eng_text_norm:latest
sudo docker tag {image id} ponddy/eng_text_norm:v1.0
sudo docker push ponddy/eng_text_norm:v1.0

```