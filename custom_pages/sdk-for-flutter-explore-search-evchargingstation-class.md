---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-evchargingstation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingStation-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">EVChargingStation class</li>
</ol>
<div class="self-name">EVChargingStation</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingStation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingStation class</h1></div>
<section class="desc markdown">
<p>Group of connectors for electric vehicles (EVs), defined by a common charging connector type and
maximum power level.</p>
<p>Use /sdk-for-flutter-explore-search-placecategory-businessandservicesevchargingstation to find stations.
In the <code>Details</code> of a <code>Place</code> result you can find the list of found pools containing stations,
if any.</p>
<p>For offline EV rich attributes, enable /sdk-for-flutter-explore-core-engine-layerconfigurationfeature
in /sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingStation.withDefaults">
/sdk-for-flutter-explore-search-evchargingstation-evchargingstation-withdefaults()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="availableConnectorCount">
/sdk-for-flutter-explore-search-evchargingstation-availableconnectorcount
↔ int?
</dt>
<dd>
  Number of available physical connectors at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargingMode">
/sdk-for-flutter-explore-search-evchargingstation-chargingmode
↔ String?
</dt>
<dd>
  Charging mode of the charging station. For more information, see
<a href="https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes">https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes</a> standard.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorCount">
/sdk-for-flutter-explore-search-evchargingstation-connectorcount
↔ int?
</dt>
<dd>
  Number of physical connectors at the charging station.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorTypeId">
/sdk-for-flutter-explore-search-evchargingstation-connectortypeid
↔ String?
</dt>
<dd>
  ID of the connector type.
For more information on the current connector types, see
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html</a>
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorTypeName">
/sdk-for-flutter-explore-search-evchargingstation-connectortypename
↔ String?
</dt>
<dd>
  Name of the connector type.
For more information on the current connector types, see
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html</a>
May include customer-facing names. In such cases, a 'customer names' label is present.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="currentRangeInAmperes">
/sdk-for-flutter-explore-search-evchargingstation-currentrangeinamperes
↔ String?
</dt>
<dd>
  Current range provided by the charging station, in amperes.
Values are alphanumeric represented by the Ampere value followed by an 'A',
for example '12A-80A'.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hasFixedCable">
/sdk-for-flutter-explore-search-evchargingstation-hasfixedcable
↔ bool?
</dt>
<dd>
  Indicates that the cable is fixed or not fixed for a specific
Connector Type on the charge station.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-search-evchargingstation-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastUpdated">
/sdk-for-flutter-explore-search-evchargingstation-lastupdated
↔ DateTime?
</dt>
<dd>
  Last update of the <code>available_connector_count</code> and <code>occupied_connector_count</code> fields.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPowerInKilowatts">
/sdk-for-flutter-explore-search-evchargingstation-maxpowerinkilowatts
↔ double?
</dt>
<dd>
  Maximum charge power of connectors in kW.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupiedConnectorCount">
/sdk-for-flutter-explore-search-evchargingstation-occupiedconnectorcount
↔ int?
</dt>
<dd>
  Number of occupied physical connectors at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="outOfServiceConnectorCount">
/sdk-for-flutter-explore-search-evchargingstation-outofserviceconnectorcount
↔ int?
</dt>
<dd>
  Number of physical connectors that are out of service at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="phaseCount">
/sdk-for-flutter-explore-search-evchargingstation-phasecount
↔ int?
</dt>
<dd>
  Number of phases used by the charging station.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="physicalReference">
/sdk-for-flutter-explore-search-evchargingstation-physicalreference
↔ String?
</dt>
<dd>
  Printed on the outside of the EVSE for visual identification.
Available only in offline search.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="powerFeedTypeId">
/sdk-for-flutter-explore-search-evchargingstation-powerfeedtypeid
↔ String?
</dt>
<dd>
  ID of the power feed type, as defined by the
<a href="https://en.wikipedia.org/wiki/SAE_J1772#Charging">https://en.wikipedia.org/wiki/SAE_J1772#Charging</a> standard.
No data in case of offline search.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="powerFeedTypeName">
/sdk-for-flutter-explore-search-evchargingstation-powerfeedtypename
↔ String?
</dt>
<dd>
  Name of the power feed type, as defined by the
<a href="https://en.wikipedia.org/wiki/SAE_J1772#Charging">https://en.wikipedia.org/wiki/SAE_J1772#Charging</a> standard.
Provides the customer information on the charge level of the specific Connector Type.
Also, can describe level that is used in North America and Australia.
In that case label 'North America (Australia)' is present.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="reservedConnectorCount">
/sdk-for-flutter-explore-search-evchargingstation-reservedconnectorcount
↔ int?
</dt>
<dd>
  Number of physical connectors that are reserved at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-evchargingstation-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="supplierName">
/sdk-for-flutter-explore-search-evchargingstation-suppliername
↔ String?
</dt>
<dd>
  The EV charging station operator.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online search using the <code>SearchEngine</code>, it can be null if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="voltageRangeInVolts">
/sdk-for-flutter-explore-search-evchargingstation-voltagerangeinvolts
↔ String?
</dt>
<dd>
  Voltage range of the charge provided by the charging station, in volts.
Values are alphanumeric represented by the voltage range followed by 'V' and
by the current type 'AC' or 'DC', for example: '100-120V AC'.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-evchargingstation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-evchargingstation-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-search-evchargingstation-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">EVChargingStation class</li>
</ol>
<h5>search library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
