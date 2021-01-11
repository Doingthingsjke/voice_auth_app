<template>
  <div class="signup_body">
    <form action="action_page">
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr />

        <label for="email"><b>Email</b></label>
        <input type="text" placeholder="Enter Email" name="email" required />

        <label for="psw"><b>Password</b></label>
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
        />
        <hr />

        <p>
          By creating an account you agree to our
          <a href="#">Terms & Privacy</a>.
        </p>
        <button type="submit" class="registerbtn">Register</button>
      </div>

      <div class="container_signup">
        <p>Already have an account? <a href="#">Sign in</a>.</p>
      </div>
    </form>
    <div class="container">
      <div class="signup_generated">
        <p>Please read generated phrase 1:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading" }}
        </div>
        <hr />
        <p>Please read generated phrase 2:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading,asdasofhah aisuaogv apishfga" }}
        </div>
        <hr />
        <p>Please read generated phrase 3:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading,asdasofhah aisuaogv apishfga" }}
        </div>
        <hr />
        <p>Please read generated phrase 4:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading,asdasofhah aisuaogv apishfga" }}
        </div>
        <hr />
        <p>Please read generated phrase 5:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading,asdasofhah aisuaogv apishfga" }}
        </div>
        <hr />
        <p>Please read generated phrase 6:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading,asdasofhah aisuaogv apishfga" }}
        </div>
        <hr />
        <p>Please read generated phrase 7:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading,asdasofhah aisuaogv apishfga" }}
        </div>

        <div class="signin_button">
          <button
            id="action"
            class="signin_button--microphone"
            v-on:click="getAudio"
          >
            <img src="~/static/img/microphone.png" />
          </button>
          <button class="signin_button--signin" v-on:click="signIn">
            Sign up
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
    email: "",
    count: 0
  }),
  methods: {
    signIn() {},
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

                const audio = new Audio(audioUrl);
                const play = () => audio.play();
                console.log(audioUrl);
                var a = document.createElement("a");
                a.style.display = "none";
                a.href = audioUrl;
                a.download = "test.wav";
                document.body.appendChild(a);
                a.click();
                setTimeout(function() {
                  document.body.removeChild(a);
                  window.URL.revokeObjectURL(audioUrl);
                }, 100);

                resolve({ audioBlob, audioUrl, play });
              });

              mediaRecorder.stop();
            });

          resolve({ start, stop });
        });

      const sleep = time => new Promise(resolve => setTimeout(resolve, time));

      const recorder = await recordAudio();
      const actionButton = document.getElementById("action");
      actionButton.disabled = true;
      recorder.start();
      await sleep(5000);
      const audio = await recorder.stop();
      const count = this.clickMe();
      alert(`Спасибо, запись звука ${count} зваершена`);
      audio.play();
      await sleep(5000);
      actionButton.disabled = false;
    },
    clickMe() {
      return (this.count += 1);
      // return (document.getElementById("action").innerHTML = this.count);
    }
  }
};
</script>

<style>
.signup_body {
  position: relative;
  display: flex;
  padding-left: 70px;
}
.container {
  width: 500px;
  padding: 20px;
  /* display: inline-block; */
  /* align-items: justify; */
}
.signup_generated {
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
  background-color: #4caf50;
  color: white;
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
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signup {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
