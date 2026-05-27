---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evchargingconnectorgroup-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVChargingConnectorGroup-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingConnectorGroup-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingConnectorGroup/EVChargingConnectorGroup.html">EVChargingConnectorGroup</a></li>
<li class="section-title">
<a href="search/EVChargingConnectorGroup-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingConnectorGroup/availableConnectorCount.html">availableConnectorCount</a></li>
<li><a href="search/EVChargingConnectorGroup/connectorCount.html">connectorCount</a></li>
<li><a href="search/EVChargingConnectorGroup/connectors.html">connectors</a></li>
<li><a href="search/EVChargingConnectorGroup/connectorType.html">connectorType</a></li>
<li><a href="search/EVChargingConnectorGroup/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingConnectorGroup/maxPowerInWatts.html">maxPowerInWatts</a></li>
<li class="inherited"><a href="search/EVChargingConnectorGroup/runtimeType.html">runtimeType</a></li>
<li><a href="search/EVChargingConnectorGroup/tariffIndexes.html">tariffIndexes</a></li>
<li class="section-title inherited"><a href="search/EVChargingConnectorGroup-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingConnectorGroup/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingConnectorGroup/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingConnectorGroup-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingConnectorGroup/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
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
<a href="../search/EVChargingConnectorGroup/EVChargingConnectorGroup.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-evchargingconnectorgroup</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="availableConnectorCount">
<a href="../search/EVChargingConnectorGroup/availableConnectorCount.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-availableconnectorcount</a>
↔ int?
</dt>
<dd>
  Number of connectors available for use at the time of query.
The field is not present if the availability is not known.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorCount">
<a href="../search/EVChargingConnectorGroup/connectorCount.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-connectorcount</a>
↔ int
</dt>
<dd>
  Number of connectors in the group. If an EVSE has multiple identical
connectors they are counted as one as only one is accessible at a time.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectors">
<a href="../search/EVChargingConnectorGroup/connectors.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-connectors</a>
↔ List&lt;<wbr/><a href="../search/EVChargingConnectorReference-class.html">/sdk-for-flutter-explore-search-evchargingconnectorreference-class</a>&gt;
</dt>
<dd>
  Array of EVSE + connector(s) pairs that belong to the group.
Provides access to EVSE statuses and more detailed connector characteristics.
Available only if <code>EVChargingLocationFeature.EVSES</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorType">
<a href="../search/EVChargingConnectorGroup/connectorType.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-connectortype</a>
↔ String
</dt>
<dd>
  The standard (type) of the connectors belonging to this group.
Should be one of the constants defined in <a href="../ev/EVChargingConnectorType-class.html">/sdk-for-flutter-explore-ev-evchargingconnectortype-class</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVChargingConnectorGroup/hashCode.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxPowerInWatts">
<a href="../search/EVChargingConnectorGroup/maxPowerInWatts.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-maxpowerinwatts</a>
↔ int
</dt>
<dd>
  Maximum power that can be delivered by the connectors, in watts (W).
Connectors without max power are not grouped.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVChargingConnectorGroup/runtimeType.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tariffIndexes">
<a href="../search/EVChargingConnectorGroup/tariffIndexes.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-tariffindexes</a>
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
<a href="../search/EVChargingConnectorGroup/noSuchMethod.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVChargingConnectorGroup/toString.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-tostring</a>(<wbr/>)
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
<a href="../search/EVChargingConnectorGroup/operator_equals.html">/sdk-for-flutter-explore-search-evchargingconnectorgroup-operator-equals</a>(<wbr/>Object other)
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
</div></div>
</div>
</HTMLBlock>
