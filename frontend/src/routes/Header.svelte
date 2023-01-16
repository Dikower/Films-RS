<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/svelte-logo.svg';
	import github from '$lib/images/github.svg';

	let path_list = [
		{name: "Главная", path: "/"},
		{name: "Фильмы", path: "/main_list"},
		{name: "Мои оценки", path: "/my_films"},
		{name: "Мои рекомендации", path: "/my_recommendations"},
		
	]
</script>




<header class="shadow p-4">
	{#each path_list as path}
		<a href={path.path} class={($page.url.pathname === path.path ? "text-lg" : "text-gray-500") + " mr-2"}>{path.name}</a>
	{/each}
</header>

