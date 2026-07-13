---
title: "MapCameraKeyframeTrack class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraKeyframeTrack-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraKeyframeTrack-class-sidebar.html">

<div>

# <span class="kind-class">MapCameraKeyframeTrack</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode.

Can only hold keyframes of a single type.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-mapcamerakeyframetrack">MapCameraKeyframeTrack</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-interpolationmode">interpolationMode</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span>  
Interpolation mode affects the shape of the spline going through all keyframes. Gets the interpolation mode for the between key frames in the track.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getanchor2dkeyframes">getAnchor2DKeyframes</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-anchor2dkeyframe-class">Anchor2DKeyframe</a></span>\></span>?</span> </span>  
Returns `List<Anchor2DKeyframe>?`. a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getgeocoordinateskeyframes">getGeoCoordinatesKeyframes</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-geocoordinateskeyframe-class">GeoCoordinatesKeyframe</a></span>\></span>?</span> </span>  
Returns `List<GeoCoordinatesKeyframe>?`. a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getgeoorientationkeyframes">getGeoOrientationKeyframes</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-geoorientationkeyframe-class">GeoOrientationKeyframe</a></span>\></span>?</span> </span>  
Returns `List<GeoOrientationKeyframe>?`. a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getpoint2dkeyframes">getPoint2DKeyframes</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-point2dkeyframe-class">Point2DKeyframe</a></span>\></span>?</span> </span>  
Returns `List<Point2DKeyframe>?`. a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-getscalarkeyframes">getScalarKeyframes</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-scalarkeyframe-class">ScalarKeyframe</a></span>\></span>?</span> </span>  
Returns `List<ScalarKeyframe>?`. a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-fieldofviewwitheasing">fieldOfViewWithEasing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-fieldOfViewWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-scalarkeyframe-class">ScalarKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span><span id="sdk-for-flutter-explore-fieldOfViewWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span><span id="sdk-for-flutter-explore-fieldOfViewWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> </span>  
Creates a map camera field-of-view keyframe track.

<span class="name deprecated"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatdistancewitheasing" class="deprecated">lookAtDistanceWithEasing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtDistanceWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-scalarkeyframe-class">ScalarKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span><span id="sdk-for-flutter-explore-lookAtDistanceWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span><span id="sdk-for-flutter-explore-lookAtDistanceWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> </span>  
Creates a map camera look-at distance keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatdistancewithkind">lookAtDistanceWithKind</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtDistanceWithKind-param-distanceKind" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind</a></span> <span class="parameter-name">distanceKind</span>, </span><span id="sdk-for-flutter-explore-lookAtDistanceWithKind-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-scalarkeyframe-class">ScalarKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span><span id="sdk-for-flutter-explore-lookAtDistanceWithKind-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span><span id="sdk-for-flutter-explore-lookAtDistanceWithKind-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> </span>  
Creates a map camera look-at distance keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatorientationwitheasing">lookAtOrientationWithEasing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtOrientationWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-geoorientationkeyframe-class">GeoOrientationKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span><span id="sdk-for-flutter-explore-lookAtOrientationWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span><span id="sdk-for-flutter-explore-lookAtOrientationWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> </span>  
Creates a map camera look-at orientation keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookattargetwitheasing">lookAtTargetWithEasing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtTargetWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-geocoordinateskeyframe-class">GeoCoordinatesKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span><span id="sdk-for-flutter-explore-lookAtTargetWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span><span id="sdk-for-flutter-explore-lookAtTargetWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> </span>  
Creates a map camera look-at target keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-normalizedprincipalpointwitheasing">normalizedPrincipalPointWithEasing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-normalizedPrincipalPointWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-anchor2dkeyframe-class">Anchor2DKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span><span id="sdk-for-flutter-explore-normalizedPrincipalPointWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span><span id="sdk-for-flutter-explore-normalizedPrincipalPointWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> </span>  
Creates a map camera principal point keyframe track.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-principalpointwitheasing">principalPointWithEasing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-principalPointWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-point2dkeyframe-class">Point2DKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span><span id="sdk-for-flutter-explore-principalPointWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span><span id="sdk-for-flutter-explore-principalPointWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> </span>  
Creates a map camera principal point keyframe track.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
