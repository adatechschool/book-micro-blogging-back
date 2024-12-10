<script>
    import TailwindCSS from "../TailwindCSS.svelte";  
  
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

<main class="flex justify-center">
    <div class="w-full max-w-[100vh] h-screen px-4 space-y-4 pb-16">
    {#each usersPostContentUsername as posts}
        <div 
            class="
                bg-white bg-opacity-20 
                backdrop-blur-md 
                rounded-lg 
                border 
                border-white border-opacity-20 
                shadow-lg
                p-4
            "
        >
            <div class="mb-3">
                <span class="font-bold text-white">@{posts[1]}</span>
            </div>
            
            <p class="text-white mb-4">
                {posts[0]}
            </p>
            
            <div class="flex justify-between text-white">
                <button class="hover:bg-white hover:bg-opacity-20 rounded-full">❤️</button>
                <button class="hover:bg-white hover:bg-opacity-20 rounded-full">#</button>
            </div>
        </div>
    {/each}
</div>
</main>

    