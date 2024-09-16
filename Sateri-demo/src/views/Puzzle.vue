<template>
	<div class="puzzle">
		<router-link to="/" class="link">返回</router-link>
	
			<h1>第二道考验</h1>

	</div>
</template>

<script>
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
	}
}
</script>

<style scoped>
.puzzle {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
	text-align: center;
}

.puzzle * {
	margin: 5px 0;
	text-align: center;
}

.link {
	margin: 20px 0;
	text-decoration: none;
	color: blue;
}
</style>