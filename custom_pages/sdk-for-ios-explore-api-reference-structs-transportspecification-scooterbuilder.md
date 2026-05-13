---
title: "ScooterBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-structs-transportspecification-scooterbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ScooterBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/ScooterBuilder"></a>
<a title="ScooterBuilder Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-transport">Transport</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-structs-transportspecification">TransportSpecification</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        ScooterBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class ScooterBuilder</code></pre>
<pre><code>extension TransportSpecification.ScooterBuilder: NativeBase</code></pre>
<pre><code>extension TransportSpecification.ScooterBuilder: Hashable</code></pre>
</div>
</div>
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-transportspecification">TransportSpecification</a></code> for a scooter.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV14ScooterBuilderCAEycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV14ScooterBuilderCAEycfc">init()</a>
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
<pre><code>public init()</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV14ScooterBuilderC04withdC0yAeA0dC0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withScooterSpecification(_:)"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV14ScooterBuilderC04withdC0yAeA0dC0VF">withScooterSpecification(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the scooter specification.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withScooterSpecification(_ scooterSpecification: ScooterSpecification) -&gt; TransportSpecification.ScooterBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>scooterSpecification</em>
</code>
</td>
<td>
<div>
<p>The scooter specification.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>TransportSpecification.ScooterBuilder</code> object with the scooter specification set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV14ScooterBuilderC011withVehicleC0yAeA0gC0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withVehicleSpecification(_:)"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV14ScooterBuilderC011withVehicleC0yAeA0gC0VF">withVehicleSpecification(_:<wbr/>)</a>
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
<pre><code>public func withVehicleSpecification(_ vehicleSpecification: VehicleSpecification) -&gt; TransportSpecification.ScooterBuilder</code></pre>
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
<p>The <code>TransportSpecification.ScooterBuilder</code> object with the vehicle specification set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV14ScooterBuilderC5buildACyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV14ScooterBuilderC5buildACyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds the <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-transportspecification">TransportSpecification</a></code> object for a scooter with the specifications taken
from the <code>TransportSpecification.ScooterBuilder</code> object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; TransportSpecification</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-transportspecification">TransportSpecification</a></code> object created from the <code>TransportSpecification.ScooterBuilder</code> object.</p>
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



</div>
`
}</HTMLBlock>
