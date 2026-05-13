---
title: "Search  Reference"
slug: "sdk-for-ios-explore-api-reference-search"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Search.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Section/Search"></a>
<a title="Search  Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        Search  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Address"></a>
<a class="token" href="#/s:7heresdk7AddressV">Address</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Information about the address of a location.</p>
<p>Used in <code><a href="Classes/Place.html#/s:7heresdk5PlaceC7addressAA7AddressVvp">Place.address</a></code>.</p>
<p>Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
<code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <code><a href="Structs/Address.html#/s:7heresdk7AddressV11addressTextSSvp">Address.addressText</a></code>.
Complete address details can be obtained by searching with <code><a href="sdk-for-ios-explore-api-reference-structs-placeidquery">PlaceIdQuery</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-address">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Address : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11AddressTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/AddressType"></a>
<a class="token" href="#/s:7heresdk11AddressTypeO">AddressType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Address type</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-addresstype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum AddressType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AddressQueryV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AddressQuery"></a>
<a class="token" href="#/s:7heresdk12AddressQueryV">AddressQuery</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options to specify an address query. A <code><a href="Structs/AddressQuery.html#/s:7heresdk12AddressQueryV5querySSvp">AddressQuery.query</a></code> can consist of parts of an address or full addresses,
optionally comma separated. <code>AddressQuery</code> should only be used to search for parts of the address,
excluding the POI name. For example, “Invalidenstraße 116, Berlin, Germany” is appropriate, whereas
“HERE, Invalidenstraße 116, Berlin, Germany” is not. To be able to include the POI name, use
<code><a href="sdk-for-ios-explore-api-reference-structs-textquery">TextQuery</a></code> instead. <code><a href="Structs/SearchOptions.html#/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp">SearchOptions.languageCode</a></code> specifies the language of the
<code><a href="Structs/AddressQuery.html#/s:7heresdk12AddressQueryV5querySSvp">AddressQuery.query</a></code> and determines the preferred language of the results.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-addressquery">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct AddressQuery : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8AreaTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/AreaType"></a>
<a class="token" href="#/s:7heresdk8AreaTypeO">AreaType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a type of area like country, state, city, county, etc.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-areatype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum AreaType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15BusinessDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BusinessDetails"></a>
<a class="token" href="#/s:7heresdk15BusinessDetailsV">BusinessDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains place details such as contacts, opening hours and some electro vehicle info.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-businessdetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct BusinessDetails : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CategoryQuery"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV">CategoryQuery</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options to specify a query by categories.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-categoryquery">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct CategoryQuery : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7ContactV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Contact"></a>
<a class="token" href="#/s:7heresdk7ContactV">Contact</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents contact information.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-contact">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Contact : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9DateRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DateRange"></a>
<a class="token" href="#/s:7heresdk9DateRangeV">DateRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the date range when the tariff element is valid. This is typically used to indicate
seasonal tariffs or to announce an update to the tariff in advance. It may also be used to
indicate spot prices, together with time period.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-daterange">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct DateRange : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9DayOfWeekO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/DayOfWeek"></a>
<a class="token" href="#/s:7heresdk9DayOfWeekO">DayOfWeek</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the day of the week.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-dayofweek">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum DayOfWeek : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Details"></a>
<a class="token" href="#/s:7heresdk7DetailsV">Details</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains details of a specific place, such as contact information,
opening hours and assigned categories.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-details">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Details : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EmailAddressV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EmailAddress"></a>
<a class="token" href="#/s:7heresdk12EmailAddressV">EmailAddress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents data related to specific email address.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-emailaddress">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EmailAddress : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EMobilityServiceProviderV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EMobilityServiceProvider"></a>
<a class="token" href="#/s:7heresdk24EMobilityServiceProviderV">EMobilityServiceProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>eMSP (e-Mobility Service Provider) for which the EV station operator has EV roaming agreements.
It is only available for online search.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-emobilityserviceprovider">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EMobilityServiceProvider : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EnergyMixV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EnergyMix"></a>
<a class="token" href="#/s:7heresdk9EnergyMixV">EnergyMix</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents details on the energy supplied at the charging location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-energymix">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EnergyMix : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EnergySourceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EnergySource"></a>
<a class="token" href="#/s:7heresdk12EnergySourceV">EnergySource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Energy source of EV charging point.
EnergyMix contains a list of this representing the energy sources.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-energysource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EnergySource : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EnergySourceType"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO">EnergySourceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents energy source type.
EnergySource contains this representing the type of the energy source.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-energysourcetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EnergySourceType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EnvironmentalImpactV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EnvironmentalImpact"></a>
<a class="token" href="#/s:7heresdk19EnvironmentalImpactV">EnvironmentalImpact</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents environmental impact for an environmental impact category.
EnergyMix contains an list of this representing the environmental impacts of different categories.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-environmentalimpact">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EnvironmentalImpact : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27EnvironmentalImpactCategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EnvironmentalImpactCategory"></a>
<a class="token" href="#/s:7heresdk27EnvironmentalImpactCategoryO">EnvironmentalImpactCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents environmental impacts category of the environmental impact for energy mix.
EnvironmentalImpact contains this representing the category of the environmental impact.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-environmentalimpactcategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EnvironmentalImpactCategory : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVAccessRestrictionReasonO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVAccessRestrictionReason"></a>
<a class="token" href="#/s:7heresdk25EVAccessRestrictionReasonO">EVAccessRestrictionReason</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the restriction reason of an <code><a href="sdk-for-ios-explore-api-reference-structs-evchargingpool">EVChargingPool</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evaccessrestrictionreason">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVAccessRestrictionReason : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVAccessTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVAccessType"></a>
<a class="token" href="#/s:7heresdk12EVAccessTypeO">EVAccessType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the accessibility level of an <code><a href="sdk-for-ios-explore-api-reference-structs-evchargingpool">EVChargingPool</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evaccesstype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVAccessType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingConnector"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV">EVChargingConnector</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a connector at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingconnector">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingConnector : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingConnectorGroup"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV">EVChargingConnectorGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the connector group at the charging location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingconnectorgroup">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingConnectorGroup : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28EVChargingConnectorReferenceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingConnectorReference"></a>
<a class="token" href="#/s:7heresdk28EVChargingConnectorReferenceV">EVChargingConnectorReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a pairing of an EVSE and its connector(s) that belong to a group.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingconnectorreference">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingConnectorReference : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingDurationRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingDurationRange"></a>
<a class="token" href="#/s:7heresdk23EVChargingDurationRangeV">EVChargingDurationRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Duration of the charging session when the tariff element is valid, in seconds.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingdurationrange">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingDurationRange : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingLocationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/EVChargingLocation"></a>
<a class="token" href="#/s:7heresdk18EVChargingLocationC">EVChargingLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-evcharginglocation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class EVChargingLocation</code></pre>
<pre><code>extension EVChargingLocation: NativeBase</code></pre>
<pre><code>extension EVChargingLocation: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingLocationFeatureO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVChargingLocationFeature"></a>
<a class="token" href="#/s:7heresdk25EVChargingLocationFeatureO">EVChargingLocationFeature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional features that can be requested for EV charging locations.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evcharginglocationfeature">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVChargingLocationFeature : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHours"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV">EVChargingOpeningHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the times when the EVSEs at the charging location can be accessed for charging.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingopeninghours">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingOpeningHours : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31EVChargingOpeningHoursExceptionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHoursException"></a>
<a class="token" href="#/s:7heresdk31EVChargingOpeningHoursExceptionV">EVChargingOpeningHoursException</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents exceptions to the regular opening hours schedule for EV charging locations,
such as special closures or extended hours.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingopeninghoursexception">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingOpeningHoursException : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingOpeningHoursScheduleV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHoursSchedule"></a>
<a class="token" href="#/s:7heresdk30EVChargingOpeningHoursScheduleV">EVChargingOpeningHoursSchedule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Opening hours schedule for EV charging locations, represented by a list of days of the week
during which the location is open in the given time periods.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingopeninghoursschedule">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingOpeningHoursSchedule : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingOperatorV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOperator"></a>
<a class="token" href="#/s:7heresdk18EVChargingOperatorV">EVChargingOperator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents name and optionally other details about operator, suboperator, or e-Mobility service provider.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingoperator">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingOperator : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21EVChargingPoolDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingPoolDetails"></a>
<a class="token" href="#/s:7heresdk21EVChargingPoolDetailsV">EVChargingPoolDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Electric vehicle charging pool details.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingpooldetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingPoolDetails : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EVChargingTariffV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariff"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV">EVChargingTariff</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tariffs provide detailed pricing information for charging electric vehicles at a specific location.
Each tariff describes how costs are calculated based on various factors such as energy consumed,
time spent charging, and session duration.
Tariffs are typically associated with specific connectors or connector groups, and are only
included in the response when relevant data is available and requested.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingtariff">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingTariff : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingTariffDimensionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVChargingTariffDimension"></a>
<a class="token" href="#/s:7heresdk25EVChargingTariffDimensionO">EVChargingTariffDimension</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the dimension the price component, which determines what is being charged and how:</p>
<ul>
<li>time: Price per unit of time spent charging.</li>
<li>energy: Price per unit of energy consumed during charging.</li>
<li>flat: One-time fee charged per session.</li>
<li>parking time: Price per unit of time not charging but parked at the charger.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evchargingtariffdimension">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVChargingTariffDimension : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingTariffElementV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariffElement"></a>
<a class="token" href="#/s:7heresdk23EVChargingTariffElementV">EVChargingTariffElement</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a tariff element, which defines how pricing is applied.
The associated condition assists the client in selecting the appropriate element for a charging session.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingtariffelement">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingTariffElement : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EVChargingTariffElementConditionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariffElementCondition"></a>
<a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV">EVChargingTariffElementCondition</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Condition that the charging session needs to meet to apply the tariff element.
Tariff elements may include conditions that define when they apply:</p>
<ul>
<li>Time of day (e.g., 22:00–06:00)</li>
<li>Day of week (e.g., weekends only)</li>
</ul><div class="aside aside-date">
<p class="aside-title">Date</p>
    Date range (e.g., seasonal pricing)

