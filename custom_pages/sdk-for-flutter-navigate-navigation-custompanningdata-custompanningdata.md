---
title: "CustomPanningData constructor"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-custompanningdata"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomPanningData.html -->


<div>
<h1>CustomPanningData constructor</h1></div>

CustomPanningData(<ol class="parameter-list single-line"> <li>Duration? estimatedAudioCueDuration, </li>
<li>double? initialAzimuthInDegrees, </li>
<li>double? sweepAzimuthInDegrees</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>estimatedAudioCueDuration</code> Customized estimated duration for playing the audio cue on the selected TTS Engine.
When not used, HERE SDK's estimation will be used instead.</li>
<li><code>initialAzimuthInDegrees</code> Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
as "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc
from the front to the right, mimicking the maneuver geometry. In this case,
it is good practice to start the trajectory from an initial azimuth that is slightly located
on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting
to play the audio cue to avoid unwanted audio "jumps".</li>
<li><code>sweepAzimuthInDegrees</code> Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on"
(i.e. <code>ManeuverAction.RightTurn</code>),
within an <code>initial_azimuth_in_degrees</code> of -5 degrees, we want to create a spatial audio arc
trajectory from the front to the right, mimicking the maneuver geometry.
In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of
+95 degrees would be required.
On the other hand, when the desired spatialization is to the left side
(i.e. <code>ManeuverAction.LeftTurn</code>), the <code>initial_azimuth_in_degrees</code> could be set to +5 degrees
and the <code>sweep_azimuth_in_degrees</code> to -95 degrees</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CustomPanningData(this.estimatedAudioCueDuration, this.initialAzimuthInDegrees, this.sweepAzimuthInDegrees);</code></pre>

 



</div>
`
}</HTMLBlock>
