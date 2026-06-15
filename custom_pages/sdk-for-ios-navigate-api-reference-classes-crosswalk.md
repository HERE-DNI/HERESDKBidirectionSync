---
title: "Crosswalk"
slug: "sdk-for-ios-navigate-api-reference-classes-crosswalk"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Crosswalk"></a>
<a title="Crosswalk Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-venues">Venues</a>

        Crosswalk Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Crosswalk</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Crosswalk</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Crosswalk</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Crosswalk</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents crosswalk’s inside the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code>. A crosswalk is an area of the road surface
where pedestrians are expected to walk across the road. The area is represented as a polygon, which is often,
but not necessarily, rectangular and oriented with the shorter dimension in the vehicle’s direction of travel.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9CrosswalkC19classificationStyleAC014ClassificationD0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/classificationStyle"></a>
<a class="token" href="#/s:7heresdk9CrosswalkC19classificationStyleAC014ClassificationD0Ovp">classificationStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets crosswalk Classification style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">classificationStyle</span><span class="p">:</span> <span class="kt">Crosswalk</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-crosswalk-classificationstyle">ClassificationStyle</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9CrosswalkC10identifierSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/identifier"></a>
<a class="token" href="#/s:7heresdk9CrosswalkC10identifierSSvp">identifier</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code>id</code> of the Crosswalk.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">identifier</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9CrosswalkC5levelAA10VenueLevelCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/level"></a>
<a class="token" href="#/s:7heresdk9CrosswalkC5levelAA10VenueLevelCvp">level</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The parent level of the crosswalk.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">level</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9CrosswalkC19ClassificationStyleO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ClassificationStyle"></a>
<a class="token" href="#/s:7heresdk9CrosswalkC19ClassificationStyleO">ClassificationStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Available Classification styles.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-crosswalk-classificationstyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ClassificationStyle</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
