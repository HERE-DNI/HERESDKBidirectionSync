---
title: "sdk-for-ios-explore-api-reference-structs-transportspecification-carbuilder"
slug: "sdk-for-ios-explore-api-reference-structs-transportspecification-carbuilder"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/CarBuilder"></a>
<a title="CarBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-transport">Transport</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a>
<img alt="" id="carat" src="/carat.png"/>
        CarBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CarBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">CarBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">CarBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">CarBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a></code> for a car.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV10CarBuilderCAEycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV10CarBuilderCAEycfc">init()</a>
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
<a name="/s:7heresdk22TransportSpecificationV10CarBuilderC011withVehicleC0yAeA0gC0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withVehicleSpecification(_:)"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV10CarBuilderC011withVehicleC0yAeA0gC0VF">withVehicleSpecification(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle specification.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withVehicleSpecification</span><span class="p">(</span><span class="n">_</span> <span class="nv">vehicleSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">CarBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>vehicleSpecification</em>
</code>
</td>
<td>
<div>
<p>The vehicle specification.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>TransportSpecification.CarBuilder</code> object with the vehicle specification set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV10CarBuilderC5buildACyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV10CarBuilderC5buildACyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds the <code><a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a></code> object for a car with the specifications taken
from the <code>TransportSpecification.CarBuilder</code> object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-explore-api-reference-structs-transportspecification">TransportSpecification</a></code> object created from the <code>TransportSpecification.CarBuilder</code> object.</p>
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
