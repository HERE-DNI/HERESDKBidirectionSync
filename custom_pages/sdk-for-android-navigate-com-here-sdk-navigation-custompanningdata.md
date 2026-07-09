---
title: "CustomPanningData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CustomPanningData.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.CustomPanningData</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">CustomPanningData</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>This class contains all the information regarding the next angular panning element, including
 a new estimated audio cue duration, and a new set of initial and sweep angular angle,
 allowing the customization of the spatial audio trajectories for any type of notification,
 such as speed or merge warners, maneuvers or even roundabouts notifications.
 The orientation in space for <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#initialAzimuthInDegrees"><code>initialAzimuthInDegrees</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#sweepAzimuthInDegrees"><code>sweepAzimuthInDegrees</code></a> can
 be represented by the following angular values:
 <table>
<thead>
<tr><th align="center">Front</th><th align="center">Right</th><th align="center">Rear</th><th align="center">Left</th></tr>
</thead>
<tbody>
<tr><td align="center">0°</td><td align="center">+90°</td><td align="center">+- 180</td><td align="center">-90°</td></tr>
</tbody>
</table>
When any of the members of <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata" title="class in com.here.sdk.navigation"><code>CustomPanningData</code></a> are initialized as null, the default value
 provided by HERE SDK will be used instead.
 The audio cue is spatialized considering the action of both maneuvers, for example,
 the audio cue 'Now turn right and then turn left' will be spatialized as following:
 'Now turn right' will be heard as coming from the right.
 'and then turn left' will be heard as coming from the left.
 Note: The estimation for playing both audio cues could be not fully accurate and therefore
 a mismatch between the audio source and the audio cue message could be perceived.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#estimatedAudioCueDuration">estimatedAudioCueDuration</a></code></div>
<div className="col-last even-row-color">
<div className="block">Customized estimated duration for playing the audio cue on the selected TTS Engine.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#initialAzimuthInDegrees">initialAzimuthInDegrees</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Initial desired angular position of the upcoming audio cue.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#sweepAzimuthInDegrees">sweepAzimuthInDegrees</a></code></div>
<div className="col-last even-row-color">
<div className="block">Sweep angle of the upcoming audio cue.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#%3Cinit%3E(com.here.time.Duration,java.lang.Double,java.lang.Double)">CustomPanningData</a><wbr/>(<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> initialAzimuthInDegrees,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> sweepAzimuthInDegrees)</code></div>
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
<section className="detail" id="estimatedAudioCueDuration">
<h3>estimatedAudioCueDuration</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">estimatedAudioCueDuration</span></div>
<div className="block"><p>Customized estimated duration for playing the audio cue on the selected TTS Engine.
 When not used, HERE SDK's estimation will be used instead.</p></div>
</section>
</li>
<li>
<section className="detail" id="initialAzimuthInDegrees">
<h3>initialAzimuthInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">initialAzimuthInDegrees</span></div>
<div className="block"><p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
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
<section className="detail" id="sweepAzimuthInDegrees">
<h3>sweepAzimuthInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">sweepAzimuthInDegrees</span></div>
<div className="block"><p>Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on"
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
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.time.Duration,java.lang.Double,java.lang.Double)">
<h3>CustomPanningData</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CustomPanningData</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> initialAzimuthInDegrees,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> sweepAzimuthInDegrees)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
