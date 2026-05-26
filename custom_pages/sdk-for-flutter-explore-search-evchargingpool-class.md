---
title: "EVChargingPool class"
slug: "sdk-for-flutter-explore-search-evchargingpool-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingPool-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingPool-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingPool/EVChargingPool.html">EVChargingPool</a></li>
<li class="section-title">
<a href="search/EVChargingPool-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingPool/access.html">access</a></li>
<li><a href="search/EVChargingPool/accessRestrictionReasons.html">accessRestrictionReasons</a></li>
<li><a href="search/EVChargingPool/chargingStations.html">chargingStations</a></li>
<li><a href="search/EVChargingPool/cpoId.html">cpoId</a></li>
<li><a href="search/EVChargingPool/details.html">details</a></li>
<li><a href="search/EVChargingPool/eMobilityServiceProviders.html">eMobilityServiceProviders</a></li>
<li><a href="search/EVChargingPool/evseInfo.html">evseInfo</a></li>
<li><a href="search/EVChargingPool/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingPool/id.html">id</a></li>
<li class="inherited"><a href="search/EVChargingPool/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/EVChargingPool-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingPool/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingPool/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingPool-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingPool/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">EVChargingPool class</li>
</ol>
<div class="self-name">EVChargingPool</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingPool-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingPool class</h1></div>
<section class="desc markdown">
<p>A charging pool for electric vehicles is an area equipped with one or more charging stations.</p>
<p>Use /sdk-for-flutter-explore-search-placecategory-businessandservicesevchargingstation to find stations.
In the <code>Details</code> of a <code>Place</code> result you can find the list of found pools containing stations,
if any.</p>
<p>For offline EV rich attributes, also enable /sdk-for-flutter-explore-core-engine-layerconfigurationfeature
in /sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingPool">
/sdk-for-flutter-explore-search-evchargingpool-evchargingpool(List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingstation-class&gt; chargingStations, List&lt;<wbr/>/sdk-for-flutter-explore-search-emobilityserviceprovider-class&gt; eMobilityServiceProviders, List&lt;<wbr/>/sdk-for-flutter-explore-search-evaccessrestrictionreason&gt; accessRestrictionReasons)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="access">
/sdk-for-flutter-explore-search-evchargingpool-access
↔ /sdk-for-flutter-explore-search-evaccesstype?
</dt>
<dd>
  The accessibility level of the charging pool, or <code>null</code> if unknown.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="accessRestrictionReasons">
/sdk-for-flutter-explore-search-evchargingpool-accessrestrictionreasons
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-evaccessrestrictionreason&gt;
</dt>
<dd>
  Contains the list of reasons for restriction.
Populated only for offline search and when access is /sdk-for-flutter-explore-search-evaccesstype.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargingStations">
/sdk-for-flutter-explore-search-evchargingpool-chargingstations
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingstation-class&gt;
</dt>
<dd>
  List of charging stations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cpoId">
/sdk-for-flutter-explore-search-evchargingpool-cpoid
↔ String?
</dt>
<dd>
  CPO (Charge Point Operator) id for charging pool.
Only online search fills this field.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="details">
/sdk-for-flutter-explore-search-evchargingpool-details
↔ /sdk-for-flutter-explore-search-evchargingpooldetails-class?
</dt>
<dd>
  EV charging station attributes details. It is available only for a place that has charging station
for electric vehicles. Only offline search fills this field.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="eMobilityServiceProviders">
/sdk-for-flutter-explore-search-evchargingpool-emobilityserviceproviders
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-emobilityserviceprovider-class&gt;
</dt>
<dd>
  List of e-Mobility Service Providers.
Only online search fills this field.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evseInfo">
/sdk-for-flutter-explore-search-evchargingpool-evseinfo
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-evse-class&gt;
</dt>
<dd>
  Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.
Only online search fills this field.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-search-evchargingpool-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-explore-search-evchargingpool-id
↔ String?
</dt>
<dd>
  HERE ID of the charging pool.
Only online search fills this field.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-evchargingpool-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-evchargingpool-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-evchargingpool-tostring(<wbr/>)
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
/sdk-for-flutter-explore-search-evchargingpool-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">EVChargingPool class</li>
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
