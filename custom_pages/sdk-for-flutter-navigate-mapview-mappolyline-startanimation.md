---
title: "startAnimation abstract method"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-startanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAnimation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mappolyline-class</li>
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
<div class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startAnimation abstract method</h1></div>
<section class="multi-line-signature">
void
startAnimation(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-animation-mappolylineanimation-class animation, </li>
<li>/sdk-for-flutter-navigate-animation-animationlistener-class listener</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Starts an animation of this map polyline.</p>
<p>The <code>MapPolylineAnimation</code> may be shared between multiple instances of <code>MapPolyline</code>.</p>
<p>Starting animation on one polyline does not influence any ongoing animations on
other polylines.
Any ongoing animation of this map polyline will get cancelled.</p>
<ul>
<li>
<p><code>animation</code> The animation to start.</p>
</li>
<li>
<p><code>listener</code> The listener to receive notifications
about animation start, completion or cancellation.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAnimation(MapPolylineAnimation animation, AnimationListener listener);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mappolyline-class</li>
<li class="self-crumb">startAnimation abstract method</li>
</ol>
<h5>MapPolyline class</h5>
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
`
}</HTMLBlock>
