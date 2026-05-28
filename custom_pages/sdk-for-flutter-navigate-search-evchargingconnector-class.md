---
title: "EVChargingConnector class"
slug: "sdk-for-flutter-navigate-search-evchargingconnector-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingConnector-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingConnector-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingConnector/EVChargingConnector.html">EVChargingConnector</a></li>
<li class="section-title">
<a href="search/EVChargingConnector-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingConnector/connectorType.html">connectorType</a></li>
<li><a href="search/EVChargingConnector/format.html">format</a></li>
<li><a href="search/EVChargingConnector/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingConnector/id.html">id</a></li>
<li><a href="search/EVChargingConnector/maxCurrentInAmperes.html">maxCurrentInAmperes</a></li>
<li><a href="search/EVChargingConnector/maxPowerInWatts.html">maxPowerInWatts</a></li>
<li><a href="search/EVChargingConnector/maxVoltageInVolts.html">maxVoltageInVolts</a></li>
<li><a href="search/EVChargingConnector/powerType.html">powerType</a></li>
<li class="inherited"><a href="search/EVChargingConnector/runtimeType.html">runtimeType</a></li>
<li><a href="search/EVChargingConnector/tariffIndexes.html">tariffIndexes</a></li>
<li><a href="search/EVChargingConnector/termsAndConditionsUrl.html">termsAndConditionsUrl</a></li>
<li class="section-title inherited"><a href="search/EVChargingConnector-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingConnector/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingConnector/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingConnector-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingConnector/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">EVChargingConnector class</li>
</ol>
<div class="self-name">EVChargingConnector</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingConnector-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingConnector class</h1></div>
<section class="desc markdown">
<p>Represents a connector at the charging point.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingConnector">
/sdk-for-flutter-navigate-search-evchargingconnector-evchargingconnector()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="connectorType">
/sdk-for-flutter-navigate-search-evchargingconnector-connectortype
↔ String
</dt>
<dd>
  Standardized type of the connector.
Should be one of the constants defined in /sdk-for-flutter-navigate-ev-evchargingconnectortype-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="format">
/sdk-for-flutter-navigate-search-evchargingconnector-format
↔ /sdk-for-flutter-navigate-ev-evchargingconnectorformat
</dt>
<dd>
  Format of the connector, whether it is a socket or a cable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-search-evchargingconnector-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-search-evchargingconnector-id
↔ String
</dt>
<dd>
  Identifier of the connector within the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxCurrentInAmperes">
/sdk-for-flutter-navigate-search-evchargingconnector-maxcurrentinamperes
↔ int
</dt>
<dd>
  Max current (in amperes) of the connector.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPowerInWatts">
/sdk-for-flutter-navigate-search-evchargingconnector-maxpowerinwatts
↔ int?
</dt>
<dd>
  Max power (in watts) of the connector, if available.
This should be set when the maximum electric power is lower than the calculated value from
voltage and amperage.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxVoltageInVolts">
/sdk-for-flutter-navigate-search-evchargingconnector-maxvoltageinvolts
↔ int
</dt>
<dd>
  Max voltage (in volts) of the connector.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="powerType">
/sdk-for-flutter-navigate-search-evchargingconnector-powertype
↔ /sdk-for-flutter-navigate-core-powertype
</dt>
<dd>
  Type of electrical power used by the connector.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-evchargingconnector-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tariffIndexes">
/sdk-for-flutter-navigate-search-evchargingconnector-tariffindexes
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  Tariffs for the connector, presented by indexes to the charging station's tariffs-list.
Available only if <code>EVChargingLocationFeature.TARIFFS</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="termsAndConditionsUrl">
/sdk-for-flutter-navigate-search-evchargingconnector-termsandconditionsurl
↔ String?
</dt>
<dd>
  URL to the operator’s terms and conditions, if available.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-search-evchargingconnector-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-evchargingconnector-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-evchargingconnector-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">EVChargingConnector class</li>
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
