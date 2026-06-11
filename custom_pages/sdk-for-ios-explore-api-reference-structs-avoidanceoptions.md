---
title: "sdk-for-ios-explore-api-reference-structs-avoidanceoptions"
slug: "sdk-for-ios-explore-api-reference-structs-avoidanceoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AvoidanceOptions"></a>
<a title="AvoidanceOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        AvoidanceOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AvoidanceOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AvoidanceOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify restrictions for route calculations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV12roadFeaturesSayAA04RoadE0OGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadFeatures"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV12roadFeaturesSayAA04RoadE0OGvp">roadFeatures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Features which routes should avoid. Best effort only (not enforced).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-roadfeatures">RoadFeatures</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV9countriesSayAA11CountryCodeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countries"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV9countriesSayAA11CountryCodeOGvp">countries</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Countries that the route must avoid. Strictly enforced.
Violations are reported as <code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">SectionNoticeCode.violatedBlockedRoad</a></code>.
<strong>Note:</strong> This avoidance option is not supported in <code><a href="sdk-for-ios-explore-api-reference-structs-isolineoptions">IsolineOptions</a></code> for isoline calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countries</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-countrycode">CountryCode</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV021avoidBoundingBoxAreasC0SayAA05Avoidef4AreaC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidBoundingBoxAreasOptions"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV021avoidBoundingBoxAreasC0SayAA05Avoidef4AreaC0VGvp">avoidBoundingBoxAreasOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of rectangular shapes which routes must not cross and additional options for this area.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">avoidBoundingBoxAreasOptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidboundingboxareaoptions">AvoidBoundingBoxAreaOptions</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV017avoidPolygonAreasC0SayAA05Avoide4AreaC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidPolygonAreasOptions"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV017avoidPolygonAreasC0SayAA05Avoide4AreaC0VGvp">avoidPolygonAreasOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of polygon shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of polygons is limited to 20.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">avoidPolygonAreasOptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV018avoidCorridorAreasC0SayAA05Avoide4AreaC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidCorridorAreasOptions"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV018avoidCorridorAreasC0SayAA05Avoide4AreaC0VGvp">avoidCorridorAreasOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of corridor shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of corridors is limited to 20.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">avoidCorridorAreasOptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidcorridorareaoptions">AvoidCorridorAreaOptions</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoneCategories"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp">zoneCategories</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zone categories which routes must not cross. Strictly enforced.
Violations are reported as <code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO23violatedZoneRestrictionyA2CmF">SectionNoticeCode.violatedZoneRestriction</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoneCategories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-zonecategory">ZoneCategory</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV8segmentsSayAA16SegmentReferenceVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segments"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV8segmentsSayAA16SegmentReferenceVGvp">segments</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Segments that routes will avoid going through.
Violations are reported as <code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">SectionNoticeCode.violatedBlockedRoad</a></code>.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>This avoidance option is not supported in <code><a href="sdk-for-ios-explore-api-reference-structs-isolineoptions">IsolineOptions</a></code> for isoline calculation.</li>
<li>The engine does not support an unlimited number of segments to avoid.
The limit is defined by the HERE backend services and may change. For now,
the maximum number of segments to avoid should be below 250. This value may change
on the backend and it is therefore not guaranteed to be stable.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV13exceptZoneIdsSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/exceptZoneIds"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV13exceptZoneIdsSaySSGvp">exceptZoneIds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Exception to <code>AvoidanceOptions.zone_categories</code>, which can be specified by list of zone identifiers.
e.g. the format of ID is like <code>here:cm:envzone:2</code>.
Information about the various routing zones originates from the respective catalogs of platform.here.com.
For example, more information on zone IDs for Environmental Zones is available under “<a href="https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview">https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview</a>”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">exceptZoneIds</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV7zoneIdsSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoneIds"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV7zoneIdsSaySSGvp">zoneIds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List containing identifiers of zones that routes should avoid going through.
e.g. the format of ID is like <code>here:cm:envzone:2</code>.
Information about the various routing zones originates from the respective catalogs of platform.here.com.
For example, more information on zone IDs for Environmental Zones is available under “<a href="https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview">https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview</a>”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoneIds</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV21avoidedTruckRoadTypesSayAA0eF4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidedTruckRoadTypes"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV21avoidedTruckRoadTypesSayAA0eF4TypeOGvp">avoidedTruckRoadTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a list of avoided truck road types for vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></code> for the available options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">avoidedTruckRoadTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16AvoidanceOptionsV12roadFeatures9countries021avoidBoundingBoxAreasC00g7PolygonjC00g8CorridorjC014zoneCategories8segments13exceptZoneIds0mR021avoidedTruckRoadTypesACSayAA0uE0OG_SayAA11CountryCodeOGSayAA05Avoidhi4AreaC0VGSayAA0ykzC0VGSayAA0ylzC0VGSayAA0Q8CategoryOGSayAA16SegmentReferenceVGSaySSGA7_SayAA0tU4TypeOGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(roadFeatures:countries:avoidBoundingBoxAreasOptions:avoidPolygonAreasOptions:avoidCorridorAreasOptions:zoneCategories:segments:exceptZoneIds:zoneIds:avoidedTruckRoadTypes:)"></a>
<a class="token" href="#/s:7heresdk16AvoidanceOptionsV12roadFeatures9countries021avoidBoundingBoxAreasC00g7PolygonjC00g8CorridorjC014zoneCategories8segments13exceptZoneIds0mR021avoidedTruckRoadTypesACSayAA0uE0OG_SayAA11CountryCodeOGSayAA05Avoidhi4AreaC0VGSayAA0ykzC0VGSayAA0ylzC0VGSayAA0Q8CategoryOGSayAA16SegmentReferenceVGSaySSGA7_SayAA0tU4TypeOGtcfc">init(roadFeatures:<wbr/>countries:<wbr/>avoidBoundingBoxAreasOptions:<wbr/>avoidPolygonAreasOptions:<wbr/>avoidCorridorAreasOptions:<wbr/>zoneCategories:<wbr/>segments:<wbr/>exceptZoneIds:<wbr/>zoneIds:<wbr/>avoidedTruckRoadTypes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>roadFeatures: Features which routes should avoid. Best effort only (not enforced).</li>
<li>countries: Countries that the route must avoid. Strictly enforced.
Violations are reported as <code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">SectionNoticeCode.violatedBlockedRoad</a></code>.
<strong>Note:</strong> This avoidance option is not supported in <code><a href="sdk-for-ios-explore-api-reference-structs-isolineoptions">IsolineOptions</a></code> for isoline calculation.</li>
<li>avoidBoundingBoxAreasOptions: List of rectangular shapes which routes must not cross and additional options for this area.</li>
<li>avoidPolygonAreasOptions: List of polygon shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of polygons is limited to 20.</li>
<li>avoidCorridorAreasOptions: List of corridor shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of corridors is limited to 20.</li>
<li>zoneCategories: Zone categories which routes must not cross. Strictly enforced.
Violations are reported as <code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO23violatedZoneRestrictionyA2CmF">SectionNoticeCode.violatedZoneRestriction</a></code>.</li>
<li>segments: Segments that routes will avoid going through.
Violations are reported as <code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">SectionNoticeCode.violatedBlockedRoad</a></code>.</li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li>This avoidance option is not supported in <code><a href="sdk-for-ios-explore-api-reference-structs-isolineoptions">IsolineOptions</a></code> for isoline calculation.</li>
<li>The engine does not support an unlimited number of segments to avoid.
  The limit is defined by the HERE backend services and may change. For now,
  the maximum number of segments to avoid should be below 250. This value may change
  on the backend and it is therefore not guaranteed to be stable.

<ul>
<li>exceptZoneIds: Exception to <code>AvoidanceOptions.zone_categories</code>, which can be specified by list of zone identifiers.
e.g. the format of ID is like <code>here:cm:envzone:2</code>.
Information about the various routing zones originates from the respective catalogs of platform.here.com.
For example, more information on zone IDs for Environmental Zones is available under “<a href="https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview">https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview</a>”.</li>
<li>zoneIds: List containing identifiers of zones that routes should avoid going through.
e.g. the format of ID is like <code>here:cm:envzone:2</code>.
Information about the various routing zones originates from the respective catalogs of platform.here.com.
For example, more information on zone IDs for Environmental Zones is available under “<a href="https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview">https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview</a>”.</li>
<li>avoidedTruckRoadTypes: Specifies a list of avoided truck road types for vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></code> for the available options.</li>
</ul></li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">roadFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-roadfeatures">RoadFeatures</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">countries</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-countrycode">CountryCode</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">avoidBoundingBoxAreasOptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidboundingboxareaoptions">AvoidBoundingBoxAreaOptions</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">avoidPolygonAreasOptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">avoidCorridorAreasOptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidcorridorareaoptions">AvoidCorridorAreaOptions</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">zoneCategories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-zonecategory">ZoneCategory</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">segments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">exceptZoneIds</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">zoneIds</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">avoidedTruckRoadTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
