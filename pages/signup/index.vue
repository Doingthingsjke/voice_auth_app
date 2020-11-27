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

      <div class="container signup">
        <p>Already have an account? <a href="#">Sign in</a>.</p>
      </div>
    </form>
    <div class="container">
      <div class="signin_generated">
        <p>Please read generated phrase:</p>
        <div type="text" class="signin_generated--phrase">
          {{ "Generated phrase for reading" }}
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
  }
};
</script>

<style>
.signup_body {
  display: flex;
  justify-content: space-around;
}
.container {
  width: 500px;
  padding: 20px;
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
