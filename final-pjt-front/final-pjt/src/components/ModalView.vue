<template>
  <transition name="modal">
    <div class="modal-container">
      <slot />
      <a @click="$emit('close-modal'), hideModal()" class="modal-close-button">
        <i class="fa-solid fa-xmark close-mark"></i>
      </a>
    </div>
  </transition>
</template>

<script>
export default {
  methods: {
    hideModal () {
      document.body.classList.remove("modal-open");
    }
  }
}
</script>

<style>
.modal-container {
  position: fixed;
  z-index: 9998;
  top: 5%;
  left: 5%;
  width: 90%;
  height: 90%;
  overflow-y: auto;
  background-color: rgba(0, 14, 59, 0.749);
  transition: opacity 0.3s ease;
  border-radius: 2px;
  box-shadow: 0 2px 8px white;
}

.modal-close-button {
  position: fixed;
  top: 0%;
  right: 0%;
  margin: 2%;
}

.close-mark {
  font-size: 30px;
  color: white;
}

::-webkit-scrollbar {
  display: none;
}
</style>