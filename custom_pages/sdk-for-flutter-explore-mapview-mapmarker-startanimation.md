---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapmarker-startanimation"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- startAnimation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a></li>
<li class="self-crumb">startAnimation abstract method</li>
</ol>
<div class="self-name">startAnimation</div>
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
<div class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startAnimation abstract method</h1></div>
<section class="multi-line-signature">
void
startAnimation(<wbr/><ol class="parameter-list single-line"> <li><a href="../../animation/MapMarkerAnimation-class.html">/sdk-for-flutter-explore-animation-mapmarkeranimation-class</a> animation, </li>
<li><a href="../../animation/AnimationListener-class.html">/sdk-for-flutter-explore-animation-animationlistener-class</a>? animationListener</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Starts animation of this map marker according to provided <a href="../../animation/MapMarkerAnimation-class.html">/sdk-for-flutter-explore-animation-mapmarkeranimation-class</a>.</p>
<p>The <code>MapMarkerAnimation</code> may be shared between multiple instances of <code>MapMarker</code>.</p>
<p>Starting animation on one map marker does not influence any ongoing animations on other map markers.
Any ongoing animation of this marker instance will get cancelled.</p>
<ul>
<li>
<p><code>animation</code> The animation to start, may be used for multiple different map markers.</p>
</li>
<li>
<p><code>animationListener</code> The listener to receive notifications about animation start, completion or cancellation.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAnimation(MapMarkerAnimation animation, AnimationListener? animationListener);</code></pre>
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
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a></li>
<li class="self-crumb">startAnimation abstract method</li>
</ol>
<h5>MapMarker class</h5>
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
