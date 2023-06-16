<template>
  <div>
    <!-- Page wrapper-->

    <div class="page-wrapper">
        
      <!-- 젤처름 꿀벌 3마리 랑 스크롤-->
      
      <section class="bg-dark dark-mode position-relative min-vh-100 overflow-hidden pt-0">
        <svg class="position-absolute top-0" width="262" height="160" viewBox="0 0 262 160" fill="none" xmlns="http://www.w3.org/2000/svg" style="left: 6%;">
          <ellipse cx="131" cy="30.5" rx="131" ry="129.5" fill="white" fill-opacity=".03"></ellipse>
        </svg>
        <div class="container position-relative zindex-5 text-center pt-5 mt-lg-4 mt-xl-5">
          <h1 class="display-1 pt-4 mt-sm-3"><span class="text-white fw-normal"><h3> 영화추천은 </h3></span><span class="d-inline-flex align-items-center"><span class="text-white">HIVE!</span></span></h1>
          <p class="fs-xl mb-5">페이지를 스크롤해주세요</p><a class="scroll-down-btn" href="#landings" data-scroll data-scroll-offset="20">
            <div class="mouse"></div>
            <p>Landings</p></a>
        </div>
        <div class="d-none d-lg-block" style="margin-top: -80px;"></div>
        <div class="d-none d-sm-block d-lg-none" style="margin-top: -40px;"></div>
        <div class="parallax mx-auto mb-n5" style="max-width: 800px;">
          <div class="rotate parallax-layer zindex-2" data-depth="0.9" style="margin-top: -4cm;"><img src="../assets/fly.png" alt="Foreground shape"></div>
          <div class="rotate parallax-layer zindex-2" data-depth="0.9" style="margin-left: -5cm; margin-left: -5cm;"><img src="../assets/fly.png" alt="Foreground shape"></div>
          <div class="rotate parallax-layer zindex-2" data-depth="0.9" style="margin-top: -7cm; margin-left: -12cm;"><img src="../assets/fly.png" alt="Foreground shape"></div>
          <div class="rotate parallax-layer zindex-2" data-depth="0.9" style="margin-top: -10cm;"><img src="../assets/fly.png" alt="Foreground shape"></div>
          <div class="rotate parallax-layer zindex-2" data-depth="0.9" style="margin-top: -3cm; margin-left: 7cm;"><img src="../assets/fly.png" alt="Foreground shape"></div>
          <div class="parallax-layer" data-depth="-0.1"><img src="assets/img/landing/intro/hero/01.png" alt="Background shapes"></div>
        </div>
      </section>
      <!-- HIVE란?-->
      <div class="bg-gray py-2 py-lg-3 py-xl-4 py-xxl-5" id="landings">
        <div class="container py-5 mt-1 mb-2 mt-sm-2 mb-sm-3 mt-md-3 mb-md-4 my-lg-4 my-xl-5">
          <h1 class="display-5 text-center pt-xxl-2">HIVE란?</h1>
          <h3 class="display-5 text-center pt-xxl-2">당신을 위해 최고의 영화를 선택해봤어요!</h3>
         
          <h4 class="fs-lg text-center  pb-3 pb-lg-0 mb-lg-5">"잠깐의 시간을 잊고 즐거운 시간을 보내실 수 있을 거예요. 여러분을 감동시키고 웃음을 안겨줄 영화를 선별했습니다. 편안한 자리에 앉아서 최고의 영화와 함께 특별한 순간을 즐겨보세요!"</h4>
          <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 gy-5 pb-xl-3">
            <!-- 사진들어가는곳-->
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/6.png"><img class="d-none d-dark-mode-block" src="../assets/6.png"></div>
                <h3 class="text-center mb-0"><a class="stretched-link" href="#">HIVE추천영화</a></h3>
              </div>
            </div>
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/2.png" ><img class="d-none d-dark-mode-block" src="../assets/2.png"></div>
                <h3 class="text-center mb-0"><a class="stretched-link" href="#">죽기전 꼭봐야하는 영화</a></h3>
              </div>
            </div>
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/1.png" ><img class="d-none d-dark-mode-block" src="../assets/1.png"></div>
                <h3 class="text-center mb-0"><a class="stretched-link" href="#">오늘 이거 어때요?</a></h3>
              </div>
            </div>
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/3.png"><img class="d-none d-dark-mode-block" src="../assets/3.png"></div>
                <h3 class="text-center mb-0"><a class="stretched-link" href="#">장르별</a></h3>
              </div>
            </div>
            
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/5.png" ><img class="d-none d-dark-mode-block" src="../assets/5.png"></div>
                <h3 class="text-center mb-0"><a class="stretched-link" href="#">게시판</a></h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
    <br>
      <!-- 사이트 목업 보여주는곳-->
      <div class="bg-gray">
      <section id="hiddenSection" class="pt-2 pt-sm-3 pt-md-4 pt-lg-3 pb-1 pb-sm-3 pb-md-4 pb-lg-5" >
        <div class="container position-relative py-5 my-lg-3 my-xl-4 my-xxl-5">
          <div class="position-absolute" style="margin-left: -9.7%;" data-aos="zoom-in" data-aos-duration="500" data-aos-offset="300" data-disable-parallax-down="lg">
            <svg class="text-warning d-none d-lg-block" width="744" height="744" viewBox="0 0 744 744" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <circle cx="372" cy="372" r="372"></circle>
            </svg>
          </div>
          <div class="d-none d-xxl-block" style="height: 190px;"></div>
          <div class="d-none d-lg-block d-xxl-none" style="height: 150px;"></div>
          <div class="row justify-content-center justify-content-lg-start position-relative zindex-2">
            <div class="col-sm-10 col-md-8 col-lg-5 col-xl-4 text-center text-lg-start" data-aos="fade-up" data-aos-duration="850" data-aos-offset="120" data-disable-parallax-down="lg">
              <div class="ignore-dark-mode d-none d-lg-block">
                <h2 class="display-5 mb-4">영화 추천 HIVE</h2>
                <p class="fs-lg text-dark pb-3 pb-sm-4 mb-lg-0">"하루의 피로를 한 번의 클릭으로 날려버리세요!  이제 한 번의 클릭으로 최고의 영화를 경험할 수 있습니다!"</p>
              </div>
              <div class="d-lg-none">
                <h2 class="display-5 mb-4">영화 추천의 새로운시작 HIVE</h2>
                <p class="fs-lg text-dark pb-3 pb-sm-4 mb-lg-0">"하루의 피로를 한 번의 클릭으로 날려버리세요!  이제 한 번의 클릭으로 최고의 영화를 경험할 수 있습니다!"</p>
              </div>
            </div>
          </div>
          <div class="d-none d-xl-block" style="margin-top: -240px;"></div>
          <div class="d-none d-lg-block d-xl-none" style="margin-top: -160px;"></div>
          <div class="d-flex position-relative zindex-2 mb-3">
            <div class="flex-xxl-shrink-0 position-relative zindex-2" style="max-width: 700px; margin-top: 26%; margin-right: 5.6%;" data-aos="fade-up" data-aos-duration="500" data-aos-delay="400" data-disable-parallax-down="lg">
              <img class="rounded-3 mt-n5 mt-lg-0 d-block d-dark-mode-none" src="assets/Group3.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(65,81,98, .2);">
              <img class="rounded-3 mt-n5 mt-lg-0 d-none d-dark-mode-block" src="assets/Group3.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(0,0,0, .2);"></div>
            <div class="flex-xxl-shrink-0 position-relative zindex-1" style="max-width: 600px; margin-top: 17.6%; margin-right: 5.5%;" data-aos="fade-up" data-aos-duration="500" data-aos-delay="200" data-disable-parallax-down="lg">
              <img class="rounded-3 mt-n5 mt-lg-0 d-block d-dark-mode-none" src="assets/Group5.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(65,81,98, .2);">
              <img class="rounded-3 mt-n5 mt-lg-0 d-none d-dark-mode-block" src="assets/Group5.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(0,0,0, .2);"></div>
            <div class="flex-xxl-shrink-0" style="max-width: 600px;" data-aos="fade-up" data-aos-duration="500" data-aos-offset="250" data-disable-parallax-down="lg">
              <img class="rounded-3 d-block d-dark-mode-none" src="assets/Group6.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(65,81,98, .2);">
              <img class="rounded-3 d-none d-dark-mode-block" src="assets/Group6.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(0,0,0, .2);"></div>
          </div>
        </div>
      </section>
    </div>
      <!-- 출연진별-->
      <div class="bg-gray">
      <section class="container pt-5 mt-lg-3 mt-xl-4 mt-xxl-5">
        <h2 class="display-5 text-center pt-2 pt-sm-3 pt-md-4 pt-lg-5 pb-lg-3 mt-xxl-2 mb-0">출연진별 모아보기</h2>
        
        <div class="row align-items-center py-4 mt-2 mt-sm-3 mt-md-4 mb-2 mb-md-3 mb-lg-4" data-aos="fade-up" data-aos-duration="600" data-aos-offset="300" data-disable-parallax-down="md">
          <div class="col-md-6 col-lg-7 order-md-2 d-flex justify-content-end"><img class="d-dark-mode-none" src="assets/출연진1.png" width="593" alt="Colors" style="border-radius: 3%;"><img class="d-none d-dark-mode-block" src="assets/출연진1.png" width="593" alt="Colors" style="border-radius: 3%;"></div>
          <div class="col-md-6 col-lg-5 order-md-1 mt-md-n5" data-aos="fade-up" data-aos-duration="850" data-aos-offset="200" data-disable-parallax-down="md">
            <h1 class="display-5 mb-4">감독/출연진</h1>
            <h2 class="fs-lg mb-0 mb-lg-4">선택한 감독/배우 별로 영화를 저희가 정성을 다해 선택해드려요!</h2>
            <h2 class="fs-lg mb-0 mb-lg-4">영화 속 세계로 여행을 떠나보세요.</h2>
          </div>
        </div>
        
      </section>
      </div>



      <!-- 다크모드 -->
      <div class="bg-gray">
      <section class="container pt-5 mt-lg-3 mt-xl-4 mt-xxl-5 ">
        <h2 class="display-5 text-center pt-2 pt-sm-3 pt-md-4 pt-lg-5 pb-lg-3 mt-xxl-2 mb-0 ">다크모드</h2>
        
        <h3 class="display-5 text-center pt-xxl-2">당신의 눈을 위한 최고의 선택!</h3>
        <div class=" row align-items-center py-4 mt-2 mt-sm-3 mt-md-4 mb-2 mb-md-3 mb-lg-4" >
          <div class="col-md-5 col-lg-5 mx-auto ">
            <img  src="assets/다크.png" width="593" height="1400" alt="Colors" style="border-radius: 3%;" >
          </div>

          <div class="col-md-5 col-lg-5 mx-auto" >
            <img  src="assets/라이트.png" width="593" height="1400" alt="Colors" style="border-radius: 3%;">
          </div>
        </div>
        
      </section>
      </div>
      
    
      
    <!-- Back to top button-->
    <a class="btn-scroll-top" href="#top" data-scroll>
      <svg viewBox="0 0 40 40" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
        <circle cx="20" cy="20" r="19" fill="none" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10"></circle>
      </svg><i class="ai-arrow-up"></i>
    </a>
    </div>
  
