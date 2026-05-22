---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraKeyframeTrack-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapCameraKeyframeTrack class</li>
</ol>
<div class="self-name">MapCameraKeyframeTrack</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraKeyframeTrack-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapCameraKeyframeTrack class abstract</h1></div>
<section class="desc markdown">
<p>Stores keyframes for interpolation of a camera property using a specific easing function
and interpolation mode.</p>
<p>Can only hold keyframes of a single type.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapCameraKeyframeTrack">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-mapcamerakeyframetrack()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="interpolationMode">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-interpolationmode
→ /sdk-for-flutter-navigate-animation-keyframeinterpolationmode
</dt>
<dd>
  Interpolation mode affects the shape of the spline going through all keyframes.
Gets the interpolation mode for the between key frames in the track.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getAnchor2DKeyframes">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-getanchor2dkeyframes(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-animation-anchor2dkeyframe-class&gt;?

</dt>
<dd>
  Returns <code>List&lt;Anchor2DKeyframe&gt;?</code>. a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.
  

</dd>
<dt class="callable" id="getGeoCoordinatesKeyframes">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-getgeocoordinateskeyframes(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-animation-geocoordinateskeyframe-class&gt;?

</dt>
<dd>
  Returns <code>List&lt;GeoCoordinatesKeyframe&gt;?</code>. a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.
  

</dd>
<dt class="callable" id="getGeoOrientationKeyframes">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-getgeoorientationkeyframes(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-animation-geoorientationkeyframe-class&gt;?

</dt>
<dd>
  Returns <code>List&lt;GeoOrientationKeyframe&gt;?</code>. a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.
  

</dd>
<dt class="callable" id="getPoint2DKeyframes">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-getpoint2dkeyframes(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-animation-point2dkeyframe-class&gt;?

</dt>
<dd>
  Returns <code>List&lt;Point2DKeyframe&gt;?</code>. a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.
  

</dd>
<dt class="callable" id="getScalarKeyframes">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-getscalarkeyframes(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-animation-scalarkeyframe-class&gt;?

</dt>
<dd>
  Returns <code>List&lt;ScalarKeyframe&gt;?</code>. a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fieldOfViewWithEasing">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-fieldofviewwitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-animation-scalarkeyframe-class&gt; keyframes, /sdk-for-flutter-navigate-animation-easing-class easing, /sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class

</dt>
<dd>
  Creates a map camera field-of-view keyframe track.
  

</dd>
<dt class="callable" id="lookAtDistanceWithEasing">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookatdistancewitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-animation-scalarkeyframe-class&gt; keyframes, /sdk-for-flutter-navigate-animation-easing-class easing, /sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class

</dt>
<dd>
  Creates a map camera look-at distance keyframe track.
  

</dd>
<dt class="callable" id="lookAtDistanceWithKind">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookatdistancewithkind(<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasurekind distanceKind, List&lt;<wbr/>/sdk-for-flutter-navigate-animation-scalarkeyframe-class&gt; keyframes, /sdk-for-flutter-navigate-animation-easing-class easing, /sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class

</dt>
<dd>
  Creates a map camera look-at distance keyframe track.
  

</dd>
<dt class="callable" id="lookAtOrientationWithEasing">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookatorientationwitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-animation-geoorientationkeyframe-class&gt; keyframes, /sdk-for-flutter-navigate-animation-easing-class easing, /sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class

</dt>
<dd>
  Creates a map camera look-at orientation keyframe track.
  

</dd>
<dt class="callable" id="lookAtTargetWithEasing">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookattargetwitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-animation-geocoordinateskeyframe-class&gt; keyframes, /sdk-for-flutter-navigate-animation-easing-class easing, /sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class

</dt>
<dd>
  Creates a map camera look-at target keyframe track.
  

</dd>
<dt class="callable" id="normalizedPrincipalPointWithEasing">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-normalizedprincipalpointwitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-animation-anchor2dkeyframe-class&gt; keyframes, /sdk-for-flutter-navigate-animation-easing-class easing, /sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class

</dt>
<dd>
  Creates a map camera principal point keyframe track.
  

</dd>
<dt class="callable" id="principalPointWithEasing">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-principalpointwitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-animation-point2dkeyframe-class&gt; keyframes, /sdk-for-flutter-navigate-animation-easing-class easing, /sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class

</dt>
<dd>
  Creates a map camera principal point keyframe track.
  

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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapCameraKeyframeTrack class</li>
</ol>
<h5>mapview library</h5>
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
