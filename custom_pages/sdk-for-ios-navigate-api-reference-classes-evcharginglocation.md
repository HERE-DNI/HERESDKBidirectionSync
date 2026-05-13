---
title: "Search / EVChargingLocation"
slug: "sdk-for-ios-navigate-api-reference-classes-evcharginglocation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/EVChargingLocation"></a>
<a title="EVChargingLocation Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingLocation Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingLocation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">EVChargingLocation</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">EVChargingLocation</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">EVChargingLocation</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>An electric vehicle (EV) charging location.</p>
<p>The semantics generally follow the OCPI 2.2.1 standard.</p>
<p>Known EV-specific acronyms:</p>
<ul>
<li>EV: Electric Vehicle</li>
<li>OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, <a href="https://evroaming.org/">https://evroaming.org/</a>)</li>
<li>CPO: Charge Point Operator (company that runs the EV charging location)</li>
<li>eMSP: e-Mobility Service Provider (customer-facing company)</li>
<li>EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)</li>
</ul>
<p>A charging location includes a collection of one or more EV supply equipment (EVSE) instances.
Typically, the charging location is the exact location of the group of EVSEs,
simplified to a single point, but it can also be the entrance of a parking structure
which contains these EVSEs.
Each EVSE supports more precise position, where applicable.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC2idSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC2idSSvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A unique identifier of the charging location.</p>
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
<a name="/s:7heresdk18EVChargingLocationC4nameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC4nameSSSgvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Display name of the charging location, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC5cpoIDSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cpoID"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC5cpoIDSSSgvp">cpoID</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>CPO’s own ID for the location.
This ID may be relevant for some clients to map the charging location data to their own
or 3rd party systems.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cpoID</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC18evChargingOperatorAA0bF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evChargingOperator"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC18evChargingOperatorAA0bF0VSgvp">evChargingOperator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Operator of the charging point, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evChargingOperator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evchargingoperator">EVChargingOperator</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC21evChargingSubOperatorAA0bG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evChargingSubOperator"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC21evChargingSubOperatorAA0bG0VSgvp">evChargingSubOperator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Suboperator of the charging point, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evChargingSubOperator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evchargingoperator">EVChargingOperator</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC25eMobilityServiceProvidersSayAA0B8OperatorVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eMobilityServiceProviders"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC25eMobilityServiceProvidersSayAA0B8OperatorVGvp">eMobilityServiceProviders</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>eMSPs with a roaming agreement enabling access to the EV charging location.
Available only if <code>EVChargingLocationFeature.EMSPS</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">eMobilityServiceProviders</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evchargingoperator">EVChargingOperator</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/facilityTypes"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp">facilityTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Facilities available at the charging location, for example hotel, wifi, parking lot etc.
Available only if <code>EVChargingLocationFeature.NEARBY</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">facilityTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-facilitytype">FacilityType</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC11parkingTypeAA07ParkingE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parkingType"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC11parkingTypeAA07ParkingE0OSgvp">parkingType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of parking at the charging location.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parkingType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-parkingtype">ParkingType</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC9energyMixAA06EnergyE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/energyMix"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC9energyMixAA06EnergyE0VSgvp">energyMix</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Details on the energy supplied at the charging location.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">energyMix</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-energymix">EnergyMix</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC5evsesSayAA8EVSEInfoVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evses"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC5evsesSayAA8EVSEInfoVGvp">evses</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of EVSEs at the charging station.
Available only if <code>EVChargingLocationFeature.EVSES</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evses</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evseinfo">EVSEInfo</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC7tariffsSayAA0B6TariffVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tariffs"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC7tariffsSayAA0B6TariffVGvp">tariffs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of tariffs or price plans for the connectors of the charging station.
Tariffs are typically connector-type specific. Hence, they are always linked with connectors
and/or connector groups, by indexes to this list.</p>
<p>This property is set only when data is available and when <code>EVSearchOptions.additional_features</code>
include either <code>EVChargingLocationFeature.EVSES</code> or <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code>.</p>
<p>By default, the list includes tariffs for ad-hoc charging, per connector type,
for EVSEs that accept payment without registering.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tariffs</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evchargingtariff">EVChargingTariff</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC15connectorGroupsSayAA0B14ConnectorGroupVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorGroups"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC15connectorGroupsSayAA0B14ConnectorGroupVGvp">connectorGroups</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Connector groups for the location.
Provides an overview of the charging connectors in the location by type and power.
Available only if <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectorGroups</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evchargingconnectorgroup">EVChargingConnectorGroup</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC17supportedVehiclesSayAA0B15VehicleCategoryOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supportedVehicles"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC17supportedVehiclesSayAA0B15VehicleCategoryOGvp">supportedVehicles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of vehicle categories this charging location can support. For example, the same location
can be suitable for charging passenger cars and motorcycles.
There may be some further restrictions specified in other attributes, for example the available
connector types may not be suitable for all vehicles in the supported category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">supportedVehicles</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-evchargingvehiclecategory">EVChargingVehicleCategory</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC17truckRestrictionsAA0B16TruckRestrictionVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRestrictions"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC17truckRestrictionsAA0B16TruckRestrictionVSgvp">truckRestrictions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access restrictions for trucks and light commercial vehicles.
Restricted, only available to customers having a specific contract with HERE
and if requested by including <code>EVChargingLocationFeature.TRUCK_RESTRICTIONS</code> in
<code>EVSearchOptions.additional_features</code>, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckRestrictions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evchargingtruckrestriction">EVChargingTruckRestriction</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC12openingHoursAA0b7OpeningE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/openingHours"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC12openingHoursAA0b7OpeningE0VSgvp">openingHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The times when the EVSEs at the charging location can be accessed for charging.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">openingHours</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evchargingopeninghours">EVChargingOpeningHours</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC12restrictionsSayAA25EVAccessRestrictionReasonOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictions"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC12restrictionsSayAA25EVAccessRestrictionReasonOGvp">restrictions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Reason(s) for restricted access.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">restrictions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-evaccessrestrictionreason">EVAccessRestrictionReason</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC18supportPhoneNumberSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supportPhoneNumber"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC18supportPhoneNumberSSSgvp">supportPhoneNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The phone number that EV drivers should call when need assistance at the charge location, in E.164 format.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">supportPhoneNumber</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC8timeZoneSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeZone"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC8timeZoneSSSgvp">timeZone</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time zone of the charging location. Based on IANA tzdata’s TZ-values.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeZone</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
