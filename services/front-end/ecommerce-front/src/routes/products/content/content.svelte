<script>
	import Cards from "../cards/cards.svelte";
import Filter from "../filter/filter.svelte";
let nombreGenero = "Genero";
let nombreCategoria="Categoria"
</script>
<div class="grid grid-cols-1 gap-4">
	<div class="flex flex-row justify-around col-span-2 my-5">
       
        <Filter nombre={nombreGenero}></Filter>
        <Filter nombre={nombreCategoria}></Filter>
        <label class="input input-bordered flex items-center gap-2">
            <input type="text" class="grow m-5" placeholder="Search" />
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" /></svg>
          </label>
    </div>
    <div class="grid grd-cols-4 gap-3">
  <Cards></Cards>
    </div>
</div>
