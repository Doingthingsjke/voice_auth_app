<template>
  <div class="signup_body">
    <form action="action_page">
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill this form to create an account.</p>
        <hr />

        <label for="first_name"><b>First Name</b></label>
        <input type="text" placeholder="Enter Email" name="email" required />
        <hr />

        <label for="second_name"><b>Second Name</b></label>
        <input type="text" placeholder="Enter Email" name="email" required />
        <hr />

        <label for="email"><b>Email</b></label>
        <input type="text" placeholder="Enter Email" name="email" required />
        <hr />

        <!-- <label for="psw"><b>Password</b></label>
        <input
          type="password"
          placeholder="Enter Password"
          name="psw"
          required
        />

        <label for="psw-repeat"><b>Repeat Password</b></label>
        <input
          type="password"
          placeholder="Repeat Password"
          name="psw-repeat"
          required
        /> -->
      </div>

      <div class="container">
        <p>
          By creating an account you agree to our
          <a href="#">Terms & Privacy</a>.
        </p>
        <p>Already have an account? <a href="#">Sign in</a>.</p>
        <button type="submit" class="registerbtn">Register</button>
      </div>
    </form>
    <div class="container">
      <div class="signup_generated container">
        <!-- <p>
          To continue registration, you need to record your voice, saying the
          phrases below.
        </p>
        <hr /> -->

        <label for="phrase"><b>Please read generated phrase 1:</b></label>
        <div type="text" class="signin_generated--phrase">
          {{ phrases.a }}
        </div>
        <hr />

        <label for="phrase"><b>Please read generated phrase 2:</b></label>
        <div type="text" class="signin_generated--phrase">
          {{ phrases.b }}
        </div>
        <hr />

        <label for="phrase"><b>Please read generated phrase 3:</b></label>
        <div type="text" class="signin_generated--phrase">
          {{ phrases.c }}
        </div>
        <hr />

        <label for="phrase"><b>Please read generated phrase 4:</b></label>
        <div type="text" class="signin_generated--phrase">
          {{ phrases.d }}
        </div>
        <hr />

        <label for="phrase"><b>Please read generated phrase 5:</b></label>
        <div type="text" class="signin_generated--phrase">
          {{ phrases.e }}
        </div>
        <hr />

        <label for="phrase"><b>Please read generated phrase 6:</b></label>
        <div type="text" class="signin_generated--phrase">
          {{ phrases.f }}
        </div>
        <hr />

        <label for="phrase"><b>Please read generated phrase 7:</b></label>
        <div type="text" class="signin_generated--phrase">
          {{ phrases.g }}
        </div>
        <hr />

        <div class="signin_button">
          <button
            id="action"
            class="signin_button--microphone"
            v-on:click="getAudioAuth"
          >
            <img src="~/static/img/microphone.png" />
          </button>
          <!-- <button class="signin_button--signin" v-on:click="signIn">
            Sign up
          </button> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  head() {
    return {
      title: "",
      meta: [{ hid: "description", name: "description", content: "Test desc" }]
    };
  },
  data: () => ({
    audioChunks: [],
    password: "",
    phrases: {},
    email: "",
    count: 0
  }),
  methods: {
    signIn() {},
    async getAudioAuth() {
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
                  type: "audio/wav; codecs=opus"
                });
                const voice = new File([audioBlob], `voice ${this.count}.wav`, {
                  lastModified: new Date(),
                  type: "audio/wav; codecs=opus"
                });
                const formData = new FormData();
                formData.append("audio", voice, `voice ${this.count}.wav`);
                console.log(formData.state);

                axios({
                  method: "POST",
                  url: "https://192.168.0.12:5000",
                  data: formData,
                  headers: {
                    "content-type": "multipart/form-data;"
                  }
                })
                  .then(response => console.log(response))
                  .catch(error => console.log(error));

                const audioUrl = URL.createObjectURL(audioBlob);
                var a = document.createElement("a");
                a.style.display = "none";
                a.href = audioUrl;
                a.download = `voice ${this.count}.wav`;
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

      if (this.count >= 8) {
        alert("Спасибо, больше нет необходимости записывать звук");
      } else {
        actionButton.disabled = true;
        const recorder = await recordAudio();
        recorder.start();
        await sleep(5000);
        const audio = await recorder.stop();
        alert(`Спасибо, запись звука ${this.count} завершена`);
        actionButton.disabled = false;
      }
    }
  },
  mounted() {
    axios
      .get("https://192.168.1.35:5000/register_phrase")
      .then(response => (this.phrases = response.data))
      .catch(error => console.log(error));
  }
};
</script>

<style>
.signin_block {
  padding-top: 10px;
}
.signup_body {
  position: relative;
  display: flex;
  padding-left: 120px;
}
.container {
  width: 500px;
  padding: 20px;
  /* display: inline-block; */
  /* align-items: justify; */
}
.signup_generated {
  padding-top: 23px;
  padding-left: 50px;
}

/* Full-width input fields */
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type="text"]:focus,
input[type="password"]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit/register button */
.registerbtn {
  background-color: rgb(76, 126, 126);
  color: black;
  font-size: 15px;
  font-weight: bold;
  padding: 16px 20px;
  width: 100%;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: rgb(76, 126, 126);
}

/* Set a grey background color and center the text of the "sign in" section */
.signup {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
