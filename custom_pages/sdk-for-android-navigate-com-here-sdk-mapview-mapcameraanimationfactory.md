---
title: "MapCameraAnimationFactory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapCameraAnimationFactory.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapCameraAnimationFactory</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapCameraAnimationFactory</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Factory for creating MapCameraAnimation objects to change map's camera over time.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="createAnimation(com.here.sdk.mapview.MapCameraUpdate,com.here.time.Duration,com.here.sdk.animation.Easing)">
<h3>createAnimation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span className="element-name">createAnimation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing)</span></div>
<div className="block"><p>Creates a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview"><code>MapCameraAnimation</code></a> to gradually update the camera properties within a specified
 duration from its current values to the ones defined in the <code>cameraUpdate</code>. <code>MapCameraAnimation</code>
 instances created from <a href="sdk-for-android-navigate-mapcameraupdatefactory#compositeUpdate(java.util.List)"><code>MapCameraUpdateFactory.compositeUpdate(java.util.List<com.here.sdk.mapview.mapcameraupdate>)</com.here.sdk.mapview.mapcameraupdate></code></a> instances are not supported. An
 <a href="sdk-for-android-navigate-com-here-sdk-animation-animationlistener" title="interface in com.here.sdk.animation"><code>AnimationListener</code></a> will receive an <a href="sdk-for-android-navigate-animationstate#CANCELLED"><code>AnimationState.CANCELLED</code></a> signal
 when trying to apply such animations.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cameraUpdate</code> - <p>Update which should be applied to the map camera.</p></dd>
<dd><code>duration</code> - <p>Duration of the animation. Negative duration results in no camera change when applied.</p></dd>
<dd><code>easing</code> - <p>Easing to apply.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="createAnimation(com.here.sdk.mapview.MapCameraKeyframeTrack)">
<h3>createAnimation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span className="element-name">createAnimation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a> track)</span></div>
<div className="block"><p>Creates a MapCameraAnimation for a movement defined by the supplied <code>track</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>track</code> - <p>The track</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="createAnimation(java.util.List)">
<h3>createAnimation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span className="element-name">createAnimation</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a>&gt; tracks)</span>
                                          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation-instantiationexception" title="class in com.here.sdk.mapview">MapCameraAnimation.InstantiationException</a></span></div>
<div className="block"><p>Creates a MapCameraAnimation for a movement defined by the supplied list of <code>tracks</code>.
 Keyframe tracks specify how the map camera properties change during the animation.
 For the animation to be possible, no two different tracks can
 affect the same map camera property. The input tracks are validated with that in mind.
 However, the following cases can only be detected at the time when animation is started:
 <ul>
<li>Changing altitude of camera position also changes camera look-at distance
 and at high altitudes, also camera look-at orientation.</li>
<li>Changing tilt of camera orientation also changes camera look-at distance
 and camera look-at target.</li>
<li>Changing bearing of camera orientation also changes
 camera look-at target if current tilt is not 0.</li>
<li>Changing tilt or bearing of camera look-at orientation also changes
 camera position.</li>
<li>Changing camera look-at orientation also changes camera look-at distance
 if tilt is not 0.</li>
</ul></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tracks</code> - <p>The list of tracks</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation-instantiationexception" title="class in com.here.sdk.mapview">MapCameraAnimation.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span className="element-name">flyTo</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div className="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.
 The beginning and end of the animation will use the current zoom.
 Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     A bow factor of 0 does not change the camera's zoom over time.
     Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     The bow factor is clamped to [-1, +1].
     Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     Note that currently, bow factor is ignored and assumed to be 1 if either start or end
     of animation has a non zero tilt.</p></dd>
<dd><code>duration</code> - <p>Duration of the flight. Negative duration results in no camera change when applied.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span className="element-name">flyTo</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div className="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.
 The beginning and end of the animation will use the current zoom.
 Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>orientation</code> - <p>The orientation at destination.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     A bow factor of 0 does not change the camera's zoom over time.
     Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     The bow factor is clamped to [-1, +1].
     Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     Note that currently, bow factor is ignored and assumed to be 1 if either start or end
     of animation has a non zero tilt.</p></dd>
<dd><code>duration</code> - <p>Duration of the flight. Negative duration results in no camera change when applied.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span className="element-name">flyTo</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div className="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.
 The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.
 Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>zoom</code> - <p>The zoom at the end of the animation.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     A bow factor of 0 does not affect the camera's zoom over time.
     Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     The bow factor is clamped to [-1, +1].
     Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     Note that currently, bow factor is ignored and assumed to be 1 if either start or end
     of animation has a non zero tilt.</p></dd>
<dd><code>duration</code> - <p>Duration of the flight. Negative duration results in no camera change when applied.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span className="element-name">flyTo</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div className="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.
 The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.
 Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>orientation</code> - <p>The orientation at destination.</p></dd>
<dd><code>zoom</code> - <p>The zoom at the end of the animation.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     A bow factor of 0 does not affect the camera's zoom over time.
     Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     The bow factor is clamped to [-1, +1].
     Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     Note that currently, bow factor is ignored and assumed to be 1 if either start or end
     of animation has a non zero tilt.</p></dd>
<dd><code>duration</code> - <p>Duration of the flight. Negative duration results in no camera change when applied.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
