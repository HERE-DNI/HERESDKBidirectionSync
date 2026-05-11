---
title: "MapPolylineAnimation (API Reference)"
slug: "sdk-for-android-explore-mappolylineanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolylineAnimation.html -->
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
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li>Method</li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.animation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.animation.MapPolylineAnimation</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapPolylineAnimation</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>An animation that can be applied to the <a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a> object.</p></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mappolylineanimation-instantiationerrorcode" title="enum class in com.here.sdk.animation">MapPolylineAnimation.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to create a <a href="sdk-for-android-explore-mappolylineanimation" title="class in com.here.sdk.animation"><code>MapPolylineAnimation</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mappolylineanimation-instantiationexception" title="class in com.here.sdk.animation">MapPolylineAnimation.InstantiationException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Thrown when a problem occurs while trying to create a <a href="sdk-for-android-explore-mappolylineanimation" title="class in com.here.sdk.animation"><code>MapPolylineAnimation</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.animation.MapItemKeyFrameTrack)">MapPolylineAnimation</a><wbr/>(<a href="sdk-for-android-explore-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a> track)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an animation of <a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a> based on provided keyframe track.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.animation.MapItemKeyFrameTrack)">
<h3>MapPolylineAnimation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapPolylineAnimation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapitemkeyframetrack" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a> track)</span>
                     throws <span class="exceptions"><a href="sdk-for-android-explore-mappolylineanimation-instantiationexception" title="class in com.here.sdk.animation">MapPolylineAnimation.InstantiationException</a></span></div>
<div class="block"><p>Creates an animation of <a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a> based on provided keyframe track.
 Supports tracks created with <a href="sdk-for-android-explore-mapitemkeyframetrack" title="class in com.here.sdk.animation"><code>MapItemKeyFrameTrack</code></a> 'polylineProgress*' methods.
 For starting the animation, see <a href="sdk-for-android-explore-mappolyline#startAnimation(com.here.sdk.animation.MapPolylineAnimation,com.here.sdk.animation.AnimationListener)"><code>MapPolyline.startAnimation(com.here.sdk.animation.MapPolylineAnimation, com.here.sdk.animation.AnimationListener)</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>track</code> - <p>The track holding the keyframes for the animation.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mappolylineanimation-instantiationexception" title="class in com.here.sdk.animation">MapPolylineAnimation.InstantiationException</a></code> - <p>If the specified keyframe track cannot be used to create animation of a <a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>.</p></dd>
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
