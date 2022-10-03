<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        imglst
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/yiunsr/imglst"
        target="_blank"
        text
      >
        <span class="mr-2">github</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <v-row>
          <v-col cols="2">
            <v-sheet elevation="2">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="text-h6">
                    imglst
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    이미지 관련 작업 라이브러리 샘플
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>

              <v-divider></v-divider>

              <v-list dense nav>
                <v-list-item link to="facelandmark">
                  <v-list-item-icon>
                    <v-icon>mdi-face-recognition</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title link >얼굴 랜드마크 추출</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            

            
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
              min-height="70vh"
              rounded="lg"
            >
              <router-view></router-view>
            </v-sheet>
          </v-col>
        </v-row>
        
      
      </v-container>
        
    </v-main>
    
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    //
  }),
};
</script>
