---
title: "PedestrianBuilder"
slug: "sdk-for-ios-navigate-structs-transportspecification-pedestrianbuilder"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PedestrianBuilder"></a>
<a title="PedestrianBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-transport">Transport</a>

<a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a>

        PedestrianBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PedestrianBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PedestrianBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">PedestrianBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">PedestrianBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class constructs a <code><a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a></code> for pedestrian.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV17PedestrianBuilderCAEycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV17PedestrianBuilderCAEycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
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
<a name="/s:7heresdk22TransportSpecificationV17PedestrianBuilderC04withdC0yAeA0dC0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPedestrianSpecification(_:)"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV17PedestrianBuilderC04withdC0yAeA0dC0VF">withPedestrianSpecification(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the pedestrian specification.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withPedestrianSpecification</span><span class="p">(</span><span class="n">_</span> <span class="nv">pedestrianSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-pedestrianspecification">PedestrianSpecification</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">PedestrianBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>pedestrianSpecification</em>
</code>
</td>
<td>
<div>
<p>The pedestrian specification.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>TransportSpecification.PedestrianBuilder</code> object with the pedestrian specification set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV17PedestrianBuilderC5buildACyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV17PedestrianBuilderC5buildACyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds the <code><a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a></code> object for a pedestrian profile with the specifications taken
from the <code>TransportSpecification.PedestrianBuilder</code> object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a></code> object created from the <code>TransportSpecification.PedestrianBuilder</code> object.</p>
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
