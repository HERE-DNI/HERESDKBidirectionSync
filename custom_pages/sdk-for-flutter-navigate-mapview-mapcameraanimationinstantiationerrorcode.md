---
title: "MapCameraAnimationInstantiationErrorCode enum - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraAnimationInstantiationErrorCode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraAnimationInstantiationErrorCode-enum-sidebar.html">

<div>

# <span class="kind-enum">MapCameraAnimationInstantiationErrorCode</span> enum

</div>

<div class="section desc markdown">

Describes a reason for failing to create a multi-track <a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a>.

</div>

## Values

<span class="name">emptyTrackList</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks is empty.

<span class="name">multipleCameraPositionTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera position tracks.

<span class="name">cameraPositionModifiedByCameraLookatTargetTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's position is already modified by an earlier track that modifies camera's look-at target.

<span class="name">cameraPositionModifiedByCameraLookatOrientationTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's position is already modified by an earlier track that modifies camera's look-at orientation.

<span class="name">cameraPositionModifiedByCameraLookatDistanceTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's position is already modified by an earlier track that modifies camera's look-at distance.

<span class="name">multipleCameraOrientationTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera orientation tracks.

<span class="name">cameraOrientationModifiedByCameraLookatOrientationTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's orientation is already modified by an earlier track that modifies camera's look-at orientation.

<span class="name">cameraOrientationModifiedByCameraLookatDistanceTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's orientation is already modified by an earlier track that modifies camera's look-at distance.

<span class="name">multipleCameraLookatTargetTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera look-at target tracks.

<span class="name">cameraLookatTargetModifiedByCameraPositionTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's look-at target is already modified by an earlier track that modifies camera's position.

<span class="name">cameraLookatTargetModifiedByCameraOrientationTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's look-at target is already modified by an earlier track that modifies camera's orientation.

<span class="name">multipleCameraLookatOrientationTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera look-at orientation tracks.

<span class="name">cameraLookatOrientationModifiedByCameraPositionTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's look-at orientation is already modified by an earlier track that modifies camera's position.

<span class="name">cameraLookatOrientationModifiedByCameraOrientationTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's look-at orientation is already modified by an earlier track that modifies camera's orientation.

<span class="name">multipleCameraLookatDistanceTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera look-at distance tracks.

<span class="name">cameraLookatDistanceModifiedByCameraPositionTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's look-at distance is already modified by an earlier track that modifies camera's position.

<span class="name">cameraLookatDistanceModifiedByCameraOrientationTrack</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Camera's look-at distance is already modified by an earlier track that modifies camera's orientation.

<span class="name">multipleCameraFieldOfViewTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera field-of-view tracks.

<span class="name">multipleCameraFocalLengthTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera focal length tracks.

<span class="name">multipleCameraPrincipalPointTracks</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
List of keyframe tracks contains multiple camera principal point tracks.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
