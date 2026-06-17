---
title: "LocationSimulator"
slug: "sdk-for-ios-navigate-classes-locationsimulator"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/LocationSimulator"></a>
<a title="LocationSimulator Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-positioning">Positioning</a>

        LocationSimulator Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationSimulator</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LocationSimulator</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationSimulator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationSimulator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the <code>LocationSimulator</code> to generate locations along a route or a GPX document. It notifies
the registered object about the current location at a fixed interval. In order to customize
the interval, see <code><a href="sdk-for-ios-navigate-structs-locationsimulatoroptions">LocationSimulatorOptions</a></code>.
The locations are closely matched to the shape and proceeded from the start to the
destination as found in the provided route or the GPX document.
When providing a route, the <code>LocationSimulator</code> uses a base speed taken from each span
found in the provided route object. This base speed can be multiplied upfront
with a custom <code>speedFactor</code> for simulation purposes.
Effectively, this means that traffic-related information is not considered
to adjust the speed of the simulation.
For the <code><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></code>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <code><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></code> and inserted into the provided <code><a href="sdk-for-ios-navigate-structs-location">Location</a></code> object: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code> and <code>locationTechnology</code>.</p>
<p>Note that simulation works offline and independent from any map data</p>
<ul>
<li>only the information found in the provided route or GPX document is considered.</li>
<li>When initializing the <code>LocationSimulator</code> with a route, then interpolations take place between the vertices of the route’s
polyline. The distance between interpolated locations is a function of the current span’s speed and the set notification interval.</li>
<li>When initializing the <code>LocationSimulator</code> with a GPX file, the <code>LocationSimulator</code> does not apply
any interpolation on the provided location data as this would shadow the recorded GPX data.</li>
</ul>
<p>Notifications will stop after the entire route has been traveled.</p>
<p><strong>Note:</strong>
Map-matched locations are only accessible from <code><a href="sdk-for-ios-navigate-structs-routeprogress">RouteProgress</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationSimulatorC5route7optionsAcA5RouteC_AA0bC7OptionsVtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(route:options:)"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC5route7optionsAcA5RouteC_AA0bC7OptionsVtKcfc">init(route:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-route">Route</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-locationsimulatoroptions">LocationSimulatorOptions</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>route</em>
</code>
</td>
<td>
<div>
<p>The route to travel.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options to specify how the location simulator will behave.</p>
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
<a name="/s:7heresdk17LocationSimulatorC8gpxTrack7optionsAcA8GPXTrackC_AA0bC7OptionsVtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(gpxTrack:options:)"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC8gpxTrack7optionsAcA8GPXTrackC_AA0bC7OptionsVtKcfc">init(gpxTrack:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create a location simulator</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">gpxTrack</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-locationsimulatoroptions">LocationSimulatorOptions</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>gpxTrack</em>
</code>
</td>
<td>
<div>
<p>The GPX track to travel.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options to specify how the location simulator will behave.</p>
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
<a name="/s:7heresdk17LocationSimulatorC8delegateAA0B8Delegate_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/delegate"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC8delegateAA0B8Delegate_pSgvp">delegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The object that notifies on location updates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationSimulatorC5startyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start()"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC5startyyF">start()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts the location provider to send notifications to the subscribers.
Calling this method will always start the location simulator from the route’s first
<code><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></code>, even if a simulation has already been started or stopped.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationSimulatorC4stopyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stop()"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC4stopyyF">stop()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stops the location provider from sending notifications to the subscribers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">stop</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationSimulatorC5pauseyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/pause()"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC5pauseyyF">pause()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pauses sending notifications to the subscribers.
Calling this function has no effect when location provider is not started.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">pause</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationSimulatorC6resumeyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resume()"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC6resumeyyF">resume()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Resumes sending notifications to the subscribers.
Calling this function has no effect when location provider is not started.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">resume</span><span class="p">()</span></code></pre>
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
