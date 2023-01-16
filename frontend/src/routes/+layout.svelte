<script>
	import Header from './Header.svelte';
	import './styles.css';
</script>

<div class="w-auto mx-4 sm:w-6/12 sm:mx-auto shadow">
	<Header />

	<main>
		<slot />
	</main>
</div>
