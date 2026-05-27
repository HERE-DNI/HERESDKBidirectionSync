---
title: "Implementation"
slug: "sdk-for-flutter-explore-animation-mappolylineanimation-mappolylineanimation"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolylineAnimation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../animation/animation-library.html">/sdk-for-flutter-explore-animation-animation-library</a></li>
<li><a href="../../animation/MapPolylineAnimation-class.html">/sdk-for-flutter-explore-animation-mappolylineanimation-class</a></li>
<li class="self-crumb">MapPolylineAnimation factory constructor</li>
</ol>
<div class="self-name">MapPolylineAnimation</div>
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
<div class="main-content" data-above-sidebar="animation/MapPolylineAnimation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapPolylineAnimation constructor</h1></div>
<section class="multi-line-signature">
MapPolylineAnimation(<wbr/><ol class="parameter-list single-line"> <li><a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a> track</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates an animation of <a href="../../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a> based on provided keyframe track.</p>
<p>Supports tracks created with <a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a> 'polylineProgress*' methods.
For starting the animation, see <a href="../../mapview/MapPolyline/startAnimation.html">/sdk-for-flutter-explore-mapview-mappolyline-startanimation</a>.</p>
<ul>
<li><code>track</code> The track holding the keyframes for the animation.</li>
</ul>
<p>Throws <a href="../../animation/MapPolylineAnimationInstantiationException-class.html">/sdk-for-flutter-explore-animation-mappolylineanimationinstantiationexception-class</a>. If the specified keyframe track cannot be used to create animation of a <a href="../../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineAnimation(MapItemKeyFrameTrack track) =&gt; $prototype.$init(track);</code></pre>
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
<li><a href="../../animation/MapPolylineAnimation-class.html">/sdk-for-flutter-explore-animation-mappolylineanimation-class</a></li>
<li class="self-crumb">MapPolylineAnimation factory constructor</li>
</ol>
<h5>MapPolylineAnimation class</h5>
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
