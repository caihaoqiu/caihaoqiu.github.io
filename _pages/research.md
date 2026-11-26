---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

<style>
  /* Main Page Title (About Me font size + spacing) */
  .page__content h1,
  .archive .page__title {
    font-size: 1.4em !important;
    margin-bottom: 0.5em !important;
  }

  /* Section Headings (About Me 1.18em font size + CV spacing & underline) */
  .page__content h2,
  .page__content h3,
  .archive h1:not(.page__title),
  .archive h2,
  .archive h3 {
    font-size: 1.18em !important;
    border-bottom: 1px solid #888 !important;
    padding-bottom: 0.25em !important;
    margin-top: 1.4em !important;
    margin-bottom: 0.6em !important;
  }

  /* Body Text & List Items (About Me 0.88em font size + CV 1.5 line spacing) */
  .page__content p,
  .page__content ul li,
  .page__content ol li,
  .archive p,
  .archive ul li,
  .archive ol li {
    font-size: 0.88em !important;
    line-height: 1.5 !important;
  }

  /* List Block Spacing (CV spacing) */
  .page__content ul,
  .page__content ol,
  .archive ul,
  .archive ol {
    margin-top: 0.25em !important;
    margin-bottom: 0.75em !important;
  }

  /* Prevent Nested Sub-Bullets from Shrinking Twice */
  .page__content li ul li,
  .page__content li ol li,
  .archive li ul li,
  .archive li ol li {
    font-size: 1em !important;
  }

  /* Rolling Figure Gallery Styles */
  .fig-carousel {
    position: relative;
    width: 100%;
    margin: 1.0rem 0 1.3rem 0;
    overflow: hidden;
    text-align: center;
  }
  .fig-track {
    display: flex;
    transition: transform 0.5s ease-in-out;
  }
  .fig-slide {
    min-width: 100%;
    box-sizing: border-box;
    padding: 0 2.2rem; /* leaves room for side arrows */
  }
  .fig-slide img {
    max-width: 85%;
    height: 270px;
    object-fit: contain;
    border: 1px solid #e5e7eb;
    border-radius: 4px;
    display: inline-block;
  }
  .fig-caption {
    font-size: 0.78rem;
    color: #666;
    margin-top: 0.35rem;
  }
  .fig-btn {
    position: absolute;
    top: 44%;
    transform: translateY(-50%);
    background: rgba(55, 55, 55, 0.8);
    color: #fff;
    border: none;
    width: 26px;
    height: 36px;
    cursor: pointer;
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
  }
  .fig-btn:hover {
    background: rgba(20, 20, 20, 0.95);
  }
  .fig-prev { left: 0; }
  .fig-next { right: 0; }
  .fig-dots {
    text-align: center;
    margin-top: 0.45rem;
  }
  .fig-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    margin: 0 4px;
    border-radius: 50%;
    cursor: pointer;
    border: 1px solid #cccccc;
    transition: all 0.3s;
  }
</style>


### Thermodynamics and Kinetics of Interfaces and Interface-Mediated Plasticity

<div class="fig-carousel">
  <div class="fig-track">
    <div class="fig-slide">
      <img src="/images/research/disconnection_geometry.svg" alt="Interface faceting-defaceting" />
      <div class="fig-caption">Fig. 1: The disconnection description of an arbitrarily curved GB (green curve) where the black lattice (representing one grain) and the white lattice (representing the other grain) meet together.</div>
    </div>
    <div class="fig-slide">
      <img src="/images/research/faceting.jpg" alt="Second figure" />
      <div class="fig-caption">Fig. 2: Interface faceting-defaceting mediated by disconnections</div>
    </div>
    <div class="fig-slide">
      <img src="/images/research/rotation.svg" alt="Third figure" />
      <div class="fig-caption">Fig. 3: Grain rotation during grain growth mediated by disconnection</div>
    </div> <!-- <-- THIS CLOSING TAG WAS MISSING -->
  </div>
  <button class="fig-btn fig-prev" aria-label="Previous">&#10094;</button>
  <button class="fig-btn fig-next" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>


Developing theoretical, bicrystallography-respecting, disconnection-mechanism-based continuum models to describe interface/grain boundary thermodynamics (e.g., interface/GB energy and equilibrium interface/GB structure); diffusive and non-diffusive interface/GB kinetics (e.g., interface/GB diffusion, faceting-defaceting, roughening, and migration); and interface-mediated plasticity (e.g., dislocation–interface interactions). 


### Microstructure Evolution in Polycrystals

<div class="fig-carousel">
  <div class="fig-track">
    <div class="fig-slide">
      <img src="/images/research/polycrystal_1.jpg" alt="Polycrystal figure 1" />
      <div class="fig-caption">Fig. 1: Description of first polycrystal figure</div>
    </div>
    <div class="fig-slide">
      <img src="/images/research/polycrystal_2.jpg" alt="Polycrystal figure 2" />
      <div class="fig-caption">Fig. 2: Description of second polycrystal figure</div>
    </div>
  </div>
  <button class="fig-btn fig-prev" aria-label="Previous">&#10094;</button>
  <button class="fig-btn fig-next" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>

