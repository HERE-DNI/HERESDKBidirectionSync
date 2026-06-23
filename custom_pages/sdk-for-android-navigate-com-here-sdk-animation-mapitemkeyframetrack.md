---
title: "MapItemKeyFrameTrack (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-animation-mapitemkeyframetrack"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapItemKeyFrameTrack.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.animation.MapItemKeyFrameTrack</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapItemKeyFrameTrack</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Stores keyframes for interpolation of a map item property using a specific
 easing function and interpolation mode.
 </p><p>The keyframe track object is used to create animations,
 see <a href="sdk-for-android-navigate-mapmarkeranimation" title="class in com.here.sdk.animation"><code>MapMarkerAnimation</code></a> and <a href="sdk-for-android-navigate-mappolylineanimation" title="class in com.here.sdk.animation"><code>MapPolylineAnimation</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapitemkeyframetrack.instantiationerrorcode" title="enum class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to create a <a href="sdk-for-android-navigate-mapitemkeyframetrack" title="class in com.here.sdk.animation"><code>MapItemKeyFrameTrack</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapitemkeyframetrack.instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-navigate-mapitemkeyframetrack" title="class in com.here.sdk.animation"><code>MapItemKeyFrameTrack</code></a>.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#moveTo(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">moveTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-navigate-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-navigate-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map item position keyframe track.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#polylineProgress(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">polylineProgress</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-navigate-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-navigate-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a keyframe track used to animate the progress of a polyline.</div>
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
<section class="detail" id="moveTo(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>moveTo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a></span> <span class="element-name">moveTo</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                   throws <span class="exceptions"><a href="sdk-for-android-navigate-mapitemkeyframetrack.instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a map item position keyframe track. It enables animations over the geographical
 coordinates where the map item is positioned.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the map item position changes over time.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>MapItemKeyFrameTrack instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapitemkeyframetrack.instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></code> - <p>If the supplied keyframe list is empty or first keyframe duration is not 0.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="polylineProgress(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>polylineProgress</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a></span> <span class="element-name">polylineProgress</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-navigate-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-navigate-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span class="exceptions"><a href="sdk-for-android-navigate-mapitemkeyframetrack.instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a keyframe track used to animate the progress of a polyline.
 </p><p>Each scalar keyframe specifies the progress property
 (as passed to <a href="sdk-for-android-navigate-mappolyline#setProgress(double)"><code>MapPolyline.setProgress(double)</code></a>) at key points of the animation.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>keyframes</code> - <p>The list of keyframes that specify how the polyline progress changes
     over time.</p></dd>
<dd><code>easing</code> - <p>The easing to apply during keyframe interpolation.</p></dd>
<dd><code>interpolationMode</code> - <p>The type of interpolation done between keyframe values.</p></dd>
<dt>Returns:</dt>
<dd><p>MapItemKeyFrameTrack instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapitemkeyframetrack.instantiationexception" title="class in com.here.sdk.animation">MapItemKeyFrameTrack.InstantiationException</a></code> - <p>If the supplied keyframe list is empty or first keyframe duration is not 0.</p></dd>
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
