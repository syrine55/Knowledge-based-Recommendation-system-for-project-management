<template>
	<div>
		<vx-card card-background="linear-gradient(120deg, #7f7fd5, #86a8e7, #91eae4)">
			<vs-row>
				<vs-col :key="index" v-tooltip="'col - 6'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="5.85">
					<vx-card class="pointer" @click="redirectToScope()">
						<h5 class="title_cards">Project Scope Management</h5>
					</vx-card>
				</vs-col>
				<vs-col vs-offset="0" v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="0.3">
				</vs-col>
				<vs-col :key="index" v-tooltip="'col - 6'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="5.85">
					<vx-card class="pointer" @click="redirectToSchedule()">
						<h5 class="title_cards">Project Schedule Management</h5>
					</vx-card>
				</vs-col>
			</vs-row>
			<br>
			<vs-row>
				<vs-col vs-offset="0" v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
				</vs-col>
				<vs-col :key="index" v-tooltip="'col - 4'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="5.85">
					<vx-card class="pointer" @click="redirectToCost()">
						<h5 class="title_cards">Project Cost Management</h5>
					</vx-card>
				</vs-col>
				<vs-col vs-offset="0" v-tooltip="'col - 2'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
				</vs-col>
			</vs-row>
		</vx-card>
	</div>
</template>

<script>
export default{
	methods: {
			redirectToSchedule() {
				this.$router.push('/Schedule').catch(() => {})
			},
			redirectToScope() {
				this.$router.push('/Scope').catch(() => {})
			},
			redirectToCost() {
				this.$router.push('/Cost').catch(() => {})
			}
		}
}
</script>

