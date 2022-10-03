<template>
  <v-container class="mb-7">
    <v-row class="text-center">
      <v-col class="mt-4">
        <h1 class="h5 font-weight-bold mb-1">
          Detect Face Landmark(Apply sticker after Landmark detect)
        </h1>
        <h1 class="subtitle-1 font-weight-bold mb-3">
          얼굴 랜드마크 추출(Landmark Detect 후, 스티커를 적용할 것)
        </h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="mt-4">
        <v-btn color="success" class="mr-4 ml-8  my-2" @click="canvasLandmark">
          Landmark Detect
        </v-btn>
      </v-col>
      <v-col class="mt-4">
        <v-sheet color="blue lighten-4" class="pl-2 py-2" elevation="2">
          <v-btn color="success" class="mr-4 ml-8" @click="canvasSticker">
            Apply Sticker
          </v-btn>
          <v-btn color="success" class="mr-4 ml-8" @click="clearCanvas">
            Clear
          </v-btn>
        </v-sheet>
      </v-col>
    </v-row>
      <v-col class="mt-0">
        <v-card>
          <v-tabs v-model="tab" background-color="deep-purple accent-4" centered dark @change="clearCanvas">
            <v-tabs-slider></v-tabs-slider>
            <v-tab href="#tab-1">
              sample image1
            </v-tab>
            <v-tab href="#tab-2">
              sample image1
            </v-tab>

            <v-tab href="#tab-3">
              userupload
            </v-tab>
          </v-tabs>

          <v-tabs-items v-model="tab" >
            <v-tab-item value="tab-1">
              <v-card flat>
                <v-card-text>sample image1</v-card-text>
                <!-- <img src="/static/res/person/person04_01.jpg"> -->
                <canvas ref="canvas1"
                  :width="canvasWidth" :height="canvasHeight"
                ></canvas>
                
              </v-card>
            </v-tab-item>
            <v-tab-item value="tab-2">
              <v-card flat>
                <v-card-text>sample image2</v-card-text>
                <canvas ref="canvas2"
                  :width="canvasWidth" :height="canvasHeight"
                ></canvas>
                
              </v-card>
            </v-tab-item>
            <v-tab-item value="tab-3">
              <v-card flat>
                <v-card-text>userupload</v-card-text>
                <v-file-input truncate-length="15" @change="fileUploadChange" v-model="userUploadFile"></v-file-input>
                <canvas ref="canvas3" :style="{'zoom':zoom}" :width="canvasWidth" :height="canvasHeight"></canvas>
              </v-card>
            </v-tab-item>
          </v-tabs-items>

        </v-card>
      </v-col>
    <v-row class="text-center px-4">
      <v-col class="mt-4">
        <v-card color="blue lighten-4" elevation="2" outlined>
          <v-card-title>Eyes(눈)</v-card-title>
          <v-radio-group v-model="eyes" row>
            <v-radio value="0" class="mr-8">
              <template v-slot:label>
                <div><h2>None(없음)</h2>
                </div>
              </template>
            </v-radio>
            <v-radio value="1" class="mr-8">
              <template v-slot:label>
                <div>
                  <img width="150" ref="eyes_1" :src="eyes_img[1]">
                </div>
              </template>
            </v-radio>
            <v-radio value="2" class="mr-8">
              <template v-slot:label>
                <div>
                  <img class="float-left" width="60"  ref="eyes_2_1" :src="eyes_img[2][0]">
                  <img class="float-right" width="60" ref="eyes_2_2" :src="eyes_img[2][1]">
                </div>
              </template>
            </v-radio>
          </v-radio-group>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="text-center px-4">
      <v-col class="mt-4">
        <v-card color="blue lighten-4" elevation="2" outlined>
          <v-card-title>Nose(코)</v-card-title>
          <v-radio-group v-model="nose" row>
            <v-radio value="0" class="mr-8 mb-4">
              <template v-slot:label>
                <div><h2>None(없음)</h2>
                </div>
              </template>
            </v-radio>
            <v-radio value="1" class="mr-8 mb-4">
              <template v-slot:label>
                <div>
                  <img width="100" ref="nose_1" :src="nose_img[1]">
                </div>
              </template>
            </v-radio>
            <v-radio value="2" class="mr-8 mb-4">
              <template v-slot:label>
                <div>
                  <img width="100" ref="nose_2" :src="nose_img[2]">
                </div>
              </template>
            </v-radio>
          </v-radio-group>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="text-center px-4">
      <v-col class="mt-4">
        <v-card color="blue lighten-4" elevation="2" outlined>
          <v-card-title>Mouth(입)</v-card-title>
          <v-radio-group v-model="mouth" row>
            <v-radio value="0" class="mr-8 mb-4">
              <template v-slot:label>
                <div><h2>None(없음)</h2>
                </div>
              </template>
            </v-radio>
            <v-radio value="1" class="mr-8 mb-4">
              <template v-slot:label>
                <div>
                  <img width="100" ref="mouth_1" :src="mouth_img[1]">
                </div>
              </template>
            </v-radio>
            <v-radio value="2" class="mr-8 mb-4">
              <template v-slot:label>
                <div>
                  <img width="100" ref="mouth_2" :src="mouth_img[2]">
                </div>
              </template>
            </v-radio>
          </v-radio-group>
        </v-card>
      </v-col>
    </v-row>

    <v-overlay :value="overlay">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>

  </v-container>
