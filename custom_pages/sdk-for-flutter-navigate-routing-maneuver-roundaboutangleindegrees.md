---
title: "roundaboutAngleInDegrees property"
slug: "sdk-for-flutter-navigate-routing-maneuver-roundaboutangleindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- roundaboutAngleInDegrees.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-maneuver-class</li>
<li class="self-crumb">roundaboutAngleInDegrees property</li>
</ol>
<div class="self-name">roundaboutAngleInDegrees</div>
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
<div class="main-content" data-above-sidebar="routing/Maneuver-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>roundaboutAngleInDegrees property</h1></div>
<section id="getter">
<section class="multi-line-signature">
double?
roundaboutAngleInDegrees
</section>
<section class="desc markdown">
<p>The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route
parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from
the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a
vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects
the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive
in right-hand side driving country, and negative in left-hand side countries.
Note that the value is available for both the enter roundabout actions and the exit roundabout
actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the
roundabout itself is not representing a perfect circle, then the accuracy of the angle may be
compromised.
<strong>Note:</strong> These attributes are only available for the Navigate license.
The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? get roundaboutAngleInDegrees;</code></pre>
</section>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-maneuver-class</li>
<li class="self-crumb">roundaboutAngleInDegrees property</li>
</ol>
<h5>Maneuver class</h5>
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
