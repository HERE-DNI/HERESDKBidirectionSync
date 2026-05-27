---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapCameraKeyframeTrack-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapCameraKeyframeTrack-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/MapCameraKeyframeTrack.html">MapCameraKeyframeTrack</a></li>
<li class="section-title">
<a href="mapview/MapCameraKeyframeTrack-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapCameraKeyframeTrack/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/interpolationMode.html">interpolationMode</a></li>
<li class="inherited"><a href="mapview/MapCameraKeyframeTrack/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapCameraKeyframeTrack-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/getAnchor2DKeyframes.html">getAnchor2DKeyframes</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/getGeoCoordinatesKeyframes.html">getGeoCoordinatesKeyframes</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/getGeoOrientationKeyframes.html">getGeoOrientationKeyframes</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/getPoint2DKeyframes.html">getPoint2DKeyframes</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/getScalarKeyframes.html">getScalarKeyframes</a></li>
<li class="inherited"><a href="mapview/MapCameraKeyframeTrack/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapCameraKeyframeTrack/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapCameraKeyframeTrack-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapCameraKeyframeTrack/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="mapview/MapCameraKeyframeTrack-class.html#static-methods">Static methods</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/fieldOfViewWithEasing.html">fieldOfViewWithEasing</a></li>
<li><a class="deprecated" href="mapview/MapCameraKeyframeTrack/lookAtDistanceWithEasing.html">lookAtDistanceWithEasing</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/lookAtDistanceWithKind.html">lookAtDistanceWithKind</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/lookAtOrientationWithEasing.html">lookAtOrientationWithEasing</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/lookAtTargetWithEasing.html">lookAtTargetWithEasing</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/normalizedPrincipalPointWithEasing.html">normalizedPrincipalPointWithEasing</a></li>
<li><a href="mapview/MapCameraKeyframeTrack/principalPointWithEasing.html">principalPointWithEasing</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
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
<a href="../mapview/MapCameraKeyframeTrack/MapCameraKeyframeTrack.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-mapcamerakeyframetrack</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapCameraKeyframeTrack/hashCode.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="interpolationMode">
<a href="../mapview/MapCameraKeyframeTrack/interpolationMode.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-interpolationmode</a>
→ <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a>
</dt>
<dd>
  Interpolation mode affects the shape of the spline going through all keyframes.
Gets the interpolation mode for the between key frames in the track.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapCameraKeyframeTrack/runtimeType.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-runtimetype</a>
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
<a href="../mapview/MapCameraKeyframeTrack/getAnchor2DKeyframes.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getanchor2dkeyframes</a>(<wbr/>)
    → List&lt;<wbr/><a href="../animation/Anchor2DKeyframe-class.html">/sdk-for-flutter-explore-animation-anchor2dkeyframe-class</a>&gt;?

</dt>
<dd>
  Returns <code>List&lt;Anchor2DKeyframe&gt;?</code>. a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.
  

</dd>
<dt class="callable" id="getGeoCoordinatesKeyframes">
<a href="../mapview/MapCameraKeyframeTrack/getGeoCoordinatesKeyframes.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getgeocoordinateskeyframes</a>(<wbr/>)
    → List&lt;<wbr/><a href="../animation/GeoCoordinatesKeyframe-class.html">/sdk-for-flutter-explore-animation-geocoordinateskeyframe-class</a>&gt;?

</dt>
<dd>
  Returns <code>List&lt;GeoCoordinatesKeyframe&gt;?</code>. a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.
  

</dd>
<dt class="callable" id="getGeoOrientationKeyframes">
<a href="../mapview/MapCameraKeyframeTrack/getGeoOrientationKeyframes.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getgeoorientationkeyframes</a>(<wbr/>)
    → List&lt;<wbr/><a href="../animation/GeoOrientationKeyframe-class.html">/sdk-for-flutter-explore-animation-geoorientationkeyframe-class</a>&gt;?

</dt>
<dd>
  Returns <code>List&lt;GeoOrientationKeyframe&gt;?</code>. a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.
  

</dd>
<dt class="callable" id="getPoint2DKeyframes">
<a href="../mapview/MapCameraKeyframeTrack/getPoint2DKeyframes.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getpoint2dkeyframes</a>(<wbr/>)
    → List&lt;<wbr/><a href="../animation/Point2DKeyframe-class.html">/sdk-for-flutter-explore-animation-point2dkeyframe-class</a>&gt;?

</dt>
<dd>
  Returns <code>List&lt;Point2DKeyframe&gt;?</code>. a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.
  

