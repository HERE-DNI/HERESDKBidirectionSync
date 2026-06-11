---
title: "GPXTrackWriter"
slug: "sdk-for-ios-navigate-api-reference-classes-gpxtrackwriter"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/GPXTrackWriter"></a>
<a title="GPXTrackWriter Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        GPXTrackWriter Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>GPXTrackWriter</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">GPXTrackWriter</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrackWriter</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrackWriter</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Writes GPX track points to <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code>.
The instance of the class should be added as a listener to the
<code><a href="sdk-for-ios-navigate-api-reference-classes-locationengine">LocationEngine</a></code> for GPX track recording.
Appends the new location to the back segment of the track whenever the listener is called.
The following data (if provided) can be recorded and inserted into the resulting <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code>: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>pitchInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code>, <code>bearingAccuracyInDegrees</code>, <code>speedAccuracyInMetersPerSecond</code> and <code>locationTechnology</code>.</p>
<p>Use case examples:</p>
<p>A user wants to create and save a new <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxdocument">GPXDocument</a></code> with one <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code>:</p>
<ul>
<li>create <code>GPXTrackWriter</code> and add it as a location listener to <code><a href="sdk-for-ios-navigate-api-reference-classes-locationengine">LocationEngine</a></code>.</li>
<li>set user parameters to <code><a href="../Classes/GPXTrackWriter.html#/s:7heresdk14GPXTrackWriterC5trackAA0B0Cvp">GPXTrackWriter.track</a></code> (e.g. <code><a href="../Classes/GPXTrack.html#/s:7heresdk8GPXTrackC4nameSSvp">GPXTrack.name</a></code> or <code><a href="../Classes/GPXTrack.html#/s:7heresdk8GPXTrackC11descriptionSSvp">GPXTrack.description</a></code>).</li>
<li>when writing is completed, create a new <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxdocument">GPXDocument</a></code> with a list of one <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code> and save the document via <code><a href="../Classes/GPXDocument.html#/s:7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF">GPXDocument.save(...)</a></code>.</li>
</ul>
<p>A user wants to modify and save <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code> in the existing <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxdocument">GPXDocument</a></code>:</p>
<ul>
<li>load <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxdocument">GPXDocument</a></code> from a file by the relevant constructor.</li>
<li>create <code>GPXTrackWriter</code> with the required track in the list <code><a href="../Classes/GPXDocument.html#/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">GPXDocument.tracks</a></code>,
add the created instance as a location listener to <code><a href="sdk-for-ios-navigate-api-reference-classes-locationengine">LocationEngine</a></code>.</li>
<li>when writing is completed, save the document via <code><a href="../Classes/GPXDocument.html#/s:7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF">GPXDocument.save(...)</a></code>.</li>
</ul>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxdocument">GPXDocument</a></code> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GPXTrackWriterCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk14GPXTrackWriterCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of GPXTrackWriter with an empty track inside.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GPXTrackWriterC5trackAcA0B0C_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(track:)"></a>
<a class="token" href="#/s:7heresdk14GPXTrackWriterC5trackAcA0B0C_tcfc">init(track:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of <code>GPXTrackWriter</code> with <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code>.
Use this constructor to append locations to an existing track.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">track</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>track</em>
</code>
</td>
<td>
<div>
<p>GPX track.</p>
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
<a name="/s:7heresdk14GPXTrackWriterC5trackAA0B0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/track"></a>
<a class="token" href="#/s:7heresdk14GPXTrackWriterC5trackAA0B0Cvp">track</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>GPX track into which GPX track points are written.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">track</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GPXTrackWriterC17onLocationUpdatedyyAA0E0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onLocationUpdated(_:)"></a>
<a class="token" href="#/s:7heresdk14GPXTrackWriterC17onLocationUpdatedyyAA0E0VF">onLocationUpdated(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called each time a new location is available.
In a navigation context while using the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-classes-visualnavigator">VisualNavigator</a></code>,
it’s required to set the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter for each <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code>
object so that the HERE SDK can map-match the locations properly.
If the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter is missing, the location will be ignored.
For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
parameters for each <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code> object.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onLocationUpdated</span><span class="p">(</span><span class="n">_</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>location</em>
</code>
</td>
<td>
<div>
<p>Current location.</p>
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
