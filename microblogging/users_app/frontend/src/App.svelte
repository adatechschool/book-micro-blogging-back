<script>
  import Counter from './lib/Counter.svelte'
  import TailwindCSS from "./TailwindCSS.svelte";

  // @ts-ignore
  let username = (window.initialAppState)? window.initialAppState : 'Unknown'
</script>

<TailwindCSS />

<main>
  <h1 class="bg-slate-50">Coucou bisous {username}</h1>
</main>


