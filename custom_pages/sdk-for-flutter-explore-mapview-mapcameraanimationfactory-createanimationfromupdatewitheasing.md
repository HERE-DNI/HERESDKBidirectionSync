---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromupdatewitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createAnimationFromUpdateWithEasing.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</li>
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
/sdk-for-flutter-explore-mapview-mapcameraanimation-class
createAnimationFromUpdateWithEasing(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-mapcameraupdate-class cameraUpdate, </li>
<li>Duration duration, </li>
<li>/sdk-for-flutter-explore-animation-easing-class easing</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a /sdk-for-flutter-explore-mapview-mapcameraanimation-class to gradually update the camera properties within a specified
duration from its current values to the ones defined in the <code>MapCameraAnimationFactory.createAnimationFromUpdateWithEasing.cameraUpdate</code>.</p>
<p><code>MapCameraAnimation</code>
instances created from /sdk-for-flutter-explore-mapview-mapcameraupdatefactory-compositeupdate instances are not supported. An
/sdk-for-flutter-explore-animation-animationlistener-class will receive an /sdk-for-flutter-explore-animation-animationstate signal
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
<p>Returns /sdk-for-flutter-explore-mapview-mapcameraanimation-class. MapCameraAnimation instance</p>
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</li>
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



</div>
`
}</HTMLBlock>