Investigating the mechanisms governing microstructure evolution in polycrystals (i.e., grain growth and static/dynamic recrystallization), and developing theories, mechanism-based continuum models, and numerical methods to predict microstructure evolution in polycrystalline materials.


### Materials Behavior under Far-from-Equilibrium Conditions

<div class="fig-carousel">
  <div class="fig-track">
    <div class="fig-slide">
      <img src="/images/research/noneq_1.jpg" alt="Far-from-equilibrium figure 1" />
      <div class="fig-caption">Fig. 1: Description of first far-from-equilibrium figure</div>
    </div>
    <div class="fig-slide">
      <img src="/images/research/noneq_2.jpg" alt="Far-from-equilibrium figure 2" />
      <div class="fig-caption">Fig. 2: Description of second far-from-equilibrium figure</div>
    </div>
  </div>
  <button class="fig-btn fig-prev" aria-label="Previous">&#10094;</button>
  <button class="fig-btn fig-next" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>

Investigating defect dynamics, microstructure evolution, and mechanical/functional properties under far-from-equilibrium conditions, including rapid quenching, severe plastic deformation, impact loading, oscillatory driving, and strong temperature gradients.


### Bio-inspired Architected and Heterostructured Materials

<div class="fig-carousel">
  <div class="fig-track">
    <div class="fig-slide">
      <img src="/images/research/bio_1.jpg" alt="Bio-inspired figure 1" />
      <div class="fig-caption">Fig. 1: Description of first bio-inspired figure</div>
    </div>
    <div class="fig-slide">
      <img src="/images/research/bio_2.jpg" alt="Bio-inspired figure 2" />
      <div class="fig-caption">Fig. 2: Description of second bio-inspired figure</div>
    </div>
  </div>
  <button class="fig-btn fig-prev" aria-label="Previous">&#10094;</button>
  <button class="fig-btn fig-next" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>

Designing heterogeneous microstructures in polycrystalline and composite materials inspired by natural architectures (e.g., nacre, bamboo, leaves, and butterfly-wing scales) to overcome conventional property trade-offs and achieve multifunctionality.


### Physics-informed AI-assisted Materials Design

<div class="fig-carousel">
  <div class="fig-track">
    <div class="fig-slide">
      <img src="/images/research/ai_1.jpg" alt="AI materials design figure 1" />
      <div class="fig-caption">Fig. 1: Description of first AI-assisted design figure</div>
    </div>
    <div class="fig-slide">
      <img src="/images/research/ai_2.jpg" alt="AI materials design figure 2" />
      <div class="fig-caption">Fig. 2: Description of second AI-assisted design figure</div>
    </div>
  </div>
  <button class="fig-btn fig-prev" aria-label="Previous">&#10094;</button>
  <button class="fig-btn fig-next" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>

Integrating physical laws and mechanistic models with deep learning to efficiently navigate large processing and microstructure parametric spaces, combining predictive accuracy with mechanistic interpretability and advancing toward autonomous materials design.


<script>
  document.querySelectorAll('.fig-carousel').forEach((carousel) => {
    const track = carousel.querySelector('.fig-track');
    const slides = carousel.querySelectorAll('.fig-slide');
    const dotsContainer = carousel.querySelector('.fig-dots');
    const prevBtn = carousel.querySelector('.fig-prev');
    const nextBtn = carousel.querySelector('.fig-next');
    let index = 0;
    let timer;

    // Hide arrows & dots if a section only has 1 picture so far
    if (slides.length <= 1) {
      prevBtn.style.display = 'none';
      nextBtn.style.display = 'none';
      return;
    }

    slides.forEach((_, i) => {
      const dot = document.createElement('span');
      dot.className = 'fig-dot';
      dot.onclick = () => goToSlide(i);
      dotsContainer.appendChild(dot);
    });

    function update() {
      track.style.transform = `translateX(-${index * 100}%)`;
      Array.from(dotsContainer.children).forEach((dot, i) => {
        dot.style.background = i === index ? '#000000' : 'transparent';
        dot.style.borderColor = i === index ? '#000000' : '#cccccc';
      });
    }

    function moveSlide(step) {
      index = (index + step + slides.length) % slides.length;
      update();
      resetTimer();
    }

    function goToSlide(i) {
      index = i;
      update();
      resetTimer();
    }

    function resetTimer() {
      clearInterval(timer);
      timer = setInterval(() => moveSlide(1), 5000);
    }

    prevBtn.onclick = () => moveSlide(-1);
    nextBtn.onclick = () => moveSlide(1);

    carousel.addEventListener('mouseenter', () => clearInterval(timer));
    carousel.addEventListener('mouseleave', resetTimer);

    update();
    resetTimer();
  });
</script>
