<template>
  <div class="home">
    <h1>SATERI DEMO</h1>
    <div>
      <p>当前时间: {{ currentTime }}</p>
      <p>时区: {{ timezone }}</p>
    </div>
    <p>为第三回蚊集令准备的特供DEMO！</p>
      <button @click="navigateToInstructionPage">阅读说明</button>
      <button @click="flipCoin">试试手气</button>
    <p class="hidden-text" @click="navigateToHiddenPage">这里似乎藏着什么东西</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';
import { useCurrentTime } from '../utils/timeUtils';
import { flipCoin as flipCoinUtil } from '../utils/coinFlip';

export default defineComponent({
  name: 'Home',
  setup() {
    const { currentTime, timezone } = useCurrentTime();
    const router = useRouter();

    const flipCoin = () => {
      const result = flipCoinUtil();
      const side = result === 0 ? 'A' : 'B';
      router.push(`/disk/${side}`);
    };

    const navigateToHiddenPage = () => {
      router.push('/password');
    };

    const navigateToInstructionPage = () => {
      router.push('/instruction');
    };

    return {
      currentTime,
      timezone,
      flipCoin,
      navigateToHiddenPage,
      navigateToInstructionPage
    };
  }
});
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}

.home * {
  margin: 5px 0;
}

.link {
  margin: 20px 0;
  text-decoration: none;
  color: blue;
}

.hidden-text {
  color: white;
  cursor: pointer;
  text-decoration: underline;
  font-size: 4px;
  margin-top: 20px;
}
</style>