</div><ul>
<li>Charging session duration</li>
<li>Battery level thresholds (e.g., overstay fees)</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingtariffelementcondition">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingTariffElementCondition : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30EVChargingTariffPriceComponentV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariffPriceComponent"></a>
<a class="token" href="#/s:7heresdk30EVChargingTariffPriceComponentV">EVChargingTariffPriceComponent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the price component of an EV charging tariff.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingtariffpricecomponent">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingTariffPriceComponent : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingTariffRequestV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariffRequest"></a>
<a class="token" href="#/s:7heresdk23EVChargingTariffRequestV">EVChargingTariffRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a search option to choose the eMSP or CPO whose tariff should be included in the response.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingtariffrequest">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingTariffRequest : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20EVChargingTariffTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVChargingTariffType"></a>
<a class="token" href="#/s:7heresdk20EVChargingTariffTypeO">EVChargingTariffType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the tariff pricing model (adhoc, emsp, or cpo).
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evchargingtarifftype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVChargingTariffType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26EVChargingTruckRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTruckRestriction"></a>
<a class="token" href="#/s:7heresdk26EVChargingTruckRestrictionV">EVChargingTruckRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents access restrictions for trucks and light commercial vehicles.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evchargingtruckrestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVChargingTruckRestriction : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVChargingVehicleCategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVChargingVehicleCategory"></a>
<a class="token" href="#/s:7heresdk25EVChargingVehicleCategoryO">EVChargingVehicleCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the category of the vehicle supported at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evchargingvehiclecategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVChargingVehicleCategory : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28EVCP3SearchCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/EVCP3SearchCompletionHandler"></a>
<a class="token" href="#/s:7heresdk28EVCP3SearchCompletionHandlera">EVCP3SearchCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method that will be called on the main thread when a search operation in <code><a href="sdk-for-ios-explore-api-reference-classes-evsearchengine">EVSearchEngine</a></code>
has been completed.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias EVCP3SearchCompletionHandler = (_ error: EVSearchError?, _ chargingLocations: [EVChargingLocation]?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>error</em>
</code>
</td>
<td>
<div>
<p>The ev search error.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>chargingLocations</em>
</code>
</td>
<td>
<div>
<p>The ev charging locations.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Evse"></a>
<a class="token" href="#/s:7heresdk4EvseV">Evse</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evse">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Evse : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVSearchEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/EVSearchEngine"></a>
<a class="token" href="#/s:7heresdk14EVSearchEngineC">EVSearchEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code>EVSearchEngine</code> API provides detailed information about charging locations.
It requires an online connection to execute the requests.
A licence is required to use this API. Details can be found in
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-v3-developer-guide/page/topics/quick-start-platform.html">HERE EV Charge Points API v3 - Developer Guide</a>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-evsearchengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class EVSearchEngine : EVSearchInterface</code></pre>
<pre><code>extension EVSearchEngine: NativeBase</code></pre>
<pre><code>extension EVSearchEngine: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVSearchError"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO">EVSearchError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible errors that <code><a href="sdk-for-ios-explore-api-reference-classes-evsearchengine">EVSearchEngine</a></code> may report.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evsearcherror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVSearchError : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVSearchInterfaceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/EVSearchInterface"></a>
<a class="token" href="#/s:7heresdk17EVSearchInterfaceP">EVSearchInterface</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the protocol for the <code><a href="sdk-for-ios-explore-api-reference-classes-evsearchengine">EVSearchEngine</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-evsearchinterface">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol EVSearchInterface : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15EVSearchOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVSearchOptions"></a>
<a class="token" href="#/s:7heresdk15EVSearchOptionsV">EVSearchOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Encapsulates additional options that control the behavior of <code><a href="sdk-for-ios-explore-api-reference-classes-evsearchengine">EVSearchEngine</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evsearchoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVSearchOptions : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSEConnectorV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVSEConnector"></a>
<a class="token" href="#/s:7heresdk13EVSEConnectorV">EVSEConnector</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE connector.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evseconnector">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVSEConnector : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVSEInfo"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV">EVSEInfo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents an EVSE at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-evseinfo">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EVSEInfo : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10EVSEStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVSEStatus"></a>
<a class="token" href="#/s:7heresdk10EVSEStatusO">EVSEStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE status</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-evsestatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EVSEStatus : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12FacilityTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/FacilityType"></a>
<a class="token" href="#/s:7heresdk12FacilityTypeO">FacilityType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents facility type available at the location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-facilitytype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum FacilityType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12FuelAdditiveV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FuelAdditive"></a>
<a class="token" href="#/s:7heresdk12FuelAdditiveV">FuelAdditive</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains fuel additive information for generic fuel type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-fueladditive">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct FuelAdditive : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16FuelAdditiveTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/FuelAdditiveType"></a>
<a class="token" href="#/s:7heresdk16FuelAdditiveTypeO">FuelAdditiveType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines possible fuel additives that a fuel could contain.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-fueladditivetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum FuelAdditiveType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11FuelStationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FuelStation"></a>
<a class="token" href="#/s:7heresdk11FuelStationV">FuelStation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains information about a specific fuel station.</p>
<p>Use <code><a href="Classes/PlaceCategory.html#/s:7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ">PlaceCategory.businessAndServicesPetrolGasolineStation</a></code> to find fuel stations.
In the <code><a href="sdk-for-ios-explore-api-reference-structs-details">Details</a></code> of a <code><a href="sdk-for-ios-explore-api-reference-classes-place">Place</a></code> result you can find the associated fuel station information,
if any.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-fuelstation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct FuelStation : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/FuelType"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO">FuelType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines possible fuel types provided by a fuel station.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-fueltype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum FuelType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GenericFuelV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GenericFuel"></a>
<a class="token" href="#/s:7heresdk11GenericFuelV">GenericFuel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains generic fuel type info of fuel station.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-genericfuel">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GenericFuel : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoPlace"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV">GeoPlace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>GeoPlace struct represents a location object:
such as a country, a city, a point of interest (POI) etc.
It can be used for PersonalPlace creation, in order to provide search on custom places.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-geoplace">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoPlace : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13HighlightTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/HighlightType"></a>
<a class="token" href="#/s:7heresdk13HighlightTypeO">HighlightType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies members of Suggestion class to which input query can be matched.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-highlighttype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum HighlightType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10IndexRangeC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/IndexRange"></a>
<a class="token" href="#/s:7heresdk10IndexRangeC">IndexRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds information to which part of the text, input query was matched.
The first character is denoted by a value of 0.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-indexrange">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class IndexRange</code></pre>
<pre><code>extension IndexRange: NativeBase</code></pre>
<pre><code>extension IndexRange: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LandlinePhoneV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LandlinePhone"></a>
<a class="token" href="#/s:7heresdk13LandlinePhoneV">LandlinePhone</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents data related to specific landline phone number.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-landlinephone">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LandlinePhone : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocationDetails"></a>
<a class="token" href="#/s:7heresdk15LocationDetailsV">LocationDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains geographical info about location</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-locationdetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LocationDetails : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MobilePhoneV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MobilePhone"></a>
<a class="token" href="#/s:7heresdk11MobilePhoneV">MobilePhone</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents data related to specific mobile phone number.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-mobilephone">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct MobilePhone : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12OpeningHoursV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/OpeningHours"></a>
<a class="token" href="#/s:7heresdk12OpeningHoursV">OpeningHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents opening hours information.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-openinghours">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct OpeningHours : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ParkingTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ParkingType"></a>
<a class="token" href="#/s:7heresdk11ParkingTypeO">ParkingType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents parking type available at the location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-parkingtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum ParkingType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Place"></a>
<a class="token" href="#/s:7heresdk5PlaceC">Place</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a location object, such as a country, a city, a point of interest (POI) etc.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-place">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class Place</code></pre>
<pre><code>extension Place: NativeBase</code></pre>
<pre><code>extension Place: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PlaceCategory"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC">PlaceCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a category of place with different levels of granularity.
This class also defines a set of most commonly used categories.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-placecategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class PlaceCategory</code></pre>
<pre><code>extension PlaceCategory: NativeBase</code></pre>
<pre><code>extension PlaceCategory: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10PlaceChainV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PlaceChain"></a>
<a class="token" href="#/s:7heresdk10PlaceChainV">PlaceChain</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parameters related to HERE Places chain system.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-placechain">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct PlaceChain : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PlaceFilter"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV">PlaceFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The filter options to specify a place.
Consists of fuel, truck and EV options.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-placefilter">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct PlaceFilter : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceFoodTypeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PlaceFoodType"></a>
<a class="token" href="#/s:7heresdk13PlaceFoodTypeV">PlaceFoodType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parameters related to HERE Places cuisine system.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-placefoodtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct PlaceFoodType : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12PlaceIdQueryV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PlaceIdQuery"></a>
<a class="token" href="#/s:7heresdk12PlaceIdQueryV">PlaceIdQuery</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options to specify a Place id query.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-placeidquery">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct PlaceIdQuery : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30PlaceIdSearchCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/PlaceIdSearchCompletionHandler"></a>
<a class="token" href="#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when a search by id call has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias PlaceIdSearchCompletionHandler = (_ searchError: SearchError?, _ place: Place?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>searchError</em>
</code>
</td>
<td>
<div>
<p>The search error.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>place</em>
</code>
</td>
<td>
<div>
<p>The place.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/PlaceIdSearchExtendedCompletionHandler"></a>
<a class="token" href="#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when a search by id call has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias PlaceIdSearchExtendedCompletionHandler = (_ searchError: SearchError?, _ place: Place?, _ responseDetails: ResponseDetails?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>searchError</em>
</code>
</td>
<td>
<div>
<p>The search error.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>place</em>
</code>
</td>
<td>
<div>
<p>The place.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>responseDetails</em>
</code>
</td>
<td>
<div>
<p>The response details.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23PlaceSerializationErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PlaceSerializationError"></a>
<a class="token" href="#/s:7heresdk23PlaceSerializationErrorO">PlaceSerializationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents and error, which occurs during place serialization and deserialization routines.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-placeserializationerror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum PlaceSerializationError : UInt32, CaseIterable, Codable</code></pre>
<pre><code>extension PlaceSerializationError : Error</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27PlaceSerializationExceptiona"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/PlaceSerializationException"></a>
<a class="token" href="#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Place serialization exception</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias PlaceSerializationException = PlaceSerializationError</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PlaceTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PlaceType"></a>
<a class="token" href="#/s:7heresdk9PlaceTypeO">PlaceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies place type of Place result from a search query.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-placetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum PlaceType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17POIPaymentDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/POIPaymentDetails"></a>
<a class="token" href="#/s:7heresdk17POIPaymentDetailsV">POIPaymentDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Details about the payment options at the POI.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-poipaymentdetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct POIPaymentDetails : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16POIPaymentMethodV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/POIPaymentMethod"></a>
<a class="token" href="#/s:7heresdk16POIPaymentMethodV">POIPaymentMethod</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds constants that represent payment methods.</p>
<p>See <code><a href="sdk-for-ios-explore-api-reference-structs-poipaymentdetails">POIPaymentDetails</a></code> for usage.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-poipaymentmethod">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct POIPaymentMethod</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ResponseDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ResponseDetails"></a>
<a class="token" href="#/s:7heresdk15ResponseDetailsV">ResponseDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Structure holding various information received with response to a query.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-responsedetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct ResponseDetails : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15ScheduleDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ScheduleDetails"></a>
<a class="token" href="#/s:7heresdk15ScheduleDetailsV">ScheduleDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Encapsulates schedule details complying with the iCalendar specification: <a href="https://tools.ietf.org/html/rfc5545">https://tools.ietf.org/html/rfc5545</a>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-scheduledetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct ScheduleDetails : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23SearchCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/SearchCompletionHandler"></a>
<a class="token" href="#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when a search call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias SearchCompletionHandler = (_ searchError: SearchError?, _ places: [Place]?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>searchError</em>
</code>
</td>
<td>
<div>
<p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>places</em>
</code>
</td>
<td>
<div>
<p>The list of search results. It is <code>nil</code> in case of an error.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31SearchExtendedCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/SearchExtendedCompletionHandler"></a>
<a class="token" href="#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when a search call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias SearchExtendedCompletionHandler = (_ searchError: SearchError?, _ places: [Place]?, _ responseDetails: ResponseDetails?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>searchError</em>
</code>
</td>
<td>
<div>
<p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>places</em>
</code>
</td>
<td>
<div>
<p>The list of search results. It is <code>nil</code> in case of an error.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>responseDetails</em>
</code>
</td>
<td>
<div>
<p>Additional information provided with response. It is <code>nil</code> in case of an error.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12SearchEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SearchEngine"></a>
<a class="token" href="#/s:7heresdk12SearchEngineC">SearchEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services
to provide developers with unmatched flexibility to create differentiating location-enabled
applications. It enables to search for HERE points of interests, forward and reverse
geocode addresses and geographic coordinates from the HERE map and search for suggested addresses
or place candidates based on incomplete or misspelled queries.</p>
<p>It also allows to search along a given <code><a href="sdk-for-ios-explore-api-reference-structs-geopolyline">GeoPolyline</a></code> set inside a <code><a href="sdk-for-ios-explore-api-reference-structs-geocorridor">GeoCorridor</a></code>
as part of a <code><a href="sdk-for-ios-explore-api-reference-structs-textquery">TextQuery</a></code>.</p>
<p>The SearchEngine API requires an online connection to execute the requests.</p>
<p><strong>Note:</strong> All methods are provided in two flavors. One uses a <code><a href="Search.html#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a></code> and the
other uses a <code><a href="Search.html#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a></code>: The later adds a <code><a href="sdk-for-ios-explore-api-reference-structs-responsedetails">ResponseDetails</a></code> result type
that provides the <code>requestId</code> of a search request and a <code>correlationId</code> to identify multiple,
related queries. This may be useful for debug purposes.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-searchengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class SearchEngine : SearchInterface</code></pre>
<pre><code>extension SearchEngine: NativeBase</code></pre>
<pre><code>extension SearchEngine: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SearchError"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO">SearchError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible errors that may result from a search query.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-searcherror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum SearchError : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SearchInterfaceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/SearchInterface"></a>
<a class="token" href="#/s:7heresdk15SearchInterfaceP">SearchInterface</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the protocol for the online and offline
search engines.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-searchinterface">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol SearchInterface : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SearchOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SearchOptions"></a>
<a class="token" href="#/s:7heresdk13SearchOptionsV">SearchOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Encapsulates options that control the behavior of search and suggest operations.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-searchoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct SearchOptions : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/StructuredQuery"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV">StructuredQuery</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options to specify a structured query.
Only supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-structuredquery">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct StructuredQuery : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SuggestionC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Suggestion"></a>
<a class="token" href="#/s:7heresdk10SuggestionC">Suggestion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Suggestion is meant to provide relevant suggestions to partial queries, like “restaur”, “starbu”, “eiffel”.
Represents a relevant response to user queries.
Suggestions (please check <code><a href="sdk-for-ios-explore-api-reference-enums-suggestiontype">SuggestionType</a></code>) are either:
Place: <code><a href="Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5placeyA2CmF">SuggestionType.place</a></code>
Query: <code><a href="Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5chainyA2CmF">SuggestionType.chain</a></code> or <code><a href="Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">SuggestionType.category</a></code></p>
<p>With “Place” you get data for a concrete place in the world.
With “Query” something to follow-up, a way to perform more focused search.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-suggestion">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class Suggestion</code></pre>
<pre><code>extension Suggestion: NativeBase</code></pre>
<pre><code>extension Suggestion: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14SuggestionTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SuggestionType"></a>
<a class="token" href="#/s:7heresdk14SuggestionTypeO">SuggestionType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the type of suggestion returned for query.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-suggestiontype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum SuggestionType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SuggestCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/SuggestCompletionHandler"></a>
<a class="token" href="#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when a suggest call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias SuggestCompletionHandler = (_ searchError: SearchError?, _ suggestions: [Suggestion]?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>searchError</em>
</code>
</td>
<td>
<div>
<p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>suggestions</em>
</code>
</td>
<td>
<div>
<p>The list of suggestion results. It is <code>nil</code> in case of an error.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32SuggestExtendedCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/SuggestExtendedCompletionHandler"></a>
<a class="token" href="#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when a suggest call has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.
This API is not supported by offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias SuggestExtendedCompletionHandler = (_ searchError: SearchError?, _ suggestions: [Suggestion]?, _ responseDetails: ResponseDetails?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>searchError</em>
</code>
</td>
<td>
<div>
<p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>suggestions</em>
</code>
</td>
<td>
<div>
<p>The list of suggestion results. It is <code>nil</code> in case of an error.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>responseDetails</em>
</code>
</td>
<td>
<div>
<p>Additional information provided with response. It is <code>nil</code> in case of an error.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SupplierReferenceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SupplierReference"></a>
<a class="token" href="#/s:7heresdk17SupplierReferenceV">SupplierReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of the place as provided by the supplier</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-supplierreference">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct SupplierReference : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TextQueryV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TextQuery"></a>
<a class="token" href="#/s:7heresdk9TextQueryV">TextQuery</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options to specify a text query.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-textquery">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct TextQuery : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14TimeOfDayRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TimeOfDayRange"></a>
<a class="token" href="#/s:7heresdk14TimeOfDayRangeV">TimeOfDayRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time period when the tariff element is valid, in local time. The time period wraps around to
the next day, when end time of the period <code><a href="Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV2toSSvp">TimeOfDayRange.to</a></code>
is smaller than the beginning <code><a href="Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV4fromSSvp">TimeOfDayRange.from</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-timeofdayrange">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct TimeOfDayRange : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14TruckAmenitiesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TruckAmenities"></a>
<a class="token" href="#/s:7heresdk14TruckAmenitiesV">TruckAmenities</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck amenities struct, represents availability (true/false) for each feature,
except shower_count - number of showers, if data is available.
Note: This is a BETA feature and thus subject to change.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-truckamenities">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct TruckAmenities : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TruckFuelV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TruckFuel"></a>
<a class="token" href="#/s:7heresdk9TruckFuelV">TruckFuel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains truck fuel type info of fuel station.
Note: This is a BETA feature and thus subject to change.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-truckfuel">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct TruckFuel : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10WebDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WebDetails"></a>
<a class="token" href="#/s:7heresdk10WebDetailsV">WebDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains information about images, editorials, rating and a urls to them.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-webdetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct WebDetails : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WebEditorialV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WebEditorial"></a>
<a class="token" href="#/s:7heresdk12WebEditorialV">WebEditorial</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains information about editorial article and a link to it.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-webeditorial">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct WebEditorial : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WebImageV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WebImage"></a>
<a class="token" href="#/s:7heresdk8WebImageV">WebImage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains image information and direct link to it.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-webimage">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct WebImage : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9WebRatingV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WebRating"></a>
<a class="token" href="#/s:7heresdk9WebRatingV">WebRating</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains information about rating and a url to review.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-webrating">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct WebRating : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14WebsiteAddressV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WebsiteAddress"></a>
<a class="token" href="#/s:7heresdk14WebsiteAddressV">WebsiteAddress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents data related to specific website address</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-websiteaddress">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct WebsiteAddress : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9WebSourceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WebSource"></a>
<a class="token" href="#/s:7heresdk9WebSourceV">WebSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains information about provider of the item
and a direct link to the item.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-websource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct WebSource : Hashable</code></pre>
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



</div>
`
}</HTMLBlock>
