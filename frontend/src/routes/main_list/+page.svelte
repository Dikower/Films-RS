<script lang="ts">
  import FilmCard from "$lib/components/film_card.svelte";
  import { getFilms } from "$lib/funtions";
  import { onMount } from "svelte";

  let films: any[] = [];
  onMount(async () => {
    films = await getFilms(0);
    console.log(films);
  })
</script>

{#each films as film}
  <FilmCard film_info = {film} add_class = "mx-auto"/>  
{/each}