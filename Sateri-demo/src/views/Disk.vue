<template>
  <div class="disk">
		<router-link to="/" class="link">返回主页</router-link>
    <h1>Sateri {{ side }}-side</h1>
    <video controls class="video-player">
      <source :src="videoSrc" type="video/mp4">
    </video>
  </div>
</template>

<script>
export default {
  name: 'Disk',
  data() {
    return {
      side: this.$route.params.side,
      videoSrc: ''
    };
  },
  created() {
    this.videoSrc = this.side === 'A' ? '/public/Sateri A-side.mp4' : '/public/Sateri B-side.mp4';
  }
}
</script>

<style scoped>
.disk {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}

.video-player {
  width: 80%;
  max-width: 800px;
  margin-top: 20px;
}
</style>