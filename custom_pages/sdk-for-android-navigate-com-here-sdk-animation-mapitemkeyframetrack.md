---
title: "MapItemKeyFrameTrack (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapItemKeyFrameTrack.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.animation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.animation.MapItemKeyFrameTrack</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapItemKeyFrameTrack</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Stores keyframes for interpolation of a map item property using a specific
 easing function and interpolation mode.
 The keyframe track object is used to create animations,
 see <a href="sdk-for-android-navigate-com-here-sdk-animation-mapmarkeranimation" title="class in com.here.sdk.animation"><code>MapMarkerAnimation</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-animation-mappolylineanimation" title="class in com.here.sdk.animation"><code>MapPolylineAnimation</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack-instantiationerrorcode" title="enum class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes a reason for failing to create a <a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack" title="class in com.here.sdk.animation"><code>MapItemKeyFrameTrack</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack" title="class in com.here.sdk.animation"><code>MapItemKeyFrameTrack</code></a>.</div>
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
<section className="detail" id="moveTo(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>moveTo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a></span> <span className="element-name">moveTo</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                   throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a map item position keyframe track. It enables animations over the geographical
 coordinates where the map item is positioned.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the map item position changes over time.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>MapItemKeyFrameTrack instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></code> - <p>If the supplied keyframe list is empty or first keyframe duration is not 0.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="polylineProgress(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>polylineProgress</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a></span> <span className="element-name">polylineProgress</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></span></div>
<div className="block"><p>Creates a keyframe track used to animate the progress of a polyline.
 Each scalar keyframe specifies the progress property
 (as passed to <a href="sdk-for-android-navigate-mappolyline#setProgress(double)"><code>MapPolyline.setProgress(double)</code></a>) at key points of the animation.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the polyline progress changes
     over time.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>MapItemKeyFrameTrack instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></code> - <p>If the supplied keyframe list is empty or first keyframe duration is not 0.</p></dd>
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
