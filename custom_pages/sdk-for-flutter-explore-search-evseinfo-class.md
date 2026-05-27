---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evseinfo-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVSEInfo-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVSEInfo-class.html#constructors">Constructors</a></li>
<li><a href="search/EVSEInfo/EVSEInfo.html">EVSEInfo</a></li>
<li class="section-title">
<a href="search/EVSEInfo-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVSEInfo/capabilities.html">capabilities</a></li>
<li><a href="search/EVSEInfo/connectors.html">connectors</a></li>
<li><a href="search/EVSEInfo/coordinates.html">coordinates</a></li>
<li><a href="search/EVSEInfo/evseID.html">evseID</a></li>
<li><a href="search/EVSEInfo/floorLevel.html">floorLevel</a></li>
<li><a href="search/EVSEInfo/hashCode.html">hashCode</a></li>
<li><a href="search/EVSEInfo/id.html">id</a></li>
<li><a href="search/EVSEInfo/lastUpdated.html">lastUpdated</a></li>
<li><a href="search/EVSEInfo/paymentSupports.html">paymentSupports</a></li>
<li><a href="search/EVSEInfo/physicalReference.html">physicalReference</a></li>
<li class="inherited"><a href="search/EVSEInfo/runtimeType.html">runtimeType</a></li>
<li><a href="search/EVSEInfo/status.html">status</a></li>
<li><a href="search/EVSEInfo/uid.html">uid</a></li>
<li class="section-title inherited"><a href="search/EVSEInfo-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVSEInfo/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVSEInfo/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVSEInfo-class.html#operators">Operators</a></li>
<li><a href="search/EVSEInfo/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVSEInfo class</li>
</ol>
<div class="self-name">EVSEInfo</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVSEInfo-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVSEInfo class</h1></div>
<section class="desc markdown">
<p>Represents an EVSE at the charging point.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVSEInfo">
<a href="../search/EVSEInfo/EVSEInfo.html">/sdk-for-flutter-explore-search-evseinfo-evseinfo</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="capabilities">
<a href="../search/EVSEInfo/capabilities.html">/sdk-for-flutter-explore-search-evseinfo-capabilities</a>
↔ List&lt;<wbr/><a href="../ev/EVSECapability.html">/sdk-for-flutter-explore-ev-evsecapability</a>&gt;
</dt>
<dd>
  Capabilities of the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectors">
<a href="../search/EVSEInfo/connectors.html">/sdk-for-flutter-explore-search-evseinfo-connectors</a>
↔ List&lt;<wbr/><a href="../search/EVChargingConnector-class.html">/sdk-for-flutter-explore-search-evchargingconnector-class</a>&gt;
</dt>
<dd>
  List of available connectors on the EVSE. An operational EVSE should have at least one connector.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="coordinates">
<a href="../search/EVSEInfo/coordinates.html">/sdk-for-flutter-explore-search-evseinfo-coordinates</a>
↔ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?
</dt>
<dd>
  The geographic coordinates of the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evseID">
<a href="../search/EVSEInfo/evseID.html">/sdk-for-flutter-explore-search-evseinfo-evseid</a>
↔ String?
</dt>
<dd>
  Identifier compliant with the EVSE ID from eMI3 standard version V1.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="floorLevel">
<a href="../search/EVSEInfo/floorLevel.html">/sdk-for-flutter-explore-search-evseinfo-floorlevel</a>
↔ String?
</dt>
<dd>
  Floor level on which the EVSE is located.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVSEInfo/hashCode.html">/sdk-for-flutter-explore-search-evseinfo-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
<a href="../search/EVSEInfo/id.html">/sdk-for-flutter-explore-search-evseinfo-id</a>
↔ String?
</dt>
<dd>
  Human-readable globally unique identifier for the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lastUpdated">
<a href="../search/EVSEInfo/lastUpdated.html">/sdk-for-flutter-explore-search-evseinfo-lastupdated</a>
↔ DateTime
</dt>
<dd>
  Timestamp when the status of this EVSE was last updated.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="paymentSupports">
<a href="../search/EVSEInfo/paymentSupports.html">/sdk-for-flutter-explore-search-evseinfo-paymentsupports</a>
↔ List&lt;<wbr/><a href="../ev/EVSEPaymentSupport.html">/sdk-for-flutter-explore-ev-evsepaymentsupport</a>&gt;
</dt>
<dd>
  List of payment support functionalities on EVSE for ad-hoc customers (without pre-registration).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="physicalReference">
<a href="../search/EVSEInfo/physicalReference.html">/sdk-for-flutter-explore-search-evseinfo-physicalreference</a>
↔ String?
</dt>
<dd>
  A number or string printed on the outside of the EVSE for visual identification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVSEInfo/runtimeType.html">/sdk-for-flutter-explore-search-evseinfo-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="status">
<a href="../search/EVSEInfo/status.html">/sdk-for-flutter-explore-search-evseinfo-status</a>
↔ <a href="../ev/EVSEState.html">/sdk-for-flutter-explore-ev-evsestate</a>
</dt>
<dd>
  Status of the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="uid">
<a href="../search/EVSEInfo/uid.html">/sdk-for-flutter-explore-search-evseinfo-uid</a>
↔ String
</dt>
<dd>
  Uniquely identifies the EVSE within the CPOs platform (and suboperator platforms).
For example a database ID or the actual "EVSE ID". This field can never be changed, modified or renamed.
This is the 'technical' identification of the EVSE, not to be used as 'human readable' identification, use the field <a href="../search/EVSEInfo/id.html">/sdk-for-flutter-explore-search-evseinfo-id</a> for that.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/EVSEInfo/noSuchMethod.html">/sdk-for-flutter-explore-search-evseinfo-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVSEInfo/toString.html">/sdk-for-flutter-explore-search-evseinfo-tostring</a>(<wbr/>)
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
<a href="../search/EVSEInfo/operator_equals.html">/sdk-for-flutter-explore-search-evseinfo-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">EVSEInfo class</li>
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