</template>

<script>
export default {
  data() {
    return {
      target: null,
    };
  },
  methods: {
    scrollEvents() {
      if (window.scrollY > 1800) {
        document.querySelector('#hiddenSection').classList.add('see')
        document.querySelector('#hiddenSection').classList.remove('noneSee')
      } else {
        document.querySelector('#hiddenSection').classList.remove('see')
        document.querySelector('#hiddenSection').classList.add('noneSee')
      }
      
    }
  },
  components: {
    // 컴포넌트의 내용
  },
  mounted() {
    window.scrollTo(0, 0);
    document.addEventListener('scroll', this.scrollEvents);
  },
  destroyed() {
    document.removeEventListener('scroll', this.scrollEvents);
  },
  
};
</script>

<style scoped>
.see {
  opacity: 1;
  transition: 2s; 
}

.noneSee {
  opacity: 0;
  transition: 2s; 
}

.board-list {
    border: solid var(--ar-gray-900);
    border-radius: 20px;
    
  }

.scroll-down-btn {
        display: inline-block;
        text-decoration: none;
      }
      .scroll-down-btn p {
        margin-top: 1.25rem;
        color: white;
        font-size: .875rem;
        font-weight: 500;
        letter-spacing: .375rem;
        text-indent: .375rem;
        animation: colorText 5s ease-out infinite, nudgeText 5s ease-out infinite;
      }
      .mouse {
        background: #2c333e linear-gradient(transparent 0%, transparent 50%, white 50%, white 100%);
        position: relative;
        width: 38px;
        height: 65px;
        margin: 0 auto;
        border-radius: 6rem;
        background-size: 100% 200%;
        animation: colorSlide 5s linear infinite, nudgeMouse 5s ease-out infinite;
      }
      .mouse:before, .mouse:after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        margin: auto;
      }
      .mouse:before {
        width: 34px;
        height: 61px;
        background-color: #121519;
        border-radius: 6rem;
      }
      .mouse:after {
        background-color: white;
        width: .375rem;
        height: .375rem;
        border-radius: 100%;
        animation: trackBallSlide 5s linear infinite;
      }
      @keyframes colorSlide {
        0% { background-position: 0% 100%; }
        20% { background-position: 0% 0%; }
        21% { background-color: #2c333e; }
        29.99% {
          background-color: white;
          background-position: 0% 0%;
        }
        30% {
          background-color: #2c333e;
          background-position: 0% 100%;
        }
        50% { background-position: 0% 0%; }
        51% { background-color: #2c333e; }
        59% {
          background-color: white;
          background-position: 0% 0%;
        }
        60% {
          background-color: #2c333e;
          background-position: 0% 100%;
        }
        80% { background-position: 0% 0%; }
        81% { background-color: #2c333e; }
        90%, 100% {
          background-color: white;
        }
      }
      @keyframes trackBallSlide {
        0% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        6% {
          opacity: 1;
          transform: scale(0.9) translateY(5px);
        }
        14% {
          opacity: 0;
          transform: scale(0.4) translateY(40px);
        }
        15%, 19% {
          opacity: 0;
          transform: scale(0.4) translateY(-20px);
        }
        28%, 29.99% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        30% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        36% {
          opacity: 1;
          transform: scale(0.9) translateY(5px);
        }
        44% {
          opacity: 0;
          transform: scale(0.4) translateY(40px);
        }
        45%, 49% {
          opacity: 0;
          transform: scale(0.4) translateY(-20px);
        }
        58%, 59.99% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        60% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        66% {
          opacity: 1;
          transform: scale(0.9) translateY(5px);
        }
        74% {
          opacity: 0;
          transform: scale(0.4) translateY(40px);
        }
        75%, 79% {
          opacity: 0;
          transform: scale(0.4) translateY(-20px);
        }
        88%, 100% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
      }
      @keyframes nudgeMouse {
        0%, 30%, 60%, 90% { transform: translateY(0); }
        20%, 50%, 80% { transform: translateY(8px); }
      }
      @keyframes nudgeText {
        0%, 30%, 60%, 90% { transform: translateY(0); }
        20%, 50%, 80% { transform: translateY(2px); }
      }
      @keyframes colorText {
        21%, 51%, 81% { color: #2c333e; }
        30%, 60%, 90% { color: white; }
      }
  









      @keyframes rotate_image {
  0% {
    left: 1600px;
    transform: rotate(0deg) translateY(0);
  }
  12.5% {
    transform: rotate(2.5deg) translateY(5px);
  }
  25% {
    transform: rotate(0deg) translateY(-5px);
  }
  37.5% {
    transform: rotate(2.5deg) translateY(5px);
  }
  50% {
    transform: rotate(0deg) translateY(-5px);
  }
  62.5% {
    transform: rotate(2.5deg) translateY(5px);
  }
  75% {
    transform: rotate(0deg) translateY(-5px);
  }
  87.5% {
    transform: rotate(-.5deg) translateY(5px);
  }
  100% {
    left: -1300px;
  }
}

.rotate {
  animation: rotate_image 11s linear infinite;
  position: absolute;
}

</style>
