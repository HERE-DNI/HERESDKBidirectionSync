---
title: "createAnimationFromKeyframeTracks method - MapCameraAnimationFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraanimationfactory-createanimationfromkeyframetracks"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createAnimationFromKeyframeTracks.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraAnimationFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">createAnimationFromKeyframeTracks</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> <span class="name">createAnimationFromKeyframeTracks</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-createAnimationFromKeyframeTracks-param-tracks" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span>\></span></span> <span class="parameter-name">tracks</span></span>

)

</div>

<div class="section desc markdown">

Creates a MapCameraAnimation for a movement defined by the supplied list of `MapCameraAnimationFactory.createAnimationFromKeyframeTracks.tracks`.

Keyframe tracks specify how the map camera properties change during the animation. For the animation to be possible, no two different tracks can affect the same map camera property. The input tracks are validated with that in mind.

However, the following cases can only be detected at the time when animation is started:

- Changing altitude of camera position also changes camera look-at distance and at high altitudes, also camera look-at orientation.

- Changing tilt of camera orientation also changes camera look-at distance and camera look-at target.

- Changing bearing of camera orientation also changes camera look-at target if current tilt is not 0.

- Changing tilt or bearing of camera look-at orientation also changes camera position.

- Changing camera look-at orientation also changes camera look-at distance if tilt is not 0.

- `tracks` The list of tracks

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a>. MapCameraAnimation instance

Throws <a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationexception-class">MapCameraAnimationInstantiationException</a>. Indicates an instantiation issue.

</div>

## Implementation

``` dart
static MapCameraAnimation createAnimationFromKeyframeTracks(List<MapCameraKeyframeTrack> tracks) => $prototype.createAnimationFromKeyframeTracks(tracks);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
