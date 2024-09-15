<template>
  <div class="disk">
		<router-link to="/" class="link">返回</router-link>
    <h1>Sateri {{ side }}-side</h1>

    <p>如果视频无法加载，请检查网络连接或刷新页面。</p>
    <video controls class="video-player">
      <source :src="videoSrc" type="video/mp4">
    </video>
    <p class="hidden-text">什么，你问我为什么要联网？问就是图省事没做离线 :P</p>
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
    // HACK: 这里直接图省事把视频放在了 GitHub Pages 上，实际项目中应该放在 CDN 或 OSS 上。
    this.videoSrc = this.side === 'A' 
      ? 'https://akutazehy.github.io/assets/videos/sateri/Sateri%20A-side.mp4' 
      : 'https://akutazehy.github.io/assets/videos/sateri/Sateri%20B-side.mp4';
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
  margin-top: 10px;
}

.hidden-text {
  font-size: 12px;
  color: whitesmoke;
}

</style>