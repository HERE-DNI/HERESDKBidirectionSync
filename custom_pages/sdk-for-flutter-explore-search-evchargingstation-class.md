---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evchargingstation-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVChargingStation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingStation-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingStation/EVChargingStation.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="search/EVChargingStation-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingStation/availableConnectorCount.html">availableConnectorCount</a></li>
<li><a href="search/EVChargingStation/chargingMode.html">chargingMode</a></li>
<li><a href="search/EVChargingStation/connectorCount.html">connectorCount</a></li>
<li><a href="search/EVChargingStation/connectorTypeId.html">connectorTypeId</a></li>
<li><a href="search/EVChargingStation/connectorTypeName.html">connectorTypeName</a></li>
<li><a href="search/EVChargingStation/currentRangeInAmperes.html">currentRangeInAmperes</a></li>
<li><a href="search/EVChargingStation/hasFixedCable.html">hasFixedCable</a></li>
<li><a href="search/EVChargingStation/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingStation/lastUpdated.html">lastUpdated</a></li>
<li><a href="search/EVChargingStation/maxPowerInKilowatts.html">maxPowerInKilowatts</a></li>
<li><a href="search/EVChargingStation/occupiedConnectorCount.html">occupiedConnectorCount</a></li>
<li><a href="search/EVChargingStation/outOfServiceConnectorCount.html">outOfServiceConnectorCount</a></li>
<li><a href="search/EVChargingStation/phaseCount.html">phaseCount</a></li>
<li><a href="search/EVChargingStation/physicalReference.html">physicalReference</a></li>
<li><a href="search/EVChargingStation/powerFeedTypeId.html">powerFeedTypeId</a></li>
<li><a href="search/EVChargingStation/powerFeedTypeName.html">powerFeedTypeName</a></li>
<li><a href="search/EVChargingStation/reservedConnectorCount.html">reservedConnectorCount</a></li>
<li class="inherited"><a href="search/EVChargingStation/runtimeType.html">runtimeType</a></li>
<li><a href="search/EVChargingStation/supplierName.html">supplierName</a></li>
<li><a href="search/EVChargingStation/voltageRangeInVolts.html">voltageRangeInVolts</a></li>
<li class="section-title inherited"><a href="search/EVChargingStation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingStation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingStation/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingStation-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingStation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
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
<p>Use <a href="../search/PlaceCategory/businessAndServicesEvChargingStation.html">/sdk-for-flutter-explore-search-placecategory-businessandservicesevchargingstation</a> to find stations.
In the <code>Details</code> of a <code>Place</code> result you can find the list of found pools containing stations,
if any.</p>
<p>For offline EV rich attributes, enable <a href="../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>
in <a href="../core.engine/SDKOptions/layerConfiguration.html">/sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingStation.withDefaults">
<a href="../search/EVChargingStation/EVChargingStation.withDefaults.html">/sdk-for-flutter-explore-search-evchargingstation-evchargingstation-withdefaults</a>()
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
<a href="../search/EVChargingStation/availableConnectorCount.html">/sdk-for-flutter-explore-search-evchargingstation-availableconnectorcount</a>
↔ int?
</dt>
<dd>
  Number of available physical connectors at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargingMode">
<a href="../search/EVChargingStation/chargingMode.html">/sdk-for-flutter-explore-search-evchargingstation-chargingmode</a>
↔ String?
</dt>
<dd>
  Charging mode of the charging station. For more information, see
<a href="https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes">https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes</a> standard.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorCount">
<a href="../search/EVChargingStation/connectorCount.html">/sdk-for-flutter-explore-search-evchargingstation-connectorcount</a>
↔ int?
</dt>
<dd>
  Number of physical connectors at the charging station.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorTypeId">
