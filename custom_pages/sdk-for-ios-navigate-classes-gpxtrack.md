---
title: "GPXTrack"
slug: "sdk-for-ios-navigate-classes-gpxtrack"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/GPXTrack"></a>
<a title="GPXTrack Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        GPXTrack Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>GPXTrack</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">GPXTrack</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrack</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrack</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Single track from the <code><a href="sdk-for-ios-navigate-classes-gpxdocument">GPXDocument</a></code>. Can be used as an input to the <code><a href="sdk-for-ios-navigate-classes-locationsimulator">LocationSimulator</a></code>.
Can be created and modified via <code><a href="sdk-for-ios-navigate-classes-gpxtrackwriter">GPXTrackWriter</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GPXTrackC4nameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk8GPXTrackC4nameSSvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of the name of the element in the trkType.
Can be overridden by the user. If nothing was set before, defaults to an empty string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GPXTrackC11descriptionSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/description"></a>
<a class="token" href="#/s:7heresdk8GPXTrackC11descriptionSSvp">description</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of the description of the element in the trkType.
Can be overridden by the user. If nothing was set before, defaults to an empty string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">description</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GPXTrackC12getLocationsSayAA8LocationVGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getLocations()"></a>
<a class="token" href="#/s:7heresdk8GPXTrackC12getLocationsSayAA8LocationVGyF">getLocations()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a list of all stored track points converted to a <code><a href="sdk-for-ios-navigate-structs-location">Location</a></code> object.
See <a href="https://www.topografix.com/GPX/1/1/#type_wptType">type_wptType</a> for more details on the <code>wptType</code> format that is used for a track point.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getLocations</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-location">Location</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>List of <code><a href="sdk-for-ios-navigate-structs-location">Location</a></code> objects.</p>
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
