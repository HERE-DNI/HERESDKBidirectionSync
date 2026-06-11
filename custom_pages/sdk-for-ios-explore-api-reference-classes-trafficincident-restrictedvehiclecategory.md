---
title: "sdk-for-ios-explore-api-reference-classes-trafficincident-restrictedvehiclecategory"
slug: "sdk-for-ios-explore-api-reference-classes-trafficincident-restrictedvehiclecategory"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RestrictedVehicleCategory"></a>
<a title="RestrictedVehicleCategory Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-traffic">Traffic</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-classes-trafficincident">TrafficIncident</a>
<img alt="" id="carat" src="/carat.png"/>
        RestrictedVehicleCategory Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RestrictedVehicleCategory</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RestrictedVehicleCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>The vehicle categories that can be restricted.
Note, a vehicle can belong to several categories (e.g. a passenger motor car
belongs to <code><a href="../../Classes/TrafficIncident/RestrictedVehicleCategory.html#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF">TrafficIncident.RestrictedVehicleCategory.car</a></code>, <code><a href="../../Classes/TrafficIncident/RestrictedVehicleCategory.html#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF">TrafficIncident.RestrictedVehicleCategory.motorVehicle</a></code>, and <code><a href="../../Classes/TrafficIncident/RestrictedVehicleCategory.html#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF">TrafficIncident.RestrictedVehicleCategory.all</a></code>).
A vehicle is restricted if it belongs to the category presented in the map <code><a href="../../Classes/TrafficIncident.html#/s:7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp">TrafficIncident.vehicleRestrictions</a></code>
and at least one of the vehicle properties is under the matching <code><a href="sdk-for-ios-explore-api-reference-classes-trafficincident-vehiclerestriction">TrafficIncident.VehicleRestriction</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3busyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bus"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3busyA2EmF">bus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bus.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">bus</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/car"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF">car</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">car</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO010heavyGoodsE0yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/heavyGoodsVehicle"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO010heavyGoodsE0yA2EmF">heavyGoodsVehicle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Heavy goods vehicle (or large goods vehicle).
In the European Union heavy goods vehicle is any truck with a gross combination mass (GCM) of over 3,500 kg.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">heavyGoodsVehicle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5truckyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truck"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5truckyA2EmF">truck</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">truck</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO10motorcycleyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/motorcycle"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO10motorcycleyA2EmF">motorcycle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Motorcycle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">motorcycle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/motorVehicle"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF">motorVehicle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Motor vehicle. Definition: it is a self-propelled vehicle,
that does not operate on rails and is used for the transportation of people or cargo.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">motorVehicle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO4taxiyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/taxi"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO4taxiyA2EmF">taxi</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Taxi.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">taxi</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5trainyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/train"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5trainyA2EmF">train</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Train.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">train</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO28transportingAbnormalSizeLoadyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/transportingAbnormalSizeLoad"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO28transportingAbnormalSizeLoadyA2EmF">transportingAbnormalSizeLoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Transporting an abnormal size load. See rules of the exact country that describe the exact parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">transportingAbnormalSizeLoad</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO26transportingHazardousGoodsyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/transportingHazardousGoods"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO26transportingHazardousGoodsyA2EmF">transportingHazardousGoods</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Transporting hazardous goods.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">transportingHazardousGoods</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO18vehicleWithTraileryA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/vehicleWithTrailer"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO18vehicleWithTraileryA2EmF">vehicleWithTrailer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle with trailer.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">vehicleWithTrailer</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5otheryA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/other"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5otheryA2EmF">other</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Other vehicles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">other</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/all"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF">all</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All the vehicles are applicable for this category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">all</span></code></pre>
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