<a href="../search/EVChargingStation/connectorTypeId.html">/sdk-for-flutter-explore-search-evchargingstation-connectortypeid</a>
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
<a href="../search/EVChargingStation/connectorTypeName.html">/sdk-for-flutter-explore-search-evchargingstation-connectortypename</a>
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
<a href="../search/EVChargingStation/currentRangeInAmperes.html">/sdk-for-flutter-explore-search-evchargingstation-currentrangeinamperes</a>
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
<a href="../search/EVChargingStation/hasFixedCable.html">/sdk-for-flutter-explore-search-evchargingstation-hasfixedcable</a>
↔ bool?
</dt>
<dd>
  Indicates that the cable is fixed or not fixed for a specific
Connector Type on the charge station.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVChargingStation/hashCode.html">/sdk-for-flutter-explore-search-evchargingstation-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastUpdated">
<a href="../search/EVChargingStation/lastUpdated.html">/sdk-for-flutter-explore-search-evchargingstation-lastupdated</a>
↔ DateTime?
</dt>
<dd>
  Last update of the <code>available_connector_count</code> and <code>occupied_connector_count</code> fields.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPowerInKilowatts">
<a href="../search/EVChargingStation/maxPowerInKilowatts.html">/sdk-for-flutter-explore-search-evchargingstation-maxpowerinkilowatts</a>
↔ double?
</dt>
<dd>
  Maximum charge power of connectors in kW.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupiedConnectorCount">
<a href="../search/EVChargingStation/occupiedConnectorCount.html">/sdk-for-flutter-explore-search-evchargingstation-occupiedconnectorcount</a>
↔ int?
</dt>
<dd>
  Number of occupied physical connectors at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="outOfServiceConnectorCount">
<a href="../search/EVChargingStation/outOfServiceConnectorCount.html">/sdk-for-flutter-explore-search-evchargingstation-outofserviceconnectorcount</a>
↔ int?
</dt>
<dd>
  Number of physical connectors that are out of service at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="phaseCount">
<a href="../search/EVChargingStation/phaseCount.html">/sdk-for-flutter-explore-search-evchargingstation-phasecount</a>
↔ int?
</dt>
<dd>
  Number of phases used by the charging station.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="physicalReference">
<a href="../search/EVChargingStation/physicalReference.html">/sdk-for-flutter-explore-search-evchargingstation-physicalreference</a>
↔ String?
</dt>
<dd>
  Printed on the outside of the EVSE for visual identification.
Available only in offline search.
This field can be <code>null</code> if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="powerFeedTypeId">
<a href="../search/EVChargingStation/powerFeedTypeId.html">/sdk-for-flutter-explore-search-evchargingstation-powerfeedtypeid</a>
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
<a href="../search/EVChargingStation/powerFeedTypeName.html">/sdk-for-flutter-explore-search-evchargingstation-powerfeedtypename</a>
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
<a href="../search/EVChargingStation/reservedConnectorCount.html">/sdk-for-flutter-explore-search-evchargingstation-reservedconnectorcount</a>
↔ int?
</dt>
<dd>
  Number of physical connectors that are reserved at the charging station.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVChargingStation/runtimeType.html">/sdk-for-flutter-explore-search-evchargingstation-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="supplierName">
<a href="../search/EVChargingStation/supplierName.html">/sdk-for-flutter-explore-search-evchargingstation-suppliername</a>
↔ String?
</dt>
<dd>
  The EV charging station operator.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online search using the <code>SearchEngine</code>, it can be null if data is unavailable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="voltageRangeInVolts">
<a href="../search/EVChargingStation/voltageRangeInVolts.html">/sdk-for-flutter-explore-search-evchargingstation-voltagerangeinvolts</a>
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
<a href="../search/EVChargingStation/noSuchMethod.html">/sdk-for-flutter-explore-search-evchargingstation-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVChargingStation/toString.html">/sdk-for-flutter-explore-search-evchargingstation-tostring</a>(<wbr/>)
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
<a href="../search/EVChargingStation/operator_equals.html">/sdk-for-flutter-explore-search-evchargingstation-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
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
</div></div>
</div>
</HTMLBlock>
