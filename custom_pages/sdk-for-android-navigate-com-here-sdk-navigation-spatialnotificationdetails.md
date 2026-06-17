---
title: "SpatialNotificationDetails (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SpatialNotificationDetails.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.SpatialNotificationDetails</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SpatialNotificationDetails</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>This class provides all the information for a spatial text notification, including the
 maneuver data and extra data which is required to set the direction of spatialization
 of the audio cue.</p></div>
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
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#audioCuePanning">audioCuePanning</a></code></div>
<div class="col-last even-row-color">
<div class="block">Object to start the angular panning when spatialization of the text notification is desired</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#estimatedAudioCueDuration">estimatedAudioCueDuration</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Estimation of the required time to play an audio cue at speech rate 1.0.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#initialAzimuthInDegrees">initialAzimuthInDegrees</a></code></div>
<div class="col-last even-row-color">
<div class="block">Initial desired angular position of the upcoming audio cue.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(double,com.here.sdk.navigation.SpatialAudioCuePanning,com.here.time.Duration)">SpatialNotificationDetails</a><wbr/>(double initialAzimuthInDegrees,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a> audioCuePanning,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
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
<section class="detail" id="initialAzimuthInDegrees">
<h3>initialAzimuthInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">initialAzimuthInDegrees</span></div>
<div class="block"><p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
 "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
 from the front to the right, mimicking the maneuver geometry.
 In this case, it is good practice to start the trajectory from an initial azimuth that is located
 slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
 and terminate the trajectory fully on the right side. The initial azimuth angle of such
 a trajectory would be, for example, -5.0 (slightly front-left).
 This azimuth value is needed to set the position of the audio renderer before starting to play
 the audio cue to avoid unwanted audio "jumps".
 The orientation in space for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#initialAzimuthInDegrees"><code>initialAzimuthInDegrees</code></a> can be represented by the
 following angular values:
 <table>
<thead>
<tr><th align="center">Front</th><th align="center">Right</th><th align="center">Rear</th><th align="center">Left</th></tr>
</thead>
<tbody>
<tr><td align="center">0°</td><td align="center">+90°</td><td align="center">+- 180</td><td align="center">-90°</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="audioCuePanning">
<h3>audioCuePanning</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a></span> <span class="element-name">audioCuePanning</span></div>
<div class="block"><p>Object to start the angular panning when spatialization of the text notification is desired</p></div>
</section>
</li>
<li>
<section class="detail" id="estimatedAudioCueDuration">
<h3>estimatedAudioCueDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">estimatedAudioCueDuration</span></div>
<div class="block"><p>Estimation of the required time to play an audio cue at speech rate 1.0.
 For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds.
 Therefore, an estimation of this audio cue duration is needed to correctly sync the movement
 of sound to the cue (so that audio movement and audio duration match).</p></div>
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
<section class="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.SpatialAudioCuePanning,com.here.time.Duration)">
<h3>SpatialNotificationDetails</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SpatialNotificationDetails</span><wbr/><span class="parameters">(double initialAzimuthInDegrees,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a> audioCuePanning,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initialAzimuthInDegrees</code> - <p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
 "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
 from the front to the right, mimicking the maneuver geometry.
 In this case, it is good practice to start the trajectory from an initial azimuth that is located
 slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
 and terminate the trajectory fully on the right side. The initial azimuth angle of such
 a trajectory would be, for example, -5.0 (slightly front-left).
 This azimuth value is needed to set the position of the audio renderer before starting to play
 the audio cue to avoid unwanted audio "jumps".
 The orientation in space for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#initialAzimuthInDegrees"><code>initialAzimuthInDegrees</code></a> can be represented by the
 following angular values:
 <table>
<thead>
<tr><th align="center">Front</th><th align="center">Right</th><th align="center">Rear</th><th align="center">Left</th></tr>
</thead>
<tbody>
<tr><td align="center">0°</td><td align="center">+90°</td><td align="center">+- 180</td><td align="center">-90°</td></tr>
</tbody>
</table></p></dd>
<dd><code>audioCuePanning</code> - <p>Object to start the angular panning when spatialization of the text notification is desired</p></dd>
<dd><code>estimatedAudioCueDuration</code> - <p>Estimation of the required time to play an audio cue at speech rate 1.0.
 For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds.
 Therefore, an estimation of this audio cue duration is needed to correctly sync the movement
 of sound to the cue (so that audio movement and audio duration match).</p></dd>
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
`
}</HTMLBlock>
