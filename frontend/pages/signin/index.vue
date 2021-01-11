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
          в наибольшей мере как нам известно от таких конфликтов страдают именно
          женщины и девушки
        </div>
      </div>
      <div class="signin_button">
        <button
          id="action"
          class="signin_button--microphone"
          v-on:click="getAudio"
        >
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
        <!-- <button class="signin_button--signin" v-on:click="download">
          download
        </button> -->
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
    password: "",
    count: 0
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
    async getAudio() {
      const recordAudio = () =>
        new Promise(async resolve => {
          const audioChunks = this.audioChunks;
          const stream = await navigator.mediaDevices.getUserMedia({
            audio: true,
            video: false
          });
          const mediaRecorder = new MediaRecorder(stream);

          mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
          });

          const start = () => mediaRecorder.start();

          const stop = () =>
            new Promise(resolve => {
              mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks, {
                  type: "audio/wav"
                });
                const audioUrl = URL.createObjectURL(audioBlob);
                var a = document.createElement("a");
                a.style.display = "none";
                a.href = audioUrl;
                a.download = `voice.wav`;
                document.body.appendChild(a);
                a.click();
                setTimeout(function() {
                  document.body.removeChild(a);
                  window.URL.revokeObjectURL(audioUrl);
                }, 100);

                resolve({ audioBlob, audioUrl });
              });

              mediaRecorder.stop();
            });

          resolve({ start, stop });
        });

      const sleep = time => new Promise(resolve => setTimeout(resolve, time));
      const actionButton = document.getElementById("action");
      this.count += 1;

      if (this.count >= 2) {
        alert("Спасибо, больше нет необходимости записывать звук");
      } else {
        actionButton.disabled = true;
        const recorder = await recordAudio();
        recorder.start();
        await sleep(5000);
        const audio = await recorder.stop();
        alert(`Спасибо, запись звука завершена`);
        actionButton.disabled = false;
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
  margin-top: 30px;
  margin-left: auto;
  margin-right: auto;
  /* position: absolute; */
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
  background: rgb(76, 126, 126);
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
.signin_generated {
  text-align: center;
  width: 250px;
  /* align-items: center; */
}
/* .signin_generated--phrase {
  text-align: center; 
  position: relative;
} */
</style>
