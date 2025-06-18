<script lang="ts">
  import { onMount } from 'svelte';

  let data: any;

  onMount(async () => {
    const response = await fetch('/api/data'); // Modifica l'endpoint in base alle tue esigenze
    data = await response.json();
  });
</script>

<main>
  <h1>Benvenuto nella mia applicazione SvelteKit!</h1>
  {#if data}
    <ul>
      {#each data as item}
        <li>{item.name}</li> <!-- Modifica in base alla struttura dei dati -->
      {/each}
    </ul>
  {:else}
    <p>Caricamento...</p>
  {/if}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 600px;
    margin: 0 auto;
  }
</style>