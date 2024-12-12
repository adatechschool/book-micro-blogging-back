<script>
  import TailwindCSS from "../TailwindCSS.svelte";
  import Header from "../components/Header.svelte"; 
  import Posts from "../components/Posts.svelte"; 
  import Menu from "../components/Menu.svelte";
</script>

<TailwindCSS />

<main class="h-fit bg-gradient-to-b from-indigo-400 from-10% via-sky-500 via-30% to-emerald-500 to-100% pb-10">
  
  <Header />
  <Posts />
  <footer class="fixed bottom-0 w-auto bg-blue-200">
    <Menu />
  </footer>
</main>




