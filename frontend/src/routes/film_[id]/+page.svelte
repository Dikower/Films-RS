<script lang="ts">
  import { onMount } from "svelte";
  import { getSimilarFilms, getFilm } from "$lib/funtions";
  import FilmCard from "$lib/components/film_card.svelte";

  let id: any = null;
  let films: any[] = [];
  let film_info: any = null;
  onMount(async () => {
    id = Number(document.location.pathname.match(/\d+/));
    films = await getSimilarFilms(id);
    film_info = await getFilm(id);
    // let genres = JSON.parse(film_info.genres);
    console.log(film_info);
  })
</script>

{#if film_info !== null}
  <div class="m-4 flex mx-auto">

    {#if !true}
      <img class="w-16 h-16 my-auto mx-2" src={"https://image.tmdb.org/t/p/w500" + film_info.poster_path} alt="">
    {:else}
      <img class="w-16 h-16 my-auto mx-2" src="./film_reel.png" alt="">
    {/if}

    <div class="flex flex-col" style="width: calc(100% - 9rem);">
      {#if film_info.homepage !== ""}
        <a class="text-blue-500" target="_blank" href={film_info.homepage}>{film_info.title}</a>
      {:else}
        <p>{film_info.title}</p>
      {/if}
      <p class="text-xs text-gray-500 truncate">{film_info.tagline}</p>
      <p class="text-xs text-gray-500 mt-2">{film_info.overview}</p>
      <p class="text-xs text-gray-500 mt-2">{film_info.release_date}</p>
      <!-- <p class="flex mt-auto text-xs text-gray-500 whitespace-nowrap trancate">
        {#each film_info.genres as gener}
          {gener.name} &nbsp
        {/each}
      </p> -->
    </div>
    <div class="w-16 h-16 my-auto ml-auto mr-2 flex">
      {#if film_info.rating !== undefined}
        <p class="m-auto text-2xl text-green-400">{film_info.vote_average}</p>
        <p class="m-auto text-xl text-gray-400">({film_info.rating})</p>
      {:else}
        <p class="m-auto text-2xl text-green-400">{film_info.vote_average}</p>
      {/if}
      
    </div>
    <!-- <button class="rounded hover:bg-gray-50 border mr-auto px-2 text-sm">Получить подборку</button> -->
  </div>
  <p class="ml-4">Похожие фильмы:</p>
{/if}

{#each films as film}
  <FilmCard film_info = {film} add_class = "mx-auto"/>  
{/each}

