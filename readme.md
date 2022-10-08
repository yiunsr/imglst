
## imglst 
* 이미지 관련 작업 라이브러리 샘플

### live demo
 * [http://imglst.labstoo.com/](http://imglst.labstoo.com/)


### 사용 라이브러리
* [dlib](http://dlib.net/)
   * 특히 [http://dlib.net/face_landmark_detection.py.html](http://dlib.net/face_landmark_detection.py.html) 코드를 이용했다. 
* [face_morphe](https://github.com/alyssaq/face_morpher)
   * 특히 [http://imglst.labstoo.com/demo/morhping](http://imglst.labstoo.com/demo/morhping)에서
    코드가 이용되었다. 
* [exif-js](https://github.com/exif-js/exif-js])
  * exif 정보를 이용해서 사진을 rotation 을 잡아줌
   
### 샘플 이미지 
* https://pixabay.com/en/child-portrait-girl-model-young-1871104/
* https://pixabay.com/en/baby-child-toddler-looking-girl-933097/
* https://pixabay.com/photos/female-girl-winter-cap-gloves-1188508/
* https://pixabay.com/photos/girl-child-young-childhood-model-1871104/

## 개발서버 실행
* front 실행
```
cd front
yarn serve
```

## 배포시 작업
* 첫 배포시
```
# yarn 설치 후
$ cd front 
$ yarn
$ yarn build
``
