<script lang="ts">
  import DraggableWindow from '$lib/DraggableWindow.svelte';
  import { notebooks, startNotebook, stopNotebooks } from '$stores/notebook';

  let notebookList: { id: string; url: string }[] = [];
  notebooks.subscribe(value => notebookList = value);

  async function handleStartNotebook() {
    try {
      await startNotebook();
    } catch (error) {
      console.error('Error starting notebook:', error);
    }
  }

  async function handleStopNotebooks() {
    try {
      await stopNotebooks();
    } catch (error) {
      console.error('Error stopping notebooks:', error);
    }
  }
</script>

<button on:click={handleStartNotebook}>Start Notebook</button>
<button on:click={handleStopNotebooks}>Stop All Notebooks</button>

{#each notebookList as notebook (notebook.id)}
  <DraggableWindow>
    <iframe src={notebook.url} width="100%" height="100%"></iframe>
  </DraggableWindow>
{/each}

<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  :global(html, body) {
    width: 100%;
    height: 100%;
    background-color: #f0f0f0;
  }
</style>
