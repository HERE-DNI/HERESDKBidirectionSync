---
title: "EVChargingLocation class abstract"
slug: "sdk-for-flutter-explore-search-evcharginglocation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingLocation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingLocation-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingLocation/EVChargingLocation.html">EVChargingLocation</a></li>
<li class="section-title">
<a href="search/EVChargingLocation-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingLocation/connectorGroups.html">connectorGroups</a></li>
<li><a href="search/EVChargingLocation/cpoID.html">cpoID</a></li>
<li><a href="search/EVChargingLocation/eMobilityServiceProviders.html">eMobilityServiceProviders</a></li>
<li><a href="search/EVChargingLocation/energyMix.html">energyMix</a></li>
<li><a href="search/EVChargingLocation/evChargingOperator.html">evChargingOperator</a></li>
<li><a href="search/EVChargingLocation/evChargingSubOperator.html">evChargingSubOperator</a></li>
<li><a href="search/EVChargingLocation/evses.html">evses</a></li>
<li><a href="search/EVChargingLocation/facilityTypes.html">facilityTypes</a></li>
<li class="inherited"><a href="search/EVChargingLocation/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingLocation/id.html">id</a></li>
<li><a href="search/EVChargingLocation/name.html">name</a></li>
<li><a href="search/EVChargingLocation/openingHours.html">openingHours</a></li>
<li><a href="search/EVChargingLocation/parkingType.html">parkingType</a></li>
<li><a href="search/EVChargingLocation/restrictions.html">restrictions</a></li>
<li class="inherited"><a href="search/EVChargingLocation/runtimeType.html">runtimeType</a></li>
<li><a href="search/EVChargingLocation/supportedVehicles.html">supportedVehicles</a></li>
<li><a href="search/EVChargingLocation/supportPhoneNumber.html">supportPhoneNumber</a></li>
<li><a href="search/EVChargingLocation/tariffs.html">tariffs</a></li>
<li><a href="search/EVChargingLocation/timeZone.html">timeZone</a></li>
<li><a href="search/EVChargingLocation/truckRestrictions.html">truckRestrictions</a></li>
<li class="section-title inherited"><a href="search/EVChargingLocation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingLocation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingLocation/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/EVChargingLocation-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/EVChargingLocation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">EVChargingLocation class</li>
</ol>
<div class="self-name">EVChargingLocation</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingLocation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingLocation class abstract</h1></div>
<section class="desc markdown">
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
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingLocation">
/sdk-for-flutter-explore-search-evcharginglocation-evcharginglocation()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="connectorGroups">
/sdk-for-flutter-explore-search-evcharginglocation-connectorgroups
→ List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingconnectorgroup-class&gt;
</dt>
<dd>
  Connector groups for the location.
Provides an overview of the charging connectors in the location by type and power.
Available only if <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
Gets the connector groups for the location.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="cpoID">
/sdk-for-flutter-explore-search-evcharginglocation-cpoid
→ String?
</dt>
<dd>
  CPO's own ID for the location.
This ID may be relevant for some clients to map the charging location data to their own
or 3rd party systems.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.
Gets the CPO's own ID for the location.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="eMobilityServiceProviders">
/sdk-for-flutter-explore-search-evcharginglocation-emobilityserviceproviders
→ List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingoperator-class&gt;
</dt>
<dd>
  eMSPs with a roaming agreement enabling access to the EV charging location.
Available only if <code>EVChargingLocationFeature.EMSPS</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
Gets the list of eMSPs with a roaming agreement enabling access to the EV charging location.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="energyMix">
/sdk-for-flutter-explore-search-evcharginglocation-energymix
→ /sdk-for-flutter-explore-search-energymix-class?
</dt>
<dd>
  Details on the energy supplied at the charging location.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.
Gets the details on the energy supplied at the charging location.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="evChargingOperator">
/sdk-for-flutter-explore-search-evcharginglocation-evchargingoperator
→ /sdk-for-flutter-explore-search-evchargingoperator-class?
</dt>
<dd>
  Operator of the charging point, if available.
Gets the operator of the charging point, if available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="evChargingSubOperator">
/sdk-for-flutter-explore-search-evcharginglocation-evchargingsuboperator
→ /sdk-for-flutter-explore-search-evchargingoperator-class?
</dt>
<dd>
  Suboperator of the charging point, if available.