</dd>
<dt class="callable" id="getScalarKeyframes">
<a href="../mapview/MapCameraKeyframeTrack/getScalarKeyframes.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getscalarkeyframes</a>(<wbr/>)
    → List&lt;<wbr/><a href="../animation/ScalarKeyframe-class.html">/sdk-for-flutter-explore-animation-scalarkeyframe-class</a>&gt;?

</dt>
<dd>
  Returns <code>List&lt;ScalarKeyframe&gt;?</code>. a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapCameraKeyframeTrack/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapCameraKeyframeTrack/toString.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-tostring</a>(<wbr/>)
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
<a href="../mapview/MapCameraKeyframeTrack/operator_equals.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-operator-equals</a>(<wbr/>Object other)
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
<a href="../mapview/MapCameraKeyframeTrack/fieldOfViewWithEasing.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-fieldofviewwitheasing</a>(<wbr/>List&lt;<wbr/><a href="../animation/ScalarKeyframe-class.html">/sdk-for-flutter-explore-animation-scalarkeyframe-class</a>&gt; keyframes, <a href="../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode)
    → <a href="../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
</dt>
<dd>
  Creates a map camera field-of-view keyframe track.
  

</dd>
<dt class="callable" id="lookAtDistanceWithEasing">
<a class="deprecated" href="../mapview/MapCameraKeyframeTrack/lookAtDistanceWithEasing.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatdistancewitheasing</a>(<wbr/>List&lt;<wbr/><a href="../animation/ScalarKeyframe-class.html">/sdk-for-flutter-explore-animation-scalarkeyframe-class</a>&gt; keyframes, <a href="../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode)
    → <a href="../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
</dt>
<dd>
  Creates a map camera look-at distance keyframe track.
  

</dd>
<dt class="callable" id="lookAtDistanceWithKind">
<a href="../mapview/MapCameraKeyframeTrack/lookAtDistanceWithKind.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatdistancewithkind</a>(<wbr/><a href="../mapview/MapMeasureKind.html">/sdk-for-flutter-explore-mapview-mapmeasurekind</a> distanceKind, List&lt;<wbr/><a href="../animation/ScalarKeyframe-class.html">/sdk-for-flutter-explore-animation-scalarkeyframe-class</a>&gt; keyframes, <a href="../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode)
    → <a href="../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
</dt>
<dd>
  Creates a map camera look-at distance keyframe track.
  

</dd>
<dt class="callable" id="lookAtOrientationWithEasing">
<a href="../mapview/MapCameraKeyframeTrack/lookAtOrientationWithEasing.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatorientationwitheasing</a>(<wbr/>List&lt;<wbr/><a href="../animation/GeoOrientationKeyframe-class.html">/sdk-for-flutter-explore-animation-geoorientationkeyframe-class</a>&gt; keyframes, <a href="../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode)
    → <a href="../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
</dt>
<dd>
  Creates a map camera look-at orientation keyframe track.
  

</dd>
<dt class="callable" id="lookAtTargetWithEasing">
<a href="../mapview/MapCameraKeyframeTrack/lookAtTargetWithEasing.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookattargetwitheasing</a>(<wbr/>List&lt;<wbr/><a href="../animation/GeoCoordinatesKeyframe-class.html">/sdk-for-flutter-explore-animation-geocoordinateskeyframe-class</a>&gt; keyframes, <a href="../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode)
    → <a href="../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
</dt>
<dd>
  Creates a map camera look-at target keyframe track.
  

</dd>
<dt class="callable" id="normalizedPrincipalPointWithEasing">
<a href="../mapview/MapCameraKeyframeTrack/normalizedPrincipalPointWithEasing.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-normalizedprincipalpointwitheasing</a>(<wbr/>List&lt;<wbr/><a href="../animation/Anchor2DKeyframe-class.html">/sdk-for-flutter-explore-animation-anchor2dkeyframe-class</a>&gt; keyframes, <a href="../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode)
    → <a href="../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
</dt>
<dd>
  Creates a map camera principal point keyframe track.
  

</dd>
<dt class="callable" id="principalPointWithEasing">
<a href="../mapview/MapCameraKeyframeTrack/principalPointWithEasing.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-principalpointwitheasing</a>(<wbr/>List&lt;<wbr/><a href="../animation/Point2DKeyframe-class.html">/sdk-for-flutter-explore-animation-point2dkeyframe-class</a>&gt; keyframes, <a href="../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, <a href="../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode)
    → <a href="../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
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
</div></div>
</div>
</HTMLBlock>
