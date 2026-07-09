---
title: "SpatialNotificationDetails (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SpatialNotificationDetails.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.SpatialNotificationDetails</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SpatialNotificationDetails</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>This class provides all the information for a spatial text notification, including the
 maneuver data and extra data which is required to set the direction of spatialization
 of the audio cue.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#audioCuePanning">audioCuePanning</a></code></div>
<div className="col-last even-row-color">
<div className="block">Object to start the angular panning when spatialization of the text notification is desired</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#estimatedAudioCueDuration">estimatedAudioCueDuration</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Estimation of the required time to play an audio cue at speech rate 1.0.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#initialAzimuthInDegrees">initialAzimuthInDegrees</a></code></div>
<div className="col-last even-row-color">
<div className="block">Initial desired angular position of the upcoming audio cue.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#%3Cinit%3E(double,com.here.sdk.navigation.SpatialAudioCuePanning,com.here.time.Duration)">SpatialNotificationDetails</a><wbr/>(double initialAzimuthInDegrees,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a> audioCuePanning,
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="initialAzimuthInDegrees">
<h3>initialAzimuthInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">initialAzimuthInDegrees</span></div>
<div className="block"><p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
 "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
 from the front to the right, mimicking the maneuver geometry.
 In this case, it is good practice to start the trajectory from an initial azimuth that is located
 slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
 and terminate the trajectory fully on the right side. The initial azimuth angle of such
 a trajectory would be, for example, -5.0 (slightly front-left).
 This azimuth value is needed to set the position of the audio renderer before starting to play
 the audio cue to avoid unwanted audio "jumps".
 The orientation in space for <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#initialAzimuthInDegrees"><code>initialAzimuthInDegrees</code></a> can be represented by the
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
<section className="detail" id="audioCuePanning">
<h3>audioCuePanning</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a></span> <span className="element-name">audioCuePanning</span></div>
<div className="block"><p>Object to start the angular panning when spatialization of the text notification is desired</p></div>
</section>
</li>
<li>
<section className="detail" id="estimatedAudioCueDuration">
<h3>estimatedAudioCueDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">estimatedAudioCueDuration</span></div>
<div className="block"><p>Estimation of the required time to play an audio cue at speech rate 1.0.
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
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.SpatialAudioCuePanning,com.here.time.Duration)">
<h3>SpatialNotificationDetails</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SpatialNotificationDetails</span><wbr/><span className="parameters">(double initialAzimuthInDegrees,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a> audioCuePanning,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
 The orientation in space for <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#initialAzimuthInDegrees"><code>initialAzimuthInDegrees</code></a> can be represented by the
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
