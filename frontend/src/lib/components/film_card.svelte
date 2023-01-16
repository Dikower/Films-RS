<script lang="ts">
  import { goto } from "$app/navigation";

  export let film_info:any = {};
  export let add_class = "";
</script>


<div class={"border-21 shadow m-4 h-20 flex hover:bg-gray-50 hover:shadow-lg cursor-pointer " + add_class} on:click={() => {goto("/film_" + film_info.id)}} on:keydown={() => {}}>

  {#if !true}
    <img class="w-16 h-16 my-auto mx-2" src={"https://image.tmdb.org/t/p/w500" + film_info.poster_path} alt="">
  {:else}
    <img class="w-16 h-16 my-auto mx-2" src="./film_reel.png" alt="">
  {/if}

  <div class="flex flex-col" style="width: calc(100% - 9rem);">
    <p>{film_info.title}</p>
    {#if film_info.tagline !== null}
      <p class="text-xs text-gray-500 truncate">{film_info.tagline}</p>
    {/if}
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
