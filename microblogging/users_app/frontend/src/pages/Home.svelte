<script>
    import TailwindCSS from "../TailwindCSS.svelte";
    import Header from "../components/Header.svelte"; 
    import Posts from "../components/Posts.svelte"; 
    import Menu from "../components/Menu.svelte";
  </script>
  
  <TailwindCSS />

  <main class="min-h-screen bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90% pb-20">
  
    <Header />
    <br>
    <Posts />
    <footer class="fixed bottom-0 w-auto bg-blue-200">
      <Menu />
    </footer>
  </main>