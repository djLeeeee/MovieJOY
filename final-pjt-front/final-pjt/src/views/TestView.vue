<template>
   <div>
     <input v-model="speachTest" type="text">
     <button @click="onVoice"><i class="fa-solid fa-microphone"></i></button>
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
      
      let p = ''
      console.log(p)
      this.speachTest = p

      recognition.addEventListener('result', e => {
      const transcript = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('');

        p = transcript;
        this.speachTest += p
        console.log(p)

        if (e.results[0].isFinal) {
          p = ''
          this.speachTest += p
          console.log(p)
        }
      });
      
    recognition.addEventListener('end', recognition.start);

    recognition.start();

    }
  }
}
</script>

<style>

</style>