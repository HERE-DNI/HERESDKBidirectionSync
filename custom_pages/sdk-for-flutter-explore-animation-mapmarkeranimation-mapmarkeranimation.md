---
title: "Implementation"
slug: "sdk-for-flutter-explore-animation-mapmarkeranimation-mapmarkeranimation"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapMarkerAnimation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../animation/animation-library.html">/sdk-for-flutter-explore-animation-animation-library</a></li>
<li><a href="../../animation/MapMarkerAnimation-class.html">/sdk-for-flutter-explore-animation-mapmarkeranimation-class</a></li>
<li class="self-crumb">MapMarkerAnimation factory constructor</li>
</ol>
<div class="self-name">MapMarkerAnimation</div>
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
<div class="main-content" data-above-sidebar="animation/MapMarkerAnimation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapMarkerAnimation constructor</h1></div>
<section class="multi-line-signature">
MapMarkerAnimation(<wbr/><ol class="parameter-list single-line"> <li><a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a> track</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates an animation of <a href="../../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a> based on provided keyframe track.</p>
<p>Supports tracks created with <a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a> 'moveTo*' methods.</p>
<p>For starting the animation see <a href="../../mapview/MapMarker/startAnimation.html">/sdk-for-flutter-explore-mapview-mapmarker-startanimation</a>.</p>
<ul>
<li><code>track</code> The track holding the keyframes for the animation.</li>
</ul>
<p>Throws <a href="../../animation/MapMarkerAnimationInstantiationException-class.html">/sdk-for-flutter-explore-animation-mapmarkeranimationinstantiationexception-class</a>. If the specified keyframe track cannot be used to create animation of a <a href="../../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarkerAnimation(MapItemKeyFrameTrack track) =&gt; $prototype.$init(track);</code></pre>
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
<li><a href="../../animation/MapMarkerAnimation-class.html">/sdk-for-flutter-explore-animation-mapmarkeranimation-class</a></li>
<li class="self-crumb">MapMarkerAnimation factory constructor</li>
</ol>
<h5>MapMarkerAnimation class</h5>
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
