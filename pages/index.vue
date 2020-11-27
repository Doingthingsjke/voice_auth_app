<template>
  <div class="container">
    <p>Home page</p>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: "Home page",
      meta: [
        { hid: "description", name: "description", content: "Home page" },
        { hid: "robots", name: "robots", content: "noindex, nofollow" }
      ]
    };
  },
  layout: "main"
};
</script>

<style></style>
