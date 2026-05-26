---
title: "flyToWithOrientation static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flytowithorientation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- flyToWithOrientation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</li>
<li class="self-crumb">flyToWithOrientation static method</li>
</ol>
<div class="self-name">flyToWithOrientation</div>
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
<h1>flyToWithOrientation static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-mapcameraanimation-class
flyToWithOrientation(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, </li>
<li>/sdk-for-flutter-explore-core-geoorientationupdate-class orientation, </li>
<li>double bowFactor, </li>
<li>Duration duration, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.</p>
<p>The beginning and end of the animation will use the current zoom.</p>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The coordinates of the camera destination point.
Any target sub-element value that is not finite will be set to the current camera target sub-element value.
Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</li>
<li>
<p><code>orientation</code> The orientation at destination.</p>
</li>
<li>
<p><code>bowFactor</code> A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
</li>
</ul>
<p>The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
curve is relative to the travel distance between current camera target and destination target.</p>
<p>A bow factor of 0 does not change the camera's zoom over time.</p>
<p>Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.</p>
<p>The bow factor is clamped to [-1, +1].</p>
<p>Note that the lowest possible camera distance to earth is 0 meters and that the animation
curve will not go below this value.</p>
<p>Note that currently, bow factor is ignored and assumed to be 1 if either start or end
of animation has a non zero tilt.</p>
<ul>
<li><code>duration</code> Duration of the flight. Negative duration results in no camera change when applied.</li>
</ul>
<p>Returns /sdk-for-flutter-explore-mapview-mapcameraanimation-class. MapCameraAnimation instance</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraAnimation flyToWithOrientation(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, double bowFactor, Duration duration) =&gt; $prototype.flyToWithOrientation(target, orientation, bowFactor, duration);</code></pre>
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
<li class="self-crumb">flyToWithOrientation static method</li>
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
`
}</HTMLBlock>
