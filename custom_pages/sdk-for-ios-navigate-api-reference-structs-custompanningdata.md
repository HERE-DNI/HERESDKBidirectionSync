---
title: "CustomPanningData"
slug: "sdk-for-ios-navigate-api-reference-structs-custompanningdata"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CustomPanningData"></a>
<a title="CustomPanningData Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        CustomPanningData Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CustomPanningData</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CustomPanningData</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class contains all the information regarding the next angular panning element, including
a new estimated audio cue duration, and a new set of initial and sweep angular angle,
allowing the customization of the spatial audio trajectories for any type of notification,
such as speed or merge warners, maneuvers or even roundabouts notifications.
The orientation in space for <code><a href="../Structs/CustomPanningData.html#/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp">CustomPanningData.initialAzimuthInDegrees</a></code> and <code><a href="../Structs/CustomPanningData.html#/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp">CustomPanningData.sweepAzimuthInDegrees</a></code> can
be represented by the following angular values:</p>
<table><thead>
<tr>
<th style="text-align: center">Front</th>
<th style="text-align: center">Right</th>
<th style="text-align: center">Rear</th>
<th style="text-align: center">Left</th>
</tr>
</thead><tbody>
<tr>
<td style="text-align: center">0°</td>
<td style="text-align: center">+90°</td>
<td style="text-align: center">+- 180</td>
<td style="text-align: center">-90°</td>
</tr>
</tbody></table>
<p>When any of the members of <code>CustomPanningData</code> are initialized as null, the default value
provided by HERE SDK will be used instead.
The audio cue is spatialized considering the action of both maneuvers, for example,
the audio cue ‘Now turn right and then turn left’ will be spatialized as following:
‘Now turn right’ will be heard as coming from the right.
‘and then turn left’ will be heard as coming from the left.
Note: The estimation for playing both audio cues could be not fully accurate and therefore
a mismatch between the audio source and the audio cue message could be perceived.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CustomPanningDataV25estimatedAudioCueDurationSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/estimatedAudioCueDuration"></a>
<a class="token" href="#/s:7heresdk17CustomPanningDataV25estimatedAudioCueDurationSdSgvp">estimatedAudioCueDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Customized estimated duration for playing the audio cue on the selected TTS Engine.
When not used, HERE SDK’s estimation will be used instead.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">estimatedAudioCueDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/initialAzimuthInDegrees"></a>
<a class="token" href="#/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp">initialAzimuthInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
as “Turn right on” (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc
from the front to the right, mimicking the maneuver geometry. In this case,
it is good practice to start the trajectory from an initial azimuth that is slightly located
on the opposite direction of the maneuver (e.g. slightly starting from “front-left”)
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting
to play the audio cue to avoid unwanted audio “jumps”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">initialAzimuthInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sweepAzimuthInDegrees"></a>
<a class="token" href="#/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp">sweepAzimuthInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sweep angle of the upcoming audio cue. For example, for a maneuver such as “Turn right on”
(i.e. <code>ManeuverAction.RightTurn</code>),
within an <code>initial_azimuth_in_degrees</code> of -5 degrees, we want to create a spatial audio arc
trajectory from the front to the right, mimicking the maneuver geometry.
In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of
+95 degrees would be required.
On the other hand, when the desired spatialization is to the left side
(i.e. <code>ManeuverAction.LeftTurn</code>), the <code>initial_azimuth_in_degrees</code> could be set to +5 degrees
and the <code>sweep_azimuth_in_degrees</code> to -95 degrees</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sweepAzimuthInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CustomPanningDataV25estimatedAudioCueDuration23initialAzimuthInDegrees05sweepjkL0ACSdSg_A2Gtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(estimatedAudioCueDuration:initialAzimuthInDegrees:sweepAzimuthInDegrees:)"></a>
<a class="token" href="#/s:7heresdk17CustomPanningDataV25estimatedAudioCueDuration23initialAzimuthInDegrees05sweepjkL0ACSdSg_A2Gtcfc">init(estimatedAudioCueDuration:<wbr/>initialAzimuthInDegrees:<wbr/>sweepAzimuthInDegrees:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">estimatedAudioCueDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">initialAzimuthInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">sweepAzimuthInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>
