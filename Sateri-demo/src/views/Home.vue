<template>
  <div class="home">
    <h1>SATERI DEMO</h1>
    <button @click="flipCoin">Flip a coin</button>
  </div>
</template>

<script>
import { flipCoin } from '../utils/coinFlip';

export default {
  name: 'Home',
	methods: {
		flipCoin() {
			const result = flipCoin();
			const side = result === 0 ? 'A' : 'B';
			this.$router.push(`/disk/${side}`);
		}
	}
}
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

.link {
  margin: 20px 0;
  text-decoration: none;
  color: blue;
}

.video-player {
  width: 80%;
  max-width: 800px;
  margin-top: 20px;
}
</style>