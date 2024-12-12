<script>
    import TailwindCSS from "../TailwindCSS.svelte";  

    // @ts-ignore
    let posts = window.initialPosts
    
    let fullLike = "m12.75 20.66 6.184-7.098c2.677-2.884 2.559-6.506.754-8.705-.898-1.095-2.206-1.816-3.72-1.855-1.293-.034-2.652.43-3.963 1.442-1.315-1.012-2.678-1.476-3.973-1.442-1.515.04-2.825.76-3.724 1.855-1.806 2.201-1.915 5.823.772 8.706l6.183 7.097c.19.216.46.34.743.34a.985.985 0 0 0 .743-.34Z";
    let emptyLike = "M12.01 6.001C6.5 1 1 8 5.782 13.001L12.011 20l6.23-7C23 8 17.5 1 12.01 6.002Z";
    
    // Tracker les likes par post
    let likedPosts = new Set();
    
    const toggleLike = (postId) => { 
        // Basculer le like pour ce post spécifique
        if (likedPosts.has(postId)) {
            likedPosts.delete(postId);
        } else {
            likedPosts.add(postId);
        }
        // Forcer une mise à jour de Svelte
        posts = [...posts];
    } 
</script>

<TailwindCSS />

<main class="flex justify-center">
    <div class="w-full max-w-[100vh] h-screen px-4 space-y-4 pb-16">
    {#each posts as post}
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
                <span class="font-bold text-white">@{post.user}</span>
            </div>
            
            <p class="text-white mb-4">
                {post.content}
            </p>
            
            <div class="flex justify-between text-white">
                <button on:click={() => toggleLike(post.id)} aria-label="like">
                    <svg 
                        class="rounded-full w-6 h-6 text-gray-800 dark:text-white" 
                        aria-hidden="true" 
                        xmlns="http://www.w3.org/2000/svg" 
                        width="24" 
                        height="24" 
                        fill={likedPosts.has(post.id) ? "currentColor" : "none"} 
                        viewBox="0 0 24 24"
                    >
                        <path 
                            stroke="currentColor" 
                            stroke-linecap="round" 
                            stroke-linejoin="round" 
                            stroke-width="2" 
                            d={likedPosts.has(post.id) ? fullLike : emptyLike}
                        />
                    </svg>
                </button>
                <button class="hover:bg-white hover:bg-opacity-20 rounded-full">{post.tags}</button>
            </div>
        </div>
    {/each}
</div>
</main>