---
title: "Untitled"
slug: "sdk-for-flutter-explore-animation-animation-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- animation-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li class="self-crumb">animation.dart</li>
</ol>
<div class="self-name">animation</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="animation/animation-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>animation library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="Anchor2DKeyframe">
/sdk-for-flutter-explore-animation-anchor2dkeyframe-class
</dt>
<dd>
  An Anchor2D keyframe.
</dd>
<dt id="AnimationListener">
/sdk-for-flutter-explore-animation-animationlistener-class
</dt>
<dd>
  A listener for animation events.
</dd>
<dt id="Easing">
/sdk-for-flutter-explore-animation-easing-class
</dt>
<dd>
  Animation easing representing an easing function to be used during animations.
</dd>
<dt id="GeoCoordinatesKeyframe">
/sdk-for-flutter-explore-animation-geocoordinateskeyframe-class
</dt>
<dd>
  A GeoCoordinatesKeyframe consists of a GeoCoordinates and an animation duration.
</dd>
<dt id="GeoOrientationKeyframe">
/sdk-for-flutter-explore-animation-geoorientationkeyframe-class
</dt>
<dd>
  A GeoOrientationKeyframe consists of a GeoOrientation (camera orientation) and an animation duration.
</dd>
<dt id="MapItemKeyFrameTrack">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class
</dt>
<dd>
  Stores keyframes for interpolation of a map item property using a specific
easing function and interpolation mode.
</dd>
<dt id="MapMarkerAnimation">
/sdk-for-flutter-explore-animation-mapmarkeranimation-class
</dt>
<dd>
  An animation that can be applied to the /sdk-for-flutter-explore-mapview-mapmarker-class object.
</dd>
<dt id="MapPolylineAnimation">
/sdk-for-flutter-explore-animation-mappolylineanimation-class
</dt>
<dd>
  An animation that can be applied to the /sdk-for-flutter-explore-mapview-mappolyline-class object.
</dd>
<dt id="Point2DKeyframe">
/sdk-for-flutter-explore-animation-point2dkeyframe-class
</dt>
<dd>
  A Point2D keyframe.
</dd>
<dt id="ScalarKeyframe">
/sdk-for-flutter-explore-animation-scalarkeyframe-class
</dt>
<dd>
  A ScalarKeyframe consists of a scalar value (e.g,: distance in meters) and an animation duration.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="AnimationState">
/sdk-for-flutter-explore-animation-animationstate
</dt>
<dd>
  Describes the possible states of an animation.
</dd>
<dt id="EasingFunction">
/sdk-for-flutter-explore-animation-easingfunction
</dt>
<dd>
  Animation easing functions.
</dd>
<dt id="EasingInstantiationErrorCode">
/sdk-for-flutter-explore-animation-easinginstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create an /sdk-for-flutter-explore-animation-easing-class.
</dd>
<dt id="KeyframeInterpolationMode">
/sdk-for-flutter-explore-animation-keyframeinterpolationmode
</dt>
<dd>
  Specifies type of interpolation performed between keyframes.
</dd>
<dt id="MapItemKeyFrameTrackInstantiationErrorCode">
/sdk-for-flutter-explore-animation-mapitemkeyframetrackinstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create a /sdk-for-flutter-explore-animation-mapitemkeyframetrack-class.
</dd>
<dt id="MapMarkerAnimationInstantiationErrorCode">
/sdk-for-flutter-explore-animation-mapmarkeranimationinstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create a /sdk-for-flutter-explore-animation-mapmarkeranimation-class.
</dd>
<dt id="MapPolylineAnimationInstantiationErrorCode">
/sdk-for-flutter-explore-animation-mappolylineanimationinstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create a /sdk-for-flutter-explore-animation-mappolylineanimation-class.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="EasingInstantiationException">
/sdk-for-flutter-explore-animation-easinginstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create an /sdk-for-flutter-explore-animation-easing-class.
</dd>
<dt id="MapItemKeyFrameTrackInstantiationException">
/sdk-for-flutter-explore-animation-mapitemkeyframetrackinstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create /sdk-for-flutter-explore-animation-mapitemkeyframetrack-class.
</dd>
<dt id="MapMarkerAnimationInstantiationException">
/sdk-for-flutter-explore-animation-mapmarkeranimationinstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create a /sdk-for-flutter-explore-animation-mapmarkeranimation-class.
</dd>
<dt id="MapPolylineAnimationInstantiationException">
/sdk-for-flutter-explore-animation-mappolylineanimationinstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create a /sdk-for-flutter-explore-animation-mappolylineanimation-class.
</dd>
</dl>
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
<li class="self-crumb">animation.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-explore-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-explore-ev-ev-library</li>
<li>/sdk-for-flutter-explore-gestures-gestures-library</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-transport-transport-library</li>
</ol>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
<h5>animation library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
