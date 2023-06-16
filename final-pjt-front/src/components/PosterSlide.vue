<template>
  <div>
    <div class="f-carousel" :id="`myCarousel${num}`" >
      <div id="carouselPoster" class="f-carousel__slide poster" v-for="(movie) in movies" :key="movie.id" >
        <img class="back" :src="'https://image.tmdb.org/t/p/original/' + movie?.poster_path" >
        <img class="bgimg" :src="'https://image.tmdb.org/t/p/original/' + movie?.poster_path" 
        :alt="movie?.title">
        <div class="title">
          <h2>{{ movie.title }}</h2>
          <p>{{ movie.overview.slice(0, 150) + '...' }}</p>
        </div>
        <PosterSlideItem id="posterbutton" :movie="movie"/>
      </div>
    </div>
    <div class="f-carousel" :id="`myNavigation${this.num}`">
      <div class="f-carousel__slide zoom" v-for="(movie) in movies" :key="movie.id">
        <img :src="'https://image.tmdb.org/t/p/original/' + movie?.poster_path" 
        width="150px" height="210px" :alt="movie?.title">
      </div>
    </div>
  </div>
</template>

<script>
import { Carousel } from "@fancyapps/ui/dist/carousel/carousel.esm.js";
import "@fancyapps/ui/dist/carousel/carousel.css";
import PosterSlideItem from "./PosterSlideItem.vue";
import { Autoplay } from "@fancyapps/ui/dist/carousel/carousel.autoplay.esm.js";
import "@fancyapps/ui/dist/carousel/carousel.autoplay.css";

export default {
  name: 'PosterSlide',
  components: {
    PosterSlideItem
  },
  props: {
    movies: Array,
    num: Number
  },
  updated() {
    const mainContainer = document.getElementById(`myCarousel${this.num}`)
    // const mainOptions = {
    //   Autoplay: {
    //     timeout: 3000,
        
    //   },
    // };

    const mainCarousel = new Carousel(mainContainer, {
      Autoplay: {
        timeout: 2000,
        showProgress: false
      }
    }, {
      Autoplay
    });

    // Carousel for navigation
    const navContainer = document.getElementById(`myNavigation${this.num}`);
    const navOptions = {
      Sync: {
        target: mainCarousel,
      },
    };

    new Carousel(navContainer, navOptions)
  }
}
</script>

<style>
  .f-carousel__slide {
    display: flex;
    align-items: center;
    justify-content: center;

    min-height: 100px;
    text-align: center;
    font-size: 1.25rem;
  }

  .f-carousel__slide.is-nav-selected {
    color: #fff;
    border:#ff3520;
  }

  #myCarousel {
    --f-carousel-slide-width: 100%;
    --f-carousel-spacing: 10px;

    margin-bottom: 1rem;
  }

  #myNavigation1 {
    --f-carousel-slide-width: 150px;
    --f-carousel-spacing: 5px;
  }

  #myNavigation2 {
    --f-carousel-slide-width: 150px;
    --f-carousel-spacing: 5px;
  }
  #myNavigation3 {
    --f-carousel-slide-width: 150px;
    --f-carousel-spacing: 5px;
  }

  .zoom:hover {
    transform: scale(1.2);
    transition: .5s;
  }

  .bgimg {
    background-size: cover;
    height: 400px;
    object-fit: cover;
  }
  .back{
    position: absolute;
    opacity: 0.3;
    z-index: -1;
    object-fit: cover;
    width: 100%;
    height: 100%;
  }
  
  .zoom {
    position: relative;
  }

  #carouselPoster {
    position: relative;
  }

  .poster:hover {
    transition: .7s;
    transform: scale(1.2);
    opacity: 1;
  }

  .poster:hover .bgimg {
    opacity: 0.5;
  }

  .title {
    position: absolute;
    text-align: left;
    padding-top: 5%;
    left: 10%;
    width: 80%;
    height: 100%; 
    opacity: 0;
  }

  .poster:hover .title {
    opacity: 1;
    transform: scale(0.8);
  }

  #posterbutton {
    position: absolute;
    right: 10%;
    top: 70%;
    opacity: 0;
  }

  .poster:hover #posterbutton {
    opacity: 1;
    transform: scale(0.6);
  }

  h2 {
    color: #FFD963;
  }

</style>