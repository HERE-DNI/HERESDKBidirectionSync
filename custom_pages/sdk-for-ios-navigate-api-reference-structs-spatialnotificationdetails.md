---
title: "Navigation / SpatialNotificationDetails"
slug: "sdk-for-ios-navigate-api-reference-structs-spatialnotificationdetails"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpatialNotificationDetails"></a>
<a title="SpatialNotificationDetails Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SpatialNotificationDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpatialNotificationDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpatialNotificationDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class provides all the information for a spatial text notification, including the
maneuver data and extra data which is required to set the direction of spatialization
of the audio cue.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/initialAzimuthInDegrees"></a>
<a class="token" href="#/s:7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegreesSdvp">initialAzimuthInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
“Turn right on” (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
from the front to the right, mimicking the maneuver geometry.
In this case, it is good practice to start the trajectory from an initial azimuth that is located
slightly on the opposite direction of the maneuver (e.g. slightly starting from “front-left”)
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting to play
the audio cue to avoid unwanted audio “jumps”.
The orientation in space for <code>SpatialNotificationDetails.initialAzimuthInDegrees</code> can be represented by the
following angular values:</p>
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
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">initialAzimuthInDegrees</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26SpatialNotificationDetailsV15audioCuePanningAA0b5AudiofG0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/audioCuePanning"></a>
<a class="token" href="#/s:7heresdk26SpatialNotificationDetailsV15audioCuePanningAA0b5AudiofG0Cvp">audioCuePanning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to start the angular panning when spatialization of the text notification is desired</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">audioCuePanning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-spatialaudiocuepanning">SpatialAudioCuePanning</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26SpatialNotificationDetailsV25estimatedAudioCueDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/estimatedAudioCueDuration"></a>
<a class="token" href="#/s:7heresdk26SpatialNotificationDetailsV25estimatedAudioCueDurationSdvp">estimatedAudioCueDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimation of the required time to play an audio cue at speech rate 1.0.
For example the cue “Turn right on Name-Of-A-Street” will playback over an X number of milliseconds.
Therefore, an estimation of this audio cue duration is needed to correctly sync the movement
of sound to the cue (so that audio movement and audio duration match).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">estimatedAudioCueDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegrees15audioCuePanning014estimatedAudioJ8DurationACSd_AA0bmjK0CSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(initialAzimuthInDegrees:audioCuePanning:estimatedAudioCueDuration:)"></a>
<a class="token" href="#/s:7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegrees15audioCuePanning014estimatedAudioJ8DurationACSd_AA0bmjK0CSdtcfc">init(initialAzimuthInDegrees:<wbr/>audioCuePanning:<wbr/>estimatedAudioCueDuration:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>initialAzimuthInDegrees: Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
“Turn right on” (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
from the front to the right, mimicking the maneuver geometry.
In this case, it is good practice to start the trajectory from an initial azimuth that is located
slightly on the opposite direction of the maneuver (e.g. slightly starting from “front-left”)
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting to play
the audio cue to avoid unwanted audio “jumps”.
The orientation in space for <code><a href="../Structs/SpatialNotificationDetails.html#/s:7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegreesSdvp">SpatialNotificationDetails.initialAzimuthInDegrees</a></code> can be represented by the
following angular values:</li>
</ul>
<p>|  Front |  Right | Rear  | Left  |
  |:—-:|:—-:|:—-:|:—-:|
  |  0° | +90° | +- 180 | -90° |</p>
<ul>
<li>audioCuePanning: Object to start the angular panning when spatialization of the text notification is desired</li>
<li>estimatedAudioCueDuration: Estimation of the required time to play an audio cue at speech rate 1.0.
For example the cue “Turn right on Name-Of-A-Street” will playback over an X number of milliseconds.
Therefore, an estimation of this audio cue duration is needed to correctly sync the movement
of sound to the cue (so that audio movement and audio duration match).</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">initialAzimuthInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">audioCuePanning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-spatialaudiocuepanning">SpatialAudioCuePanning</a></span><span class="p">,</span> <span class="nv">estimatedAudioCueDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span></code></pre>
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
}</HTMLBlock>
