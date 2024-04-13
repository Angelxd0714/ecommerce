
<script lang="ts">
  import { Carousel } from 'flowbite-svelte';
    export const images = [
    {
      alt: 'Cosmic timetraveler',
      src: './img/shoping.jpg',
      title: 'cosmic-timetraveler-pYyOZ8q7AII-unsplash.com',
      
    },
    {
      alt: 'Cristina Gottardi',
      src: './img/screen.jpg',
      title: 'cristina-gottardi-CSpjU6hYo_0-unsplash.com',
     
    },
    {
      alt: 'Johannes Plenio',
      src: './img/web.jpg',
      title: 'johannes-plenio-RwHv7LgeC7s-unsplash.com',
      
    },
    
  ];
</script>
<div class="w-full h-full space-y-4">
  <Carousel {images} duration={3000} imgClass="h-auto max-w-full max-h-80 transition-all duration-300 rounded-lg cursor-pointer filter grayscale hover:grayscale-0" />
</div>