</template>

<script>
  import axios from 'axios'
  // var EXIF = require('exif-js');
  
  export default {
    name: 'FaceLandmark',

    data: () => ({
      tab: null, canvasFaceLandMark: null, uploadImgLandmark: null,
      canvasWidth: 100, canvasHeight: 100, zoom: 1,
      img1: null, img2: null, overlay: false, userUploadImg: null, userUploadFile: null,
      eyes: 0, nose: 0, mouth: 0, 
      eyes_img: [
        null, 
        "/static/res/sticker/sticker_eye_001.png",
        ["/static/res/sticker/sticker_eye_002_01.png", "/static/res/sticker/sticker_eye_002_02.png"]
      ],
      nose_img: [
        null,
        "/static/res/sticker/sticker_nose_001.png",
        "/static/res/sticker/sticker_nose_002.png"
      ],
      mouth_img: [
        null,
        "/static/res/sticker/sticker_mouth_001.png",
        "/static/res/sticker/sticker_mouth_002.png"
      ]
    }),
    mounted() {
      this.img1 = new Image();
      this.img1.src = "/static/res/person/person04_01.jpg";
      this.img2 = new Image();
      this.img2.src = "/static/res/person/person05_01.jpg";
    },
    methods: {
      fileUploadChange(){
        // debugger;   // eslint-disable-line no-debugger
        this.userUploadImg = new Image();
        let img = this.userUploadImg;
        let this_ = this;
        this.userUploadImg.onload = function(){
          this_.canvasWidth = img.width;
          this_.canvasHeight = img.height;
          let zoom_base = Math.max(img.width , img.height);
          if(zoom_base > 512){
            this_.zoom = 512 / zoom_base;
          }
          let ctx = this_.$refs.canvas3.getContext('2d');
          // why ctx does not work sync??
          setTimeout(() => {
            ctx.drawImage(img, 0,0 , img.width, img.height );
          }, 100);
        }
        this.userUploadImg.src = URL.createObjectURL(this.userUploadFile);
      },
      clearCanvas: function(){
        setTimeout(() => {
          if(this.tab == "tab-1"){
            this.clearSingleCanvas(this.$refs.canvas1, 1);
          }
          else if(this.tab == "tab-2"){
            this.clearSingleCanvas(this.$refs.canvas2, 2);
          }
          else if(this.tab == "tab-3"){
            this.clearSingleCanvas(this.$refs.canvas3, 3);
          }
        }, 200);
        
      }, 
      clearSingleCanvas($el, idx){
        let img = "";
        if(idx == 1){
          img = this.img1;
        }
        if(idx == 2){
          img = this.img2;
        }
        if(idx == 3){
          img = this.userUploadImg;
        }
        this.canvasWidth = img.width;
        this.canvasHeight = img.height;
        let ctx = $el.getContext('2d');
        // why ctx does not work sync??
        setTimeout(() => {
          ctx.drawImage(img, 0,0 , img.width, img.height );
        }, 200);
      },
      loading(show) {
        this.overlay = show;
      }, 
      drawPolygon(canvas, points, number){
        var ctx = canvas.getContext('2d');
        for(var  index = 0 ; index < points.length ; index++ ) {
          var point = points[index];
          ctx.fillRect(point[0]-1,point[1]-1,2,2);
          if(number){
            ctx.font = "10px Arial";
            ctx.fillText(""+index,  point[0] , point[1] - 2 );
          }
        }
      },
      canvasToFile( canvas ){
        var imgType = "image/jpeg" ;  //  image/jpeg  or image/png
        var dataUrl = canvas.toDataURL(imgType);
        var blobBin = atob(dataUrl.split(',')[1]);

        var array = [];
        for(var i = 0; i < blobBin.length; i++) {
          array.push(blobBin.charCodeAt(i));
        }
  
        var fileObj=new Blob([new Uint8Array(array)], {type: imgType});
        return fileObj;
      },
      getCurrentCanvasSelector(){
        if(this.tab == "tab-1"){
          return this.$refs.canvas1;
        }
        else if(this.tab == "tab-2"){
          return this.$refs.canvas2;
        }
        return this.$refs.canvas3;
      },
      canvasLandmark(){
        let this_ = this;
        setTimeout(() => {
          this_.clearCanvas();
          let canvas= this_.getCurrentCanvasSelector();
          let img = this_.canvasToFile(canvas);
          this_.landmark(img, canvas, "landmark");
        }, 200);
        
      },
      landmark(img, canvasEle, drawType){
        this.loading(true);
        let this_ = this;
        let formdata = new FormData();
        formdata.append("img", img);
        axios.post('/demo/landmark', formdata, {headers: {
            'Content-Type': 'multipart/form-data'
          }})
          .then(function(response) {
            let canvasFaceLandMark = response.data;
            this_.loading(false);
            if(drawType == "landmark")
              this_.drawPolygon(canvasEle, canvasFaceLandMark.img_points, true);
            else if(drawType == "sticker"){
              this_.drawSticker(canvasEle, canvasFaceLandMark);
            }
          })
          .catch(function (error) {
          if (error.response) {
            console.log(error.response.status);
            console.log(error.response.headers);
          }
        });
      },
      canvasSticker(){
        let this_ = this;
        setTimeout(() => {
          this_.clearCanvas();
          let canvas= this_.getCurrentCanvasSelector();
          let img = this_.canvasToFile(canvas);
          this_.landmark(img, canvas, "sticker");
        }, 200);
      },

      drawSticker(canvasEle, landmark){
        let ctx = canvasEle.getContext('2d');
        let left_eyes_points = landmark.left_eye_points;
        let right_eyes_points = landmark.right_eye_points;
        // let left_brow_point = landmark.left_brow_point;
        // let right_brow_point = landmark.right_brow_point;
        let nose_points  = landmark.nose_points;
        let mouth_points = landmark.mouth_points;

        switch(this.eyes){
          case "1":{
            let img = this.$refs.eyes_1;
            let rect = this.poly2rect(left_eyes_points.concat(right_eyes_points), 0.3, 0.8);
            ctx.drawImage(img, rect[0][0],rect[0][1] , rect[1][0]-rect[0][0], rect[1][1] - rect[0][1]  );
            break;
          }
          case "2":{
            let eyes_left_img = this.$refs.eyes_2_1;
            let eyes_right_img = this.$refs.eyes_2_2;
            //// 사진이므로 사람의 오른쪽은 사진에서 왼쪽이기 때문에 방향이 반대이다. 
            let right_rect = this.poly2rect(left_eyes_points, 0.1,0.1);
            ctx.drawImage(eyes_right_img, right_rect[0][0],right_rect[0][1] , right_rect[1][0]-right_rect[0][0], right_rect[1][1] - right_rect[0][1]  );
            let left_rect = this.poly2rect(right_eyes_points, 0.1,0.1);
            ctx.drawImage(eyes_left_img, left_rect[0][0],left_rect[0][1] , left_rect[1][0]-left_rect[0][0], left_rect[1][1] - left_rect[0][1]  );
            break;
          }
        }

        switch(this.nose){
          case "1":{
            let img = this.$refs.nose_1;
            let rect = this.poly2rect(nose_points, 0.5, 0.1);
            ctx.drawImage(img, rect[0][0],rect[0][1] , rect[1][0]-rect[0][0], rect[1][1] - rect[0][1]  );
            break;
          }
          case "2":{
            let img = this.$refs.nose_2;
            let rect = this.poly2rect(nose_points, 0.1, 0.1);
            ctx.drawImage(img, rect[0][0],rect[0][1] , rect[1][0]-rect[0][0], rect[1][1] - rect[0][1]  );
            break; 
          }
        }

        switch(this.mouth){
          case "1":{
            let img = this.$refs.mouth_1;
            let rect = this.poly2rect(mouth_points, 0.2, 0.2);
            ctx.drawImage(img, rect[0][0],rect[0][1] , rect[1][0]-rect[0][0], rect[1][1] - rect[0][1]  );
            break;
          }
          case "2":{
            let img = this.$refs.mouth_2;
            let rect = this.poly2rect(mouth_points, 0.2, 0.2);
            ctx.drawImage(img, rect[0][0],rect[0][1] , rect[1][0]-rect[0][0], rect[1][1] - rect[0][1]  );
            break;
          }
        }
        this.loading(false);
      },
      poly2rect(points, marginXRatio, marginYRatio){
        let maxX = 0;
        let maxY = 0;
        let minX = 99999999;
        let minY=99999999;
        for(let index in points){
          var point = points[index];
          maxX = Math.max(maxX, point[0]  );
          maxY = Math.max(maxY, point[1]  );
          minX = Math.min(minX, point[0]  );
          minY = Math.min(minY, point[1]  );
        }
        let marginX = (maxX - minX ) * marginXRatio;
        let marginY = (maxY - minY ) * marginYRatio;
        return [[minX - marginX ,minY - marginY], [maxX + marginX, maxY + marginY]];
      },

    },
    
  }
</script>
