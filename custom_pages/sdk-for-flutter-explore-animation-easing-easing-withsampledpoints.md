---
title: "Implementation"
slug: "sdk-for-flutter-explore-animation-easing-easing-withsampledpoints"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Easing.withSampledPoints.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../animation/animation-library.html">/sdk-for-flutter-explore-animation-animation-library</a></li>
<li><a href="../../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a></li>
<li class="self-crumb">Easing.withSampledPoints factory constructor</li>
</ol>
<div class="self-name">Easing.withSampledPoints</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="animation/Easing-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>Easing.withSampledPoints constructor</h1></div>
<section class="multi-line-signature">
Easing.withSampledPoints(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>&gt; points</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates an instance of customized <a href="../../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> using a specified number of points describing an
easing function.</p>
<ul>
<li><code>points</code> List of sampled data points that define an easing function.
X describes normalized time values in the range [0, 1].
Y describes normalized animated value changes. Values can fall outside of the range [0, 1]. During
an animation run animated target value is multiplied with Y value. In case resulting animated target value
falls outside of its own supported range it will be clamped to its range (e.g. when negative values used for
color animation).
X values must increase monotonically.
There must be at least 2 data points specified. The first point's X value must be 0, the last point's
X value must be 1.
During an animation run for any given time value X' from the animation engine that
satisfies the relation X(i) &lt; X' &lt; X(i+1) for the given X data points the corresponding
Y' value will be calculated by linearly interpolating between Y(i) and Y(i+1) data points.
The higher the sampling rate of the easing curve used for the data points the more precise the results.
In order to achieve the same animation precision for animations with different durations
(shorter vs longer) it is recommended to use a higher sampling rate for longer animation duration.</li>
</ul>
<p>Throws <a href="../../animation/EasingInstantiationException-class.html">/sdk-for-flutter-explore-animation-easinginstantiationexception-class</a>. Instantiation error in case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory Easing.withSampledPoints(List&lt;Point2D&gt; points) =&gt; $prototype.withSampledPoints(points);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../animation/animation-library.html">/sdk-for-flutter-explore-animation-animation-library</a></li>
<li><a href="../../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a></li>
<li class="self-crumb">Easing.withSampledPoints factory constructor</li>
</ol>
<h5>Easing class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
