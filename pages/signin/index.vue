<template>
  <div class="signin_main">
    <div class="signin">
      <h1>Sign in</h1>
      <div class="signin_email">
        <p>Your email:</p>
        <input type="text" v-model="email" placeholder="email@mail.com" />
      </div>
      <div class="signin_password">
        <p>Your password:</p>
        <input
          type="password"
          required
          autocomplete="off"
          v-model="password"
          placeholder="password"
        />
        <p class="forgot"><a href="#">Forgot Password?</a></p>
      </div>
      <div class="signin_generated">
        <p>Please read generated phrase:</p>
        <div type="text" class="signin_generated--phrase">
          <input
            type="password"
            required
            autocomplete="off"
            v-model="password"
            placeholder="password"
          />
        </div>
      </div>
      <div class="signin_button">
        <button class="signin_button--microphone" v-on:click="getAudio">
          <img src="~/static/img/microphone.png" />
        </button>
        <!-- <button v-on:click="stopRecording">
          Stop
        </button> -->
      </div>

      <div>
        <button class="signin_button--signin" v-on:click="signIn">
          Sign in
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@nuxtjs/axios";

export default {
  head() {
    return {
      title: "Sign in",
      meta: [{ hid: "description", name: "description", content: "Sign in" }]
    };
  },
  data: () => ({
    audioChunks: [],
    email: "",
    password: ""
  }),
  methods: {
    signIn() {
      let signData = {
        email: this.email,
        password: this.password
      };
      // axios.post("http://localhost:3000/api/something", signData).then(
      //   setTimeout(() => {
      //     this.$router.push("something");
      //   }, 500)
      // );
    },
    getAudio() {
      navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        const mediaRec = new MediaRecorder(stream);
        mediaRecorder.start();
        mediaRecorder.addEventListener("dataavailable", function(event) {
          this.audioChunks.push(event.data);
        });
      });

      // надо подумать, искуственная задержка или две кнопки "старт" и "стоп"
      // можно жобавить часть с выводом аудио на экран, чтобы можно было прослушать
      setTimeout(() => stopRecording, 120000);
      function stopRecording() {
        MediaRecorder.stop();
        MediaRecorder.addEventListener("stop", function(event) {
          const audioBlob = new Blob(this.audioChunks, {
            type: "audio/wav"
          });

          let formData = new FormData();
          formData.append("voice", audioBlob);
          sendAudioToAPI(formData);
          this.audioChunks = [];
        });

        async function sendAudioToAPI(form) {
          let promise = await fetch(URL, {
            method: "POST",
            body: form
          });
          if (promise.ok) {
            let response = await promise.json();
            console.log(response.data);
          }
        }
      }
    }
  }
};
</script>

<style>
.signin_main {
  width: 100%;
  position: relative;
}
.signin {
  position: absolute;
  top: 30%;
  width: 400px;
  height: 600px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
  border: 1px solid #000000;
  box-shadow: 5px;
}
.signin_button {
  padding-top: 10px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
}
.signin_button--microphone {
  background: rgb(224, 8, 8);
  border-radius: 50%;
  height: 3em;
  width: 3em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  text-decoration: none;
}
.signin_button--microphone:hover {
  background-color: rgb(224, 59, 59);
}
.signin_button--microphone:active,
.signin_button--microphone:focus {
  outline: none !important;
}
.signin_button--microphone img {
  padding-left: 1.9px;
  height: 2rem;
  width: 2rem;
}
.signin_button--signin {
  margin-top: 10px;
  font-size: 20px;
}
</style>
