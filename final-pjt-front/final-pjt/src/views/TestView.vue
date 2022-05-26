<template>
   <div>
     <input v-model="speachTest" type="text">
     <button @mouseover="onVoice"><i class="voice-btn fa-solid fa-microphone"></i></button>
     <div class="words" contenteditable>
  </div>
   </div>
</template>

<script>



export default {
  name: "TestView",
  data: function () {
    return {
      speachTest: '',
    }
  },
  methods: {
    onVoice: function () {
      window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      const recognition = new window.SpeechRecognition();
      recognition.interimResults = false;
      recognition.lang = 'ko-KR'; 
      const btn = document.querySelector('.voice-btn')

      btn.classList.add('on-voice')
      let p = ''
    
      recognition.addEventListener('result', e => {
      const transcript = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('');

        p = transcript;
        this.speachTest += p

        if (e.results[0].isFinal) {
          p = ' '
          this.speachTest += p
          btn.classList.remove('on-voice')
        }
      });
      
    // recognition.addEventListener('end', recognition.start);
    recognition.start();
    }
  }
}
</script>

<style>
</style>