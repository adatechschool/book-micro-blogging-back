<script>
    import TailwindCSS from "../TailwindCSS.svelte";
    import Header from "../components/Header.svelte"; 
    import Menu from "../components/Menu.svelte";
    import LoginForm from "../components/LoginForm.svelte"
  </script>
  
  <TailwindCSS />

  <main class="min-h-screen bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90% pb-40">
  
    <Header />
    <br>
    <LoginForm />
    <footer class="fixed bottom-0 w-auto bg-blue-200">
      <Menu />
    </footer>
  </main>