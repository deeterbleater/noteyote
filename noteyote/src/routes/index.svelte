<script>
  import { onMount } from 'svelte';
  import { fetchUsers } from '$lib/api';

  let users = [];

  onMount(async () => {
    users = await fetchUsers();
  });
</script>

<main>
  <h1>Welcome to SvelteKit</h1>
  <h2>Users</h2>
  <ul>
    {#each users as user}
      <li>{user.username}</li>
    {/each}
  </ul>
</main>

