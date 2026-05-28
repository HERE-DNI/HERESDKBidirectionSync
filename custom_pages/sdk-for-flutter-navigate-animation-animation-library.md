---
title: "animation library"
slug: "sdk-for-flutter-navigate-animation-animation-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- animation-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="animation/animation-library.html#classes">Classes</a></li>
<li><a href="animation/Anchor2DKeyframe-class.html">Anchor2DKeyframe</a></li>
<li><a href="animation/AnimationListener-class.html">AnimationListener</a></li>
<li><a href="animation/Easing-class.html">Easing</a></li>
<li><a href="animation/GeoCoordinatesKeyframe-class.html">GeoCoordinatesKeyframe</a></li>
<li><a href="animation/GeoOrientationKeyframe-class.html">GeoOrientationKeyframe</a></li>
<li><a href="animation/MapItemKeyFrameTrack-class.html">MapItemKeyFrameTrack</a></li>
<li><a href="animation/MapMarkerAnimation-class.html">MapMarkerAnimation</a></li>
<li><a href="animation/MapPolylineAnimation-class.html">MapPolylineAnimation</a></li>
<li><a href="animation/Point2DKeyframe-class.html">Point2DKeyframe</a></li>
<li><a href="animation/ScalarKeyframe-class.html">ScalarKeyframe</a></li>
<li class="section-title"><a href="animation/animation-library.html#enums">Enums</a></li>
<li><a href="animation/AnimationState.html">AnimationState</a></li>
<li><a href="animation/EasingFunction.html">EasingFunction</a></li>
<li><a href="animation/EasingInstantiationErrorCode.html">EasingInstantiationErrorCode</a></li>
<li><a href="animation/KeyframeInterpolationMode.html">KeyframeInterpolationMode</a></li>
<li><a href="animation/MapItemKeyFrameTrackInstantiationErrorCode.html">MapItemKeyFrameTrackInstantiationErrorCode</a></li>
<li><a href="animation/MapMarkerAnimationInstantiationErrorCode.html">MapMarkerAnimationInstantiationErrorCode</a></li>
<li><a href="animation/MapPolylineAnimationInstantiationErrorCode.html">MapPolylineAnimationInstantiationErrorCode</a></li>
<li class="section-title"><a href="animation/animation-library.html#exceptions">Exceptions</a></li>
<li><a href="animation/EasingInstantiationException-class.html">EasingInstantiationException</a></li>
<li><a href="animation/MapItemKeyFrameTrackInstantiationException-class.html">MapItemKeyFrameTrackInstantiationException</a></li>
<li><a href="animation/MapMarkerAnimationInstantiationException-class.html">MapMarkerAnimationInstantiationException</a></li>
<li><a href="animation/MapPolylineAnimationInstantiationException-class.html">MapPolylineAnimationInstantiationException</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
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
/sdk-for-flutter-navigate-animation-anchor2dkeyframe-class
</dt>
<dd>
  An Anchor2D keyframe.
</dd>
<dt id="AnimationListener">
/sdk-for-flutter-navigate-animation-animationlistener-class
</dt>
<dd>
  A listener for animation events.
</dd>
<dt id="Easing">
/sdk-for-flutter-navigate-animation-easing-class
</dt>
<dd>
  Animation easing representing an easing function to be used during animations.
</dd>
<dt id="GeoCoordinatesKeyframe">
/sdk-for-flutter-navigate-animation-geocoordinateskeyframe-class
</dt>
<dd>
  A GeoCoordinatesKeyframe consists of a GeoCoordinates and an animation duration.
</dd>
<dt id="GeoOrientationKeyframe">
/sdk-for-flutter-navigate-animation-geoorientationkeyframe-class
</dt>
<dd>
  A GeoOrientationKeyframe consists of a GeoOrientation (camera orientation) and an animation duration.
</dd>
<dt id="MapItemKeyFrameTrack">
/sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class
</dt>
<dd>
  Stores keyframes for interpolation of a map item property using a specific
easing function and interpolation mode.
</dd>
<dt id="MapMarkerAnimation">
/sdk-for-flutter-navigate-animation-mapmarkeranimation-class
</dt>
<dd>
  An animation that can be applied to the /sdk-for-flutter-navigate-mapview-mapmarker-class object.
</dd>
<dt id="MapPolylineAnimation">
/sdk-for-flutter-navigate-animation-mappolylineanimation-class
</dt>
<dd>
  An animation that can be applied to the /sdk-for-flutter-navigate-mapview-mappolyline-class object.
</dd>
<dt id="Point2DKeyframe">
/sdk-for-flutter-navigate-animation-point2dkeyframe-class
</dt>
<dd>
  A Point2D keyframe.
</dd>
<dt id="ScalarKeyframe">
/sdk-for-flutter-navigate-animation-scalarkeyframe-class
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
/sdk-for-flutter-navigate-animation-animationstate
</dt>
<dd>
  Describes the possible states of an animation.
</dd>
<dt id="EasingFunction">
/sdk-for-flutter-navigate-animation-easingfunction
</dt>
<dd>
  Animation easing functions.
</dd>
<dt id="EasingInstantiationErrorCode">
/sdk-for-flutter-navigate-animation-easinginstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create an /sdk-for-flutter-navigate-animation-easing-class.
</dd>
<dt id="KeyframeInterpolationMode">
/sdk-for-flutter-navigate-animation-keyframeinterpolationmode
</dt>
<dd>
  Specifies type of interpolation performed between keyframes.
</dd>
<dt id="MapItemKeyFrameTrackInstantiationErrorCode">
/sdk-for-flutter-navigate-animation-mapitemkeyframetrackinstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create a /sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class.
</dd>
<dt id="MapMarkerAnimationInstantiationErrorCode">
/sdk-for-flutter-navigate-animation-mapmarkeranimationinstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create a /sdk-for-flutter-navigate-animation-mapmarkeranimation-class.
</dd>
<dt id="MapPolylineAnimationInstantiationErrorCode">
/sdk-for-flutter-navigate-animation-mappolylineanimationinstantiationerrorcode
</dt>
<dd>
  Describes a reason for failing to create a /sdk-for-flutter-navigate-animation-mappolylineanimation-class.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="EasingInstantiationException">
/sdk-for-flutter-navigate-animation-easinginstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create an /sdk-for-flutter-navigate-animation-easing-class.
</dd>
<dt id="MapItemKeyFrameTrackInstantiationException">
/sdk-for-flutter-navigate-animation-mapitemkeyframetrackinstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create /sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class.
</dd>
<dt id="MapMarkerAnimationInstantiationException">
/sdk-for-flutter-navigate-animation-mapmarkeranimationinstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create a /sdk-for-flutter-navigate-animation-mapmarkeranimation-class.
</dd>
<dt id="MapPolylineAnimationInstantiationException">
/sdk-for-flutter-navigate-animation-mappolylineanimationinstantiationexception-class
</dt>
<dd>
  Thrown when a problem occurs while trying to create a /sdk-for-flutter-navigate-animation-mappolylineanimation-class.
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
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">animation.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-navigate-animation-animation-library</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-navigate-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-ev-ev-library</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-style-venue-style-library</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
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
</div></div>
</div>
`
}</HTMLBlock>