Gets the suboperator of the charging point, if available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="evses">
/sdk-for-flutter-explore-search-evcharginglocation-evses
→ List&lt;<wbr/>/sdk-for-flutter-explore-search-evseinfo-class&gt;
</dt>
<dd>
  List of EVSEs at the charging station.
Available only if <code>EVChargingLocationFeature.EVSES</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
Gets the list of EVSEs at the charging station.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="facilityTypes">
/sdk-for-flutter-explore-search-evcharginglocation-facilitytypes
→ List&lt;<wbr/>/sdk-for-flutter-explore-search-facilitytype&gt;
</dt>
<dd>
  Facilities available at the charging location, for example hotel, wifi, parking lot etc.
Available only if <code>EVChargingLocationFeature.NEARBY</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
Gets the list of facilities available at the charging location, for example
hotel, wifi, parking lot etc.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-search-evcharginglocation-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-explore-search-evcharginglocation-id
→ String
</dt>
<dd>
  A unique identifier of the charging location.
Gets the unique identifier of the charging location.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-explore-search-evcharginglocation-name
→ String?
</dt>
<dd>
  Display name of the charging location, if available.
Gets the display name of the charging location, if available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="openingHours">
/sdk-for-flutter-explore-search-evcharginglocation-openinghours
→ /sdk-for-flutter-explore-search-evchargingopeninghours-class?
</dt>
<dd>
  The times when the EVSEs at the charging location can be accessed for charging.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.
Gets the times when the EVSEs at the charging location can be accessed for charging.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="parkingType">
/sdk-for-flutter-explore-search-evcharginglocation-parkingtype
→ /sdk-for-flutter-explore-search-parkingtype?
</dt>
<dd>
  The type of parking at the charging location.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.
Gets the type of parking at the charging location.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="restrictions">
/sdk-for-flutter-explore-search-evcharginglocation-restrictions
→ List&lt;<wbr/>/sdk-for-flutter-explore-search-evaccessrestrictionreason&gt;
</dt>
<dd>
  Reason(s) for restricted access.
Gets the list of restrictions.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-evcharginglocation-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="supportedVehicles">
/sdk-for-flutter-explore-search-evcharginglocation-supportedvehicles
→ List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingvehiclecategory&gt;
</dt>
<dd>
  List of vehicle categories this charging location can support. For example, the same location
can be suitable for charging passenger cars and motorcycles.
There may be some further restrictions specified in other attributes, for example the available
connector types may not be suitable for all vehicles in the supported category.
Gets the list of vehicle categories this charging location can support. For example,
the same location can be suitable for charging passenger cars and motorcycles.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="supportPhoneNumber">
/sdk-for-flutter-explore-search-evcharginglocation-supportphonenumber
→ String?
</dt>
<dd>
  The phone number that EV drivers should call when need assistance at the charge location, in E.164 format.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.
Gets the phone number that EV drivers should call when need assistance at the charge location.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="tariffs">
/sdk-for-flutter-explore-search-evcharginglocation-tariffs
→ List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingtariff-class&gt;
</dt>
<dd>
  List of tariffs or price plans for the connectors of the charging station.
Tariffs are typically connector-type specific. Hence, they are always linked with connectors
and/or connector groups, by indexes to this list.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="timeZone">
/sdk-for-flutter-explore-search-evcharginglocation-timezone
→ String?
</dt>
<dd>
  The time zone of the charging location. Based on IANA tzdata's TZ-values.
Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.
Gets the time zone of the charging location. Based on IANA tzdata's TZ-values.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="truckRestrictions">
/sdk-for-flutter-explore-search-evcharginglocation-truckrestrictions
→ /sdk-for-flutter-explore-search-evchargingtruckrestriction-class?
</dt>
<dd>
  Access restrictions for trucks and light commercial vehicles.
Restricted, only available to customers having a specific contract with HERE
and if requested by including <code>EVChargingLocationFeature.TRUCK_RESTRICTIONS</code> in
<code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.
Gets the access restrictions for trucks and light commercial vehicles.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-evcharginglocation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-evcharginglocation-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-search-evcharginglocation-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li class="self-crumb">EVChargingLocation class</li>
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
`
}</HTMLBlock>
