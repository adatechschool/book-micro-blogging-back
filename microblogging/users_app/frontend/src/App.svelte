<script>
  import TailwindCSS from "./TailwindCSS.svelte";
  import Header from "./components/Header.svelte"; 


  // @ts-ignore
  let username = (window.initialAppState) ? window.initialAppState : 'Unknown';
  // @ts-ignore
  let post = (window.initialPost) ? window.initialPost : 'Unknown';
  // @ts-ignore
  let usersPostContentUsername = window.postsContentUsername
  // @ts-ignore
  let userName = window.users
  
</script>

<TailwindCSS />
<Header />

<main>
{#each usersPostContentUsername as posts}
    <ul>
      <li>{posts[0]} + {posts[1]}</li>
    </ul>
{/each}
</main>


