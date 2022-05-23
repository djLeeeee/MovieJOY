<template>
  <div>
    <div id="release-box">
      <p class="release-main-text">Check the screening information</p>
      <p class="release-text">Check now playing and up comming movies</p>
      <a href="#">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Now Playing
      </a>
      <a href="#">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Up Comming
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReleaseView',
}
</script>

<style>
.release-main-text {
	color: white;
	font-size: 2rem;
}

.release-text {
	color: rgba(255, 255, 255, 0.753);
	margin-bottom: 2rem;
}

#release-box {
  padding: 2rem;
  margin-top: 30vh;
  transition: 0.8s;
}

/* genre-select-btn */
#release-box a{
  position: relative;
  display: inline-block;
  padding: 15px 20px;
  margin: 0.8rem;
  color: #03e9f4;
  text-decoration: none;
  text-transform: uppercase;
  transition: 0.5s;
  letter-spacing: 4px;
  overflow: hidden;
  font-size: 0.9rem; 
}
#release-box a:focus{
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4,
                0 0 25px #03e9f4,
                0 0 50px #03e9f4,
                0 0 200px #03e9f4;
     -webkit-box-reflect:below 1px linear-gradient(transparent, #0005);
}

#release-box a:hover span{
    position: absolute;
    display: block;
}
#release-box a span:nth-child(1){
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg,transparent,#03e9f4);
    animation: animate1 1s linear infinite;
}
@keyframes animate1{
    0%{
        left: -100%;
    }
    50%,100%{
        left: 100%;
    }
}
#release-box a span:nth-child(2){
    top: -100%;
    right: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(180deg,transparent,#03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}
@keyframes animate2{
    0%{
        top: -100%;
    }
    50%,100%{
        top: 100%;
    }
}
#release-box a span:nth-child(3){
    bottom: 0;
    right: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(270deg,transparent,#03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.50s;
}
@keyframes animate3{
    0%{
        right: -100%;
    }
    50%,100%{
        right: 100%;
    }
}


#release-box a span:nth-child(4){
    bottom: -100%;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(360deg,transparent,#03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}
@keyframes animate4{
    0%{
        bottom: -100%;
    }
    50%,100%{
        bottom: 100%;
    }
}
</style>