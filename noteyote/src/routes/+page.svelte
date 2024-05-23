<script lang="ts">
    import { notebooks, startNotebook, stopNotebooks } from '../stores/notebook';
    import DraggableWindow from '$lib/DraggableWindow.svelte';

    let notebookList: any[] = [];
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

<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/users">Users</a></li>
    </ul>
</nav>

<main>
    <button on:click={handleStartNotebook}>Start Notebook</button>
    <button on:click={handleStopNotebooks}>Stop All Notebooks</button>

    {#each notebookList as notebook (notebook.id)}
        <DraggableWindow>
            <iframe src={notebook.url} width="100%" height="100%"></iframe>
        </DraggableWindow>
    {/each}
</main>

<style>
    nav {
        background-color: #333;
        color: white;
        padding: 1rem;
    }

    nav ul {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
    }

    nav ul li {
        margin-right: 1rem;
    }

    nav ul li a {
        color: white;
        text-decoration: none;
    }

    nav ul li a:hover {
        text-decoration: underline;
    }

    main {
        padding: 1rem;
    }
</style>
