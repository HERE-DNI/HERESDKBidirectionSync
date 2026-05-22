---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- initialAzimuthInDegrees.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-custompanningdata-class</li>
<li class="self-crumb">initialAzimuthInDegrees property</li>
</ol>
<div class="self-name">initialAzimuthInDegrees</div>
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
<div class="main-content" data-above-sidebar="navigation/CustomPanningData-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>initialAzimuthInDegrees property</h1></div>
<section class="multi-line-signature">
        
        double?
        initialAzimuthInDegrees
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
as "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc
from the front to the right, mimicking the maneuver geometry. In this case,
it is good practice to start the trajectory from an initial azimuth that is slightly located
on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting
to play the audio cue to avoid unwanted audio "jumps".</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? initialAzimuthInDegrees;</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-custompanningdata-class</li>
<li class="self-crumb">initialAzimuthInDegrees property</li>
</ol>
<h5>CustomPanningData class</h5>
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
