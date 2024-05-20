<script>
  import { createUser } from '$lib/api';

  let username = '';
  let password = '';

  const handleSubmit = async () => {
    await createUser(username, password);
    alert('User created');
  };
</script>

<main>
  <h1>Create User</h1>
  <form on:submit|preventDefault={handleSubmit}>
    <label for="username">Username</label>
    <input id="username" bind:value={username} />
    <label for="password">Password</label>
    <input id="password" type="password" bind:value={password} />
    <button type="submit">Create User</button>
  </form>
</main>

