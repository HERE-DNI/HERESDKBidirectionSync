---
title: "Navigation / SpatialAudioCuePanning"
slug: "sdk-for-ios-navigate-api-reference-classes-spatialaudiocuepanning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SpatialAudioCuePanning"></a>
<a title="SpatialAudioCuePanning Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SpatialAudioCuePanning Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpatialAudioCuePanning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SpatialAudioCuePanning</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpatialAudioCuePanning</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpatialAudioCuePanning</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the <code>SpatialAudioCuePanning</code> to notify each of the azimuths which compose a spatial audio
trajectory along the audio cue.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22SpatialAudioCuePanningC02onB21AzimuthStarterHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/onSpatialAzimuthStarterHandler"></a>
<a class="token" href="#/s:7heresdk22SpatialAudioCuePanningC02onB21AzimuthStarterHandlera">onSpatialAzimuthStarterHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called once <code>startAngularPanning()</code> starts.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="n">onSpatialAzimuthStarterHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">spatialTrajectoryData</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-spatialtrajectorydata">SpatialTrajectoryData</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>spatialTrajectoryData</em>
</code>
</td>
<td>
<div>
<p>The angular panning information of the current spatial trajectory.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22SpatialAudioCuePanningC012startAngularE0010nextCustomE4Data15azimuthCallbackyAA0ieJ0VSg_yAA0b10TrajectoryJ0VctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/startAngularPanning(nextCustomPanningData:azimuthCallback:)"></a>
<a class="token" href="#/s:7heresdk22SpatialAudioCuePanningC012startAngularE0010nextCustomE4Data15azimuthCallbackyAA0ieJ0VSg_yAA0b10TrajectoryJ0VctF">startAngularPanning(nextCustomPanningData:<wbr/>azimuthCallback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.
An optional custom value for <code><a href="../Structs/CustomPanningData.html#/s:7heresdk17CustomPanningDataV25estimatedAudioCueDurationSdSgvp">CustomPanningData.estimatedAudioCueDuration</a></code>,
<code><a href="../Structs/CustomPanningData.html#/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp">CustomPanningData.initialAzimuthInDegrees</a></code>,  or its <code><a href="../Structs/CustomPanningData.html#/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp">CustomPanningData.sweepAzimuthInDegrees</a></code>
can be here defined if the default data does not fully match the utilized Language or TTS engine
or angle expectations.
If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full
completion of a previous spatial audio trajectory, then <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-eventtextdelegate">EventTextDelegate</a></code> will retrieve
the azimuth values of the new maneuver.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">startAngularPanning</span><span class="p">(</span><span class="nv">nextCustomPanningData</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-custompanningdata">CustomPanningData</a></span><span class="p">?,</span> <span class="nv">azimuthCallback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">SpatialAudioCuePanning</span><span class="o">.</span><span class="n"><a href="../Classes/SpatialAudioCuePanning.html#/s:7heresdk22SpatialAudioCuePanningC02onB21AzimuthStarterHandlera">onSpatialAzimuthStarterHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>nextCustomPanningData</em>
</code>
</td>
<td>
<div>
<p>Defines a new set of values related to spatial audio panning.
When <code><a href="sdk-for-ios-navigate-api-reference-..-structs-custompanningdata">CustomPanningData</a></code> is initialized as <code>nil</code>, the default set of values provided by HERE SDK
will be used instead.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>azimuthCallback</em>
</code>
</td>
<td>
<div>
<p>Callback that will signal the next azimuth required to complete a spatial audio trajectory
once the angular panning has started.
Azimuth angular values are retrieved individually until the full duration of the audio trajectory
has been reached,
or a new text message has started its angular panning.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
