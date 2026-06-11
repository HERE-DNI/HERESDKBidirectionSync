---
title: "TransportSpecification"
slug: "sdk-for-ios-navigate-api-reference-structs-transportspecification"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TransportSpecification"></a>
<a title="TransportSpecification Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-transport">Transport</a>

        TransportSpecification Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TransportSpecification</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransportSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains transport attributes details related to the transport mode.
<strong>Notes</strong></p>
<ul>
<li>By default all vehicle specifications from <code>RoutingOptions.transport_specification</code> are set to
<code>nil</code> and the <code>RoutingOptions.transport_specification.transport_mode</code> is set to <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>.</li>
<li>A route can be calculated with only the <code>RoutingOptions.transport_specification.transport_mode</code> set.</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transportMode"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">transportMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Transport mode.
Defaults to <code>CAR</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleSpecification"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">vehicleSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The vehicle specification for the transport mode.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV010pedestrianC0AA010PedestrianC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pedestrianSpecification"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV010pedestrianC0AA010PedestrianC0VSgvp">pedestrianSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The pedestrian specification for the transport mode.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pedestrianSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-pedestrianspecification">PedestrianSpecification</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV04taxiC0AA04TaxiC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/taxiSpecification"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV04taxiC0AA04TaxiC0VSgvp">taxiSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The taxi specification for the transport mode.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">taxiSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-taxispecification">TaxiSpecification</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV07scooterC0AA07ScooterC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/scooterSpecification"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV07scooterC0AA07ScooterC0VSgvp">scooterSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The scooter specification for the transport mode.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">scooterSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-scooterspecification">ScooterSpecification</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV13transportMode07vehicleC0010pedestrianC004taxiC007scooterC0AcA0bE0O_AA07VehicleC0VSgAA010PedestrianC0VSgAA04TaxiC0VSgAA07ScooterC0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(transportMode:vehicleSpecification:pedestrianSpecification:taxiSpecification:scooterSpecification:)"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV13transportMode07vehicleC0010pedestrianC004taxiC007scooterC0AcA0bE0O_AA07VehicleC0VSgAA010PedestrianC0VSgAA04TaxiC0VSgAA07ScooterC0VSgtcfc">init(transportMode:<wbr/>vehicleSpecification:<wbr/>pedestrianSpecification:<wbr/>taxiSpecification:<wbr/>scooterSpecification:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></span><span class="o">.</span><span class="n">car</span><span class="p">,</span> <span class="nv">vehicleSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">pedestrianSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-pedestrianspecification">PedestrianSpecification</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">taxiSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-taxispecification">TaxiSpecification</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">scooterSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-scooterspecification">ScooterSpecification</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV10CarBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/CarBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV10CarBuilderC">CarBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for a car.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-carbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">CarBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">CarBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">CarBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV12TruckBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TruckBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV12TruckBuilderC">TruckBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for a truck.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-truckbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TruckBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">TruckBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">TruckBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV17PedestrianBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PedestrianBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV17PedestrianBuilderC">PedestrianBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for pedestrian.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-pedestrianbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PedestrianBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">PedestrianBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">PedestrianBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV14ScooterBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ScooterBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV14ScooterBuilderC">ScooterBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for a scooter.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-scooterbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ScooterBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">ScooterBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">ScooterBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV14BicycleBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/BicycleBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV14BicycleBuilderC">BicycleBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for a bicycle.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-bicyclebuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">BicycleBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">BicycleBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">BicycleBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV11TaxiBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TaxiBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV11TaxiBuilderC">TaxiBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for a taxi.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-taxibuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TaxiBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">TaxiBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">TaxiBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV10BusBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/BusBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV10BusBuilderC">BusBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for a bus.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-busbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">BusBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV17PrivateBusBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PrivateBusBuilder"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV17PrivateBusBuilderC">PrivateBusBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> for a private bus.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification-privatebusbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PrivateBusBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">PrivateBusBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="o">.</span><span class="kt">PrivateBusBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
