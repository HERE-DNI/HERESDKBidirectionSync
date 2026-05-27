---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromupdatewitheasing"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- createAnimationFromUpdateWithEasing.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraAnimationFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</a></li>
<li class="self-crumb">createAnimationFromUpdateWithEasing static method</li>
</ol>
<div class="self-name">createAnimationFromUpdateWithEasing</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraAnimationFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>createAnimationFromUpdateWithEasing static method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a>
createAnimationFromUpdateWithEasing(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview/MapCameraUpdate-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdate-class</a> cameraUpdate, </li>
<li>Duration duration, </li>
<li><a href="../../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a <a href="../../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a> to gradually update the camera properties within a specified
duration from its current values to the ones defined in the <code>MapCameraAnimationFactory.createAnimationFromUpdateWithEasing.cameraUpdate</code>.</p>
<p><code>MapCameraAnimation</code>
instances created from <a href="../../mapview/MapCameraUpdateFactory/compositeUpdate.html">/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-compositeupdate</a> instances are not supported. An
<a href="../../animation/AnimationListener-class.html">/sdk-for-flutter-explore-animation-animationlistener-class</a> will receive an <a href="../../animation/AnimationState.html">/sdk-for-flutter-explore-animation-animationstate</a> signal
when trying to apply such animations.</p>
<ul>
<li>
<p><code>cameraUpdate</code> Update which should be applied to the map camera.</p>
</li>
<li>
<p><code>duration</code> Duration of the animation. Negative duration results in no camera change when applied.</p>
</li>
<li>
<p><code>easing</code> Easing to apply.</p>
</li>
</ul>
<p>Returns <a href="../../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a>. MapCameraAnimation instance</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraAnimation createAnimationFromUpdateWithEasing(MapCameraUpdate cameraUpdate, Duration duration, Easing easing) =&gt; $prototype.createAnimationFromUpdateWithEasing(cameraUpdate, duration, easing);</code></pre>
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
<li><a href="../../mapview/MapCameraAnimationFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</a></li>
<li class="self-crumb">createAnimationFromUpdateWithEasing static method</li>
</ol>
<h5>MapCameraAnimationFactory class</h5>
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
