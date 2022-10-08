<template>
  <v-container class="mb-7">
    <v-row class="text-center">
      <v-col class="mt-4">
        <h1 class="h5 font-weight-bold mb-1">
          Morph on face
        </h1>
        <h1 class="subtitle-1 font-weight-bold mb-3">
          두 얼굴에 대해 모핑
        </h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="5">
        <v-slider class="mt-4" v-model="percent" label="percent" thumb-label="always" max="100" min="0" step="5">
        </v-slider>
        <v-subheader class="pl-0">
          0% : left(top) &nbsp;&nbsp;  50% : average  &nbsp;&nbsp; 100% : right(bottom)
        </v-subheader>
      </v-col>
      <v-col class="mt-4">
        <v-btn color="success" class="mt-0" @click="morphing">
          Morphing
        </v-btn>
      </v-col>
      
    </v-row>
    <v-row>
      <v-col class="mt-0">
        <v-card class="pa-2">
          <v-card-subtitle>Left</v-card-subtitle>
          <v-file-input accept="image/*" label="User Upload" v-model="left_file" @change="fileUploadChange('left')"></v-file-input>
          <img ref="left_img" :src="left_src" style="max-width:400px;">
        </v-card>
         
      </v-col>

      <v-col class="mt-0">
        <v-card class="pa-2">
          <v-card-subtitle>Right</v-card-subtitle>
          <v-file-input accept="image/*" label="User Upload" v-model="right_file" @change="fileUploadChange('right')"></v-file-input>
          <img ref="right_img" :src="right_src" style="max-width:400px;">
        </v-card>
         
      </v-col>
    </v-row>

    <v-row>
      <v-col class="mt-0">
        <v-card class="pa-2">
          <v-card-subtitle>Result</v-card-subtitle>
          <img :src="result_src">
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
      percent: 50,
      left_src: null, right_src: null, result_src: null,
      left_file: null, right_file: null,
      overlay: false, virtual_canvas: null, virtual_canvas_ctx: null,
    }),
    mounted() {
      this.left_src = "/static/res/person/person04_01.jpg";
      this.right_src = "/static/res/person/person03_01.jpg";

      let canvas = document.createElement("canvas");
      this.virtual_canvas = canvas;
      // ctx 는 sync 하게 동작하지 못하는 것 같아 미리 생성한다.
      this.virtual_canvas_ctx = canvas.getContext("2d");
      let this_ = this;
      setTimeout(() => {
        this_.left_file = this.imgToFile(this_.$refs.left_img);
        this_.right_file = this.imgToFile(this_.$refs.right_img);
      }, 100);
    },
    methods: {
      fileUploadChange(left_or_right){
        // debugger;   // eslint-disable-line no-debugger
        if(left_or_right == "left"){
          this.left_src= URL.createObjectURL(this.left_file)
        }
        else if(left_or_right == "right"){
          this.right_src= URL.createObjectURL(this.right_file)
        }
      },
      loading(show) {
        this.overlay = show;
      },
      imgToFile(img) {
        let canvas = this.virtual_canvas;
        let ctx = this.virtual_canvas_ctx;
        canvas.width = img.width;
        canvas.height = img.height;
        // canvas.canvasHeight = img.height;
        ctx.drawImage(img, 0,0 , img.width, img.height );
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
      morphing(){
        this.loading(true);
        let this_ = this;
        let formdata = new FormData();
        let left = this.imgToFile(this.$refs.left_img);
        let right = this.imgToFile(this.$refs.right_img);
        //let left = URL.createObjectURL(this.left_src);
        // let right = URL.createObjectURL(this.right_src);
        formdata.append("left", left);
        formdata.append("right", right);
        formdata.append("percent", 100 - this.percent);
        //formdata.append("img", img);
        axios.post('/demo/morhping', formdata, {headers: {
            'Content-Type': 'multipart/form-data'
          }})
          .then(function(result) {
            this_.loading(false);
            this_.result_src = result.data.img;
          })
          .catch(function (error) {
          if (error.response) {
            console.log(error.response.status);
            console.log(error.response.headers);
          }
        });
      },
      

    },
    
  }
</script>
