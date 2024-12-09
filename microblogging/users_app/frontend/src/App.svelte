<script>
  import Counter from './lib/Counter.svelte'
  import TailwindCSS from "./TailwindCSS.svelte";

  // @ts-ignore
  let username = (window.initialAppState) ? window.initialAppState : 'Unknown';
  // @ts-ignore
  let post = (window.initialPost) ? window.initialPost : 'Unknown';
  // @ts-ignore
  let userName = window.users
  
</script>

<TailwindCSS />

<main>
  <h1 class="bg-slate-50">Bonjour {username}</h1>
<p>Le premier post : {post}</p>
{#each userName as user} 
  <ul><li>{user.username}

  </li></ul>
{/each}
</main>


