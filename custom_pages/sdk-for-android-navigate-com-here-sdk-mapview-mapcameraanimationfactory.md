---
title: "MapCameraAnimationFactory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapCameraAnimationFactory.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapCameraAnimationFactory</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapCameraAnimationFactory</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Factory for creating MapCameraAnimation objects to change map's camera over time.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory#createAnimation(com.here.sdk.mapview.MapCameraKeyframeTrack)">createAnimation</a><wbr/>(<a href="sdk-for-android-navigate-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a> track)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a MapCameraAnimation for a movement defined by the supplied <code>track</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory#createAnimation(com.here.sdk.mapview.MapCameraUpdate,com.here.time.Duration,com.here.sdk.animation.Easing)">createAnimation</a><wbr/>(<a href="sdk-for-android-navigate-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate,
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration,
 <a href="sdk-for-android-navigate-easing" title="class in com.here.sdk.animation">Easing</a> easing)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview"><code>MapCameraAnimation</code></a> to gradually update the camera properties within a specified
 duration from its current values to the ones defined in the <code>cameraUpdate</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory#createAnimation(java.util.List)">createAnimation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a>&gt; tracks)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a MapCameraAnimation for a movement defined by the supplied list of <code>tracks</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,double,com.here.time.Duration)">flyTo</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 double bowFactor,
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,double,com.here.time.Duration)">flyTo</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 <a href="sdk-for-android-navigate-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 double bowFactor,
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration)">flyTo</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 <a href="sdk-for-android-navigate-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double bowFactor,
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory#flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration)">flyTo</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double bowFactor,
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="createAnimation(com.here.sdk.mapview.MapCameraUpdate,com.here.time.Duration,com.here.sdk.animation.Easing)">
<h3>createAnimation</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">createAnimation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate,
 @NonNull
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration,
 @NonNull
 <a href="sdk-for-android-navigate-easing" title="class in com.here.sdk.animation">Easing</a> easing)</span></div>
<div class="block"><p>Creates a <a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview"><code>MapCameraAnimation</code></a> to gradually update the camera properties within a specified
 duration from its current values to the ones defined in the <code>cameraUpdate</code>. <code>MapCameraAnimation</code>
 instances created from <a href="sdk-for-android-navigate-mapcameraupdatefactory#compositeUpdate(java.util.List)"><code>MapCameraUpdateFactory.compositeUpdate(java.util.List&lt;com.here.sdk.mapview.MapCameraUpdate&gt;)</code></a> instances are not supported. An
 <a href="sdk-for-android-navigate-animationlistener" title="interface in com.here.sdk.animation"><code>AnimationListener</code></a> will receive an <a href="sdk-for-android-navigate-animationstate#CANCELLED"><code>AnimationState.CANCELLED</code></a> signal
 when trying to apply such animations.</p></div>
<dl class="notes">
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
<section class="detail" id="createAnimation(com.here.sdk.mapview.MapCameraKeyframeTrack)">
<h3>createAnimation</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">createAnimation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a> track)</span></div>
<div class="block"><p>Creates a MapCameraAnimation for a movement defined by the supplied <code>track</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>track</code> - <p>The track</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnimation(java.util.List)">
<h3>createAnimation</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">createAnimation</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a>&gt; tracks)</span>
                                          throws <span class="exceptions"><a href="sdk-for-android-navigate-mapcameraanimation.instantiationexception" title="class in com.here.sdk.mapview">MapCameraAnimation.InstantiationException</a></span></div>
<div class="block"><p>Creates a MapCameraAnimation for a movement defined by the supplied list of <code>tracks</code>.
 Keyframe tracks specify how the map camera properties change during the animation.
 For the animation to be possible, no two different tracks can
 affect the same map camera property. The input tracks are validated with that in mind.
 </p><p>However, the following cases can only be detected at the time when animation is started:
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
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tracks</code> - <p>The list of tracks</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapcameraanimation.instantiationexception" title="class in com.here.sdk.mapview">MapCameraAnimation.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div class="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.
 </p><p>The beginning and end of the animation will use the current zoom.
 </p><p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     </p><p>The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     </p><p>A bow factor of 0 does not change the camera's zoom over time.
     </p><p>Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     </p><p>The bow factor is clamped to [-1, +1].
     </p><p>Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     </p><p>Note that currently, bow factor is ignored and assumed to be 1 if either start or end
     of animation has a non zero tilt.</p></dd>
<dd><code>duration</code> - <p>Duration of the flight. Negative duration results in no camera change when applied.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div class="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.
 </p><p>The beginning and end of the animation will use the current zoom.
 </p><p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>orientation</code> - <p>The orientation at destination.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     </p><p>The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     </p><p>A bow factor of 0 does not change the camera's zoom over time.
     </p><p>Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     </p><p>The bow factor is clamped to [-1, +1].
     </p><p>Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     </p><p>Note that currently, bow factor is ignored and assumed to be 1 if either start or end
     of animation has a non zero tilt.</p></dd>
<dd><code>duration</code> - <p>Duration of the flight. Negative duration results in no camera change when applied.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div class="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.
 </p><p>The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.
 </p><p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>zoom</code> - <p>The zoom at the end of the animation.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     </p><p>The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     </p><p>A bow factor of 0 does not affect the camera's zoom over time.
     </p><p>Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     </p><p>The bow factor is clamped to [-1, +1].
     </p><p>Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     </p><p>Note that currently, bow factor is ignored and assumed to be 1 if either start or end
     of animation has a non zero tilt.</p></dd>
<dd><code>duration</code> - <p>Duration of the flight. Negative duration results in no camera change when applied.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraAnimation instance</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flyTo(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure,double,com.here.time.Duration)">
<h3>flyTo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double bowFactor,
 @NonNull
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div class="block"><p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.
 </p><p>The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.
 </p><p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The coordinates of the camera destination point.
     Any target sub-element value that is not finite will be set to the current camera target sub-element value.
     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
     will consider the target point as being located on the ground.</p></dd>
<dd><code>orientation</code> - <p>The orientation at destination.</p></dd>
<dd><code>zoom</code> - <p>The zoom at the end of the animation.</p></dd>
<dd><code>bowFactor</code> - <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.
     </p><p>The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
     curve is relative to the travel distance between current camera target and destination target.
     </p><p>A bow factor of 0 does not affect the camera's zoom over time.
     </p><p>Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.
     </p><p>The bow factor is clamped to [-1, +1].
     </p><p>Note that the lowest possible camera distance to earth is 0 meters and that the animation
     curve will not go below this value.
     </p><p>Note that currently, bow factor is ignored and assumed to be 1 if either start or end
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
`
}</HTMLBlock>
