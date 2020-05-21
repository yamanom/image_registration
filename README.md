# image_registration

## アフィン変換の変換行列を推定
4点以上の点から最適なアフィン変換の変換行列を求めるメソッドがなかったので、実装する。

### 参考
[画像位置合わせ：SIFTから深層学習まで](https://qiita.com/suuungwoo/items/9598cbac5adf5d5f858e)

### 環境作成
dockerコンテナ作成、起動する。
```
cd c:/Users/user01/work/opencv
#docker build -t jupyterlab-opencv:1.0 .
docker-compose up -d
```

### 接続
http://localhost:8888/
