<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in loginAuthError" :key="field">
      {{ field }}
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">
          {{ error }}
        </li>
      </ul>
    </p>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['loginAuthError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: white;
  }
</style>
