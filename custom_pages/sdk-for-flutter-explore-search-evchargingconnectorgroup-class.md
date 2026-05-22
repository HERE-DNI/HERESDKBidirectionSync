---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-evchargingconnectorgroup-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingConnectorGroup-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">EVChargingConnectorGroup class</li>
</ol>
<div class="self-name">EVChargingConnectorGroup</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingConnectorGroup-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingConnectorGroup class</h1></div>
<section class="desc markdown">
<p>Represents the connector group at the charging location.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingConnectorGroup">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-evchargingconnectorgroup()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="availableConnectorCount">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-availableconnectorcount
↔ int?
</dt>
<dd>
  Number of connectors available for use at the time of query.
The field is not present if the availability is not known.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorCount">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-connectorcount
↔ int
</dt>
<dd>
  Number of connectors in the group. If an EVSE has multiple identical
connectors they are counted as one as only one is accessible at a time.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectors">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-connectors
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingconnectorreference-class&gt;
</dt>
<dd>
  Array of EVSE + connector(s) pairs that belong to the group.
Provides access to EVSE statuses and more detailed connector characteristics.
Available only if <code>EVChargingLocationFeature.EVSES</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorType">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-connectortype
↔ String
</dt>
<dd>
  The standard (type) of the connectors belonging to this group.
Should be one of the constants defined in /sdk-for-flutter-explore-ev-evchargingconnectortype-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxPowerInWatts">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-maxpowerinwatts
↔ int
</dt>
<dd>
  Maximum power that can be delivered by the connectors, in watts (W).
Connectors without max power are not grouped.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tariffIndexes">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-tariffindexes
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  Tariffs for the connector group, represented by indexes to the charging station's tariffs-list.
Available only if <code>EVChargingLocationFeature.TARIFFS</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-evchargingconnectorgroup-tostring(<wbr/>)
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
/sdk-for-flutter-explore-search-evchargingconnectorgroup-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">EVChargingConnectorGroup class</li>
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
