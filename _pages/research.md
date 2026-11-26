---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

<style>
  .page__content h1, .archive .page__title {
    font-size: 1.4em !important;
    margin-bottom: 0.5em !important;
  }
  .page__content h2, .page__content h3, .archive h1:not(.page__title), .archive h2, .archive h3 {
    font-size: 1.18em !important;
    border-bottom: 1px solid #888 !important;
    padding-bottom: 0.25em !important;
    margin-top: 1.4em !important;
    margin-bottom: 0.6em !important;
  }
  .page__content p, .page__content ul li, .page__content ol li, .archive p, .archive ul li, .archive ol li {
    font-size: 0.88em !important;
    line-height: 1.5 !important;
  }
  .page__content ul, .page__content ol, .archive ul, .archive ol {
    margin-top: 0.25em !important;
    margin-bottom: 0.75em !important;
  }
  .page__content li ul li, .page__content li ol li, .archive li ul li, .archive li ol li {
    font-size: 1em !important;
  }
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
    padding: 0 2.2rem;
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
    width: 28px;
    height: 38px;
    cursor: pointer;
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 99 !important;
    pointer-events: auto !important;
    padding: 0 !important;
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

### Grain Boundary Kinetics and Grain Growth 

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
    </div>
        <div class="fig-slide">
      <img src="/images/research/GG1.svg" alt="Fourth figure" />
      <div class="fig-caption">Fig. 4: Internal stress field evolution during grain growth and loss of correlation between GB velocity and curvature due to internal stress</div>
    </div>
    <div class="fig-slide">
      <img src="/images/research/GG2.jpg" alt="Fifth figure" />
      <div class="fig-caption">Fig. 5: Statistics of grain growth considering shear coupling </div>
    </div>
  </div>
  <button type="button" class="fig-btn fig-prev" onclick="moveFigSlide(this, -1)" aria-label="Previous">&#10094;</button>
  <button type="button" class="fig-btn fig-next" onclick="moveFigSlide(this, 1)" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>


Despite decades of investigation, the classical mean curvature flow-description of grain growth fails to explain numerous experimentally observed phenomena. 
We resolved the longstanding discrepancies between theory and experiment by developing theory and a mechanism-based continuum model for grain boundary (GB) migration. 
GB migration in crystalline materials is mediated by disconnections, i.e., line defects constrained on GBs/interfaces possessing both step and/or dislocation character. 
Disconnection-description offers a unified description of GB kinetics, reconciling the shear-coupled migration and conventional capillarity-driven migration
We demonstrate that disconnection-mediated GB migration intrinsically generates internal stress field that, in turn, act on GB migration, which firmly demonstrates that realistic grain growth is disconnection flow instead of classical curvature flow. 
This work revised curvature-driven grain growth with a defect-dynamics-based framework, providing a unified and multiscale understanding of microstructure evolution.

**References**
1. **C. Qiu**, D. J. Srolovitz, G. S. Rohrer, J. Han, and M. Salvalaglio. “Shear-coupled grain growth statistics.” *Acta Materialia*, 317 (2026) 122494.
2. **C. Qiu**, D. J. Srolovitz, G. S. Rohrer, J. Han, and M. Salvalaglio. “Why grain growth is not curvature flow.” *Proceedings of the National Academy of Sciences*, 122 (2025) e2500707122.
3. **C. Qiu**, M. Salvalaglio, D. J. Srolovitz, and J. Han. “Disconnection flow–mediated grain rotation.” *Proceedings of the National Academy of Sciences*, 121 (2024) e2310302121.
4. Y. Tian, X. Gong, M. Xu, **C. Qiu**, Y. Han, Y. Bi, L. V. Estrada, E. Boltynjuk, H. Hahn, J. Han, D. J. Srolovitz, and X. Pan. “Grain rotation mechanisms in nanocrystalline materials: Multiscale observations in Pt thin films.” *Science*, 386 (2024) 49–54.
5. **C. Qiu**, M. Salvalaglio, D. J. Srolovitz, and J. Han. “Interface faceting–defaceting mediated by disconnections.” *Acta Materialia*, 251 (2023) 118880.


### Interface-Mediated Plasticity and Recrystallization Mechanism


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
  <button type="button" class="fig-btn fig-prev" onclick="moveFigSlide(this, -1)" aria-label="Previous">&#10094;</button>
  <button type="button" class="fig-btn fig-next" onclick="moveFigSlide(this, 1)" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>

Understanding the effect of interface on plastic deformation is important to understand, predict and design the mechanical behavior of materials. While it is well understood in homogeneous materials, the presence of interfaces in polycrystals and composites introduces strong constraints and heterogeneity for plastic deformation, fundamentally changing deformation pathways. My research demonstrates how interface properties control plastic deformation pathways and instability.  


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
  <button type="button" class="fig-btn fig-prev" onclick="moveFigSlide(this, -1)" aria-label="Previous">&#10094;</button>
  <button type="button" class="fig-btn fig-next" onclick="moveFigSlide(this, 1)" aria-label="Next">&#10095;</button>
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
  <button type="button" class="fig-btn fig-prev" onclick="moveFigSlide(this, -1)" aria-label="Previous">&#10094;</button>
  <button type="button" class="fig-btn fig-next" onclick="moveFigSlide(this, 1)" aria-label="Next">&#10095;</button>
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
  <button type="button" class="fig-btn fig-prev" onclick="moveFigSlide(this, -1)" aria-label="Previous">&#10094;</button>
  <button type="button" class="fig-btn fig-next" onclick="moveFigSlide(this, 1)" aria-label="Next">&#10095;</button>
  <div class="fig-dots"></div>
</div>

Integrating physical laws and mechanistic models with deep learning to efficiently navigate large processing and microstructure parametric spaces, combining predictive accuracy with mechanistic interpretability and advancing toward autonomous materials design.

<script>
window.moveFigSlide = function(btn, step) {
  var c = btn.closest('.fig-carousel');
  if (c && c._goTo) c._goTo(c._idx + step);
};
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.fig-carousel').forEach(function(c) {
    var track = c.querySelector('.fig-track');
    var slides = c.querySelectorAll('.fig-slide');
    var dotsBox = c.querySelector('.fig-dots');
    var prev = c.querySelector('.fig-prev');
    var next = c.querySelector('.fig-next');
    var timer;
    c._idx = 0;
    if (slides.length <= 1) {
      if (prev) prev.style.display = 'none';
      if (next) next.style.display = 'none';
      return;
    }
    dotsBox.innerHTML = '';
    slides.forEach(function(_, i) {
      var d = document.createElement('span');
      d.className = 'fig-dot';
      d.onclick = function() { c._goTo(i); };
      dotsBox.appendChild(d);
    });
    c._goTo = function(n) {
      c._idx = (n + slides.length) % slides.length;
      track.style.transform = 'translateX(-' + (c._idx * 100) + '%)';
      Array.from(dotsBox.children).forEach(function(d, i) {
        d.style.background = i === c._idx ? '#000' : 'transparent';
        d.style.borderColor = i === c._idx ? '#000' : '#ccc';
      });
      clearInterval(timer);
      timer = setInterval(function() { c._goTo(c._idx + 1); }, 5000);
    };
    c.addEventListener('mouseenter', function() { clearInterval(timer); });
    c.addEventListener('mouseleave', function() {
      clearInterval(timer);
      timer = setInterval(function() { c._goTo(c._idx + 1); }, 5000);
    });
    c._goTo(0);
  });
});
</script>
