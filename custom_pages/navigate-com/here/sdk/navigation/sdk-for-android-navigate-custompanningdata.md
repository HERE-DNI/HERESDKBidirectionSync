---
title: "CustomPanningData (API Reference)"
slug: "sdk-for-android-navigate-custompanningdata"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CustomPanningData.html -->
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
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.CustomPanningData</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">CustomPanningData</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>This class contains all the information regarding the next angular panning element, including
 a new estimated audio cue duration, and a new set of initial and sweep angular angle,
 allowing the customization of the spatial audio trajectories for any type of notification,
 such as speed or merge warners, maneuvers or even roundabouts notifications.
 The orientation in space for <a href="#initialAzimuthInDegrees"><code>initialAzimuthInDegrees</code></a> and <a href="#sweepAzimuthInDegrees"><code>sweepAzimuthInDegrees</code></a> can
 be represented by the following angular values:
 <table>
<thead>
<tr><th align="center">Front</th><th align="center">Right</th><th align="center">Rear</th><th align="center">Left</th></tr>
</thead>
<tbody>
<tr><td align="center">0°</td><td align="center">+90°</td><td align="center">+- 180</td><td align="center">-90°</td></tr>
</tbody>
</table>
<p>When any of the members of <a href="sdk-for-android-navigate-custompanningdata" title="class in com.here.sdk.navigation"><code>CustomPanningData</code></a> are initialized as null, the default value
 provided by HERE SDK will be used instead.
 The audio cue is spatialized considering the action of both maneuvers, for example,
 the audio cue 'Now turn right and then turn left' will be spatialized as following:
 'Now turn right' will be heard as coming from the right.
 'and then turn left' will be heard as coming from the left.
 Note: The estimation for playing both audio cues could be not fully accurate and therefore
 a mismatch between the audio source and the audio cue message could be perceived.</p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#estimatedAudioCueDuration">estimatedAudioCueDuration</a></code></div>
<div class="col-last even-row-color">
<div class="block">Customized estimated duration for playing the audio cue on the selected TTS Engine.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#initialAzimuthInDegrees">initialAzimuthInDegrees</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Initial desired angular position of the upcoming audio cue.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#sweepAzimuthInDegrees">sweepAzimuthInDegrees</a></code></div>
<div class="col-last even-row-color">
<div class="block">Sweep angle of the upcoming audio cue.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.time.Duration,java.lang.Double,java.lang.Double)">CustomPanningData</a><wbr/>(<a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> initialAzimuthInDegrees,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> sweepAzimuthInDegrees)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="estimatedAudioCueDuration">
<h3>estimatedAudioCueDuration</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">estimatedAudioCueDuration</span></div>
<div class="block"><p>Customized estimated duration for playing the audio cue on the selected TTS Engine.
 When not used, HERE SDK's estimation will be used instead.</p></div>
</section>
</li>
<li>
<section class="detail" id="initialAzimuthInDegrees">
<h3>initialAzimuthInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">initialAzimuthInDegrees</span></div>
<div class="block"><p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
 as "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc
 from the front to the right, mimicking the maneuver geometry. In this case,
 it is good practice to start the trajectory from an initial azimuth that is slightly located
 on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
 and terminate the trajectory fully on the right side. The initial azimuth angle of such
 a trajectory would be, for example, -5.0 (slightly front-left).
 This azimuth value is needed to set the position of the audio renderer before starting
 to play the audio cue to avoid unwanted audio "jumps".</p></div>
</section>
</li>
<li>
<section class="detail" id="sweepAzimuthInDegrees">
<h3>sweepAzimuthInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">sweepAzimuthInDegrees</span></div>
<div class="block"><p>Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on"
 (i.e. <code>ManeuverAction.RightTurn</code>),
 within an <code>initial_azimuth_in_degrees</code> of -5 degrees, we want to create a spatial audio arc
 trajectory from the front to the right, mimicking the maneuver geometry.
 In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of
 +95 degrees would be required.
 On the other hand, when the desired spatialization is to the left side
 (i.e. <code>ManeuverAction.LeftTurn</code>), the <code>initial_azimuth_in_degrees</code> could be set to +5 degrees
 and the <code>sweep_azimuth_in_degrees</code> to -95 degrees</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.time.Duration,java.lang.Double,java.lang.Double)">
<h3>CustomPanningData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CustomPanningData</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> initialAzimuthInDegrees,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> sweepAzimuthInDegrees)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>estimatedAudioCueDuration</code> - <p>Customized estimated duration for playing the audio cue on the selected TTS Engine.
 When not used, HERE SDK's estimation will be used instead.</p></dd>
<dd><code>initialAzimuthInDegrees</code> - <p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
 as "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc
 from the front to the right, mimicking the maneuver geometry. In this case,
 it is good practice to start the trajectory from an initial azimuth that is slightly located
 on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
 and terminate the trajectory fully on the right side. The initial azimuth angle of such
 a trajectory would be, for example, -5.0 (slightly front-left).
 This azimuth value is needed to set the position of the audio renderer before starting
 to play the audio cue to avoid unwanted audio "jumps".</p></dd>
<dd><code>sweepAzimuthInDegrees</code> - <p>Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on"
 (i.e. <code>ManeuverAction.RightTurn</code>),
 within an <code>initial_azimuth_in_degrees</code> of -5 degrees, we want to create a spatial audio arc
 trajectory from the front to the right, mimicking the maneuver geometry.
 In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of
 +95 degrees would be required.
 On the other hand, when the desired spatialization is to the left side
 (i.e. <code>ManeuverAction.LeftTurn</code>), the <code>initial_azimuth_in_degrees</code> could be set to +5 degrees
 and the <code>sweep_azimuth_in_degrees</code> to -95 degrees</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
