---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-trafficincident"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficIncident.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficIncident"></a>
<a title="TrafficIncident Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-traffic">Traffic</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficIncident Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficIncident</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficIncident</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-trafficincidentbase">TrafficIncidentBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficIncident</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficIncident</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>TrafficIncident provides details about a traffic incident.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC6impactAA0bC6ImpactOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/impact"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC6impactAA0bC6ImpactOvp">impact</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The impact of the incident.
The value is <code><a href="../Enums/TrafficIncidentImpact.html#/s:7heresdk21TrafficIncidentImpactO7unknownyA2CmF">TrafficIncidentImpact.unknown</a></code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">impact</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-trafficincidentimpact">TrafficIncidentImpact</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The category of the incident.
The value is <code><a href="../Enums/TrafficIncidentType.html#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">TrafficIncidentType.unknown</a></code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-trafficincidenttype">TrafficIncidentType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC11descriptionAA13LocalizedTextVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/description"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC11descriptionAA13LocalizedTextVvp">description</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The human readable description of the incident, possibly with location information.
The description is currently not present in our map data. Therefore, when
accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
always an empty string is returned. This does not apply when using the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trafficengine">TrafficEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">description</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-localizedtext">LocalizedText</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC9startTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startTime"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC9startTime10Foundation4DateVSgvp">startTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time from which the incident is valid, before this time the incident should not be considered.
The value is <code>nil</code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC7endTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/endTime"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC7endTime10Foundation4DateVSgvp">endTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time until which the incident is valid, after this time the incident should not be considered.
The value is <code>nil</code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">endTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC2idSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC2idSSvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique current identifier for a traffic incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC10originalIdSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/originalId"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC10originalIdSSvp">originalId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique identifier of the first traffic incident.
The original id remains the same whenever the traffic incident is updated and <code><a href="../Classes/TrafficIncident.html#/s:7heresdk15TrafficIncidentC2idSSvp">TrafficIncident.id</a></code> is changed.
Once an incident chain has been created, this value will never change.
The traffic incident an be looked up by original id using <code><a href="../Classes/TrafficEngine.html#/s:7heresdk13TrafficEngineC14lookupIncident4with0D7Options10completionAA10TaskHandle_pSS_AA0be6LookupG0VyAA0B10QueryErrorOSg_AA0bE0CSgtctF">TrafficEngine.lookupIncident(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">originalId</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC8parentIdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parentId"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC8parentIdSSSgvp">parentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The identifier of another incident to which this incident is linked.
The value is <code>nil</code> if the incident doesn’t have a parent.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parentId</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC23junctionsTraversabilityAA09JunctionsE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/junctionsTraversability"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC23junctionsTraversabilityAA09JunctionsE0Ovp">junctionsTraversability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The traversability of junctions along the affected road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">junctionsTraversability</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-junctionstraversability">JunctionsTraversability</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC12isRoadClosedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRoadClosed"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC12isRoadClosedSbvp">isRoadClosed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicates whether road is closed or not.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRoadClosed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC5codesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/codes"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC5codesSays5Int32VGvp">codes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.
Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">codes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC7summaryAA13LocalizedTextVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/summary"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC7summaryAA13LocalizedTextVvp">summary</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The human readable summary of the incident.
The summary field provides a short version of the description containing no location information.
The expected summary language can be managed
via <code><a href="../Structs/TrafficIncidentsQueryOptions.html#/s:7heresdk28TrafficIncidentsQueryOptionsV12languageCodeAA08LanguageG0OSgvp">TrafficIncidentsQueryOptions.languageCode</a></code> and <code><a href="../Structs/TrafficIncidentLookupOptions.html#/s:7heresdk28TrafficIncidentLookupOptionsV12languageCodeAA08LanguageG0OSgvp">TrafficIncidentLookupOptions.languageCode</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">summary</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-localizedtext">LocalizedText</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC9entryTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/entryTime"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC9entryTime10Foundation4DateVSgvp">entryTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time the incident was entered into the system.
The value is <code>nil</code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">entryTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC8locationAA0B8LocationVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/location"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC8locationAA0B8LocationVvp">location</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The location of the incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficlocation">TrafficLocation</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleRestrictions"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp">vehicleRestrictions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map of restricted vehicle categories to restrictions.
A vehicle is restricted if at least one restriction field is applicable for it.
If the map is empty, there’re no restricted vehicles for the incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleRestrictions</span><span class="p">:</span> <span class="p">[</span><span class="kt">TrafficIncident</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trafficincident-restrictedvehiclecategory">RestrictedVehicleCategory</a></span> <span class="p">:</span> <span class="kt">TrafficIncident</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trafficincident-vehiclerestriction">VehicleRestriction</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RestrictedVehicleCategory"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO">RestrictedVehicleCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The vehicle categories that can be restricted.
Note, a vehicle can belong to several categories (e.g. a passenger motor car
belongs to <code><a href="../Classes/TrafficIncident/RestrictedVehicleCategory.html#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF">TrafficIncident.RestrictedVehicleCategory.car</a></code>, <code><a href="../Classes/TrafficIncident/RestrictedVehicleCategory.html#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF">TrafficIncident.RestrictedVehicleCategory.motorVehicle</a></code>, and <code><a href="../Classes/TrafficIncident/RestrictedVehicleCategory.html#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF">TrafficIncident.RestrictedVehicleCategory.all</a></code>).
A vehicle is restricted if it belongs to the category presented in the map <code><a href="../Classes/TrafficIncident.html#/s:7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp">TrafficIncident.vehicleRestrictions</a></code>
and at least one of the vehicle properties is under the matching <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trafficincident-vehiclerestriction">TrafficIncident.VehicleRestriction</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trafficincident-restrictedvehiclecategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RestrictedVehicleCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleRestriction"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV">VehicleRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The vehicle restriction representing a vehicle category and relevant restriction rules.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trafficincident-vehiclerestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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

</div>
`
}</HTMLBlock>
