<script>
	import About from "../about/about.svelte";
	import Card from "../cards/card.svelte";
import Caurosel from "../couroles/caurosel.svelte";
	import Footer from "../footer/footer.svelte";
   
</script>
<div class="flex flex-col my-1">
  <Caurosel></Caurosel>
  <About></About>
  <div class=" flex flex-row flex-wrap justify-center my-8">
  <Card></Card>
  <Card></Card>
  <Card></Card>
  </div>
  <Footer></Footer>
</div>