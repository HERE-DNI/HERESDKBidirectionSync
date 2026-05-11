---
title: "MapCameraKeyframeTrack (API Reference)"
slug: "sdk-for-android-explore-mapcamerakeyframetrack"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapCameraKeyframeTrack.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapCameraKeyframeTrack</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapCameraKeyframeTrack</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Stores keyframes for interpolation of a camera property using a specific easing function
 and interpolation mode. Can only hold keyframes of a single type.</p></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to create a MapCameraKeyframeTrack.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview"><code>MapCameraKeyframeTrack</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fieldOfView(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">fieldOfView</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map camera field-of-view keyframe track.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnchor2DKeyframes()">getAnchor2DKeyframes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeoCoordinatesKeyframes()">getGeoCoordinatesKeyframes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeoOrientationKeyframes()">getGeoOrientationKeyframes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInterpolationMode()">getInterpolationMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the interpolation mode for the between key frames in the track.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPoint2DKeyframes()">getPoint2DKeyframes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getScalarKeyframes()">getScalarKeyframes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAtDistance(com.here.sdk.mapview.MapMeasure.Kind,java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">lookAtDistance</a><wbr/>(<a href="sdk-for-android-explore-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a> distanceKind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map camera look-at distance keyframe track.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#lookAtDistance(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">lookAtDistance</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAtOrientation(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">lookAtOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map camera look-at orientation keyframe track.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAtTarget(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">lookAtTarget</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map camera look-at target keyframe track.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalizedPrincipalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">normalizedPrincipalPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map camera principal point keyframe track.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#principalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">principalPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>&gt; keyframes,
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map camera principal point keyframe track.</div>
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
<section class="detail" id="getScalarKeyframes()">
<h3>getScalarKeyframes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt;</span> <span class="element-name">getScalarKeyframes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPoint2DKeyframes()">
<h3>getPoint2DKeyframes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>&gt;</span> <span class="element-name">getPoint2DKeyframes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnchor2DKeyframes()">
<h3>getAnchor2DKeyframes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>&gt;</span> <span class="element-name">getAnchor2DKeyframes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeoCoordinatesKeyframes()">
<h3>getGeoCoordinatesKeyframes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt;</span> <span class="element-name">getGeoCoordinatesKeyframes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeoOrientationKeyframes()">
<h3>getGeoOrientationKeyframes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>&gt;</span> <span class="element-name">getGeoOrientationKeyframes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAtDistance(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtDistance</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtDistance</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span class="exceptions"><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0. Use <scalarkeyframe>, Easing, KeyframeInterpolationMode) instead.</scalarkeyframe></p></div>
</div>
<div class="block"><p>Creates a map camera look-at distance keyframe track. It enables animations of the distance
 from the map camera to the target point that the camera looks at in meters. The values will
 be clamped according to the minimum and maximum zoom levels set for the map camera.</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAtDistance(com.here.sdk.mapview.MapMeasure.Kind,java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtDistance</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtDistance</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a> distanceKind,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span class="exceptions"><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a map camera look-at distance keyframe track. It enables animations of the distance
 from the map camera to the target point that the camera looks at. The measure kind of that distance can be
 specified. The values will be clamped according to the minimum and maximum zoom levels set for the map
 camera.</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAtTarget(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtTarget</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtTarget</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                           throws <span class="exceptions"><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a map camera look-at target keyframe track. It enables animations over the
 geographical coordinates of the target point that the map camera is looking at.
 Altitude components of coordinates are ignored.</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAtOrientation(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>lookAtOrientation</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtOrientation</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                                throws <span class="exceptions"><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a map camera look-at orientation keyframe track. It enables animations over the
 orientation of the map camera target (bearing and tilt).</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="principalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>principalPoint</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">principalPoint</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                             throws <span class="exceptions"><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a map camera principal point keyframe track. It enables animations on the pixel point
 where the map camera's target is placed in view coordinates. (0,0) is top left of the
 viewport, (viewport width, viewport height) is bottom right.</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="normalizedPrincipalPoint(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>normalizedPrincipalPoint</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">normalizedPrincipalPoint</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                                       throws <span class="exceptions"><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a map camera principal point keyframe track. It enables animations on the point
 where the map camera's target is placed in normalized view coordinates. (0,0) is top left of
 the viewport, (1, 1) is bottom right.</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fieldOfView(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode)">
<h3>fieldOfView</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">fieldOfView</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>&gt; keyframes,
 @NonNull
 <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation">Easing</a> easing,
 @NonNull
 <a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span>
                                          throws <span class="exceptions"><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span></div>
<div class="block"><p>Creates a map camera field-of-view keyframe track. It enables animations over the angle of
 the field of view captured by the map camera in degrees. Values will be clamped to a range
 from 1 to 150.</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInterpolationMode()">
<h3>getInterpolationMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a></span> <span class="element-name">getInterpolationMode</span>()</div>
<div class="block"><p>Gets the interpolation mode for the between key frames in the track.</p></div>
<dl class="notes">
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
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
