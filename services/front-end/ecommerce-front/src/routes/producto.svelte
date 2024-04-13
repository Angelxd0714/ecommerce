<script>
	import { onMount } from "svelte";
	import Content from "./products/content/content.svelte";
   onMount(()=>{
    console.log(" mounted ")
   })
</script>
<div>
    <Content></Content>
</div>