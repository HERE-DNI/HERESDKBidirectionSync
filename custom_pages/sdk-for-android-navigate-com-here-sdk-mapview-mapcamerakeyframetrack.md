---
title: "MapCameraKeyframeTrack (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapCameraKeyframeTrack.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapCameraKeyframeTrack</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapCameraKeyframeTrack</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Stores keyframes for interpolation of a camera property using a specific easing function
 and interpolation mode. Can only hold keyframes of a single type.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes a reason for failing to create a MapCameraKeyframeTrack.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview"><code>MapCameraKeyframeTrack</code></a>.</div>
</div>
</div>
</section>
</li>
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
<section className="detail" id="getScalarKeyframes()">
<h3>getScalarKeyframes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt;</span> <span className="element-name">getScalarKeyframes</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPoint2DKeyframes()">
<h3>getPoint2DKeyframes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>&gt;</span> <span className="element-name">getPoint2DKeyframes</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAnchor2DKeyframes()">
<h3>getAnchor2DKeyframes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>&gt;</span> <span className="element-name">getAnchor2DKeyframes</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeoCoordinatesKeyframes()">
<h3>getGeoCoordinatesKeyframes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt;</span> <span className="element-name">getGeoCoordinatesKeyframes</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeoOrientationKeyframes()">
<h3>getGeoOrientationKeyframes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>&gt;</span> <span className="element-name">getGeoOrientationKeyframes</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAtDistance(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtDistance</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span className="element-name">lookAtDistance</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.27.0. Use <scalarkeyframe>, Easing, KeyframeInterpolationMode) instead.</scalarkeyframe></p></div>
</div>
<div className="block"><p>Creates a map camera look-at distance keyframe track. It enables animations of the distance
 from the map camera to the target point that the camera looks at in meters. The values will
 be clamped according to the minimum and maximum zoom levels set for the map camera.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the camera property is changed.
     Keyframe time offsets are considered to be relative to the previous keyframe
     in the list or relative to the start of the animation if the current keyframe
     is first in the list.
     Time offset of the first keyframe in the list should be 0, otherwise an error occurs
     and creation of the keyframe track will fail.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>A keyframe track over the distance from the map camera to its target.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAtDistance(com.here.sdk.mapview.MapMeasure.Kind,java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtDistance</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span className="element-name">lookAtDistance</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a> distanceKind,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a map camera look-at distance keyframe track. It enables animations of the distance
 from the map camera to the target point that the camera looks at. The measure kind of that distance can be
 specified. The values will be clamped according to the minimum and maximum zoom levels set for the map
 camera.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>distanceKind</code> - <p>The kind of measure of distance between camera and target point.</p></dd>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the camera property is changed.
     Keyframe time offsets are considered to be relative to the previous keyframe
     in the list or relative to the start of the animation if the current keyframe
     is first in the list.
     Time offset of the first keyframe in the list should be 0, otherwise an error occurs
     and creation of the keyframe track will fail.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>A keyframe track over the distance from the map camera to its target.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAtTarget(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtTarget</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span className="element-name">lookAtTarget</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a map camera look-at target keyframe track. It enables animations over the
 geographical coordinates of the target point that the map camera is looking at.
 Altitude components of coordinates are ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the camera property is changed.
     Keyframe time offsets are considered to be relative to the previous keyframe
     in the list or relative to the start of the animation if the current keyframe
     is first in the list.
     Time offset of the first keyframe in the list should be 0, otherwise an error occurs
     and creation of the keyframe track will fail.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>A keyframe track over the map camera target coordinates.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAtOrientation(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtOrientation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span className="element-name">lookAtOrientation</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                                throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a map camera look-at orientation keyframe track. It enables animations over the
 orientation of the map camera target (bearing and tilt).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the camera property is changed.
     Keyframe time offsets are considered to be relative to the previous keyframe
     in the list or relative to the start of the animation if the current keyframe
     is first in the list.
     Time offset of the first keyframe in the list should be 0, otherwise an error occurs
     and creation of the keyframe track will fail.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>A keyframe track over the map camera target orientation.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="principalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>principalPoint</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span className="element-name">principalPoint</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a map camera principal point keyframe track. It enables animations on the pixel point
 where the map camera's target is placed in view coordinates. (0,0) is top left of the
 viewport, (viewport width, viewport height) is bottom right.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the camera property is changed.
     Point values must be in screen (pixel) coordinates with origin (0,0) in the top left of the viewport.
     Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation.
     Keyframe time offsets are considered to be relative to the previous keyframe
     in the list or relative to the start of the animation if the current keyframe
     is first in the list.
     Time offset of the first keyframe in the list should be 0, otherwise an error occurs
     and creation of the keyframe track will fail.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>A keyframe track over the principal point.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="normalizedPrincipalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>normalizedPrincipalPoint</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span className="element-name">normalizedPrincipalPoint</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                                       throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a map camera principal point keyframe track. It enables animations on the point
 where the map camera's target is placed in normalized view coordinates. (0,0) is top left of
 the viewport, (1, 1) is bottom right.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the camera property is changed.
     Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport.
     Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation.
     Keyframe time offsets are considered to be relative to the previous keyframe
     in the list or relative to the start of the animation if the current keyframe
     is first in the list.
     Time offset of the first keyframe in the list should be 0, otherwise an error occurs
     and creation of the keyframe track will fail.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>A keyframe track over the principal point.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fieldOfView(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>fieldOfView</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span className="element-name">fieldOfView</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a map camera field-of-view keyframe track. It enables animations over the angle of
 the field of view captured by the map camera in degrees. Values will be clamped to a range
 from 1 to 150.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the camera property is changed.
     Keyframe time offsets are considered to be relative to the previous keyframe
     in the list or relative to the start of the animation if the current keyframe
     is first in the list.
     Time offset of the first keyframe in the list should be 0, otherwise an error occurs
     and creation of the keyframe track will fail.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>A keyframe track over the map camera field-of-view.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInterpolationMode()">
<h3>getInterpolationMode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a></span> <span className="element-name">getInterpolationMode</span>()</div>
<div className="block"><p>Gets the interpolation mode for the between key frames in the track.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Interpolation mode affects the shape of the spline going through all keyframes.</p></dd>
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
