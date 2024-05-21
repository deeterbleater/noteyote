<script lang="ts">
  import { onMount } from 'svelte';
  import api from './api';

  let items: any[] = [];
  let itemId: number; // Explicitly define the type for itemId

  onMount(async () => {
    try {
      const response = await api.getItems();
      items = response.data;
    } catch (error) {
      console.error('Error fetching items:', error);
    }
  });

  async function fetchItem(itemId: number) { // Explicitly define the type for itemId
    try {
      const response = await api.getItem({itemId: itemId});
      console.log('Fetched item:', response.data);
    } catch (error) {
      console.error('Error fetching item:', error);
    }
  }
</script>

<main>
  <h1>Items</h1>
  <ul>
    {#each items as item}
      <li>{item.item_id}: {item.q}</li>
    {/each}
  </ul>
</main>
