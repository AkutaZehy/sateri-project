<template>
	<div class="password">
		<div v-if="showInput">
			<router-link to="/" class="link">返回</router-link>
		
			<h1>你发现了一个隐藏的页面</h1>
			<br />
			<p>首先，秘钥是：</p>

			<input v-model="password" placeholder="XXXX-XXXX-XXXX" />
			<br />
			<button @click="checkPassword">提交</button>
		</div>
		<p v-if="errorMessage" class="error">{{ errorMessage }}</p>
	</div>
</template>

<script>
import { flipCoin } from '../utils/coinFlip';
import { checkPassword } from '../utils/checkPassword';
import { useRouter } from 'vue-router';

export default {
	name: 'Home',
	data () {
		return {
			password: '',
			errorMessage: '',
			errorCount: 0,
			showInput: true
		};
	},
	methods: {
		checkPassword () {
			if (checkPassword(this.password)) {
				this.$router.push('/puzzle');
			} else {
				this.errorCount++;
				if (this.errorCount >= 3) {
					this.errorMessage = '错误次数过多，已锁定页面。';
					this.showInput = false;
				} else {
					this.errorMessage = '错误，请重试。你还有 ' + (3 - this.errorCount) + ' 次机会。';
				}
			}
		}
	}
}
</script>

<style scoped>
.password {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
	text-align: center;
}

.password * {
	margin: 5px 0;
	text-align: center;
}

.link {
	margin: 20px 0;
	text-decoration: none;
	color: blue;
}
</style>